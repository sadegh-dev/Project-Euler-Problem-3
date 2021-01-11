"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143  ?
"""
prime_factors = [2,]
counter = 3
the_number = 600851475143
while counter <= the_number :
	flag = 1
	for x in prime_factors :
		if counter % x == 0 :
			flag = 0
			break
	if flag == 1 :
		prime_factors.append(counter)
	counter += 1


#print(prime_factors)
print("largest prime factor of the number 600851475143 :"+ str(prime_factors[-1]))
