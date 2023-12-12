import re

print(re.findall(r'[Pp]ython','Python is a user friendly programming language, python has large user community'))

match = re.search(r'Krushna','Krushna is from moolya')
print(match)
print(match.group())
print('Start Index : ',match.start())
print('end Index : ',match.end())

print('Range',re.search(r'[a-zA-Z]','123'))
print(re.search(r'[^a-z]','Krushna'))
print(re.search(r'K[^u]','Krushna'))

print('Any character', re.search(r'p.th.n','python 3'))

print('Date{dd-mm-yyyy} : ',re.search(r'[\d]{2}-[\d]{2}-[\d]{4}', '18-08-2020'))

print(re.search(r'[0-9.]','$55.0'))
print(re.search(r'[0-9][.]','$ 55.0'))
print(re.findall(r'[0-9][.]','$ 55.0'))
print("$ 55.0".split('$',))
