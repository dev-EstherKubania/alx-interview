#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
"""

import sys
import signal


def print_stats(total_size, status_codes):
    """
    Print the computed statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing the count of lines for each status code.
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))

def signal_handler(sig, frame):
    """
    Handler for SIGINT signal (Ctrl+C).
    Prints the statistics and exits gracefully.
    """
    print_stats(total_size, status_codes)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            size = int(parts[-1])
            status_code = parts[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += size
            line_count += 1
            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0
        except ValueError:
            pass
except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    sys.exit(0)
