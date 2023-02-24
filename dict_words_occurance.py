'''
Input Format

The first line contains the integer, N.
The next N lines each contain a word.

Output Format

Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input:

4
bcdef
abcdefg
bcde
bcdef

Sample Output:

3
2 1 1
'''
d = {}
n = int(input())
for i in range(n):
    word = input()
    if word in d.keys():
        d[word] += 1
    else:
        d[word] = d.setdefault(word, 1)

# To find the last key in the dict
last_key = list(d.keys())[-1]
print(last_key)

print(len(d))
for k,v in d.items():
    if k != last_key:
        # print(k)
        print(v, end=" ")
    else:
        print(v, end="")

