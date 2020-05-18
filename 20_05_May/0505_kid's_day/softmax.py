import numpy as np
import matplotlib.pyplot as plt
 
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()
 
x = np.array([1.0,1.0,2.0])
 
y = softmax(x)
print(y)
 
print(np.sum(y))
 
ratio = y
labels = y
 
plt.pie(ratio, labels=labels, shadow=True, startangle=90)
plt.show()

