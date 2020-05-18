from module import sum
import pkgtest
# from collections import Counter
# from pkgtest import shrimp

# __name__ if '__main__' -> python이 내 스크립트를 실행
# __name__ if {모듈이름} -> module로서 import된 것.

print('demo.py', __name__)

# <symbol table>

# __name__ symbol table 현재 파이썬이 이 스크립트를 어떻게 load했는지?
# __init__.py 현재 package에서 초기화될 때 실행해야하는 스크립트인지?

# sum = 1
# pylint
print(sum(5, 5))
