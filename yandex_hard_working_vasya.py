n,k = tuple(map(int,input().strip().split(' ')))
num_list = list(map(int,input().strip().split(' ')))

def count_days(some_list,N = n):
	if N == 0:
		return 0
	elif N == 1:
		return 1

	Max = max(some_list)
	Min = min(some_list)

	if Max-Min <= k:
		return N
	else:
		day_count = 0
		elements = [some_list[0]]
		R = 1
		while R < N:
			if some_list[R] - elements[-1] > k:
				popped_el = some_list.pop(R)
				elements.append(popped_el)
				N -= 1
			else:
				R += 1

		del some_list[0]
		N -= 1

		day_count += 1 + count_days(some_list,N = N)
		return day_count

num_list.sort()
print(count_days(num_list,N = n))

#k = 1
#[1,2]
#els = [1]
#R = 1
#N = 2



