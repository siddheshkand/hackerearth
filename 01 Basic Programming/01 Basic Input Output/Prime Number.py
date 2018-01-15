'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def is_prime(n):
    if n == 1:
        return False
    for x in range(2, (n // 2) + 1):
        if n % x == 0:
            return False
    else:
        return True


n = int(input())
for x in range(2, n):
    if is_prime(x):
        print(x, end=" ")
