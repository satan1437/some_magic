import re

Test_text = '''
{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}
'''

list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']


def validate_data_reliable(text: str) -> bool:
	"""
	Time complexity: O(n)
	Space complexity: O(n)
	Проверяет правильность очерёдности закрытия скобок.
	"""
	if text.count('{') != text.count('}'):
		return False
	raw_data = []
	start_pair, pair_closed = 0, True
	for indx, symbol in enumerate(text):
		if symbol == '{':
			if not pair_closed:
				return False
			start_pair = indx
			pair_closed = False
		elif symbol == '}':
			raw_data.append(text[start_pair:indx + 1])
			pair_closed = True
		if indx == len(text) - 1 and not pair_closed:
			return False
	return all([False for item in raw_data if item[1:-1:] not in list_keys])


def validate_data_lite(text: str) -> bool:
	"""
	Time complexity: O(n)
	Space complexity: O(n)
	Не проверяет правильность очерёдности закрытия скобок.
	"""
	if text.count('{') != text.count('}'):
		return False
	raw_data = re.findall(r'\{[a-zA-Z_]+\}', text)  # noqa
	for item in raw_data:
		if item[1:-1:] not in list_keys:
			return False
	return True


if __name__ == '__main__':
	print(validate_data_lite(Test_text))
	print(validate_data_reliable(Test_text))
