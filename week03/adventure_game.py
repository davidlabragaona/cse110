#Creativity: Player name addition. Better incorrect response handling
"""
Author: David Labra Gaona
Purpose: Create your own text-based adventure game with at least three levels of
choices. It's up to you to determine the scenarios, the choices, and the 
consequences.
"""

#Let's define the texts that will be presented to the user based on the 
#selection he or she makes.

t0 = """You have been contacted to work with a team of experts investigating
all the possible issues with the global warming. During the past 2 years, the
team traveled to different countries to study volcanos, both active and dormant.
You love traveling, but this time you are little worried. You can't explain it,
but somehow feel that this trip will not be the same, as if it could be your
last trip.

Dr. Barbados is the leader and is waiting for your response. You told him that
you were going to answer him no latter than Sunday afternoon.

It's Sunday 4:15 p.m. Your cell-phone rings. As you glance at it, you see Dr.
Barbados' number on the screen. If you choose to join the team this time, type 
JOIN, otherwise ANSWER, to answer the phone, and tell Dr Barbados, that this 
time you will not be able to help them. Perhaps next time.
"""

t1 = """Dr. Barbados: -Hello Dr. {}. How are you?
You: -Hello Dr. Barbados. My answer is yes. I'll go with you.
Dr. Barbados: -Well, good, as always is good to have you with us. I'll tell my
secretary to give you the specifics. In that case, there is not much to talk
about. I'll see you in two weeks. Bye {}.
You: Bye Dr. Barbados.

2 weeks later you arrive to Junín de los Andes. You will visit a Volcano called
Lanín, which means "Dead Rock" in mapundungun, the tongue of native villagers.
You don't want to waste time. The ascension to the top of the volcano will not
be easy. After a brief meeting with the team, the ascension begins.

After 17 hours of walking you are close to the top. You decide to sit on a rock.
It is cold. You take your water bottle and drink a little. You seem to recover
your breath. You didn't realize that you are close to a cliff. As you want to
stand up, you trip on a branch and start falling through the cliff. All of a
sudden, your fall stops and you remain in the air. Your foot is tight to a rope
and that is the only element preserving your life. Your team members quickly
give you instructions. You don't have much time, you have to decide whether if
you keep your backpack or drop it so you can try to climb through the rope that
keeps you in the air.

What would you like to do? Type KEEP, to keep your backpack or DROP, to remove
the extra weight. You can also try to OPEN your backpack to get your computer.
"""


t2 = """Dr. Barbados: -Hello Dr {}. What is your response at this time.
You: -Hello Dr. Barbados. I've been thinking about this matter, and I'm going
to have to decline this time.
Dr. Barbados: -Are you sure? Is that your final answer?
You: Yes... At least for this trip, I haven't been feeling good about it.
Dr. Barbados: -Ok, fair enough. Let me know if you change your mind...
You: -Sure.
Dr. Barbados: -Bye Dr. {}.
You: -Bye.

Type WALK to go to the park for a walk, or READ if you want to read a book to
distract your mind.
"""
t3 = """You will not drop your backpack. You have special tools you will need
for your investigation. You talk to the team members that are trying to bring
you back safely. They are telling you to drop it, but why? Your computer is in
your backpack also. As you hold your backpack your team members start telling
you that the rope is not going to support your weight. As they scream this to
you, you are resolute to keep the backpack. The result is obvious. The rope was
not able to hold you.
"""

t4 = """You take your coat, the weather is not very cold, but when the sun goes 
down, you feel it.
You walk down the stairs. Close the door and start walking towards the park.
The scene is gorgeous. Some trees have lost their leaves and some have turn
yellowish. The sun bathes them with its soft rays and everything looks golden.
You are almost there, but incorrectly decide to cross the street by the middle.
As you were thinking of your conversation with Dr. Barbados, you didn't see a
car that was going by. To your surprise, you see it at the last second, but it
is too late. The car hits you. You loose conscience and spend two days at the
hospital in comma and finally die.
"""

t5 = """You realize that the extra weight will not help in this situation, so
you quickly drop your backpack. Your computer was there. You save your life and
that is all what matters. Of course, without your computer, you will not be able
to help this time, but there will be more opportunities for that. The global
warming or climate change is something serious and needs action.
"""

t6 = """You love reading books, specially novel books. It is so easy for you to
put yourself in the eyes of the main character.
You look for your comfy chair, take off your shoes and open the book. By your
side you have a mug with hot cocoa. You spend all the afternoon reading and then
fall asleep.
"""

t7 = """You know that you will need to drop the backpack, but your computer is
inside. You will not be able to carry your investigation unless you have it.
You store a lot of mathematical models and without them you will not be of much
help. You try very hard to get the computer out of the backpack. You accomplished
it. Your team members are able to bring you back to solid ground.

After 2 weeks you provide very accurate predictions based on your studies. It
could be said that you were key to correlate different weather conditions.
Based on your models and predictions the complete scientific community started
building new models specially to make crops more resistent to global phenomena.
"""

#responses
r0 = "Type JOIN or ANSWER: "
r1 = "Type KEEP, DROP or OPEN: "
r2 = "Type WALK or READ: "
rtry = "The option you selected is incorrect. Please try again."

#Game Logic:
exit = False
state = 0

print("Welcome to Choose your own destiny game.")
print("Please, enter your name and lastname")
name = input("Name: ")
lastname = input("Lastname: ")

print(f"\nThank you {name.capitalize()} {lastname.capitalize()}.\n")

#Lvl1
print(t0)
while not exit:
    option = input(r0)
    if option.lower() == "join":
        exit = True
        state = 1
    elif option.lower() == "answer":
        exit = True
        state = 2
    else:
        print(rtry)
print()

#lvl2
exit = False
if state == 1:
    print(t1.format(lastname, name))
    state = r1
else:
    print(t2.format(lastname, name))
    state = r2
while not exit:
    option = input(state)
    if option.lower() == "keep":
        exit = True
        state = 3
    elif option.lower() == "drop":
        exit = True
        state = 5
    elif option.lower() == "open":
        exit = True
        state = 7
    elif option.lower() == "walk":
        exit = True
        state = 4
    elif option.lower() == "read":
        exit = True
        state = 6
    else:
        print(rtry)
print()

#lvl3
exit = False
if state == 3:
    print(t3)
elif state == 4:
    print(t4)
elif state == 5:
    print(t5)
elif state == 6:
    print(t6)
else:
    print(t7)

print("The End.")