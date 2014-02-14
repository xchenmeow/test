def valid_len(s):
	return len(s) == 7


def valid_begin(s):
	return s[0] not in ['0', '1']


def valid(s):
	return valid_len(s) and valid_begin(s)


if __name__ == '__main__':
	# vars begin with t are valid string
	t0 = ''
	t1 = ''
	# vars begin with f are invalid string
	f0 = ''
	f1 = ''