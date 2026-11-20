"""Sum up 19 November 2026 world news in one image.

Entry for make.fun bounty news-image-20261119.

The program copies the finished front-page image shipped in this
repository (entry.png, 1024x1024, under 1 MiB) to /output/entry.png.
It uses only the Python standard library, makes no network calls,
uses no wall-clock time and no randomness, so two runs write
byte-identical output.
"""

import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    # Validate what we wrote: a real PNG, at most 1 MiB, as the
    # bounty gate requires. Fail loudly instead of shipping a
    # truncated or oversized file.
    data = destination.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if len(data) > 1_048_576:
        raise ValueError("entry.png is larger than 1 MiB")


if __name__ == "__main__":
    main()
