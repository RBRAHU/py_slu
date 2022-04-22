from sqlalchemy import true


num=int (input("enter any number"))



if num > 1:
      for i in range(2,num):
            if (num%2==0):
              print("the number is not a prime number")
              break

            else:
                print("the number is prime number")
                break

else:
    print ("the number is not a prime number")
    