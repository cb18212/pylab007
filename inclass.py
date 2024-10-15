import re
def reverse(str_in):
	result = ""
	for i in str_in:
		result = i + result
	return result

def half_mirror(str_in):
	str_in = str_in.strip()
	str_in = str_in[:(len(str_in)-1)//2]
	str_in = reverse(str_in)
	return str_in

def count_pattern_occurances(pattern, str_in):
	result = re.findall(pattern, str_in)
	return len(result)


print(half_mirror("Testing 123"))
print(count_pattern_occurances(r"(?i)a", "arhgui pupi ap ua puaa uipaA"))