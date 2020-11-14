#!/usr/bin/env python3
from framework import *
import re

class Meu_mapper(Mapper):
  def map(self):
    for linha in self:
      for palavra in linha.split():
        palavra = re.sub('[^a-z]+', '', palavra.lower())
        palavra = re.sub('[\s]+', '', palavra)
        if palavra != "":
          self.emit(palavra.strip(),1)

mapper = Meu_mapper()
mapper.map()
