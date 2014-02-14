move_map = {
	1 : (6, 8),
	2 : (7, 9),
	3 : (4, 8),
	4 : (3, 9, 0),
	5 : (),
	6 : (1, 7, 0),
	7 : (2, 6),
	8 : (1, 3),
	9 : (4, 2),
	0 : (4, 6)
}

if __name__ == '__main__':
	valid_nums = [[1 for x in xrange(10)] for x in xrange(7)]

	for digits in xrange(2, 8):
		for start in xrange(0, 10):
			if start == 5:
				valid_nums[digits-1][start] = 0
			elif start == 4 or start == 6:
				valid_nums[digits-1][start] = valid_nums[digits - 2][move_map[start][0]] + valid_nums[digits - 2][move_map[start][1]] + valid_nums[digits - 2][move_map[start][2]]
			else:
				try:
					valid_nums[digits-1][start] = valid_nums[digits - 2][move_map[start][0]] + valid_nums[digits - 2][move_map[start][1]]
				except:
					print digits, start

	print sum([valid_nums[6][i] for i in range(2,10)]) 
