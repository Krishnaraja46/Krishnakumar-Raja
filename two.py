a=14
b=((a-5)*8+100)
c=int(input("Enter the number"))
if(a<=5 and c==0):
	print(100)
elif(a<=5 and c==1):
	print(125)
d=(0.25*b)
if(a>5 and c==0):
	print(b)
elif(a>5 and c==1):
	print(d+b)

