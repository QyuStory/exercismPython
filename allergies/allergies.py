class Allergies(object):

    def __init__(self, score):
        self.score = score%256
        dic = {1: 'eggs', 2: 'peanuts', 4: 'shellfish', 8: 'strawberries',
                    16: 'tomatoes', 32: 'chocolate', 64: 'pollen', 128: 'cats'}
        self._lst = []
        for k in reversed(sorted(dic.keys())):
            if self.score is not 0:
                if self.score - k >= 0:
                    self._lst.append(dic.get(k))
                    self.score -= k

    def is_allergic_to(self, item):
        if item in self._lst:
            return True
        else:
            return False

    @property
    def lst(self):
        return self._lst
