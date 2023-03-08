'''The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.

Sample Input:

7
UK
China
USA
France
New Zealand
UK
France 

Sample Output:

5
'''

s = set()
n = int(input())
for i in range(n):
    c = input()
    s.add(c)

print(len(s))