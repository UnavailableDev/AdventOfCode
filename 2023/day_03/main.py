

def f_is_num(a):
   return a >= "0" and a <= "9"

def f_is_symbol(a):
   if not f_is_num(a) and a != "." and a != "\n":
      return True
   return False

def f_find_symbol(line : str):
   results = [0,0,0,0,0,0,0,0,0]
   length = 0
   for index, c in enumerate(line):
      if f_is_symbol(c):
         results[length] = index
         length = length + 1
   return results, length

def f_func(positions : tuple, lines : tuple):
   sum = 0
   last_found = False
   for index, pos in enumerate(positions):
      for line in lines:
         for x in range(pos-1, pos+2):
            if f_is_num(line[x]) and not last_found:
               print(x, line)
               sum += int(line[x])
               print(sum)
               last_found = True
            else:
               last_found = False

   return(sum)


fp = open("input.txt", "r")
lines = fp.readlines()
prev = ""
val = 0
part_nums = 0
for index, lc in enumerate(lines):
   part_positions, len = f_find_symbol(lc.strip())
   print(lc)
   if len > 0:
      print("a: ", len)
      part_nums = f_func(part_positions, (lines[index-1], lc, lines[index+1]))
   val = val + part_nums

   prev = lc

print(val)
