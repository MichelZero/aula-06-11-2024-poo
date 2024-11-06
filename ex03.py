#
# autor: Michel
# date: 2024/11/06

# classe A filha object
class A:
  def falar(self):
    print("o A está falando!")

# classe B
class B():
  # def falar(self):
  def falar2(self):
    print("o B está falando!")

# classe C filha B e A
#class C():
#  def falar(self):
#    print("o C está falando!")
class C(B, A):
  pass  
    
# instancia das classes
a1 = A()
b1 = B()
c1 = C()

a1.falar()
b1.falar2()
c1.falar()
c1.falar2()
print(C.__mro__)