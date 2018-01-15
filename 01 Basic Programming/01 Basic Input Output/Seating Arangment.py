'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

calc = [11, 9, 7, 5, 3, 1]


def pos(x):
    return {
        '1': "WS",
        '2': "MS",
        '3': "AS",
        '4': "AS",
        '5': "MS",
        '6': "WS",
        '7': "WS",
        '8': "MS",
        '9': "AS",
        '10': "AS",
        '11': "MS",
        '0': "WS",
    }[str(x)]


n = int(input())
for x in range(n):
    nos = int(input())
    seat = nos % 12
    if seat <= 6:
        if seat == 0:
            print(nos - 11, end=" ")
        else:
            print(nos + calc[seat - 1], end=" ")
    else:
        seat = seat - 6
        print(nos - calc[-seat], end=" ")
    print(pos(str(nos % 12)))
