N,K = tuple(map(int,input().split(' ')))
main_numbers = list(map(int,input().split(' ')))





def pref_sum_list(main_ar):
	pref_list = [0]
	for ind in range(len(main_ar)):
		pref_list.append(pref_list[ind] + main_ar[ind])
	return pref_list

def count_inter_K(pref_list):
	count = 0
	L = 0
	R = 1
	while R < len(pref_list):
		delta = pref_list[R] - pref_list[L]
		if delta >= K:
			count += 0 if delta != K else 1
			L += 1
			if L == R:
				R += 1
		else:
			R += 1
	return count

print(count_inter_K(pref_sum_list(main_numbers)))


#[2]
#[0,2]
#3
#L = 0
#R = 1  < 2
#count = 0