
import math

def f_clean(a : str):
   a = a.split(" ")
   a = list(filter(None, a))
   return a

def f_count_dupes(nums_a, nums_b):
   val = 0
   for num_a in nums_a:
      for num_b in nums_b:
         if num_a == num_b:
            val += 1
   return(val)

def f_numerate(a : int):
   return math.floor(pow(2,a-1))


fp = open("input.txt", "r")
lines = fp.readlines()
val = 0
for index, lc in enumerate(lines):

   index, values = lc.strip().split(":")
   win, own = values.split(" |")
   win = f_clean(win)
   own = f_clean(own)

   val += f_numerate(f_count_dupes(win, own))
   # part_positions, length = f_find_symbol(lc.strip())

print(val)
