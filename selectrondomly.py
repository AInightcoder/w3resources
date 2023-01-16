import random

def selectrandomnum(test):
  all =5
  while all>0:
    son=random.randrange(all)
    det=test.pop(son)
    print(det)
    all=all-1

tests=[2,5,8,9,14,15,12,27]
selectrandomnum(tests)
