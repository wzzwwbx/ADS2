import nltk
import re
from gensim import corpora, models, similarities
#from nltk.corpus import stopwords
stop = open('data/english').read()
stopwords = nltk.word_tokenize(stop)
f = open('data/AR/raw-data.txt', 'rU')
vocab_list = []
# output_file = open('data/corpus_lsi.txt', 'w')
open_file = open('data/corpus_lsi.txt', 'r')
# for line in f:
# 	raw = line.strip()
# 	#raw = f.read()
# 	tokens = re.findall('[a-zA-Z]+', raw)
# 	#wnl = nltk.WordNetLemmatizer()
# 	#raw = nltk.clean_html(html)
# 	#tokens = nltk.word_tokenize(raw)
# 	#porter = nltk.PorterStemmer()
# 	#stem = [porter.stem(t) for t in tokens]
# 	#stem = [wnl.lemmatize(t) for t in tokens]
# 	words = [w.lower() for w in tokens]
# 	newwords = [w for w in words if w not in stopwords]
# 	vocab = sorted(set(newwords))
# 	#word_freq = FreqDist(words)
# 	#text = nltk.Text(tokens)
# 	#print word_freq
# 	vocab_list.append(vocab)
	#print vocab_list
# print vocab_list
# dic = corpora.Dictionary(vocab_list)
# dic.save('data/dic.dict')
dic = corpora.Dictionary().load('data/dic.dict')
# corpus = [dic.doc2bow(v) for v in vocab_list]
corpus = corpora.MmCorpus('data/corpus.mm')
# print list(corpus)
# corpora.MmCorpus.serialize('data/corpus.mm', corpus) # store to disk, for later use
# tfidf = models.TfidfModel(corpus)
# tfidf.save('data/tfidf.tfidf_model')
tfidf = models.TfidfModel().load('data/tfidf.tfidf_model')

# print tfidf.dfs
corpus_tfidf = tfidf[corpus]
# print list(corpus_tfidf)
# lsi = models.LsiModel(corpus_tfidf, id2word = dic, num_topics = 400)
lsi = models.LsiModel.load('data/lsi.model')
# lsi.save('data/lsi.model')
# lsi.load('data/lsi.npy')
# print lsi.print_topics(10)
corpus_lsi = lsi[corpus_tfidf]
index = similarities.MatrixSimilarity.load('data/index.lsi_index')
query_list = list()
for line in open_file.readlines():
	# each_list = list()
	# for elm in eval(line):
		# each_list.append(elm)
	query_list.append(line)
# print type(query_list[0])
open_file.close()
query_lsi = list()
for elem in eval(query_list[0]):
	query_lsi.append(elem)
# print query_lsi
sims = index[query_lsi]
# for vec in corpus_lsi:
	# output_file.write(str(vec) + '\n')
# output_file.close()
# print query_lsi
# index = similarities.MatrixSimilarity(lsi[corpus])
# index.save('data/index.lsi_index')
# vec = list(corpus_tfidf)[0]
# print vec
# print tfidf[vec]

# index.save('data/index.npy')
# index = similarities.SparseMatrixSimilarity().load('data/index.npy')
# #query = "that are composed of elaborate hierarchies of protocols and layers of feedback regulation"
# #query_bow = dic.doc2bow(query.lower().split())
# #query_lsi = corpus_lsi[1]
# sims = index[vec]
# print list(enumerate(sims))
sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
print sort_sims[:10]
# # # for doc in corpus_lsi:
# # # 	print doc
# # # 	#output_file.write(doc + "\n")