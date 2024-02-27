print("1) This is a file created in local repo.")
a = 0
for i in range(0, 5):
    a = a+i
    if a > 0:
        print(a)
print("2) This is a file edited by emp1 branch")
b = 5
print(a+b)
print("value in emp1",a+b)
print("3) Changes made in emp2 branch")
a = 0
b = 5
c = a+b
for i in range(0, 5):
    a = a+i
    if a > 0:
        print(a)
        print("Inside the if loop:", c)
    print("outside if loop:", c)
print("4) This line is added in emp1 to create a conflict between emp1 and emp2")

