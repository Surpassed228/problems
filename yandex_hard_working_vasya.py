n,k = tuple(map(int,input().strip().split(' ')))
num_list = list(map(int,input().strip().split(' ')))


num_list.sort()
def count_days(the_list,N = n):
	if N == 1:
		return 1
	elif N == 0:
		return 0
	elif the_list[-1] - the_list[0] <= k:
		return N
	else:
		the_mins = [the_list[0]]
		N -= 1

		ind = 1
		another_list = []
		while ind < N:
			if the_list[ind]-the_mins[-1] > k:
				the_mins.append(the_list[ind])
				N -= 1
			else:
				another_list.append(the_list[ind])
				ind += 1
		return 1 + count_days(another_list,N = N)



print(count_days(num_list,N = n))

#k = 0
#N = 1
#ind = 0
#[2]
#mins_list = [1,2]
#mins_count = 2


