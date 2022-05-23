import matplotlib.pyplot as plt
import numpy as np

# X: Digital Image Matrix
X = [[9, 7, 1, 1, 1, 2, 2, 1],
     [8, 9, 9, 7, 1, 1, 1, 1],
     [7, 8, 9, 7, 1, 2, 1, 1],
     [8, 9, 9, 9, 9, 1, 1, 2],
     [8, 9, 9, 7, 7, 2, 1, 3],
     [9, 9, 9, 9, 8, 2, 2, 1],
     [9, 9, 8, 8, 7, 1, 2, 1],
     [8, 9, 8, 6, 5, 1, 1, 3]
    ];

#Size of X
MN = len(X) * len(X)

n = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

#
h = []

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

for i in range(len(X)) :
    for j in range(len(X[0])) :
        n[X[i][j]] += 1

for r in n:
    h.append(r / MN)
    print(r / MN,  end = ' ');

print()
    
x = np.array(a)
y = np.array(h)

plt.title("Histogram")    
plt.bar(x,y)
plt.show()

plt.show()

#
p = []

b = []

sum = 0;

b_min = 1
b_max = 9

for m in h:   
    sum += m
    b.append((b_max - b_min) * sum + b_min)
 
for n in b:
    print(n, end  = ' ')

e_X = [[],[]]

#for i in range(len(X)) :
#    for j in range(len(X[0])) :
#        e_X[a[i][j]] = b[i][j]
#        print(e_X, end  = ' ')
#    print()