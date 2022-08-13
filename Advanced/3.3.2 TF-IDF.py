from collections import defaultdict
import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

# text = '''He really really loves coffee
# My sister dislikes coffee
# My sister loves tea'''


def get_term_frequency(words_list):
    term_frequency = defaultdict(int)
    for word in words_list:
        term_frequency[word] += 1
    return term_frequency


def dist(a, b):
    return sum(abs(a - b))


def main(text):
    words = text.lower().split()

    lines = text.lower().split('\n')
    document_frequency = defaultdict(int)

    word_set = set(text.lower().split())

    for line in lines:
        for word in set(text.lower().split()):
            if word in line.split():
                document_frequency[word] += 1

    tf_idf_frequency = defaultdict(list)
    for line in lines:
        line_splited = line.split()
        term_frequency = get_term_frequency(line_splited)
        for word in word_set:
            if word in term_frequency.keys():
                tf_idf_frequency[word].append(
                    (term_frequency[word] / len(line_splited)) *
                    (np.log10(len(lines) / document_frequency[word])))
            else:
                tf_idf_frequency[word].append(0)
    feature = np.array(list(tf_idf_frequency.values())).T
    diff_matrix = np.zeros((feature.shape[0], feature.shape[0]))
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j:
                diff_matrix[i][j] = np.inf
            else:
                diff_matrix[i][j] = dist(feature[i], feature[j])
    print(np.unravel_index(np.argmin(diff_matrix), diff_matrix.shape))


main(text)
