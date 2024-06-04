# 計算f(n)= 1 + 2 + 3+ .. + n-1 + n
def f(n):
   if n==1:
       return 1
   he = f(n-1)+n
   return he

print(f(3))