# Write your solution for 1.2 here!
# sum = 0


# for i in range(101):
# 	if i % 2 == 0:
# 		sum+= i
# print(sum)

for i in range(1000):
	if (i % 6 == 2) and ((i**3) % 5 == 3):
		print(i)