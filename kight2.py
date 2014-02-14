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


def valid_nums(n, k):
	# n - digits
	# k - starts from k
	if n == 1:
		return 1
	else:
		if k == 5:
			return 0
		elif k == 4 or k == 6:
			return valid_nums(n - 1, move_map[k][0]) + valid_nums(n - 1, move_map[k][1]) + valid_nums(n - 1, move_map[k][2])
		else:
			return valid_nums(n - 1, move_map[k][0]) + valid_nums(n - 1, move_map[k][1])



if __name__ == '__main__':
	# print valid_nums(1, 1)
	# print valid_nums(2, 1)
	print valid_nums(3, 1)