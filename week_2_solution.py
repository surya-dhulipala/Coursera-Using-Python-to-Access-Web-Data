# This program reads an existing file, pulls out al integers and calculates
# their total

import re # importing regular characters database

file = open('regex_sum_258793.txt') # Reading the file 'regex_sum_258793.txt'

lines = file.readlines()

totalSum = 0 # Creating total variable and storing value of 0

for line in lines:
    line = line.rstrip()
    nums = re.findall('([0-9]+)', line)

    if len(nums) > 0:
        nums = map(int, nums)
        localSum = sum(nums)
        totalSum += localSum

print (totalSum)
