from tools.matcher import ComplementiserMatcher

class IrishComplementiserClassifier:
    def __init__(self):
        self.matcher = ComplementiserMatcher()

    def __call__(self, lemmas: list[str]):
        matches = self.matcher(lemmas)
        return matches

    def match(self, sentence):
        return self.matcher(sentence)
