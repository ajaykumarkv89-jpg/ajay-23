import matplotlib.pyplot as p
p.title("cubic time complexity")
p.xlabel("input size")
p.ylabel("steps")
x=list(range(1,101))
y=[y**3 for y in x]
p.plot(x,y,'b',label='o(n^3)')
p.legend()
p.show()

print(x)
print(y)