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

for k in range (10) :
    for i in range(len(X)) :
        for j in range(len(X[0])) :
            if (k == X[i][j]):
                n[k] += 1

for r in n:
    h = r /MN;
    print(h,  end = ' ');

#
b = []

sum = 0;

for m in a:   
    sum += m;   
    print(sum, end = ' ');   
    
x = np.array(a)
y = np.array(h)
    
plt.bar(x,y, width = 0.01)
plt.show()

plt.show()

