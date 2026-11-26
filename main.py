#!/usr/bin/env python3
"""news-image-20261125 — entrypoint.

The picture itself (entry.png, 1024x1024) was drawn by a Pillow program
from a story slate in which every item was checked against its
originating wire report dated Wednesday 25 November 2026. This
entrypoint's one job is to deliver those exact bytes to the grader:
copy entry.png from this repository to the output directory
($MAKEFUN_OUTPUT_DIR, default /output) and prove the copy is intact.

Python 3.13, standard library only. No network. Deterministic: the
bytes written are the bytes in the repository, verified by SHA-256.
"""

import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)
    # The two grader runs must produce identical bytes: fail loudly if
    # what landed on disk is not exactly what the repository holds. A
    # size check alone would miss a same-length corruption, so compare
    # the full SHA-256 of the written file against the source bytes.
    with open(dst, "rb") as f:
        written = f.read()
    assert hashlib.sha256(written).digest() == hashlib.sha256(data).digest(), (
        "copied image bytes differ from entry.png"
    )
    print("wrote", dst, len(written), "bytes, sha256 verified")


if __name__ == "__main__":
    main()
