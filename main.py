a = float(input("enter celsius value: "))
b = fahrenheit = (9/5)*a + 32
print(a,"Celsius is ",b, "fahrenheit")
#convert area and volume
PI = 3.14
a,l = eval(input("enter the radius and length: "))
b = a*a*PI
print("The area is: ",b)
c = b*l
print("The volume is:",c)
#convert feet to meter
a = eval (input("Enter a value for feet: "))
b = a * 0.305
print(a,"feet is ",b,"meters")
#rate
a,b= eval(input("Enter the subtoal and gratutity rate: "))
gratutity = a*b/100
print("The gratuity is ",gratutity, "and the total is",gratutity+a)
a=eval(input("value: "))
digit1 = a % 10
a = a//10
digit2 = a % 10
a = a // 10
digit3 = a % 10
sum = digit1+digit2+digit3
print(sum)
# program to calculate energy
water= eval(input("Enter the amount of water in kilogram: "))
inittemp = eval(input("Enter the initial temperature: "))
finaltempp = eval(input("Enter the final tempertaure: "))
print("energy will be", water*(finaltempp - inittemp)*4184 )








