x=17

y1=int(x)
y2=float(x)
y3=str(x)
y4=bool(x > 8)

print(y1,type(y1))
print(y2, type(y2))
print(y3, type(y3))
print(y4, type(y4))

text=str("The value of x is ") + str(y1)+str(".")
print(text)
