count = {"I":00,"S":00,"P":00,"M":00}
word = "MISSISSIPPI"
for i in word:
	if i == "I":
		count['I'] = count['I']+1
	elif i == "S":
		count['S'] = count['S']+1
	elif i == "P":
		count['P'] = count['P']+1
	elif i == "M":
		count['M'] = count['M']+1
print(count)
