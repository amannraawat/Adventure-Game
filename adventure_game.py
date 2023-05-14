import time
print("\n")
name=input("Enter your name if you want to play this adventure game: ")
print("Welcome",name,"to this game!!")

print("\n")

print("Get ready for your Adventure")
print("\n\n")
time.sleep(2)

print("Suppose you are on a highway road and it has come to an deadend, then there is only left and right side road. Which side you want to take? \nType left if you want to take left and type right to take right.")
first_adv=input("\nEnter your choice: ")

print("\n\n")
if first_adv == 'left':
    print("As you take left, there are two roads on the way. One is good and well structured raod and second is unmetalled road.")
    print("Type 1 for good good and type 2 for unmetalled road.")
    sec_adv=int(input("\nEnter your choice: "))
    
    print("\n")
    if sec_adv==1:
        print("As you go by the good road. Then you encounter a bridge and then there are two ways to go to the other side.One is by swimming under the bridge and second is by walking through it.")
        print("Type swim if you want to go by swimming and type walk if you want to take bridge")
        
        third_adv=input("\nEnter your choice: ")
        if third_adv=='walk':
            print("You take the choice to go over the bridge. As you cross the bridge, then you encounter a car coming from behind. Then you tried to take lift.")
            fifth_adv=input("Do you want to talk the lift(yes/no)? ")
            
            if fifth_adv=='yes':
                print("\nYou took the lift and since the driver was a good man, he dropped you to your house. You Win!!")
                
            elif fifth_adv=='no':
                print("\nYou walked many kilometres and you couldn't get any help from anybody and alo you have not eaten since morning and then you died. You lose!!")
            
            else:
                print("Invalid answer. You lose the game!!")
            
        elif third_adv=='swim':
            print("You take the path of going under the bridge. As soon as you started to swim, suddenly the flow of river has gone high and unfortunately you get drowned. You lose!!")
            
        else:
            print("Invalid choice. You lose the game.")
            
    elif sec_adv == 2:
        print("As you take the unmetalled road. You walk for a while and then you encounter a women wearing white saree standing on the road. You couldn't see her face as she had kept her face down.")
        fourth_adv=input("Do you want to talk (yes/no)? ")
        
        if fourth_adv=='yes':
            print("\nAs you move closer to her, she killed you as she was a ghost. You lose!!")
        
        elif fouth_adv=='no':
            print("\nYou then walk for a while and suddenly get attacked by tiger and you died. You lose!!")
                
        else:
            print("\nInvalid answer. You lose the game!!")
             
    else:
        print("Invalid answer. You lose the game!!")
        
    
elif first_adv == 'right':
    print("As you took the right turn and you walk for a while and suddenly you saw a water tap on the side of the road.")
    sixth_adv=input("Do you want to drink water or not(yes/no)? ")
    
    if sixth_adv=='yes':
        print("\nAs you open the water tap and suddenly the sound of running water came and all the dogs of the street come and suddenly bite you as they think you are a thief. You lose!! ")
        
    elif sixth_adv=='no':
        print("\nYou walk for a few kilometres and then saw a bridge. There are two ways to pass the bridge, one is by walk above the bridge and second is under the bridge.")
        seventh_adv=input("Type above to go above the bridge and type under if you go under the bridge.")
        
        if seventh_adv=='above':
            print("\nYou then see a man standing on the bridge and he helped you in reaching your house. You win!!")
            
        elif seventh_adv=='under':
            print("\nYou take the choice of going under the bridge. If you want to cross, there is a river and you have to go to other side by swimming. As you get into river, you were eaten by crocodile. You lose!!")
            
        else:
            print("Invalid answer. You lose the game!!")
    else:
        print("Invalid answer. You lose the game!!")
    
else:
    print("Invalid answer. You lose the game!!")
    
    
print("\nThanks for playing :)")