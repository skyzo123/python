words=['cat','window','defenestrate']
print(words)
for w in words[:]:
	if len(w)>6:
		words.append(w)
	print(words)


