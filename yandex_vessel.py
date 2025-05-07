numbers = []
for _ in range(6):
	numbers.append(int(input()))

x1,y1,x2,y2,x,y = numbers

#angles
if x < x1 and y < y1:
	print('SW')
elif x > x2 and y > y2:
	print('NE')
elif x < x1 and y > y2:
	print('NW')
elif x > x2 and y < y1:
	print('SE')

#sides
elif x1 < x < x2 and y < y1:
	print('S')
elif x1 < x < x2 and y > y2:
	print('N')
elif y1 < y < y2 and x < x1:
	print('W')
elif y1 < y < y2 and x > x2:
	print('E')