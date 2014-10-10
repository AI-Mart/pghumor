# -*- coding: utf-8 -*-
from __future__ import absolute_import

import itertools

import math

from nltk.corpus import WordNetCorpusReader
from pkg_resources import resource_filename

from clasificador.features.feature import Feature
from clasificador.herramientas.freeling import Freeling
from clasificador.realidad.tweet import remover_hashtags, remover_usuarios


class Antonimos(Feature):
    def __init__(self):
        super(Antonimos, self).__init__()
        self.nombre = "Antonimos"
        self.descripcion = """
            Mide la cantidad de pares de antónimos presentes en el texto.
        """
        self.wncr = WordNetCorpusReader(resource_filename('clasificador.recursos', 'wordnet_spa'))

    def calcular_feature(self, tweet):
        freeling = Freeling(remover_hashtags(remover_usuarios(tweet.texto)))

        cant_antonimos = 0

        for token in freeling.tokens:
            antonimos = []
            for synset in self.wncr.synsets(token.lemma):
                for lemma in synset.lemmas:
                    antonimos += [lemma_antonimo.name for lemma_antonimo in lemma.antonyms()]

            for otro_token in freeling.tokens:
                if otro_token.lemma in antonimos:
                    cant_antonimos += 1
                    break

        if len(freeling.tokens) == 0:
            tweet.features[self.nombre] = 0
        else:
            tweet.features[self.nombre] = cant_antonimos / math.sqrt(len(freeling.tokens))
