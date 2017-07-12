def insertBits(n, a, b, k):
   for i in range (a,b+1):
      n=n&~(1<<i)
   return n|(k<<a)
