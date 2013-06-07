# import nltk
import re
from gensim import corpora, models, similarities

def vocab_list(raw_data_file = 'data/AR/raw-data.txt', stopwords_file = 'data/english'):
	vocab_list = []
	stop = open(stopwords_file, 'r').read()
	stopwords = nltk.word_tokenize(stop)
	raw_data = open(raw_data_file, 'rU')
	for line in raw_data:
		raw = line.strip()
		tokens = re.findall('[a-zA-Z]+', raw)
		words = [w.lower() for w in tokens]
		clear_words = [w for w in words if w not in stopwords]
		vocab = sorted(set(clear_words))
		vocab_list.append(vocab)
	return vocab_list
def create_dictionary(vocab_list, dic_file_dir = 'data/dic.dict'):
	dic = corpora.Dictionary(vocab_list)
	dic.save(dic_file_dir)
	return dic
def create_corpus(vocab_list, corpus_file_dir = 'data/corpus.mm'):
	corpus = [dic.doc2bow(v) for v in vocab_list]
	corpora.MmCorpus.serialize(corpus_file_dir, corpus)
	return corpus
def create_tfidf_model(corpus, tfidf_file_dir = 'data/tfidf.tfidf_model'):
	tfidf = models.TfidfModel(corpus)
	tfidf.save(tfidf_file_dir)
	return tfidf
def create_lsi_model(dic, corpus, tfidf, lsi_file_dir = 'data/lsi.model', topic_num = 400):
	corpus_tfidf = tfidf[corpus]
	lsi = models.LsiModel(corpus_tfidf, id2word = dic, num_topics = topic_num)
	lsi.save(lsi_file_dir)
	return lsi
def create_corpus_lsi(lsi, corpus_tfidf, corpus_lsi_file_dir = 'data/corpus_lsi.txt'):
	corpus_lsi = lsi[corpus_tfidf]
	output_file = open(corpus_lsi_file_dir, 'w')
	for vec in corpus_lsi:
		output_file.write(str(vec) + '\n')
	output_file.close()
	return corpus_lsi
def create_index(lsi, corpus, index_file_dir = 'data/index.lsi_index'):
	index = similarities.MatrixSimilarity(lsi[corpus])
	index.save(index_file_dir)
	return index
if __name__ == '__main__':
	vocab_list = vocab_list()
	dic = create_dictionary(vocab_list)
	corpus = create_corpus(vocab_list)
	tfidf = create_tfidf_model(corpus)
	lsi = create_lsi_model(dic, corpus, tfidf)
	corpus_lsi = create_corpus_lsi(lsi, tfidf[corpus])
	index = create_index(lsi, corpus)


# stop = open('data/english').read()
# stopwords = nltk.word_tokenize(stop)
# f = open('data/AR/raw-data.txt', 'rU')
# vocab_list = []
# # output_file = open('data/corpus_lsi.txt', 'w')
# open_file = open('data/corpus_lsi.txt', 'r')
# # for line in f:
# # 	raw = line.strip()
# # 	#raw = f.read()
# # 	tokens = re.findall('[a-zA-Z]+', raw)
# # 	#wnl = nltk.WordNetLemmatizer()
# # 	#raw = nltk.clean_html(html)
# # 	#tokens = nltk.word_tokenize(raw)
# # 	#porter = nltk.PorterStemmer()
# # 	#stem = [porter.stem(t) for t in tokens]
# # 	#stem = [wnl.lemmatize(t) for t in tokens]
# # 	words = [w.lower() for w in tokens]
# # 	newwords = [w for w in words if w not in stopwords]
# # 	vocab = sorted(set(newwords))
# # 	#word_freq = FreqDist(words)
# # 	#text = nltk.Text(tokens)
# # 	#print word_freq
# # 	vocab_list.append(vocab)
# 	#print vocab_list
# # print vocab_list
# # dic = corpora.Dictionary(vocab_list)
# # dic.save('data/dic.dict')
# dic = corpora.Dictionary().load('data/dic.dict')
# # corpus = [dic.doc2bow(v) for v in vocab_list]
# corpus = corpora.MmCorpus('data/corpus.mm')
# # print list(corpus)
# # corpora.MmCorpus.serialize('data/corpus.mm', corpus) # store to disk, for later use
# # tfidf = models.TfidfModel(corpus)
# # tfidf.save('data/tfidf.tfidf_model')
# tfidf = models.TfidfModel().load('data/tfidf.tfidf_model')

# # print tfidf.dfs
# corpus_tfidf = tfidf[corpus]
# # print list(corpus_tfidf)
# # lsi = models.LsiModel(corpus_tfidf, id2word = dic, num_topics = 400)
# lsi = models.LsiModel.load('data/lsi.model')
# # lsi.save('data/lsi.model')
# # print lsi.print_topics(50)
# corpus_lsi = lsi[corpus_tfidf]
# index = similarities.MatrixSimilarity.load('data/index.lsi_index')
# query_list = list()
# for line in open_file.readlines():
# 	# each_list = list()
# 	# for elm in eval(line):
# 		# each_list.append(elm)
# 	query_list.append(line)
# # print type(query_list[0])
# open_file.close()
# query_lsi = list()
# for elem in eval(query_list[0]):
# 	query_lsi.append(elem)
# # print query_lsi
# sims = index[query_lsi]
# # for vec in corpus_lsi:
# 	# output_file.write(str(vec) + '\n')
# # output_file.close()
# # print query_lsi
# # index = similarities.MatrixSimilarity(lsi[corpus])
# # index.save('data/index.lsi_index')
# # vec = list(corpus_tfidf)[0]
# # print vec
# # print tfidf[vec]

# # index.save('data/index.npy')
# # index = similarities.SparseMatrixSimilarity().load('data/index.npy')
# # #query = "that are composed of elaborate hierarchies of protocols and layers of feedback regulation"
# # #query_bow = dic.doc2bow(query.lower().split())
# # #query_lsi = corpus_lsi[1]
# # sims = index[vec]
# print list(enumerate(sims))
# sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
# print sort_sims[:10]
# # # for doc in corpus_lsi:
# # # 	print doc
# # # 	#output_file.write(doc + "\n")