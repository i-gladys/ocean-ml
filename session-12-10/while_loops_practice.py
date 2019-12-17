
# 1. Use a while loop to print numbers 1-10:
#i = 0

#while i < 11:
	#print(i)
	#i+=1
# 2. Use a while loop to print the first 10 multiples of 24:
#i = 0
#while i < 10 :
	#print (24*i)
	#i+=1
# 3. Use a while loop to find the average of these numbers:
numbers = [10,42,-2, 900,5,8,39]
print(numbers[1])
#c = 0
#for i in numbers:
	#c+=i
	#print(c)

#print(c/7)
i = 0
total = 0
while i < len(numbers):
	total += numbers[i]
	i+=1

print(total)
average = total/len(numbers)

print(average)

