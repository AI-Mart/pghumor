# -*- coding: utf-8 -*-
from __future__ import absolute_import

import math

from features.feature import Feature
from herramientas.freeling import Freeling
import herramientas.utils

class PrimeraPersona(Feature):

	def __init__(self):
		self.nombre = 'Primera Persona'
		self.descripcion = 'Esta caracteristica mide si el texto esta expresado en primera persona'
		
	def calcularFeature(self, tweet):
		tf = Freeling(tweet.texto)
		primeraPersona = 0
		for token in tf.tokens:
			if self.estaEnPrimeraPersona(token.tag):
				primeraPersona += 1

		if len(tf.tokens) == 0: # FIXME: no debería pasar
			print "Error: ", tweet.texto
			tweet.features[self.nombre] = 0
		else:
			tweet.features[self.nombre] = primeraPersona/math.sqrt(len(tf.tokens))

	def estaEnPrimeraPersona(self, tag):
		return (tag[0] == 'D' and tag[2] == '1') # determinante en primera persona
			or (tag[0] == 'V' and tag[4] == '1') # verbo en primera persona
			or (tag[0] == 'P' and tag[2] == '1') # pronombre en primera persona
