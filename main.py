# this is a calculator
operations = ["addition","subtraction","multiplication","division"]
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
