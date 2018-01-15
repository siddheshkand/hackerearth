'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
L = int(input())
N = int(input())

for x in range(N):
    dim = input().split(" ")
    width = int(dim[0])
    height = int(dim[1])
    if width < L or height < L:
        print("UPLOAD ANOTHER")
    elif width >= L and height >= L:
        if height == width:
            print("ACCEPTED")
        else:
            print("CROP IT")
