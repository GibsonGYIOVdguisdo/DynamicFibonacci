cache={0:0,1:1}

def fibonacci(num):
  if num in cache:
    return cache[num]
  cache[num]=fibonacci(num-1)+fibonacci(num-2)
  return(cache[num])
