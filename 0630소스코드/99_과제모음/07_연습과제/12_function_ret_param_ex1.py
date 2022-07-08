def add(a,b) :
    return a+b
def sub(a,b) :
    return a-b
def mul(a,b) :
    return a*b
def div(a,b) :
    return a/b

a = 9
b = 3

print(str(a) + " + " + str(b) + ' = ' + str(add(a,b)))
print(str(a) + " - " + str(b) + ' = ' + str(sub(a,b)))
print(str(a) + " * " + str(b) + ' = ' + str(mul(a,b)))
print(str(a) + " / " + str(b) + ' = ' + str(int(div(a,b))))
