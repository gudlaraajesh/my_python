'''Check if the given regex pattern is valid or not'''
import re

# pat = r'.*\+'
# pat = r'.*+'
t = int(input())
for i in range(t):
    pat = input()
    try:
        re.compile(pat)
        print(True)
    except:
        print(False)

