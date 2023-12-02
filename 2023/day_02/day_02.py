import sys

script_dir = sys.path
sys.path.append("../")

import lib.advent_math

sys.path = script_dir

def f_validator(rounds):
   max_red = 1
   max_green = 1
   max_blue = 1
   for round in rounds:
      cubes = round.split(', ')
      print(cubes)
      for cube in cubes:
         num, colour = cube.split(' ')
         num = int(num)
         match colour:
            case "red":
               max_red = max(max_red, num)  
            case "green":
               max_green = max(max_green, num)
            case "blue":
               max_blue = max(max_blue, num)
      

   return max_blue*max_green*max_red




fp = open("games.txt", "r")
lines = fp.readlines()

game_id = 0
val = 0
for li in (lines):
   game_name, game = li.strip("\n").split(': ')
   game_id = game_name.split(' ')[1]

   rounds = game.split('; ')
   
   val = val + f_validator(rounds)

print(val)
