flag =True
while flag:
    try:
        num=int(input( "enter the number"))
        num1=int(input( "enter the number"))
        print ("division result " ,num/num1)
    except ZeroDivisionError as e:
        print("enter a valid divisor")
        print(e)
    except ValueError as ve:
        print("enter a integer value")
        print(ve)
    else:
        flag=False
    
