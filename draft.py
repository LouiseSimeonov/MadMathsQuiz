import random
import operator 
#for x in range(1):
  #print random.randint(1,101)

symbol = ['+', '-', '*', '/']
opstype = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
num1 = random.randint(0,12)
num2 = random.randint(0,10)
operation = random.choice(symbol)

print(num1)
print(num2)
print(operation)

maths = num1, operation, num2

print(maths)



#print(answer)

ops = opstype[operation]


answer = raw_input()
if int(answer) == ops(num1,num2):
	print("Yay!!! You're so clever!")
else: 
	print ("Try again")


print ops(num1,num2)

#figure out how to create random numbers -done 
#figure out how to create random sign 
#figure out how to create random sum? 
#figure out the raw input thingy 
