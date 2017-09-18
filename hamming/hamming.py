def distance(s1, s2):
    if len(s1) != len(s2):
    	raise ValueError
    count = 0
    for i in range(0, len(s1)):
    	if s1[i] != s2[i]:
    		count += 1
    return count