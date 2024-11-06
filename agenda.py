#
# Author: Michel
# data: 2024/11/06

from contato import ContatoPessoa as C

class Agenda:
  pessoaD = dict()
  
  def add(self, nome, email, rua, cidade):
    self.pessoaD[nome] = C(nome, email, rua, cidade)
    
  def buscarNome(self, nome):
    if nome in self.pessoaD:
      self.pessoaD[nome].mostrar()
    else:
      print(f"{nome}, não existe!")
    
  def buscarEmail(self, email):
    pass
    
# instancia
a1 = Agenda()
a1.add("michel","email", "das casas", "CZ")
