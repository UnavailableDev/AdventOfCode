
def f_is_num(a):
   return a >= "0" and a <= "9"


def find_first_num(data : str):
   for i in range(len(data)):
      if f_is_num(data[i]):
         return data[i]
   return 0

def find_last_num(data : str):
   for i in reversed(range(len(data))):
      if f_is_num(data[i]):
         return data[i]
   return 0



fp = open("input.txt", "r")

lines = fp.readlines()

val = 0

for lc in range(len(lines)):
   first = find_first_num(lines[lc])
   val = val + int(first + find_last_num(lines[lc]))

print(val)
