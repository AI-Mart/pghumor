from __future__ import absolute_import

import subprocess

def obtenerDiccionario(filename):
	lines = [line.rstrip('\n') for line in open(filename)]
	return lines

def ejecutarComando(command):
	p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	return p.stdout.readlines()

def escapar(texto):
	return texto.replace('"','\\"').replace("'","\\'").replace("`","\\`")