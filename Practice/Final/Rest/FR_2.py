def func(x):
    x[0]=x[0]+10
    print("inside function:",x)
x=[10,20]
print("before function call:",x)
func(x)
print("after function call:",x)
