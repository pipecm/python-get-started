response = {}
response["code"] = 200
response["message"] = "OK"

print(response)
print(response.keys())
print(response.values())
print(response.items())
print(str(response))

a = 2
b = 1
print(a + b)
print(a - b)
print(a * b)
print(a / b)

a = 5
b = 3
print(a % b)
print(a ** b)
print(a // b)

if (a > b) : print("a > b")
elif (a == b) : print("a = b")
else : print("a < b")

myList = [3,6,3,8,1,2,9,6,8,9,7,4]

sum = 0
for x in myList :
    sum += x

print ("Suma: " + str(sum))

verdadero = True
falso = False

print(verdadero and falso)
print(verdadero or falso)