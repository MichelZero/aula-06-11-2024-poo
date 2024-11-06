#
# autor: Michel
# date: 2024/11/06

class Endereco:
  def __init__(self, rua, cidade):
    self.rua = str(rua)
    self.cidade = str(cidade)
  
  def mostrar(self):
    print(self.rua)
    print(self.cidade)
