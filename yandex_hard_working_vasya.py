n,k = tuple(map(int,input().strip().split(' ')))
num_list = list(map(int,input().strip().split(' ')))

# #sorting_the_list
num_list.sort()

def count_days(the_list,N = n,k = 0):
	if N == 1:
		return 1
	else:
		i = 0
		j = 0
		ans = 0
		while i < N and j < N:
			the_num = j-i+1
			if the_list[j]-the_list[i] <= k:
				ans = max(ans,the_num)
				j += 1
			else:
				i += 1
		return ans

print(count_days(num_list,N = n,k = k))

# import random as rd
# def test(N = 10):
# 	for _ in range(N):
# 		k =rd.randint(0,6)
# 		some_lists = [[] for _ in range(rd.randint(1,3))]
# 		for one_list in some_lists:
# 			the_n = rd.randint(1,4)
# 			while len(one_list) < the_n:
# 				rand_num = rd.randint(1,59)
# 				if len(one_list) == 0:
# 					one_list.append(rand_num)
# 				else:
# 					for one_num in one_list:
# 						if abs(one_num - rand_num) > k:
# 							one_list.append(rand_num)
# 		main_list = []
# 		for one_list in some_lists:
# 			main_list.extend(one_list)
# 		#test
# 		print(f'K = {k}')
# 		print(main_list)
# 		main_list.sort()
# 		print(main_list,end = '\n')
# 		print(count_days(main_list,len(main_list),k = k),end = '\n\n')



# test(10)

