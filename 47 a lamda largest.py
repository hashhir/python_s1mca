large=lambda x,y:x if x>y else y
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print("Largest number : ",large(a,b))
div=lambda x:"Divisible" if x%5==0 else "Not divisible"
a=int(input("Enter a number : "))
print(div(a))
