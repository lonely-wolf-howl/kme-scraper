x = 1

def test_1(y):
  global x # <= important!
  print(x)
  x = y
  return x

print(x) # 1
print(test_1(2)) # 1 2
print(x) # 2

''''''

def test_2():
  print(x)
  x = x + 1
  return x

test_2() # cannot access local variable 'x' where it is not associated with a value ('x' is undefined)

''''''

def test_3():
  global x # <= important!
  print(x)
  x = x + 1
  return x

print(x) # 1
test_3() # 1
print(test_3()) # 2
print(x) # 3
