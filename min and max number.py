a1 = int(input("The value of a1 is : "))
a2 = int(input("The value of a2 is : "))
a3 = int(input("The value of a3 is : "))
a4 = int(input("The value of a4 is : "))
b = int(input("The comparison value is : "))
if ((a1+a2)==b):
    print("The values {0} and {1} are the values which comes with 8". format(a1,a2))
else:
    if (a1+a3==b):
        print("The values {0} and {1} are the values which comes with 8".format(a1, a3))
    else:
        if(a1+a4==b):
            print("The values {0} and {1} are the values which comes with 8".format(a1, a4))
        else:
            if(a2+a3==b):
                print("The values {0} and {1} are the values which comes with 8".format(a2, a3))
            else:
                if(a2+a4==b):
                    print("The values {0} and {1} are the values which comes with 8".format(a2, a4))
                else:
                    if(a3+a4==b):
                        print("The values {0} and {1} are the values which comes with 8".format(a3, a4))
                    else:
                        print("None is matching")