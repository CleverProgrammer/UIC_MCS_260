from random import randrange

def most_common(my_list):
	max_num = my_list.count(my_list[-1])
	for element in my_list:
		my_list.count(element) > max_num
		max_num = my_list.count(element)
	return max_num

def ave_max_calc(C, H, D):
	busy_max = []

	for i in range(D):
		customers = []


		for i in range(C):
			print(customers)
			customers.append(randrange(0, H))

		busy_max.append(most_common(customers))

	return sum(busy_max) // len(busy_max)

print(ave_max_calc(50, 24, 100))