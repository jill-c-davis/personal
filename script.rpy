# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Ame", color="371F76")
define c = Character("Cincere", color="4FB9AF")
define m = Character("Muse", color="FF9899")
define f = Character("Frog", color="5EDD5F")
default p = "YourName"

# Romance Points (RP)
default c_points = 0 # cincere points
default a_points = 0 # ame points
default m_points = 0 # muse points

# Images

# Backgrounds 

image bg dorm:
    "images/Dorm_Final.png"
    zoom 1.5

image bg classroom:
    "images/Classroom_Final.png"
    zoom 1.5

image bg cafe:
    "images/Cafe_Final.png"
    zoom 1.25

image bg library:
    "images/Library_Final.png"

# Characters

image cincere neutral:
    "images/cincere_neutral.png"
    zoom 0.375

image cincere full smile:
    "images/cincere_smile_full.png"
    zoom 0.5

# image ame frazzled
# image ame amused

# Audio

define audio.birds = "music/birds.mp3"

define audio.door = "music/door.mp3"

define audio.startled = "music/startled.mp3"

define audio.notebook_tear = "music/notebook_tear.mp3"

define audio.notebook_crumple = "music/notebook_crumple.mp3"

# define audio.pensive = "music/pensive"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music birds

    scene black
    with dissolve

    f "Hoping that extra beauty sleep will win her affection?"

    p "I feel like I died during that nap. I can't even remember my name..."

    $ p = renpy.input("Enter your name.")

    play music door noloop

    scene bg dorm
    with fade

    show frog teasing
    with dissolve

    f "Your name is [p]."

    f "You go to Deez Nuts University and you have a class in like twenty minutes."

    play music startled noloop

    f "Ha! Your little crush isn't going to like you back if you show up looking like you just rolled out of bed."

    "You get ready as quickly as possible and head to class."

    scene bg classroom
    with fade

    "On the projector, a movie plays."

    "Cincere whispers from the desk behind you..."

    show cincere full smile
    with dissolve

    c "Hey...can I borrow your pen?"

    play music startled noloop

    "You notice you only brought one pen in your rush to class."

    menu:
            "Give her the pen.":
                $ c_points += 1
                jump pen

            "Keep the pen.":
                jump no_pen

    label pen:

        show cincere neutral at right
        with dissolve

        c "Hey... let me use some paper too?"

        play music notebook_tear noloop

        p "Here... is one page enough?"

        "Your professor's voice booms:"

        "That's enough talking in my class!"

        "A note flies over your shoulder."

        play music notebook_crumple noloop

        "You open the note and it says..."

        c "Your shirt is on inside out and it's distracting me from the movie - Cincere"

        play music startled noloop

        "You look down to check your shirt, and the seams are indeed facing outward."

        "After class, you go back to your dorm to change."

        scene bg dorm
        with fade

        # play music "disappointed"

        p "The first time we ever talk to each other and it's about how I am a mess..."

        p "Maybe it's not too late to drop this class..."

        p "No. I promised myself I would stick it out."

        p "I'll go to the cafe for a pick-me-up"
        jump cafe

    label no_pen:

        show cincere neutral at right
        with dissolve

        c "Okay, I'll ask someone else."

        "After the movie, you notice you've put your shirt on inside-out."

        "You go back to your dorm to change."

        scene bg dorm
        with fade

        p "Maybe it's not too late to drop this class..."

        p "No. I promised myself I would stick it out."

        p "I'll go the cafe for a pick-me-up."
        jump cafe

    '''label cafe:

        scene bg cafe
        with fade

        "A barista appears behind the counter."

        show ame frazzled
        with dissolve

        # play music pensive noloop

        p "I don't think I've seen her working here before..."

        p "Are you new here?"

        a "..."

        p "I did not mean to say that out loud..."

        p "Or that either..."

        show ame amused at right
        with dissolve
        
        a "Name for your order?"
        
        p "It's [p]. And just a medium roast with two creams and two sugars. Sorry. I-I mean, thank you."

        scene bg cafe
        with fade
       
       # play music pensive

        p "Today is just not my day..."

        # show ame neutral at right
        with dissolve

        a "[p]?"

        play music startled noloop

        show ame amused at right
        with dissolve

        "The barista hands you your coffee and you notice some writing on the cup."

        p "Oh uhm..."

        show ame winking at right
        with dissolve

        "The barista goes to help another customer, but you notice the note she's written on your cup:"

        scene bg cafe

        a "Yes, I'm new. I hope your drink doens't suck - Ame."

       # play music success noloop

        "You head to the library, head reeling and coffee in hand."

        scene black
        with fade

        p "I feel like she was flirting with me...but like why? It doesn't make any sense."

        p "But she winked at me!"

        menu:
            "That's totally flirting, right?":
                $ a_points += 1
                jump library

            "She was probably just being nice.":
                jump library

    label library:

        scene bg library
        with fade

        "The entire library is full of students this afternoon."

        # play music chatter

        "You look around and notice the girl at the table nearest you has moved her backpack from the seat. She's moving her things around to make room."

        p "She must have noticed my vulturing...My winning streak of first impressions is going strong. I'll ask her if I can sit next to her."

        p "Hey, is it alright if I sit here?"

        show muse neutral
        with dissolve

        m "Yes! Please do?"

        p "Um, okay."

        "You sit down and get your things to begin studying."

       #  play music rummaging

        menu:
            "Tell her your name.":
            $ m_points += 1
            jump shy
            "Say nothing":
            jump muse

    label shy:

        "You glance over and smile at the girl."

        "Her eyes meet yours because she's been staring at you the entire time."

        "You decide to talk first: "

        p "I'm [p]!"

        m "..."

        show muse shy
        with dissolve

        m "I'm shy. Sorry, I mean Muse. My name is Muse."
        jump muse

    label muse:

        scene bg library
        with fade

        "After that, you both study at the same table for a while."

        "To your surprise, the silence doesn't feel awkward, but actually kind of...nice."

        "The girl leaves first, and you don't look up from your books until she's gone."

        "When you do, you notice she left you a small note: "

        m "If you come a little earlier tomorrow, we can chat a little before studying."

        "You think of all the notes you've received today and decide that her handwriting is the prettiest."

        "Maybe you will try to see her again tomorrow..."

        "For now, you get up and head back to your dorm."

       # scene bg dorm
       # with fade

       # play music door noloop

       # show frog neutral at right
       # with dissolve

        p "Oh, you're back."

        p "I saw my crush today and I looked like a total dummy with my shirt on inside out..."

        p "Why didn't you say anything?"

        f "Woah, chill dude. I just didn't notice. I'm not your mom!"

        p "Yeah..."

        p "I guess I'm just frustrated..."

        p "I looked like a mess seeing Cincere today and I was already feeling like I made a fool of myself when I met two other beautiful women."

        f "Oh? What are their names?"

        p "Well there's Cincere, obviously. And then I met a girl named Ame and another one named Muse."

        "Your eyes start to sparkle just saying their names out loud."

        f "Are you hoping to date them?"

        p "Are you kidding? I don't have a chance in hell with any of them!"

       # show frog empathetic at right
       # with dissolve

        f "Hey, enough with the self-deprecating bs."

        f "You're quite the catch, [p]! I'm sure any one of them would be lucky to be your girlfriend."

        f "Hell, they'd be lucky to be one of your three girlfriends!"

        # play music happy

        p "I'm definitely bot getting three girlfriends, but thanks for the vote of confidence...I think?"

        f "Any time roomie, seriously."

        f "I'm something of a dting genius. I've been in more relationships than I can count and I'm on good terms with every ex."

        p "Am I supposed to be impressed?"

       # show frog proud at right
       # with dissolve

        f "I'm impressive as shit! So..."

       # show frog neutral at right
       # with dissolve

        f "Which girl is your favorite so far?"

        p "How could you ask me a question like that?! I barely know any of them..."

        #show frog teasing at right
        #with dissolve

        f "Okay, okay! Just ask me if you need any advice.I've got your back if you can wash mine ;)"

        p "Ugh, shower on your own! I'm going to sleep."

        #scene black
        #with fade
 
        "Frog's words echo in your dreams...and you have no choice but to pick a favorite:"

           # menu:
                #"Cincere":
               # $ c_points += 1
                #jump day_2

                #"Ame":
                #$ a_points += 1
               # jump day_2

                #"Muse":
                #$ m_points += 1
                #jump day_2

    label day_2:
        pass
        return'''