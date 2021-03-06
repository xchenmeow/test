# All rights reserved.
# __author__ == 'Benqing.Shen'
# python 2.7

def valid_len(s):
	return len(s) == 7


def valid_begin(s):
	return s[0] not in ['0', '1']


def valid_digit(s):
	return str.isdigit(s)


def knight_moves(x, y):
	# x and y are initial coordinates
	up = [(x + 2, y + 1), (x + 1, y + 2), (x - 1, y + 2), (x - 2, y + 1)]
	down = [(x - 2, y - 1), (x - 1, y - 2), (x + 1, y - 2), (x + 2, y - 1)]
	return up + down


keypad_map = {
	'*' : (0, 0),
	'0' : (1, 0),
	'#' : (2, 0),
	'7' : (0, 1),
	'8' : (1, 1),
	'9' : (2, 1),
	'4' : (0, 2),
	'5' : (1, 2),
	'6'	: (2, 2),
	'1' : (0, 3),
	'2' : (1, 3),
	'3' : (2, 3)}

def valid_knight_move(c1, c2):
	# c1 - coordinate 1
	# c2 - coordinate 2
	x1, y1 = c1
	x2, y2 = c2
	dx = x2 - x1
	dy = y2 - y1
	# print type(dx)
	# print type(dy)
	# print dx, dy
	return ((dx * dy == 2) or (dx * dy == -2))


def valid_consecutive_num(s1, s2):
	return valid_knight_move(keypad_map[s1], keypad_map[s2])


def valide_trace(s):
	pairs = zip(s[:-1], s[1:])
	tf = [valid_consecutive_num(pair[0], pair[1]) for pair in pairs]
	# all operator in python is short-circuit
	return all(tf)

def valid(s):
	# and operator in python is short-circuit
	return valid_len(s) and valid_begin(s) and valid_digit(s) and valide_trace(s)


if __name__ == '__main__':
	# vars begin with t are valid string
	t0 = '8349406'
	t1 = '7272949'
	# vars begin with f are invalid string
	f0 = '0618349'
	f1 = '8349405'
	print valid(t0)
	print valid(t1)
	print valid(f0)
	print valid(f1)

	phone_nums = []
	for x in xrange(1000000, 9999999):
		# print x
		if valid(str(x)):
			phone_nums.append(x)

	print len(phone_nums)

	# with open('answer.txt', 'wb') as f:
		# [f.write(str(x) + ',\n') for x in phone_nums]