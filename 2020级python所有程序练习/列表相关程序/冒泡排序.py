s=[28,65,97,76,13,27,49]
i=0
while i<7:
    for j in range(0,len(s)-i- 1):
        if s[j] < s[j + 1]:
            s[j], s[j+1] = s[j+1], s[j]
    i=i+1
    print(s)
print(s)