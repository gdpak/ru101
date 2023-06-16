from redis import StrictRedis
import random
import os
from time import time
from functools import wraps

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r took: %2.4f sec' % \
          (f.__name__, te-ts))
        return result
    return wrap

@timing
def local_search(l, e):
   for el in l:
      if el == e:
         return el

@timing      
def redis_search(r, l, e):
   ll = r.llen(l)
   for i in range(0, ll):
      v = r.lindex(l, i)
      if e == int(v):
         return v
      
def local_list(name, n):
  for i in range(n):
    elem = random.randint(1, n)
    name.append(elem)

def llist(r, intlist):
  r.delete("mylist")
  for elem in intlist:
    r.rpush("mylist", elem)
    
  
def main():
  """Entry point, allowing the function to be called from command line
  arguments"""
  redis = StrictRedis(host=os.environ.get("REDIS_HOST", "localhost"),
                      port=os.environ.get("REDIS_PORT", 6379),
                      password=os.environ.get("REDIS_PASSWORD", None),
                      db=0)
  mylist = []
  local_list(mylist, 1000000) 
# llist(redis, mylist)
  local_search(mylist, 500000)
  redis_search(redis, "mylist", 500000)

if __name__ == "__main__":
  main()
