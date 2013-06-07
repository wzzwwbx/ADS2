from gensim import corpora, models, similarities

def str_to_lsi(item, corpus_lsi_list):
	corpus_lsi = list()
	for elem in eval(corpus_lsi_list[item - 1]):
		corpus_lsi.append(elem)
	return corpus_lsi

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

def get_corpus_lsi_list(corpus_lsi_file_dir = 'data/corpus_lsi.txt'):
	corpus_lsi = open(corpus_lsi_file_dir, 'r')
	corpus_lsi_list = list()
	for line in corpus_lsi.readlines():
		corpus_lsi_list.append(line)
	return corpus_lsi_list

def get_user_profile_list(train_file_dir = 'data/AR/user-info-train.txt'):
	train_file = open(train_file_dir, 'r')
	user_profile_list = list()
	user_like_list = list()
	i = 1
	for line in train_file.readlines():
		line.strip()
		if(i == int(line.split(',')[0])):
			user_like_list.append(int(line.split(',')[1]))
		else:
			i += 1
			user_profile_list.append(user_like_list)
			user_like_list = list()
			user_like_list.append(int(line.split(',')[1]))
	user_profile_list.append(user_like_list)
	train_file.close()
	return user_profile_list

def get_avg_profile_list(user_profile_list, avg_profile_file_dir = 'data/user_profile.txt'):
	avg_profile_file = open(avg_profile_file_dir, 'w')
	avg_profile_list = list()
	corpus_lsi_list = get_corpus_lsi_list()
	for user_like_list in user_profile_list:
		sumed_tuple_list = list()
		for item in user_like_list:
			if(len(sumed_tuple_list) == 0):
				sumed_tuple_list = str_to_lsi(item, corpus_lsi_list)
			else:
				sumed_tuple_list = tuple_list_sum(str_to_lsi(item, corpus_lsi_list), sumed_tuple_list)
		avg_tuple_list = tuple_list_average(sumed_tuple_list, len(user_like_list))
		avg_profile_file.write(str(avg_tuple_list) + '\n')
		avg_profile_list.append(avg_tuple_list)
	avg_profile_file.close()
	return avg_profile_list

def get_all_similarity_with_avg_profile(avg_profile_list, index_file_dir = 'data/index.lsi_index', simi_file_dir = 'data/all_similarity.txt'):
	simi_file = open(simi_file_dir, 'w')
	index = similarities.MatrixSimilarity.load(index_file_dir)
	for profile in avg_profile_list:
		sims = index[profile]
		sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
		simi_file.write(str(sort_sims) + '\n')
	simi_file.close()

if __name__ == '__main__':
	user_profile_list = get_user_profile_list()
	avg_profile_list = get_avg_profile_list(user_profile_list)
	get_all_similarity_with_avg_profile(avg_profile_list)


# f = open('data/AR/user-info-train.txt', 'r')
# corpus_lsi = open('data/corpus_lsi.txt', 'r')
# # output = open('data/user_profile.txt', 'w')
# user_profile_list = list()
# user_like_list = list()
# i = 1
# for line in f.readlines():
# 	line.strip()
# 	# print line
# 	if(i == int(line.split(',')[0])):
# 		# print 'hello'
# 		user_like_list.append(int(line.split(',')[1]))
# 	else:
# 		i += 1
# 		user_profile_list.append(user_like_list)
# 		user_like_list = list()
# 		user_like_list.append(int(line.split(',')[1]))
# 	# user_like_list.append(int(line.split(',')[1]))
# 	# print (int(line.split(',')[0]))
# # print len(user_profile_list)
# user_profile_list.append(user_like_list)
# # print type(user_profile_list[0][0])
# f.close()

# query_list = list()
# for line in corpus_lsi.readlines():
# 	query_list.append(line)
# # print type(query_list[0])
# corpus_lsi.close()
# # print query_to_lsi(1101)
# avg_profile_lsi = list()
# for user_like_list in user_profile_list:
# 	# user_like_lsi = list()
# 	sumed_tuple_list = list()
# 	for item in user_like_list:
# 		# print len(user_like_list)
# 		# print item
# 		# print query_list[item-1]
# 		if(len(sumed_tuple_list) == 0):
# 			sumed_tuple_list = query_to_lsi(item)
# 			# print sumed_tuple_list
# 		else:
# 			sumed_tuple_list = tuple_list_sum(query_to_lsi(item), sumed_tuple_list)
# 		# user_like_lsi.append(query_to_lsi(item))
# 		# sumed_tuple_list = tuple_list_sum(query_to_lsi(item), sumed_tuple_list)
# 	# sumed_tuple_list = user_like_lsi[0]
# # 	for i in user_like_lsi:
# # 		if i[0][1] != sumed_tuple_list[0][1]:
# # 			sumed_tuple_list = tuple_list_sum(i, sumed_tuple_list)
# # 	# print len(user_like_lsi)
# 	avg_tuple_list = tuple_list_average(sumed_tuple_list, len(user_like_list))
# 	# output.write(str(avg_tuple_list) + '\n')
# 	avg_profile_lsi.append(avg_tuple_list)
# # 	# print len(avg_profile_lsi)
# # 	# break
# # # print sumed_tuple_list
# print len(avg_profile_lsi)
# output.close()


