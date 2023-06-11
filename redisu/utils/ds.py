from redis import StrictRedis
import random
import os

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

if __name__ == "__main__":
  main()
