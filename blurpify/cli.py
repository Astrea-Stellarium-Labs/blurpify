import argparse
import pathlib
import time

import blurpify


def main():
    def path_check(path):
        possible_path = pathlib.Path(path)
        if possible_path.exists():
            return possible_path
        else:
            raise ValueError(f"Path '{path}' does not exist.")

    parser = argparse.ArgumentParser(description="Blurpify an image!")
    parser.add_argument("input_image", type=path_check, help="Image to blurpify.")
    parser.add_argument(
        "output_image",
        type=path_check,
        help="Where the blurpified image should end up.",
        nargs="?",
        default=None,
    )
    parser.add_argument(
        "-noe",
        "--noe",
        "-noenhancements",
        "--noenhancements",
        action="store_true",
        help="If the image should not be enhanced to look nicer.",
    )

    start_time = time.perf_counter()

    args: argparse.Namespace = parser.parse_args()
    input_image = args.input_image
    output_image = args.output_image
    enhancements = not args.noe

    blurpify.convert(input_image, output_image, enhancements)

    end_time = time.perf_counter()
    time_taken = round(((end_time - start_time) * 1000), 2)
    print(f"Finished in {time_taken}ms.")


if __name__ == "__main__":
    main()
