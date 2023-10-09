import numpy as np
import matplotlib.pyplot as plt
def func1(n): 
    return n**3 
def func2(n): 
    return (2*n**3) + (90*n**2) - (5*n) + 6046 
def func3(n): 
    return 100*n**3 
x = np.arange(1, 11) 
y1 = [func1(i) for i in x] 
y2 = [func2(i) for i in x] 
y3 = [func3(i) for i in x] 
plt.plot(x,y1) 
plt.plot(x,y2) 
plt.plot(x,y3) 
plt.title("n^3<2n^3 + 90n^2 - 5n + 6046<100n^3") 
plt.xlabel("n") 
plt.ylabel("y") 
plt.show() 
