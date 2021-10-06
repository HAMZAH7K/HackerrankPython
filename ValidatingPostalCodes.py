regex_integer_in_range = r'^(?!(?:.*(.).\1.*){2,})(?!.*(.)(.)\2\3)[1-9]\d{5}$'	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.


import re
P = raw_input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)