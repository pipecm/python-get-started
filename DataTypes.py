x = 5
a = 5.2
b = "Hello world"

print("x es de tipo " + str(type(x)))
print("a es de tipo " + str(type(a)))
print("b es de tipo " + str(type(b)) + " de largo " + str(len(b)))

m = "manzana"

print(m[0])
print(m[1])

for x in range(0, len(m)):
    print(m[x])

print(m[2:4])
print(m[5:])
print(m[:5])

bln1 = "z" in m
bln2 = "s" in m
print(bln1)
print(bln2)

print("Este \ttexto \\ tiene \' cosas \" y \n otras cosas")

t1 = (1,2,3,4)
t2 = ("a","b","c")

print(t1)
print(t2)

list1 = [1, "a", 2, "b"]
print(list1)

login = { "user" : "pipecm", "password" : "python"}
print(login["user"])
print(login["password"])