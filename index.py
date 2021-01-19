"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143  ?
"""

pf = [2]
goal = 20


for x in range(3,goal) :
	flag_pf = True
	for y in pf:
		if x % y == 0 :
			flag_pf = False
			break	
	
	if flag_pf :
		pf.append(x)


print (pf)

			


