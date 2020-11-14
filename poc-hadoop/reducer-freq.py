#!/usr/bin/env python3
from framework import Reducer

class Meu_reducer(Reducer):
  def reduce(self):
    for palavra, values in self:
      for v in values:
        qtd, total = v[1].split(",")
      #qtd, total = (count[1].split(',') for key, count in values)
      self.emit(palavra, f"{int(qtd)/int(total)*100:.5f}%")

reducer = Meu_reducer()
reducer.reduce()
