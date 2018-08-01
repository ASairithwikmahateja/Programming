varA = input("enter num  ")
varB = input("enter another num  ")
if (varA.isnumeric() and varB.isnumeric()):
	if(varA>varB):
	 	print("bigger")
	elif(varA==varB):
		print("equal")
	else:
		print("lesser")
else:
	print("String involved")