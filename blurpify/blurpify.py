import io
import pathlib
import typing
from enum import IntEnum

from PIL import Image
from PIL import ImageEnhance

from .blurple_map import blurplify_map
from .blurple_map import old_blurplify_map


class BlurpleType(IntEnum):
    BLURPLE = 1
    OLD_BLURPLE = 0


def _blurpify(
    img_input: typing.Union[str, pathlib.Path, io.BytesIO],
    img_output: typing.Union[str, pathlib.Path, io.BytesIO],
    blurple_type: BlurpleType,
    enhancements: bool = False,
):
    """The part that actually blurpifies images."""
    try:
        img = Image.open(img_input)
        img_format = img.format  # just in case

        if img.is_animated:  # currently does not support animated GIFs
            raise ValueError("Cannot process animated GIFs!")

        if enhancements:
            """
            The original version, being made in C++, used a different
            method to grayscale compared to Pillow.
            While we cannot replicate the old grayscale 1:1, we can do
            a couple of touch-ups that makes the resulting image closer to it.

            For the new blurple, these enhancements make the resulting image look
            much nicer.
            """
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.25)
            enhancer = ImageEnhance.Contrast(img)

            if blurple_type == BlurpleType.BLURPLE:
                img = enhancer.enhance(1.05)
            else:
                img = enhancer.enhance(0.95)

        # converts image to grayscale
        img = img.convert("LA")
        img = img.convert("RGBA")

        data = img.getdata()

        # gets the blurple value based on the grayscale color, then re-adds the alpha channel
        if blurple_type == BlurpleType.BLURPLE:
            new_data = tuple(blurplify_map[p[0]] + (p[3],) for p in data)
        else:
            new_data = tuple(old_blurplify_map[p[0]] + (p[3],) for p in data)

        img.putdata(new_data)

        img.save(img_output, format=img_format)
        return img_output
    finally:
        img.close()  # type: ignore


def convert(
    img_input: typing.Union[str, pathlib.Path, io.BytesIO],
    img_output: typing.Optional[typing.Union[str, pathlib.Path, io.BytesIO]] = None,
    blurple_type: BlurpleType = BlurpleType.BLURPLE,
    enhancements: bool = True,
) -> typing.Union[str, pathlib.Path, io.BytesIO]:
    """Blurpifies the given image.

    Parameters
    ----------
    img_input: `Union[str, pathlib.Path, io.BytesIO]`
        The file to blurpify.
        Specify either a string to the path, the path itself, or a io.BytesIO container.
        Animated GIFS do not work as of yet.
    img_output: `Optional[Union[str, pathlib.Path, io.BytesIO]]`
        Where the blurpified images goes.
        Specify either a string to the output path, the path itself, or a io.BytesIO container.

        If not provided, the program will either use the path as the input
        or return a new io.BytesIO container with the new data depending on
        what was given for the input.
    blurple_type: `BlurpleType`
        What type of blurple should be used. Defaults to the old blurple.
    enhancements: `bool`
        Whether to apply enhancements to the image.

        For the new blurple, this makes it look generally nicer.
        For the old blurple, this makes it look much more like the original version.
        This does not make it 1:1 to it (as Pillow grayscales images in a different way),
        but it does make it closer.

        Defaults to `True`.

    Returns
    ----------
    `Union[str, pathlib.Path, io.BytesIO]`
        Returns whatever the value was for `img_output` or the auto-generated value for it.
        This output can be ignored if not desired.
    """

    if not img_output:
        if isinstance(img_input, (str, pathlib.Path)):
            img_output = img_input
        elif isinstance(img_input, io.BytesIO):
            img_output = io.BytesIO()
        else:
            raise ValueError("Invalid input type!")

    return _blurpify(img_input, img_output, blurple_type, enhancements)
