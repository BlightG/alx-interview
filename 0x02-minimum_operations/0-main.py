#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 3
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 27
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 81
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 243
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 486
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 972
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))