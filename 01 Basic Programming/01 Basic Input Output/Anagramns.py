'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def map(s):
    the_map = {}
    for char in s:
        if char not in the_map:
            the_map[char] = 1
        else:
            the_map[char] += 1

    return the_map


def anagram(s1, s2):
    map1 = map(s1)
    map2 = map(s2)

    diff_cnt = 0
    for key in map2.keys():
        if key not in map1:
            diff_cnt += map2[key]
        else:
            diff_cnt += max(0, map2[key] - map1[key])

    for key in map1.keys():
        if key not in map2:
            diff_cnt += map1[key]
        else:
            diff_cnt += max(0, map1[key] - map2[key])

    return diff_cnt



n = int(input())
for x in range(n):
    s1 = input()
    s2 = input()
    print(anagram(s1, s2))
