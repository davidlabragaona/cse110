"""
Author: David Labra Gaona
Purpose: Create your own text-based adventure game with at least three levels of
choices. It's up to you to determine the scenarios, the choices, and the 
consequences.
"""

#We define the Game intro
intro = """You wake up with a headache. It seems you cannot focus very well,
your eyes are blury. After some hours you feel some relief. You move your head 
around to see if you can recognize the landscape, but it is not familiar. Some
Mountains and the wind. It must be 4 o'clock in the afternoon, and by the sun
position you guess it is fall...
"""

#We define the levels
level1 = """You know it will be cold after 7pm, so you better prepare for the 
night. Would you like to IMPROVISE a small place to sleep or COLLECTING food 
seems more reasonable?
"""
level2 = ""
level3 = ""

print(intro)
print()
print(level1)
level1_option = input("Enter one of the options: ")
if level1_option.lower() == "improvise":
    level1 = """It will be dark soon, so you hurry to improvise some sort of
    place where you can spend the night. You don't remember anything from the 
    past nor how you got to that place, but you will survive and look for 
    answers.
    """
elif level1_option.lower() == "collecting":
    level1 = """You know that without food, you will not be able to make it far.
    You decide to look for food and collect it. Your survival instinct is 
    telling you that no other task is more important.
    """

