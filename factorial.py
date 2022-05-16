b = input ("ingrese un numero")
print (b)
cont = 1;
facto = int(b)

while(cont < int(b)):
    
    facto = facto  * (int(b) - cont)
    print(facto)
    cont = cont + 1
print(facto)

