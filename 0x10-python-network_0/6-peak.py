#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Lists integers to find peak and returns list of peak or None."""
    size = len(list_of_integers)
    mid_nm = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        mid_nm = mid_nm // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_nm // 2 == 0:
                mid_nm = 2
            mid = mid + mid_nm // 2
        elif mid_nm > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_nm // 2 == 0:
                mid_nm = 2
            mid = mid - mid_nm // 2
        else:
            return list_of_integers[mid]
