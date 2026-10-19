#!/usr/bin/env python3
"""Apply a page's key.json to its signs.txt and print the literal plaintext.

    python3 decode/decode.py data/f385r/key.json data/f385r/signs.txt            # one stream
    python3 decode/decode.py data/f385r/key.json data/f385r/signs.txt --by-line  # one row per line

Python 3 standard library only. The key (pipeline[0].table) gives each sign name its value:
a letter, a group of letters or a short word (a sign such as "plus"), or a list of values for a
sign that stands for more than one letter (L = a or n; f = i or s; xbar = s or ss; rC = s or z).
For those, key.json records which value was taken at every occurrence ("choices", in reading
order over the whole page), so nothing is guessed here. A sign with no value in the key prints
as [?name] in the stream and as a middle dot (·) in the by-line output.
"""
import argparse
import json
import sys


def read_signs(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            if raw.strip() and not raw.startswith("#"):
                line, _, signs = raw.rstrip("\n").partition("\t")
                rows.append((int(line), signs.split()))
    return rows


def decode(rows, key, unknown=None):
    step = key["pipeline"][0]
    table, choices = step["table"], step.get("choices", {})
    if unknown is None:
        unknown = step.get("unknown_render", "[?{sym}]")
    used = {}
    out = []
    for line, signs in rows:
        text = []
        for s in signs:
            entry = table.get(s) or {}
            value = entry.get("v")
            if isinstance(value, list):
                k = used.get(s, 0)
                used[s] = k + 1
                lst = choices.get(s, [])
                choice = lst[k] if k < len(lst) else None
                if choice is not None and choice not in value:
                    sys.exit(f"choice {choice!r} for {s!r} is not one of {value}")
                value = choice
            text.append(unknown.replace("{sym}", s) if value is None else value)
        out.append((line, "".join(text)))
    for s, lst in choices.items():
        if used.get(s, 0) != len(lst):
            sys.exit(f"{len(lst)} choices recorded for {s!r}, {used.get(s, 0)} occurrences")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("key")
    ap.add_argument("signs")
    ap.add_argument("--by-line", action="store_true")
    a = ap.parse_args()
    with open(a.key, encoding="utf-8") as f:
        key = json.load(f)
    rows = read_signs(a.signs)
    if a.by_line:
        for line, text in decode(rows, key, unknown="·"):
            print(f"{line:>3} {text}")
    else:
        print("".join(text for _, text in decode(rows, key)))
