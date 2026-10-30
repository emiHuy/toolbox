import argparse
from pathlib import Path

from PIL import Image


def parse_args():
    parser = argparse.ArgumentParser(
        prog="iconify",
        description="Convert PNG/JPEG images into multi-resolution ICO files.",
        add_help=True,
    )

    parser.add_argument("input", type=Path, help="Input image path (PNG/JPG)")

    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output ICO file (defaults to input filename with .ico)",
    )

    parser.add_argument(
        "-s",
        "--sizes",
        type=str,
        default="64",
        help="Comma-separated icon sizes (default: 64)",
    )

    parser.add_argument(
        "--crop", action="store_true", help="Center-crop the image to a square"
    )

    parser.add_argument(
        "--no-upscale",
        action="store_true",
        help="Don't enlarge images smaller than the requested size",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if not args.input.is_file():
        raise SystemExit(f"Error: Input file not found: {args.input}")

    output = args.output or args.input.with_suffix(".ico")

    try:
        sizes = [int(s.strip()) for s in args.sizes.split(",")]
        if not sizes or any(s <= 0 or s > 256 for s in sizes):
            raise ValueError
    except ValueError:
        raise SystemExit("Error: Sizes must be between 1 and 256.")

    with Image.open(args.input) as img:
        img = img.convert("RGBA")

        if args.crop:
            width, height = img.size
            side = min(width, height)
            left = (width - side) // 2
            top = (height - side) // 2
            img = img.crop((left, top, left + side, top + side))

        if args.no_upscale:
            sizes = [s for s in sizes if s <= min(img.size)]

        if not sizes:
            raise SystemExit("Error: No valid sizes to generate.")

        img.save(output, format="ICO", sizes=[(s, s) for s in sizes])


if __name__ == "__main__":
    main()
