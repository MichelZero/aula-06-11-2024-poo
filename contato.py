#
# Autor: Michel
# data: 2024/11/06

from pessoa import Pessoa
from endereco import Endereco

class ContatoPessoa(Pessoa, Endereco):
  def __init__(self, nome, email, rua, cidade):
    Pessoa.__init__(self, nome, email)
    Endereco.__init__(self, rua, cidade)
    
  def mostrar(self):
    Pessoa.mostrar(self)
    Endereco.mostrar(self)