import io
import pathlib
import typing

from PIL import Image
from PIL import ImageEnhance

from .blurple_map import blurplify_map


def _blurplify(
    img_input: typing.Union[str, pathlib.Path, io.BytesIO],
    img_output: typing.Union[str, pathlib.Path, io.BytesIO],
    enhancements: bool = False,
):
    """The part that actually blurpifies images."""
    try:
        img = Image.open(img_input)
        format = img.format  # just in case

        if img.is_animated:  # currently does not support animated GIFs
            raise ValueError("Cannot process animated GIFs!")

        if enhancements:
            """The original version, being made in C++, used a different
            method to grayscale compared to Pillow.
            While we cannot replicate the old grayscale 1:1, we can do
            a couple of touch-ups that makes the resulting image closer to it.
            """
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.25)
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(0.95)

        # converts image to grayscale
        img = img.convert("LA")
        img = img.convert("RGBA")

        data = img.getdata()
        # gets the blurple value based on the grayscale color, then re-adds the alpha channel
        new_data = tuple(blurplify_map[p[0]] + tuple([p[3]]) for p in data)
        img.putdata(new_data)

        img.save(img_output, format=format)
        return img_output
    finally:
        img.close()


def convert(
    img_input: typing.Union[str, pathlib.Path, io.BytesIO],
    img_output: typing.Optional[typing.Union[str, pathlib.Path, io.BytesIO]] = None,
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
    enhancements: `bool`
        Whether to apply enhancements to the image to make it more like the original version.
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

    return _blurplify(img_input, img_output, enhancements)
