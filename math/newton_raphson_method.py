err = 1e-6
square = 99
x0 = 1
cnt = 0
while abs(x0**2 - square) > err:
  cnt += 1
  x1 = x0 - (x0**2 - square) / (2*x0)
  x0 = x1
print(x0, x0 **2)
print(cnt)
