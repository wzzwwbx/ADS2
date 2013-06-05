# import Learning.py
f = open('data/user_profile.txt')
profile_list = list()
for line in f.readlines():
	profile_list.append(line)
print len(profile_list)
f.close()