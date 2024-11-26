# Sort the list based on how close the number is to 100
def myfunc(n):
  return abs(n - 100)

thislist = [1000, 50, 611, 82, 150]
thislist.sort(key = myfunc)
print(thislist)