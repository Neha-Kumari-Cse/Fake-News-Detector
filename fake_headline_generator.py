
#1 import the random module
import random

#2- create subjects

Subjects =[
    "Shahrukh khan",
    "Virat Kohli",
    "A mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi",

]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "delcares war on",
    "orders",
    "celebrates",
]

places_or_things=[
    "at Red Fort",
    "im mumbai Local Train",
    "a plote of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate",
]
#3- start the headline generation loop
while True:
    subject = random.choice(Subjects)
    action = random.choice(actions)
    place_or_things = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} { action} {places_or_things}"
    print("\n" +headline)

    user_input = input("\n Do you want another headline? (yes/no)").strip()
    if user_input == "no":
        break

print("\nThanks for using the Fake News Headline Generator. Have a fun day")



    
    
    
    
    
    



