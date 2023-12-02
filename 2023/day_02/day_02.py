


def f_validator(rounds):
   for round in rounds:
      red = 0
      green = 0
      blue = 0
      cubes = round.split(', ')
      print(cubes)
      for cube in cubes:
         num, colour = cube.split(' ')
         num = int(num)
         match colour:
            case "red":
               red = num
            case "green":
               green = num
            case "blue":
               blue = num
      
      if red > 12 or green > 13 or blue > 14:
         return False

   return True




fp = open("games.txt", "r")
lines = fp.readlines()

game_id = 0
val = 0
for li in (lines):
   game_name, game = li.strip("\n").split(': ')
   game_id = game_name.split(' ')[1]

   rounds = game.split('; ')
   
   if f_validator(rounds):
      print(game_id)
      val = val + int(game_id)

   val = val 

print(val)
