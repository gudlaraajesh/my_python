'''
Task

Perform append, pop, popleft and appendleft methods on an empty deque .

Input Format

The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Output Format

Print the space separated elements of deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop 
popleft 
Sample Output

1 2
'''

from collections import deque
n = int(input())

d = deque()

for i in range(n):
    fields = input().split(" ")
    if fields[0] == 'append':
        d.append(int(fields[1]))
    elif fields[0] == 'appendleft':
        d.appendleft(int(fields[1]))
    elif fields[0] == 'pop':
        d.pop()
    elif fields[0] == 'popleft':
        d.popleft()

for i in range(len(d)):
    print(d[i],end=" ")


# d =deque()
# n = int(input())

# # Open the file for reading
# with open('input_file.txt', 'r') as file:
#     # Loop over each line in the file
#     for line in file:
#         # Process the line     
#         fields = line.split(" ")
#         if fields[0] == 'append':
#             d.append(int(fields[1]))
#         elif fields[0] == 'appendleft':
#             d.appendleft(int(fields[1]))
#         elif fields[0] == 'pop':
#             d.pop()
#         elif fields[0] == 'popleft':
#             d.popleft()

# for i in range(len(d)):
#     print(d[i],end=" ")