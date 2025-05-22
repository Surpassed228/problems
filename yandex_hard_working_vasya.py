n,k = tuple(map(int,input().strip().split(' ')))
num_list = list(map(int,input().strip().split(' ')))

#sorting_the_list
num_list.sort()
def get_next(mins_list,K):#O(K)
	#use this function when there is such element
	for k in range(K):
		if k == K-1:
			return mins_list[k] + 1
		elif mins_list[k] + 1 != mins_list[k+1]:
			return mins_list[k] + 1

def get_first_good(el,from_,to_,the_list): #O(log(N))
		q = (to_-from_)//2 - 1
		q_value = the_list[from_ + q if q >= 0 else from_]

		if q < 0:
			if q_value > el + k:
				return from_
			else:
				return None

		if q_value > el + k:
			if the_list[from_+q-1] > el + k:
				return get_first_good(el,from_,from_ + q,the_list)
			else:
				return from_ + q

		else:
			return get_first_good(el,from_ + q + 1,to_,the_list)


def count_days(the_list,N = n):
	if N == 1:
		return 1
	elif N > 1:
		list_len = N
		day_count = 0
		current_ind = 0
		all_mins = []
		all_mins_K = 0
		while N > 0 and current_ind < list_len:
			the_mins = [current_ind]
			mins_K = 1
			N -= 1

			day_count += 1

			next_min = get_first_good(the_list[the_mins[-1]],from_ = the_mins[-1],to_ = list_len,the_list = the_list)
			while next_min != None and next_min < list_len:
				if next_min not in all_mins:
					the_mins.append(next_min)
					next_min = get_first_good(the_list[the_mins[-1]],from_ = the_mins[-1],to_ = list_len,the_list = the_list)
					mins_K += 1
					N -= 1
				else:
					while next_min in all_mins:
						next_min += 1
			all_mins.extend(the_mins)
			all_mins_K += mins_K
			current_ind = get_next(all_mins,all_mins_K)
		return day_count

print(count_days(num_list,N = n))



#[1,2,2]
#list_len = 3
#N = 0
#day_count = 1
#current_ind = 2
#all_mins = [0,1,2]

#the_mins = [2]
#mins_K = 1
#day_count = 2
#




# def test(N = 10):
# 	for _ in range(N):
# 		R = rd.randint(2*10**5,3*10**5)
# 		some_ar = [rd.randint(1,101) for _ in range(R)]
# 		some_ar.sort()
# 		el = some_ar[0]
# 		the_ind = None
# 		for item_ind in range(0,len(some_ar)):
# 			if some_ar[item_ind] > el + k:
# 				the_ind = item_ind
# 				break

# 		the_value = get_first_good(el,from_ = 0,to_ = len(some_ar),the_list = some_ar)
# 		if the_ind == the_value:
# 			print(f'Test #{_+1} PASSED',end = '\n\n')
# 		else:
# 			print(f'-------------------------WRONG------------------')
# 			print(some_ar)
# 			print(the_ind)
# 			print(the_value,end = '\n\n')
# 			break

# test(10)
		

