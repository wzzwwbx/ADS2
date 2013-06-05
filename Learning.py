from gensim import corpora, models, similarities
f = open('data/AR/user-info-train.txt', 'r')
corpus_lsi = open('data/corpus_lsi.txt', 'r')
output = open('data/user_profile.txt', 'w')
user_profile_list = list()
user_like_list = list()
i = 1
for line in f.readlines():
	line.strip()
	# print line
	if(i == int(line.split(',')[0])):
		# print 'hello'
		user_like_list.append(int(line.split(',')[1]))
	else:
		i += 1
		user_profile_list.append(user_like_list)
		user_like_list = list()
		user_like_list.append(int(line.split(',')[1]))
	# user_like_list.append(int(line.split(',')[1]))
	# print (int(line.split(',')[0]))
# print len(user_profile_list)
user_profile_list.append(user_like_list)
# print type(user_profile_list[0][0])
f.close()

query_list = list()
for line in corpus_lsi.readlines():
	query_list.append(line)
# print type(query_list[0])
corpus_lsi.close()

def query_to_lsi(item):
	query_lsi = list()
	for elem in eval(query_list[item - 1]):
		query_lsi.append(elem)
	return query_lsi
def tuple_sum(tuple_1, tuple_2):
	return (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
def tuple_list_sum(list_1, list_2):
	sumed_tuple_list = list()
	for (i, j) in zip(list_1, list_2):
		sumed_tuple_list.append(tuple_sum(i, j))
	return sumed_tuple_list
def tuple_div(tuples, div):
	return (tuples[0]/div, tuples[1]/div)
def tuple_list_average(tuple_list, div):
	avg_tuple_list = list()
	for tuples in tuple_list:
		avg_tuple_list.append(tuple_div(tuples, div))
	return avg_tuple_list
# print query_to_lsi(1101)
avg_profile_lsi = list()
for user_like_list in user_profile_list:
	# user_like_lsi = list()
	sumed_tuple_list = list()
	for item in user_like_list:
		# print len(user_like_list)
		# print item
		# print query_list[item-1]
		if(len(sumed_tuple_list) == 0):
			sumed_tuple_list = query_to_lsi(item)
			# print sumed_tuple_list
		else:
			sumed_tuple_list = tuple_list_sum(query_to_lsi(item), sumed_tuple_list)
		# user_like_lsi.append(query_to_lsi(item))
		# sumed_tuple_list = tuple_list_sum(query_to_lsi(item), sumed_tuple_list)
	# sumed_tuple_list = user_like_lsi[0]
# 	for i in user_like_lsi:
# 		if i[0][1] != sumed_tuple_list[0][1]:
# 			sumed_tuple_list = tuple_list_sum(i, sumed_tuple_list)
# 	# print len(user_like_lsi)
	avg_tuple_list = tuple_list_average(sumed_tuple_list, len(user_like_list))
	output.write(str(avg_tuple_list) + '\n')
	avg_profile_lsi.append(avg_tuple_list)
# 	# print len(avg_profile_lsi)
# 	# break
# # print sumed_tuple_list
print len(avg_profile_lsi)
output.close()


