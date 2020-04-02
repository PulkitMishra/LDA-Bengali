from gensim import corpora, models
import numpy as np
import json

def read_data():
    with open('data_NandV.txt') as json_file:
        data = json.load(json_file)
    return data

def build_model(data):
    from gensim import corpora, models
    print(type(data['name']))
    print(type(data['name'][0]))
    list_of_list_of_tokens = data['name']
    dictionary_LDA = corpora.Dictionary(list_of_list_of_tokens)
    dictionary_LDA.filter_extremes(no_below=3)
    corpus = [dictionary_LDA.doc2bow(list_of_tokens) for list_of_tokens in list_of_list_of_tokens]

    num_topics = 9
    lda_model = models.LdaModel(corpus, num_topics=num_topics, \
                                  id2word=dictionary_LDA, \
                                  passes=10, alpha=[0.001]*num_topics, \
                                  eta=[0.001]*len(dictionary_LDA.keys()))
    return lda_model

def results(lda_model):
    ans = []
    for i,topic in lda_model.show_topics(formatted=True, num_topics=9, num_words=10):
        ans.append(str(i)+": "+ topic)
        ans.append("\n")
    outf = open("LDA_NandV_9topics.txt",'w')
    outf.writelines(ans)
    outf.close()

def visulaize(lda_model):
    import pyLDAvis
    import pyLDAvis.gensim
    vis = pyLDAvis.gensim.prepare(topic_model=lda_model, corpus=corpus, dictionary=dictionary_LDA)
    pyLDAvis.save_html(vis, "LDA_NandV_9topics.html")

data = read_data()
lda_model = build_model(data)
results(lda_model)
visulaize(lda_model)
