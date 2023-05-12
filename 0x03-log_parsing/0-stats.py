#!/usr/bin/python3
"""a log parsing interview answer"""
import sys
from typing import Optional, Union, List
from datetime import datetime


def check_ip(ip: str) -> bool:
    """ returns true if ip is correct """
    if ip is None:
        return False

    ip_list = ip.split('.')
    if len(ip_list) != 4:
        return False
    for ips in ip_list:
        try:
            if int(ips) < 1 or int(ips) > 255:
                return False
        except ValueError:
            return False
    return True


def check_date(year: str, time: str) -> bool:
    """ returns true if date is in the correct format """

    if year is None or time is None:
        return False

    date = year + ' ' + time
    format = "%Y-%m-%d %H:%M:%S.%f"
    date = date.replace(date[0], "")
    date = date.replace(date[-1], "")
    try:
        date_format = datetime.strptime(date, format)
    except ValueError:
        return False

    if date_format > datetime.now():
        return False
    return True


def check_code(code: str) -> Union[bool, int]:
    """ checks if code is in correct format """
    if code is None:
        return False

    code_list = [200, 301, 400, 401, 403, 404, 405, 500]

    try:
        code_no = int(code)
        if code_no not in code_list:
            return False
    except ValueError:
        return False

    return code_no


def check_size(size: str) -> Union[bool, int]:
    """ checks if the size is in correct format """
    if size is None:
        return False

    try:
        int_size = int(size)
    except ValueError:
        return False

    return int_size


def check_line(line: str) -> Optional[List[int]]:
    """ checks the input line for conformity """
    # splits the str input using " " as delimter
    line_list = line.split()

    # checks no or argumets
    if len(line_list) > 9:
        return None

    # checks for proper ip address in IPV4 format
    if check_ip(line_list[0]) is False:
        return None

    # checks for correct character after IP adress
    if line_list[1] != '-':
        return None

    # checks for correct date format
    if check_date(line_list[2], line_list[3]) is False:
        return None

    # checks for correct Get request
    get_request = line_list[4] + ' ' + line_list[5] + ' ' + line_list[6]
    if get_request != "\"GET /projects/260 HTTP/1.1\"":
        return None

    # checks for correct status code
    code = check_code(line_list[7])
    if code is False:
        return None

    # checks for correct size
    size = check_size(line_list[8])
    if size is False:
        return None

    # if all checks pass returns size and code
    return [code, size]


if __name__ == "__main__":
    line_count = 0
    size = 0
    code_dict = {200: 0, 301: 0, 400: 0, 401: 0,
                 403: 0, 404: 0, 405: 0, 500: 0}
    for line in sys.stdin:

        # uses different functions to check for correct line input
        cline = check_line(line)

        # if input line is incorrect continues to next line else it counts it
        if cline is None:
            continue
        else:
            # counts the number of lines
            line_count += 1
            # adds current size to last counted sizes
            size += cline[1]
            code_dict[cline[0]] += 1

        # if 10 line are properly checked
        if line_count == 10:
            print(f'File size: {size}')
            for key, values in code_dict.items():
                if values != 0:
                    print(f'{key}: {values}')
                    code_dict[key] = 0
            line_count = 0
            size = 0
