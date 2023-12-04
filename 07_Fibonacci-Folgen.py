def fib (n):
  if (n==1) or (n==2):
      rückgabe = 1
  else:
      rückgabe = fib(n-1)+fib(n-2)
  return rückgabe

print ('Die Anzahl lautet: ', fib(2))