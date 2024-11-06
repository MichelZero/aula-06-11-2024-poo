#
# autor: Michel
# date: 2024/11/06

# importar ex01
from ex01 import B
from ex01 import A
# from ex01 import B, A
# from ex01 import *


# classe D filha de B
class D(B):
  pass

# classe E:
class E():
  pass

# classe F filha D e A
class F(D, A):
  pass