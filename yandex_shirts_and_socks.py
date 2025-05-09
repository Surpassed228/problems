Ns = []
for _ in range(4):
	Ns.append(int(input()))


A,B,C,D = Ns

m1 = min(A,B)
m2 = max(A,B)
n1 = min(C,D)
n2 = max(C,D)

the_min_min = min(m1,n1)
the_min_max = min(m2,n2)

if the_min_min in [A,B]:
	min_ans = (the_min_min+1,C+1 if the_min_min == A else D+1)
elif the_min_min in [C,D]:
	min_ans = (A+1 if the_min_min == C else B+1,the_min_min+1)

if the_min_max in [A,B]:
	if A+B-the_min_max == 0:
		max_ans = (1,C+1 if the_min_max == B else D+1)
	else:
		max_ans = (the_min_max+1,1)
elif the_min_max in [C,D]:
	if C+D-the_min_max == 0:
		max_ans = (A+1 if the_min_max == D else B+1,1)
	else:
		max_ans = (1,the_min_max+1)

ans_list = [min_ans,max_ans]
res = min(ans_list,key = lambda t: t[0] + t[1])
print(res[0],res[1])