n,k = tuple(map(int,input().strip().split(' ')))
num_list = list(map(int,input().strip().split(' ')))



num_list.sort()

def count_days(the_list,N = n):
	if N == 1:
		return 1
	elif N == 0:
		return 0
	else:
		initial_N = N
		day_count = 0
		L = 0
		R = 1

		while R < N:
			if the_list[R] - the_list[L] > k:
				del the_list[L]
				N -= 1
				L = R-1
			else:
				R += 1

		del the_list[L]
		N -= 1

		day_count += 1 + count_days(the_list,N = N) if N != initial_N-1 else initial_N
		return day_count

print(count_days(num_list,n))

#k = 0
#day_count = 0
#L = 0
#R = 1
#del_count = 0
#[]