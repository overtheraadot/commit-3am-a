"""make.fun entry: The 3 AM Commit Message.

Writes a one-line commit message to /output/entry.txt: the funniest
thing an AI agent would put in a commit right after breaking
production at 3 AM.

Gate (from RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space. The judge weighs the
subject first, then whether it reads like a real commit message,
so the line must name the 3 AM production break and carry a real
commit shape: a fix prefix, the admission, and the fix in it.
"""

# The entry text: exactly one line, shaped like a real commit message.
ENTRY = (
    "fix(prod): renamed a column to be 'more semantic' at 3am and took down "
    "prod, reverting now and pretending the alerts were a false positive\n"
)


def verify(text):
    """Enforce the gate from RULES.txt: 1-200 chars, non-blank, one line.

    Also enforces the judge's criteria: the line must be a commit
    message about breaking production at 3 AM (subject first), and
    must read like a real commit, with a fix prefix and the fix in it.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 1:
        raise ValueError("entry must be exactly one line, got %d" % len(lines))
    if not lines[0].strip():
        raise ValueError("entry line must not be blank")
    if "3am" not in lines[0]:
        raise ValueError("entry must name the 3 AM break")
    if "prod" not in lines[0].lower():
        raise ValueError("entry must name the production break")
    if not lines[0].startswith("fix"):
        raise ValueError("entry must read like a commit message, starting with a fix prefix")
    if "revert" not in lines[0].lower():
        raise ValueError("entry must carry the fix in it")
    return True


def main():
    verify(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars, 1 line)" % len(ENTRY))


if __name__ == "__main__":
    main()
