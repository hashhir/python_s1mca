try:
    a=int(input("enter an integer :"))
    if a>=90 and a<=120:
        print("success")
    else:
        raise ValueError ('abnormal condition')
except ValueError as ve:
    print(ve)
