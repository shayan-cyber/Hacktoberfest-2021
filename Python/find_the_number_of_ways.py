'''
A man has money/coins in two different bags. He visits the market to buy some items.
Bag A has N coins and Bag B has M coins. The denominations of the money are given as
array elements in a[] and b[]. He can buy products only by paying an amount which is
an even number by choosing money from both the bags. The task here is to find the number
of ways the man can buy items such that the product of money from bothn bags is an even number.
The man has to pick one coin atleast from each bag to make an even number product.

Example:

Input:
3 - Value of N
3 - Value of M
{1,2,3} -- [a] elements a[0]-a[N-1], where each element input is separated by new line
{5,6,7} -- [b] elements b[0]-b[M-1], where each element input is separated by new line

Output:
5 - Number of ways he can get an even product of coins.
'''
n = int(input())
m = int(input())
a_list=[]
b_list=[]
for i in range(n):
    a = int(input())
    a_list.append(a)
for i in range(m):
    b = int(input())
    b_list.append(b)
ans=[]
for i in a_list:
    for j in b_list:
        mul = i*j
        if mul % 2 ==0:
            ans.append(mul)
print(len(ans))