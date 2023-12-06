
def f_clean(a : str):
   a = a.strip() # removes '\n'
   a = a.split(" ")
   a = list(filter(None, a)) # removes empty chars ''
   a = a[1:] # removes first element
   return a


def check_all_single(time : int, distance : int):
   val = 0
   i = time

   while i > 0:
      # print(i, time, distance)
      # print (i * (time-i))
      if i * (time-i) > distance:
         val += 1
         # print(val)
      
      i -= 1

   return val




fp = open("input.txt", "r")
lines = fp.readlines()
val = 1
res = []

times = f_clean(lines[0])
min_dist = f_clean(lines[1])


for index, time in enumerate(times):
   res.append( check_all_single(int(time), int(min_dist[index])) )

print (res)

for r in res:
   val *= r

#    single_wins = f_count_dupes(win, own)
#    if single_wins > 0:
#       for i in range(single_wins-1):
         

#    val += f_numerate()
#    # part_positions, length = f_find_symbol(lc.strip())

print(val)
