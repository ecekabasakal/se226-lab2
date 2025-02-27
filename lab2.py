x = input("please enter a number : ")
x = int(x)
for x in range (1,x+1):
  print ('*'*x)
  for x inr range (x-1,0,-1):
  print ('*'*x)
