#!/usr/bin/env python3
"""
Convert legacy log format (pre-0.4.0) into unified diagnostics format.
Original format:
[LEVEL] [timestamp] - message
New format:
{ "level": "...", "ts": "...", "msg": "..." }
"""

import re
import json
import os

SOURCE_FILE = "legacy/dump_summary_2020.log"
TARGET_FILE = "converted/trace_2020.jsonl"

def parse_line(line):
    match = re.match(r"\[(\w+)\] ([\d-]+ [\d:]+) - (.*)", line)
    if match:
        return {
            "level": match.group(1),
            "ts": match.group(2),
            "msg": match.group(3)
        }
    return None

def convert():
    os.makedirs(os.path.dirname(TARGET_FILE), exist_ok=True)
    with open(SOURCE_FILE, 'r') as src, open(TARGET_FILE, 'w') as tgt:
        for line in src:
            parsed = parse_line(line)
            if parsed:
                json.dump(parsed, tgt)
                tgt.write('\n')

if __name__ == "__main__":
    print("Converting legacy logs...")
    convert()
    print("Done.")
