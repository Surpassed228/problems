n,r = tuple(map(int,input().strip().split(' ')))
number_list = list(map(int,input().strip().split(' ')))

R = 1
count = 0
N = len(number_list)

for L in range(N-1):
	if L == R:
		R += 1

	while R < N and number_list[R] - number_list[L] <= r:
		R += 1
	
	count += N-R if R < N else 0

print(count)