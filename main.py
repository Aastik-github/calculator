operations = ["addition","subtraction","multiplication","division","floor divison","remainder"]
a = input("please enter what you want to do out of addition,subtraction,multiplication,division -> ?")
b = int(input("please enter your first digit -> "))
c = int(input("please enter your second digit"))


if a == operations[0] :
   z = b+c
   print(f"the sum of your digits is: {z}")
elif a == operations[1]:
   x = b-c
   print(f"the differnce of your digits is : {x}")
elif a == operations[2]:
  v = b*c
  print(f"the product of your digits is : {v}")
elif a == operations[3]:
  n = b/c
  print(f"the quoitent of your digits is : {n}")
elif a == operations[4]:
    q = b//c
    print(q)
elif a == operations[5]:
     o == b%c
     print(o)
else:
    print(f"no operation named {a}")
    
