# Question: Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)

'''
Expected output: 
5
7
9
'''
print (a[0] + b[0], '\n',a[1] + b[1], '\n',a[2] + b[2])

# 2nd and write solution zip method
for x, y in zip(a,b):
    print(x+y)