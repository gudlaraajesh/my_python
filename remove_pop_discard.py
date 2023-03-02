'''
Task
You have a non-empty set , and you have to execute  commands given in  lines.
The commands will be pop, remove and discard.

Input Format

The first line contains integer N, the number of elements in the set S.
The second line contains n space separated elements of set S. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next  lines contains either pop, remove and/or discard commands followed by their associated value.

Output Format

Print the sum of the elements of set  on a single line.

Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output

4 '''


n = int(input())
s = set(map(int, input().split()))
no_of_cmds = int(input())

for i in range(no_of_cmds):
    str = input().split(" ")   
    if str[0] == 'remove':
        s.remove(int(str[1]))
    elif str[0] == 'discard':
        s.discard(int(str[1]))
    elif str[0] == 'pop':
        s.pop()
    
print(sum(s))
    