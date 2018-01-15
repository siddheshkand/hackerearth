'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
div = input().split(" ")
l = int(div[0])
r = int(div[1])
k = int(div[2])

counter = 0
for x in range(l, r + 1):
    if x % k == 0:
        counter += 1
print(counter)
