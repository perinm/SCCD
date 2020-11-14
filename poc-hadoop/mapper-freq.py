#!/usr/bin/env python3
from framework import Mapper, Reducer

class Meu_mapper(Mapper):
  def map(self):
    total = 0
    lista_de_tuplas = []
    for linha in self:
      palavra,qtd = linha.split('\t')
      total += int(qtd)
      lista_de_tuplas.append((palavra, qtd))
    for palavra, qtd in lista_de_tuplas:
      self.emit(palavra, str(qtd)+","+str(total))

mapper = Meu_mapper()
mapper.map()
