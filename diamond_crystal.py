N=int(input())
for i in range(1,N+1):
    left_space=" "*(N-i)
    hollow=" "* (2*i-2)
    print(left_space+"/"+hollow+"\\")
for i in range(1,N+1):
    left_space=" "*(i-1)
    hollow=" "* 2*(N-i)
    print(left_space+"\\"+hollow+"/")
"""
input:5
output:
    /\
   /  \
  /    \
 /      \
/        \
\        /
 \      /
  \    /
   \  /
    \/
"""
