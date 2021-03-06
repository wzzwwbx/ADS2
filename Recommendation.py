from gensim import corpora, models, similarities

def str_to_list(list_str):
	simi_list = list()
	for elem in eval(list_str):
		simi_list.append(elem)
	return simi_list

def select_candidate(simi_list, candidate_list):
	result_list = list()
	for simi_tuple in simi_list:
		if simi_tuple[0] in candidate_list:
			result_list.append(simi_tuple)
		if (len(result_list) == 5):
			break
	return result_list

def get_all_test_list(test_file_dir = 'data/AR/user-info-test.txt'):
	test_file = open(test_file_dir, 'r')
	test_list = list()
	all_test_list = list()
	i = 1
	for line in test_file.readlines():
		line.strip()
		if(i == int(line.split(',')[0])):
			test_list.append(int(line.split(',')[1]))
		else:
			i += 1
			all_test_list.append(test_list)
			test_list = list()
			test_list.append(int(line.split(',')[1]))
	all_test_list.append(test_list)
	test_file.close()
	return all_test_list

def get_result(all_test_list, all_similarity_file_dir = 'data/all_similarity.txt', result_file_dir = 'data/results.txt'):
	simi_file = open(all_similarity_file_dir, 'r')
	result_file = open(result_file_dir, 'w')
	i = 0
	for line in simi_file.readlines():
		simi_list = str_to_list(line)
		result = select_candidate(simi_list, all_test_list[i])
		if i == 5550:
			result_file.write(str(i + 1) + ',' + str(result[0][0]) + ';' + str(result[1][0]) + ';' + str(result[2][0]) + ';' + str(result[3][0]) + ';' + str(result[4][0]))
		else:
			result_file.write(str(i + 1) + ',' + str(result[0][0]) + ';' + str(result[1][0]) + ';' + str(result[2][0]) + ';' + str(result[3][0]) + ';' + str(result[4][0]) + '\n')
		i += 1
	simi_file.close()
	result_file.close()
	print 'Work Done!'

if __name__ == '__main__':
	all_test_list = get_all_test_list()
	get_result(all_test_list)


# result_file = open('data/results.txt', 'w')
# sim = open('data/all_similarity.txt', 'r')
# # test = open('data/AR/user-info-test.txt', 'r')
# # test_list = list()
# # all_test_list = list()
# # i = 1
# # for line in test.readlines():
# # 	line.strip()
# # 	# print line
# # 	if(i == int(line.split(',')[0])):
# # 		test_list.append(int(line.split(',')[1]))
# # 	else:
# # 		i += 1
# # 		all_test_list.append(test_list)
# # 		test_list = list()
# # 		test_list.append(int(line.split(',')[1]))
# # all_test_list.append(test_list)
# # test.close()

# # f = open('data/AR/user-info-train.txt', 'r')
# # user_profile_list = list()
# # user_like_list = list()
# # i = 1
# # for line in f.readlines():
# # 	line.strip()
# # 	if(i == int(line.split(',')[0])):
# # 		user_like_list.append(int(line.split(',')[1]))
# # 	else:
# # 		i += 1
# # 		user_profile_list.append(user_like_list)
# # 		user_like_list = list()
# # 		user_like_list.append(int(line.split(',')[1]))
# # user_profile_list.append(user_like_list)
# # f.close()

# i = 0
# for line in sim.readlines():
# 	simi_list = str_to_list(line)
# 	# result = select_candidate(simi_list, all_test_list[i], user_profile_list[i])
# 	result = select_candidate(simi_list, all_test_list[i])
# 	result_file.write(str(i + 1) + ',' + str(result[0][0]) + ';' + str(result[1][0]) + ';' + str(result[2][0]) + ';' + str(result[3][0]) + ';' + str(result[4][0]) + '\n')
# 	i += 1
# result_file.close()



# # print all_test_list

# # output = open('data/all_similarity.txt', 'w')
# # profile_list = list()
# # for line in f.readlines():
# # 	l = list()
# # 	for elem in eval(line):
# # 		l.append(elem)
# # 	profile_list.append(l)
# # # print type(profile_list[0][0])

# # index = similarities.MatrixSimilarity.load('data/index.lsi_index')
# # for profile in profile_list:
# # 	sims = index[profile]
# # 	sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
# # 	output.write(str(sort_sims) + '\n')
# # f.close()
# # output.close()