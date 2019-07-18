import numpy as np
import codecs
from collections import defaultdict, Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from joblib import dump, load


def prepare_train_data_for_task_1(include_dev=False):
    dataset = defaultdict(list)
    X, y = [], []

    with codecs.open(f'MSA-CA-DA-train.txt') as training:
        for i, line in enumerate(training):
            sentence_label = line.strip().partition(' ')
            X.append(sentence_label[2])
            y.append(sentence_label[0])
            dataset[sentence_label[0]].append(sentence_label[2])

    if include_dev:
        with codecs.open(f'MSA-CA-DA-test.txt') as training:
            for i, line in enumerate(training):
                sentence_label = line.strip().partition(' ')
                X.append(sentence_label[2])
                y.append(sentence_label[0])
                dataset[sentence_label[0]].append(sentence_label[2])

    return train_test_split(X, y, test_size=4000, train_size=None, shuffle=True)


if __name__ == '__main__':
    train_src, dev_src, train_tgt, dev_tgt = prepare_train_data_for_task_1(include_dev=True)

    tfidf_vect = TfidfVectorizer(analyzer='word', lowercase=False, min_df=1, ngram_range=(1, 1), smooth_idf=False,
                                 sublinear_tf=True)
    X_train = tfidf_vect.fit_transform(train_src)
    X_dev = tfidf_vect.transform(dev_src)

    # clf = MultinomialNB(alpha=0.31).fit(X_train, train_tgt)
    clf = SGDClassifier(n_jobs=-1).fit(X_train, train_tgt)
    dump(tfidf_vect, 'dialect_identification.vec')
    dump(clf, 'dialect_identification.mdl')

    train_pred = clf.predict(X_train)
    dev_pred = clf.predict(X_dev)

    print('Training Acc: ', np.around(np.mean(train_pred == train_tgt) * 100, 2), '%')
    print('Testing Acc: ', np.around(np.mean(dev_pred == dev_tgt) * 100, 2), '%')

    print(Counter(train_tgt))