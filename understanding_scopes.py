################### Scope ####################
# consider an apple tree inside of a fence vs. outside of a fence
# the apples inside the fence belong to the person inside the fence 
# the apples outside of the fence, belong to whomever outside the fence


enemies = 1

# although this function is called, the variable enemies = 2 only effects what is inside of the function
def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}") 

#this output will be 
# enemies inside function: 2
# enemies outside function:  1

def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()

# potion_strength = 2

# if we consider the following:
drink_potion()
print(potion_strength)  # this is not accessible outside of the function( it has a local scope )


#### GLOBAL SCOPE####
player_health = 10
def drink_potion():
  potion_strength = 2 ## LOCAL VARIABLE: only available inside a function ##
  print(player_health) # player health = 10 before the function is called therfore it is a global scope and is available anywhere
  # output: 10 

# there is no "Block Scope" in Python

game_level = 3
def create_enemy():
  enemies = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
    new_enemy = enemies[0]
  print(new_enemy)

### MODIFY A GLOBAL SCOPE ###
# hint don't typically name local and global variables the same 
enemies = 1
def increase_enemies():
  global enemies    # state that the variable is global however, THIS IS PRONE TO BUGS. #badIdea
  enemies +=1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}") 

## a better way to modify a global scope within a function without causing bugs
def increase_enemies():
  return enemies+ 1

enemies = increase_enemies()


## GLOBAL CONSTANT: a variable that ALWAYS remains the same
  ## write in uppercase seperated but underscores is necessary 
  ## PI = 3.14