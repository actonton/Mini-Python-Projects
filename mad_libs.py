import random

print("Welcome to Madlibs!")

play = input("Do you want to play?\n")

if play.lower() != "yes":
     quit()

print("Welcome to the MadLibs game. If you type in words, we'll give you a story. Start by typing in a name.")

name = input().capitalize()
noun1 = input("Give me a noun!\n").lower()
noun2 = input("Give me another noun!\n").lower()
noun3 = input("Give me the last noun!\n").lower()
adjective1 = input("I need an adjective.\n").lower()
adjective2 = input("I really need a dog... just kidding give me another adjective.\n").lower()
adverb = input("PLEASE! I really need an adverb!\n").lower()

k = random.randint(1, 100)
if k % 2 == 0:
    story = print("Ace and his best friend " + name + " went to Disney World today! " 
    + "They saw a " + noun1 + " in a show at the Magic Kingdom "
    + "and ate a " + adjective1 + " feast for dinner."
    + " The next day I ran " + adverb + " to meet Mickey Mouse in his " + noun2
    + " and then that night I gazed at the " + adjective2 + " fireworks shooting from the " + noun3
    + ".") 
else:
    story = print("Rex and his bestie " + name + " went to the zoo last summer. "
    + "They saw a huge " + noun1 + " and a tiny little " + noun2 + ".  That night they decided to climb "
    + adverb + " into the " + noun3 + " to get a closer look." + " The zoo was " + adjective1 
    + " at night, but they didn't care... until" + adjective2 + " apes yelled in their faces, "
    + " making Rex and " + name + " sprint all the way back home.")