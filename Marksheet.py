# Byte-compiled / optimized / DLL files
a=int(input(" Enter a Marks of English = "))
b=int(input(" Enter a marks of Maths = "))
c=int(input(" Enter a marks of Physics = "))
d=int(input(" Enter a marks of Chemistry = "))
e=int(input(" Enter a marks of Computer = "))
f=int(input(" Enter a marks of  Hindi = "))

P=(((a+b+c+d+e+f)/600)*100)
print(P)
if P>=90:
    print(" The result is A++ ")

elif P>=80 and P<90  :
    print("The result is B++ ")
    
else :
    print("The result is less than B")
    
