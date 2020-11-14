#!/usr/bin/env python3

from framework import Reducer

class Meu_reducer(Reducer):
  def reduce(self):
    for palavra, values in self:
      val = sum(int(count) for key, count in values)
      self.emit(palavra, val)

reducer = Meu_reducer()
reducer.reduce()
