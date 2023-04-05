list_version = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]


def elem_counting(array: list) -> list:
	"""
	Time complexity: O(n)
	Space complexity: O(n)
	"""
	book = {}
	for item in array:
		key = item[0] + str(item[1])
		if key not in book:
			book[key] = item + [1]
		elif book[key][1] != item[1]:
			book[key] = item + [1]
		else:
			book[key][-1] += 1
	return [elem for elem in book.values()]


print(elem_counting(list_version))
