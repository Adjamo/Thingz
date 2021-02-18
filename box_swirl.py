
#hows it g                                                            oin
# buy android worms
# buy lots of food 
# violin music for supermarkets - jon rose
# https://www.youtube.com/watch?v=i7j6ZKVJJAU

import os
import time
import random
from colorama import Fore, Back, Style
from copy import copy, deepcopy

'''

    Oliver Thingz. A celular automata in the vein of Conways game of life

    Dedicated to John Conway.

    Copyright (C) 2021 Adam Oliver


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.


    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

global num
num = 80
hei = 20
wid = 55


print('#')
print(Fore.RED + '%', end='') #
#print(Fore.LIGHTGREEN + '%') #
print(Fore.YELLOW + '*') #
print(Fore.GREEN + '&') #
print(Fore.BLUE + '$') #
#quit()

global grid
global grid2
grid = [[0 for i in range(wid)] for j in range(hei)] # 80 20 
grid2 = [[0 for i in range(wid)] for j in range(hei)] # 80 20 

# set all grid[x][y] to 6

county = 0
count = 0
for i in grid:
  for j in i:
    grid[county][count] = '6'
    
    count += 1
  count = 0 
  county += 1
# done

# set a few example variables (to be removed)

grid[0][1] = '1'
grid[0][2] = '2'
grid[0][3] = '3'
grid[0][4] = '4'
grid[0][9] = '5'
grid[1][7] = '6'

'''
buckets = ['6'] * num
buckets[9] = '7'
buckets[1] = '8'
buckets[2] = '9'
buckets[3] = '0'
buckets[4] = '1'
'''


# prints the grid2
def print_grid():

  grid2 = grid
  #grid2 = deepcopy(grid)

  count = 0
  for i in grid2:
    for e in i:

      if(e=='1'):print(Fore.WHITE + '#', end='' ) # end='' removes newline
      if(e=='2'):print(Fore.RED + '%', end='' ) # 
      if(e=='3'):print(Fore.YELLOW + '*', end='' ) # 
      if(e=='4'):print(Fore.GREEN + '&', end='' ) # 
      if(e=='5'):print(Fore.BLUE + '$', end='' ) # 
      if(e=='6'):print(Fore.BLUE + ' ', end='' ) # 

      if(e=='a'):print(Fore.WHITE + 'a', end='' ) # 
      
      count += 1
      if(count == wid): print('.'); count = 0


#print_grid()

print('')
print('')
	

# just grid
def add_a_cell():

  print('____')
  
  # change range(1) to change number of new characters
  
  for i in range(10):
    # finds a random place in the grid, adds a cell
    #print(random.randint(1,6))
    grid[random.randint(0,hei-1)][random.randint(0,wid-1)] = str(random.randint(1,6))
    #wid-1
    #hei-1
    #str(random.randint(1,6))
    
# this just stops list index out of range error
def numberz_h(thenum):

  #print('[')
  #print('wid thenum')
  #print(wid)
  #print(thenum)

  if(thenum >= wid):
    return wid - 1
  else:
    return thenum
    
def numberz(thenum):

  #print('[')
  #print('hei thenum')
  #print(hei)
  #print(thenum)

  if(thenum >= hei):
    return hei - 1
  else:
    return thenum


def expand():
  
  #grid2 = grid

  global grid

  ####a
  #y = deepcopy(x)
  grid2 = deepcopy(grid)

  count = 0
  for i in grid:
    county = 0
    for j in i:
      #pass

      #print(j)

      if( j == '1' ): # not working
        #print(':D' + str(i))
        #print('# detected')
        #print('x and y of # is: ...' + str(county) + ' ' + str(count))
        grid2[count][county-1] = '1' # up
        grid2[count][ numberz_h(county+1) ] = '1' # down
        grid2[count-1][county] = '1' # left
        grid2[ numberz(count+1) ][county] = '1' # right

        grid2[ count-1 ][county-1] = '1' # up left
        grid2[ numberz(count+1) ][ numberz_h(county+1) ] = '1' # down right
        grid2[ numberz(count+1) ][ county-1 ] = '1' # down left
        grid2[ count-1 ][ numberz_h(county+1) ] = '1' # up right
        #grid[count][county] = '4'
        
      if( j == '2' ): # not working
        #print(':D' + str(i))
        #print('# detected')
        #print('x and y of # is: ...' + str(county) + ' ' + str(count))
        grid2[count][ numberz_h(county+1) ] = '2'
        grid2[count][county-1] = '2'
        grid2[count-1][county] = '2'
        grid2[ numberz(count+1) ][county] = '2' # sometimes this goes out of the grid
        #grid[count][county] = '4'
        
        grid2[ count-1 ][county-1] = '2' # up left
        grid2[ numberz(count+1) ][ numberz_h(county+1) ] = '2' # down right
        grid2[ numberz(count+1) ][ county-1 ] = '2' # down left
        grid2[ count-1 ][ numberz_h(county+1) ] = '2' # up right

        
      if( j == '3' ): # not working
        #print(':D' + str(i))
        #print('# detected')
        #print('x and y of # is: ...' + str(county) + ' ' + str(count))
        grid2[count][county-1] = '3' # up
        grid2[count][ numberz_h(county+1) ] = '3' # down
        grid2[count-1][county] = '3' # left
        grid2[ numberz(count+1) ][county] = '3' # right

        grid2[ count-1 ][county-1] = '3' # up left
        grid2[ numberz(count+1) ][ numberz_h(county+1) ] = '3' # down right
        grid2[ numberz(count+1) ][ county-1 ] = '3' # down left
        grid2[ count-1 ][ numberz_h(county+1) ] = '3' # up right
        #grid[count][county] = '4'

      if( j == '4' ): # not working
        #print(':D' + str(i))
        #print('# detected')
        #print('x and y of # is: ...' + str(county) + ' ' + str(count))
        grid2[count][county-1] = '4' # up
        grid2[count][ numberz_h(county+1) ] = '4' # down
        grid2[count-1][county] = '4' # left
        grid2[ numberz(count+1) ][county] = '4' # right

        grid2[ count-1 ][county-1] = '4' # up left
        grid2[ numberz(count+1) ][ numberz_h(county+1) ] = '4' # down right
        grid2[ numberz(count+1) ][ county-1 ] = '4' # down left
        grid2[ count-1 ][ numberz_h(county+1) ] = '4' # up right
        #grid[count][county] = '4'
        

      county += 1
      
    count += 1







  # experiment
  count = 0
  for i in grid2:
    county = 0
    for j in i:
      if( j != grid[count][county] and ( grid[count][county] != 6 and j != 6 ) ):
        print('@ hi')
        if(int(j) > 4):
          j = '1'
        else:
          j += '1'
        #grid2[count][county] %= 4
        
      county += 1
      
    count += 1






  grid = deepcopy(grid2)

#?!

  #pass

for i in range(99):

  add_a_cell()

  print_grid()

  time.sleep(0.51)#0.1

  expand()

  #print_grid()

  #quit()
  

print('')

quit()

###
# end
#













def print_gridz(grid):

  #os.system('cls' if os.name == 'nt' else 'clear')

  for row in grid:
    for e in row:
            
      if(e=='1'):print(Fore.WHITE + '#', end='' ) # end='' removes newline
      if(e=='2'):print(Fore.RED + '%', end='' ) # 
      if(e=='3'):print(Fore.YELLOW + '*', end='' ) # 
      if(e=='4'):print(Fore.GREEN + '&', end='' ) # 
      if(e=='5'):print(Fore.BLUE + '$', end='' ) # 

      #if(e=='a'):print(Fore.BLUE + 'a', end='' ) # 


 
      '''
      #quit()
      if(e==11):print(Fore.LIGHTGREEN_EX + '%', end='') # 
      if(e==12):print(Fore.LIGHTBLACK_EX + '#', end='') # 
      if(e==13):print(Fore.BLACK + '@', end='') # 
      if(e==14):print(Fore.GREEN + '&', end='') # 

      if(e==5):print(Fore.RED + '5', end='') # 
      if(e==6):print(Fore.CYAN + '6', end='') # 

      if(e==15):print(Fore.RED + '*', end='') # 
      if(e==16):print(Fore.CYAN + '!', end='') # 

      if(e==0):print(' ', end='') # end='' removes newline
      '''      
    print('.')

print_grid(buckets)

quit()


###
# end of program
#


def col_(foo):
  if(foo > 19):
    return 0
  elif(foo == -1):
    return 19
  else:
    return foo

def row_(bar):
  if(bar > 79):
    return 0
  elif(bar == -1):
    return 79
  else:
    return bar

def ad_step(next):

  active = 0

  for player in dave:

    # if player direction is up
    if(player[2]==0): # animals direction (red,green,...)
      
      #no collision
      if(next[col_(player[3]-1)][row_(player[4])] != player[1] and
         next[col_(player[3]-1)][row_(player[4])] != player[0] + 10
         ): # 

        # move player
        next[col_(player[3]-1)][row_(player[4])] = player[0]
        next[col_(player[3])][row_(player[4])] = player[0]+10 # make an 'X'
        player[3] = col_(player[3]-1)
        active += 1
      else:
        #change direction
        player[2] = 1

    # if player direction is down
    if(player[2]==1): # animals direction

      #no collision
      if(next[col_(player[3]+1)][row_(player[4])] != player[1] and
         next[col_(player[3]+1)][row_(player[4])] != player[0] + 10
      ): # 

        next[col_(player[3]+1)][row_(player[4])] = player[0]
        next[col_(player[3])][row_(player[4])] = player[0]+10 # make an 'X'
        player[3] = col_(player[3]+1)
        active += 1
      else:
        #change direction
        player[2] = 3

    # if player direction is left
    if(player[2]==2): # animals direction
      
      #no collision
      if(next[col_(player[3])][row_(player[4]-1)] != player[1] and
         next[col_(player[3])][row_(player[4]-1)] != player[0] + 10
      ): # 

        next[col_(player[3])][row_(player[4]-1)] = player[0]
        next[col_(player[3])][row_(player[4])] = player[0]+10 # make an 'X'
        player[4] = row_(player[4]-1)
        active += 1
      else:
        #change direction
        player[2] = 0

    # if player direction is right
    if(player[2]==3): # animals direction

      #no collision
      if(next[col_(player[3])][row_(player[4]+1)] != player[1] and
         next[col_(player[3])][row_(player[4]+1)] != player[0] + 10
      ): # 

        next[col_(player[3])][row_(player[4]+1)] = player[0]
        next[col_(player[3])][row_(player[4])] = player[0]+10 # make an 'X'
        player[4] = row_(player[4]+1)
        active += 1
      else:
        #change direction
        player[2] = 2


  return next, active

    
def game(grid):

  steps = 0
  old = []

  while True:

    global dave

    new_grid, active = ad_step(grid)
    
    print()
    print()
    print_grid(new_grid)
    print(Fore.WHITE + 'Generation: ' + str(steps) )
    print(Fore.WHITE + 'Active Pieces: ' + str(active) )
    steps += 1
    time.sleep(0.1)


# initialaise variables
global dave
# what dave looks like
# dave = [1/2/3/4,@/#/%/&,direction,x coord,y coord]
# e.g. dave = [[1,14,0,1,1],[2,11,1,2,2],[3,12,2,3,3],[4,13,3,4,4]]
dave = []
# start with a random map
  
grid = [[0 for i in range(80)] for j in range(20)]

# range of 15 ends quickly
# range of 20 ends 4,000 to 27,000 generations
# range of 25 ends 80,000 generations
# range of 30 500,000 + no end

for var_name in range(25):# change this number for fun!
  for me in range(4):# number of colours

    ran_x = random.randint(0, 19)
    ran_y = random.randint(0, 79)

    grid[ran_x][ran_y] = me+1
    
    if(me == 0):# 1 cant beat 2
      dave.append( [me+1,12,me,ran_x,ran_y] )
    if(me == 1):# 2 cant beat 3
      dave.append( [me+1,13,me,ran_x,ran_y] )
    if(me == 2):# 3 cant beat 4
      dave.append( [me+1,14,me,ran_x,ran_y] )
    if(me == 3):# 4 cant beat 1
      dave.append( [me+1,11,me,ran_x,ran_y] ) # add more if you want more colours (req coding!)

new_number = game(grid)

if(new_number > number): # keep the record
  number = new_number



