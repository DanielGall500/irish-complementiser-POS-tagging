import numpy as np

class ComplementiserMatcher:
    surface_realisations = {
        "go": ["go", "gur", "gurb", "gurbh"],
        "a": ["a", "ar"]
    }
    def __call__(self, lemmas: list[str]) -> np.array:
        go_particle = self.get_go_particle(lemmas)
        a_particle = self.get_a_particle(lemmas)
        matrix = np.vstack((go_particle, a_particle))
        return matrix

    def get_particle(self, realisations: list[str], lemmas: list[str]) -> list[int]:
        n = len(lemmas)
        one_hot_encoding = np.zeros(n)
        for i,token in enumerate(lemmas):
            if token in realisations:
                one_hot_encoding[i] = 1
        return one_hot_encoding

    def get_go_particle(self, lemmas: list[str]) -> list:
        realisations = self.surface_realisations['go']
        one_hot_encoding = self.get_particle(realisations, lemmas)
        return one_hot_encoding

    def get_a_particle(self, lemmas: list[str]) -> list:
        realisations = self.surface_realisations['a']
        one_hot_encoding = self.get_particle(realisations, lemmas)
        return one_hot_encoding
