class CountVectorizer:
    def __init__(self):
        self.feature_names = None

    def fit_transform(self, file):
        parts = [doc.lower().split() for doc in file]
        self.feature_names = sorted(list(set(word for part in parts for word in part)))
        vectors = []
        for part in parts:
            vector = [0] * len(self.feature_names)
            for word in part:
                if word in self.feature_names:
                    vector[self.feature_names.index(word)] += 1
            vectors.append(vector)
        return vectors

    def get_feature_names(self):
        if not self.feature_names:
            print("Сначала fit_transform")
        return self.feature_names


if __name__ == '__main__':
    corpus = ['This is the first document',
              'This document is the second document',
              'And this is the third one',
              'Is this the first document']
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(X)
