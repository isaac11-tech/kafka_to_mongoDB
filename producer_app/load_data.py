from sklearn.datasets import fetch_20newsgroups

class LoadData:

    def __init__(self):
        self.interesting_cats = [
            'alt.atheism',
            'comp.graphics',
            'comp.os.ms-windows.misc',
            'comp.sys.ibm.pc.hardware',
            'comp.sys.mac.hardware',
            'comp.windows.x',
            'misc.forsale',
            'rec.autos',
            'rec.motorcycles',
            'rec.sport.baseball'
        ]

        self.not_interesting_cats = [
            'rec.sport.hockey',
            'sci.crypt',
            'sci.electronics',
            'sci.med',
            'sci.space',
            'soc.religion.christian',
            'talk.politics.guns',
            'talk.politics.mideast',
            'talk.politics.misc',
            'talk.religion.misc'
        ]

    def load_interesting(self):
        return fetch_20newsgroups(subset='all', categories=self.interesting_cats)

    def load_not_interesting(self):
        return fetch_20newsgroups(subset='all', categories=self.not_interesting_cats)