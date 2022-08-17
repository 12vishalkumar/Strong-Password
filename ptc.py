import math
import os
import random
import re
import sys
# Complete the 'minimumNumber' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    c1 = max(0, 6-n)
    c2 = 0
    if not any(i in password for i in numbers):
        c2 += 1
    if not any(i in password for i in lower_case):
        c2 += 1
    if not any(i in password for i in upper_case):
        c2 += 1
    if not any(i in password for i in special_characters):
        c2 += 1
    return max(c1, c2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)
    fptr.write(str(answer) + '\n')
    fptr.close