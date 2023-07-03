"""Time an date assignment."""

#!/bin/python3

from datetime import datetime
import math
import os
import random
import re
import sys


def parse_date_string(date):
    """Parse a date string."""
    date_format = "%a %d %b %Y %H:%M:%S %z"
    return datetime.strptime(date, date_format)


# Complete the time_delta function below.
def time_delta(t1, t2):
    """Time delta function."""
    t1 = parse_date_string(t1)
    t2 = parse_date_string(t2)
    delta = int((t1 - t2).total_seconds())
    return str(delta)


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t2, t1)

        print(delta + '\n')
