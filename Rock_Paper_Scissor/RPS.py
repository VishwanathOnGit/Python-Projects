# import random module 
import random 
  
# Print multiline instruction 
# performstring concatenation of string 

print("Winning Rules of the Rock Paper Scissor Game as follows: \n"
                        +"Rock vs Paper->Paper wins \n"
                        +"Rock vs Scissor->Rock wins \n"
                        +"Paper vs Scissor->Scissor wins \n")

comp_score = 0
user_score = 0
while True:

    print("Enter weapon number \n Rock      ---> 1 \n Paper     ---> 2 \n Scissor   ---> 3 \n") 
      
    # take the input from user 
    weapon = int(input("User turn: ")) 
    # looping until user enter invalid input 
    while weapon < 1 or weapon > 3: 
        weapon = int(input("enter valid input: ")) 
          
  
    # initialize value of weapon_name variable 
    # corresponding to the weapon value 
    if weapon == 1: 
        weapon_name = 'Rock'
    elif weapon == 2: 
        weapon_name = 'paper'
    else: 
        weapon_name = 'scissor'
          
    # print user weapon  
    print("user weapon is: " + weapon_name) 
    print("\nNow its computer turn.......") 

    # Using randint method of random module
    comp_weapon = random.randint(1, 3)

    # looping until comp_weapon value  
    # is equal to the weapon value 
    while comp_weapon == weapon: 
        comp_weapon = random.randint(1, 3)

    # initialize value of comp_weapon_name  
    # variable corresponding to the weapon value 
    if comp_weapon == 1: 
        comp_weapon_name = 'Rock'
    elif comp_weapon == 2: 
        comp_weapon_name = 'paper'
    else: 
        comp_weapon_name = 'scissor'
          
    print("Computer weapon is: " + comp_weapon_name) 
  
    print(weapon_name + " V/s " + comp_weapon_name) 

       # condition for winning 
    if((weapon == 1 and comp_weapon == 2) or
      (weapon == 2 and comp_weapon ==1 )): 
        print("paper wins => ", end = "") 
        result = "paper"
          
    elif((weapon == 1 and comp_weapon == 3) or
        (weapon == 3 and comp_weapon == 1)): 
        print("Rock wins =>", end = "") 
        result = "Rock"
    else: 
        print("scissor wins =>", end = "") 
        result = "scissor"
  
    # Printing either user or computer wins 
    if result == weapon_name: 
        user_score += 1
        print("<== User wins ==>") 
    else: 
        comp_score += 1
        print("<== Computer wins ==>") 
          
    print("Do you want to play again? (Y/N)") 
    ans = input() 
  
  
    # if user input n or N then condition is True 
    if ans == 'n' or ans == 'N': 
        break
      
# after coming out of the while loop 
# we print thanks for playing 
print("\nFinal Scores \n User: {}, \t Computer: {}".format(user_score, comp_score)) 
print("\nThanks for playing") 