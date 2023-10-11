#!/usr/bin/python3
""""Write a script to stdin."""


def print_stats(size, status_codes):
    """
    A script that reads stdin line by line
    and computes metrics

    """
    print("File size: {}".format(size))
    for key in sorted(status_code):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '500']
    count = 0

    try:
        for line in sys.stdin:
            line = line.split()

            try:
                status_code = int(line[-2])
                if status_code in valid_codes:
                    status_codes[status_codes] = status_codes.get
                    (status_code, 0) + 1
                size += int(line[-1])
            except (ValueError, IndexError)
            pass
    except KeyboardInterrupt:
        pass
    print_stats(size, status_codes)
