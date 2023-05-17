#!/usr/bin/python3
""" a modlue housing the log parsing function """


def validUTF8(data) -> bool:
    """ a function to validate utf-8 """

    if data is None:
        return False

    if None in data:
        return False

    for i in data:
        if i < 128:
            continue
        elif i in range(128, 256):
            # false becase in 1 byte MSB must be 0
            return False
        elif i in range(256, 65536):
            # convert i to 16 bit binary
            bin_int = bin(i)[2:].zfill(16)

            # separate binary in 8bit sections
            bin_list = [bin_int[:8], bin_int[8:]]

            # check first and consective bytes for proper starting
            if bin_list[0][:3] != '110' or bin_list[1][:2] != '10':
                return False
            # repeat similar logic upto end of utf8 range end
        elif i in range(65535, 16777215):
            bin_int = bin(i)[2:].zfill(24)
            bin_list = [bin_int[:8], bin_int[8:16], bin_int[16:]]
            # print(f'bin_list = {bin_list}, bin_int = {bin_int}, i ={i}')
            if bin_list[0][:4] != '1110':
                return False
            if bin_list[1][:2] != '10' or bin_list[2][:2] != '10':
                return False
        elif i in range(16777215, 4294967295):
            bin_int = bin(i)[2:].zfill(32)
            bin_list = [bin_int[:8],
                        bin_int[8:16],
                        bin_int[16:24],
                        bin_int[24:]]
            # print(f'bin_list = {bin_list}, bin_int = {bin_int}, i ={i}')
            if bin_list[0][:5] != '11110':
                return False
            if bin_list[1][:2] != '10' or bin_list[2][:2] != '10':
                return False
            if bin_list[3][:2] != '10':
                return False
        elif i >= 4294967295:
            # out of utf8 range
            return False

    return True
