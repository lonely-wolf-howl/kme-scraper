x = 1

def test(y):
  global x
  x = y
  return x

print(test(2)) # 2
