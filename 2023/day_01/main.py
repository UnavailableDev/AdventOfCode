
table = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def f_is_num(a):
   return a >= "0" and a <= "9"

def f_num2int(a : str):
   for i, check in enumerate(table):
      if a[:len(check)] == check:
         return i+1
   return None

def f_check_wrapper(data : str):
   oen = f_num2int(data)
   if oen != None:
      return str(oen)
   elif f_is_num(data[0]):
      return data[0]
   else:
      return None

# def f_cleanup(data : str):
#    print("BEFORE: --------")
#    print(data)

#    for i, check in enumerate(table):
#       data = data.replace(check, str(i+1))
#    print(data)
   
#    return data

def find_first_num(data : str):
   for i in range(len(data)):
      temp = f_check_wrapper(data[i:])
      if temp != None:
         return temp

   return 0

def find_last_num(data : str):
   for i in reversed(range(len(data))):
      temp = f_check_wrapper(data[i:])
      if temp != None:
         return temp
      
   return 0


fp = open("input.txt", "r")
lines = fp.readlines()

val = 0
for lc in (lines):
   first = find_first_num(lc)
   val = val + int(first + find_last_num(lc))

print(val)
