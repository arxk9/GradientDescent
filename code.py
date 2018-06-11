import math
import numpy as np
from matplotlib import pyplot as plt

def f(input):
    x = input[0]
    y = input[1]
    #return 4*x**2-3*x*y+2*y**2+24*x-20*y
    #return (1-y)**2+100*(x-y**2)**2
    #return 20 + x**2 - 10*math.cos(2*math.pi*x) + y**2 - 10*math.cos(2*math.pi*y)
    return (x+2*y-7)**2+(2*x*y-5)**2
    
def gradient(input):
    x = input[0]
    y = input[1]
    x_gradient = -(2*(x+2*y-7)+4*(2*x+y-5))#-(2*x + 10*math.sin(2*math.pi*x)*2*math.pi)#-(200*(x-y**2))#-(8*x-3*y+24)
    y_gradient = -(4*(x+2*y-7)+2*(2*x+y-5))#-(2*y + 10*math.sin(2*math.pi*y)*2*math.pi)#-(-2*(1-y)-400*y*(x-y**2))#-(-3*x+4*y-20)
    return np.array([x_gradient,y_gradient])

input = 20*np.random.random(2)-10
l = 0.01
x = []
y = []
for i in range(20):
    x.append(l)
    count = 0
    input = 20*np.random.random(2)-10
    while math.sqrt(gradient(input)[0]**2+gradient(input)[1]**2)>0.01:
        print("error",math.sqrt(gradient(input)[0]**2+gradient(input)[1]**2))
        input += gradient(input)*l
        print(input)
        count += 1
    y.append(count)
    l += 0.005

plt.plot(x,y)
plt.show()
