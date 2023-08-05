from life_forms import blinker, toad
import os
import time
import random
from copy import deepcopy


# hold current gen, compare with new gen
# To save computation skip over sections that
# were untouched in the previous iteration


def game_of_life(initial_state):

    # Initial Properties
    grid_height = len(initial_state)
    grid_width = len(initial_state)

    past_state = deepcopy(initial_state)
    current_state = deepcopy(initial_state)

    iteration = 0
  
    while True:
        time.sleep(0.1)
        os.system('cls')
        iteration += 1

        for y in range(grid_height):
            for x in range(grid_width):
                life_count = 0
                curr_cell = past_state[y][x]

                if x > 0 and past_state[y][x-1] == 1:
                    life_count += 1

                if x < grid_width-1 and past_state[y][x+1] == 1:
                    life_count += 1


                if y > 0:
                # Check above left
                    if x > 0 and past_state[y-1][x-1] == 1:
                        life_count += 1
                    # Check above
                    if past_state[y-1][x] == 1:
                        life_count += 1
                    # Check above right 
                    if x < grid_width-1 and past_state[y-1][x+1] == 1:
                        life_count += 1


                if y < grid_height-1:
                # Check below left
                    if x != 0 and past_state[y+1][x-1] == 1:
                        life_count += 1
                    # Check below
                    if past_state[y+1][x] == 1:
                        life_count += 1
                    # Check below right 
                    if x < grid_width-1 and past_state[y+1][x+1] == 1:
                        life_count += 1


                #print(f'x:{x}, y:{y}, life: {life_count}')


                # Check birth
                if curr_cell == 0:
                    if life_count == 3:
                        current_state[y][x] = 1

                # Check death - overcrowding
                if curr_cell == 1 and life_count >= 4:
                    current_state[y][x] = 0

                # Check death - Exposure
                if curr_cell == 1 and life_count <= 1:
                    current_state[y][x] = 0

                # Check survival
                if curr_cell == 1 and (life_count == 2 or life_count == 3):
                    current_state[y][x] = 1

                #print(f'({y},{x}): {cell}, local life: {life_count}')
        
        past_state = deepcopy(current_state)
        sum_alive = sum([i.count(1) for i in current_state])

        #os.system('clear')
        print(f"Iteration: {iteration}")
        print(f"Cells Alive: {sum_alive} \n")


        for row in current_state:
            chars = ['.', 'o']
            print(" ".join([chars[cell] for cell in row]))



mega_sample = [[random.choice([0,1]) for x in range(50)] for i in range(50)]

game_of_life(mega_sample)