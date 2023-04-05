import json


class JsonDiff:
	def __init__(self, old_data, new_data, diff):
		self.old_fields = self._find_json_field(old_data, diff)
		self.new_fields = self._find_json_field(new_data, diff)

	def _find_json_field(self, data: dict, field: list, result=None) -> list:
		if result is None:
			result = []
		if isinstance(data, dict):
			for key, value in data.items():
				if key in diff_list:
					result.append({key: value})
				self._find_json_field(value, field, result)
		elif isinstance(data, list):
			for item in data:
				self._find_json_field(item, field, result)
		return result

	def diff(self):
		book = {}
		for old, new in zip(self.old_fields, self.new_fields):
			if old != new:
				book.update(new)
		return book


with open('jsons/json_old.json', 'r', encoding='utf-8') as old_json, \
		open('jsons/json_new.json', 'r', encoding='utf-8') as new_json:
	diff_list = ['services', 'staff', 'datetime']
	a = JsonDiff(json.load(old_json), json.load(new_json), diff_list)
	print(a.diff())
