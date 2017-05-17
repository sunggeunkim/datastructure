def integer_divide(x, y):
  
  # We will return -1 if the
  # divisor is '0'.
  if y == 0:
    return -1
    
  if x < y:
    return 0
  elif x == y:
    return 1
  elif y == 1:
    return x

  q = 1
  val = y
  import pdb;pdb.set_trace()
  while val < x:
    val <<= 1
    # we can also use 'val = val + val;'
    q <<= 1
    # we can also use 'q = q + q;'

  if val > x:
    val >>= 1
    q >>= 1
    return q + integer_divide(x-val, y)

  return q;

print(integer_divide(11,3))
