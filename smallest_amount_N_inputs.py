N=int(input())
small=9999999
for i in range(N):
    num=int(input())
    if small>num:
        small=num
    print(small)
"""
input:3
32
6
29
output:
32
6
6
"""
