#
# autor: Michel
# date: 2024/11/06

class Pessoa:
  def __init__(self, nome, email):
    self.nome = nome
    self.email = str(email)
    
  def mostrar(self):
    print(f"Nome: {self.nome}\nEmail: {self.email}")