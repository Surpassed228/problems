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
		the_min = the_list[0]
		another_list = []
		for ind in range(1,N):
			if the_list[ind]-the_min > k:
				the_min = the_list[ind]
				N -= 1
			else:
				another_list.append(the_list[ind])
		N -= 1		
		return 1 + count_days(another_list,N = N)



print(count_days(num_list,N = n))


#[1,2,3,4,5,6,7,8,9]
#k = 0
#N = 1
#ind = 0
#[2]
#mins_list = [1,2]
#mins_count = 2


