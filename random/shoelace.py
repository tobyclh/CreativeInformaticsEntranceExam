import numpy as np
def polygon_area(x,y):
    correction = x[-1] * y[0] - y[-1]* x[0]
    main_area = np.dot(x[:-1], y[1:]) - np.dot(y[:-1], x[1:])
    return 0.5*np.abs(main_area + correction)

x = [1,1,-1,-1]
y = [1,-1,-1,1]
print(polygon_area(x, y))