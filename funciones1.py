print("------------------------------")
print("-BUSCAR UN NUMERO EN CONJUNTO-")
print("------------------------------")

# input
n = int(input("Numero a buscar: "))

# processing
a = [1,2,3,4,5]
r = False
for i in a:
    if i == n:
        print("Lo encontrĂ©")
        r = True
if r == False:
    print("No lo encontrĂ©")

# output
print("\nEso era...")