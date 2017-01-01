# Make sure to comment your code, including header comments!

"""
input: L, a list of strings;
       ascending, a boolean representing ascending (True) or descending (False)

output: return True if L is sorted in ascending (if ascending == True) or descending (if ascending == False) order

examples:
  is_sorted(['abel','Adam','baker','bArt'], True) --> True
  is_sorted(['abel','Adam','baker','bArt'], False) --> False
"""
def is_sorted(L, ascending):
  for i in range(1,len(L)):
      if compare(L[i-1], L[i]) <= 0 :
         ascending = 1
      else: 
         ascending = 0

 # return True # you'll have to change this, obviously!



"""
input: L, a list of strings;
       i and j, both integers representing valid index values (i.e. if L is of length n, then i and j can be any numbers between 0 and n-1, inclusive)

output: L, with the strings in indices i and j swapped

examples:
  swap(['abel'], 0, 0) --> ['abel']
  swap(['abel','Adam','baker'], 0, 2) --> ['baker','Adam','abel']

notes: you can assume that L will not be empty
"""
def swap(L, i, j):
  temp = L[i]
  L[i] = L[j]
  L[j] = temp

  return L # you'll have to change this, obviously!



"""
input: x and y, two strings

output: return a negative number (like -1) if x is alphabetically before y, a positive number (like 1) if x is alphabetically after y, and 0 if x and y are the same - remember to ignore case!

examples:
  compare('abel','Adam') --> -1
  compare('Zulu','abel') --> 1
  compare('Adam','adam') --> 0
"""
def compare(x, y):
  if x == y: 
     return -1
  elif x > y:
     return 1
  else: 
     return -1

 # return 0 # you'll have to change this, obviously!



"""
input: L, a list of strings;
       ascending, a boolean representing ascending (True) or descending (False)

output: L, in sorted order (either ascending if ascending == True, or descending if ascending == False)

examples:
  bubble_sort([], True) --> []
  bubble_sort([], False) --> []
  bubble_sort(['Adam','abel','bArt','baker'], True) --> ['abel','Adam','baker','bArt']
  bubble_sort(['Adam','abel','bArt','baker'], False) --> ['bArt','baker','Adam','abel']
"""
def bubble_sort(L, ascending):
  n = len(L)
  while not is_sorted(L, ascending):
    for i in range(1,n):
      # add code here!
      # what conditions should we be checking if ascending == True?
      # what about if ascending == False?
      if L[i-1] > L[i]:
             swap(L[i-1], L[i])
             ascending = 0
      else: 
             ascending = 1
  return L



# This following if statement checks whether your code was imported into another file.
# If it WASN'T imported, then the code in the if statement will run. Neat, huh?
if __name__ == '__main__':
   print "This is where your testing code goes."
