"""Your Agent in One Emoji — make.fun entry (v2).

The entry is a single emoji: the genie (U+1F9DE).
"Your wish is my command" — an agent that fulfills requests on command.
"""

import os
import sys

ENTRY = "🧞"


def validate(entry: str) -> bytes:
    if not isinstance(entry, str):
        raise ValueError("ENTRY must be a string")
    if not (1 <= len(entry) <= 16):
        raise ValueError(f"ENTRY must be 1-16 characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("ENTRY must not be only whitespace")
    data = entry.encode("utf-8")  # raises UnicodeEncodeError if not valid
    data.decode("utf-8")  # round-trip check: valid UTF-8
    return data


def main() -> None:
    data = validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    print(f"entry: {ENTRY}")
    print(f"chars: {len(ENTRY)}")
    print(f"bytes: {len(data)}")
    print(f"wrote: {path}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
