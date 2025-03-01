import re
# 2 - SIMPLE CHARACTER MATCHES


# text = 'cat bat mat rat mat mat'
# pattern = 'mat'
# re.findall('the patter would go here', 'the text would go here'
# output = re.findall(pattern,text)

# print(len(output))

# 3 - CHARACTER CLASSES

# text = 'we have 3 Apples and 14 oranges in 1343 avenue which is priced for $40.'
# pattern = r'[\w]+' #trying to get matches for letters both uppercase and lowercase and digits
# output = re.findall(pattern,text)
# print(output)

# text = 'We have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
# pattern = r'[a-zA-Z\d]+'  #trying to get matches for digits for letters both uppercase and lowercase and digits
# output = re.findall(pattern,text)
# print(output)


# text = 'We have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
# pattern = r'[\s]'  #trying to get matches for spaces
# output = re.findall(pattern,text)
# print(output)

# text = 'We have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
# pattern = r'[^\w\s]+'  #trying to get matches for spaces
# output = re.findall(pattern,text)
# print(output)

# text = 'We have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
# pattern = Apples  #trying to get matches for spaces
# output = re.sub(pattern,text)
# print(output)


