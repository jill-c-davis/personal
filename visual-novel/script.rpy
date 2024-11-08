# The script of the game goes in this file.

### "The Time I Thought I Would Be Alone Forever but Got Ghosted by Three Cute Girls and a Ghoul Instead" ###

# ---------------------------------------------------- Character Objects -------------------------------------------------------------------------------------------

# Declare characters used by this game. The color argument colorizes the name of the character.

define a = Character("Ame", color="371F76")
define c = Character("Cincere", color="4FB9AF")
define f = Character("Frog", color="5EDD5F")
define g = Character("Ghost")
define m = Character("Muse", color="FF9899")
define n = Character("Manager")
define p = Character("?")
define r = Character("Professor")

#  ---------------------------------------------------- Images ----------------------------------------------------------------------------------------------------

# Backgrounds 

image bg dorm:
    im.Scale("images/dorm.png", 1920, 1080)
image bg classroom:
    im.Scale("images/classroom.png", 1920, 1080)
image bg cafe:
    im.Scale("images/cafe.png", 1920, 1080)
image bg library:
    im.Scale("images/library.png", 1920, 1080)
image bg messenger_app:
    im.Scale("images/messenger_app.png", 1920, 1080)
image bg student_center:
    "images/student_center.png"
image bg cemetery:
    "images/cemetery.png"

# Characters

# MC
image shirt_black:
    "images/shirt_black.png"
    zoom 0.25
image shirt_blue:
    "images/shirt_blue.png"
    zoom 0.25
image shirt_red:
    "images/shirt_red.png"
    zoom 0.25


# Ame
image ame_neutral:
    "images/ame_neutral.png"
image ame_full:
    "images/ame_full.png"
image ame_happy:
    "images/ame_happy.png"
image ame_sad:
    "images/ame_sad.png"
image ame_frazzled:
    "images/ame_frazzled.png"
image ame_date_neutral:
    "images/ame_date_neutral.png"
image ame_date_full:
    "images/ame_date_full.png"
image ame_date_happy:
    "images/ame_date_happy.png"
image ame_date_sad:
    "images/ame_date_sad.png"

# Cincere
image cincere_neutral:
    "images/cincere_neutral.png"
image cincere_full:
    "images/cincere_full.png"
image cincere_happy:
    "images/cincere_happy.png"
image cincere_sad:
    "images/cincere_sad.png"
image cincere_mischievious:
    "images/cincere_mischievious.png"
image cincere_date_happy:
    "images/cincere_date_happy.png"
image cincere_date_full:
    "images/cincere_date_full.png"
image cincere_date_neutral:
    "images/cincere_date_neutral.png"
image cincere_date_sad:
    "images/cincere_date_sad.png"
image cincere_date_mischievious:
    "images/cincere_date_mischievious.png"

# Frog
image frog_neutral:
    "images/frog_neutral.png"
image frog_full:
    "images/frog_full.png"
image frog_happy:
    "images/frog_happy.png"
image frog_sad:
    "images/frog_sad.png"
image frog_teasing:
    "images/frog_teasing.png"

# Ghost
image ghost_neutral:
    "images/ghost_neutral.png"
image ghost_full:
    "images/ghost_full.png"
image ghost_happy:
    "images/ghost_happy.png"
image ghost_sad:
    "images/ghost_sad.png"
image ghost_normal:
    "images/ghost_normal.png"

# Muse
image muse_neutral:
    "images/muse_neutral.png"
image ghost_full:
    "images/muse_full.png"
image ghost_happy:
    "images/muse_happy.png"
image ghost_sad:
    "images/muse_sad.png"
image muse_shy:
    "images/muse_shy.png"
image muse_date_full:
    "images/muse_date_full.png"
image muse_date_neutral:
    "images/muse_date_neutral.png"
image muse_date_happy:
    "images/muse_date_happy.png"
image muse_date_sad:
    "images/muse_date_sad.png"

# Manager
image manager_neutral:
    "images/manager.png"

# Professor
image professor_neutral:
    "images/professor.png"

# Collectibles 

# Ame
image strawberry_roll_cake:
    "images/strawberry_roll_cake.png"
image checkerboard_cookies:
    "images/checkerboard_cookies.png"
image pudding:
    "images/pudding.png"

# Cincere 
image godzilla:
    "images/items/godzilla.png"
image dos_monjes:
    "images/dos_monjes.png"
image handmaiden:
    "images/handmaiden.png"

# Muse
image sense:
    "images/sense.png"
image dracula:
    "images/dracula.png"
image tell_tale_heart:
    "images/tell_tale_heart.png"

# Ghost
image love_letter:
    "images/love_letter.png"
image locket:
    "images/locket.png"
image class_ring:
    "images/class_ring.png"
image faith:
    "images/faith.png"

#  ---------------------------------------------------- Audio ----------------------------------------------------------------------------------------------------

# Music

define audio.moon1 = "audio/menu1.mp3" # frog menu theme
define audio.moon2 = "audio/menu2.mp3" # cincere menu theme
define audio.moon3 = "audio/menu3.mp3" # ame menu theme
define audio.moon4 = "audio/menu4.mp3" # muse menu theme
define audio.moon5 = "audio/menu5.mp3" # ghost menu theme
define audio.moon6 = "audio/menu6.mp3" # credits theme


# SFX

define audio.birds = "audio/birds.mp3"
define audio.door = "audio/door.mp3"
define audio.startled = "audio/startled.mp3"
define audio.notebook_tear = "audio/notebook_tear.mp3"
define audio.notebook_crumple = "audio/notebook_crumple.mp3"
define audio.pensive = "audio/pensive.mp3"
define audio.chatter_spooky = "audio/chatter_spooky.mp3"
define audio.success = "audio/success.mp3"
define audio.disappointed = "audio/disappointed.mp3"
define audio.stomach_growl = "audio/stomach_growl.mp3"
define audio.ticking = "audio/ticking.mp3"
define audio.texting = "audio/texting.mp3"
define audio.ping = "audio/ping.mp3"
define audio.applause = "audio/applause.mp3"
#  ---------------------------------------------------- Inventory ------------------------------------------------------------------------------------------------

# Define the inventory as a dictionary to store items

default inventory = {
    "Ame" : [
        "Strawberry Roll Cake" if persistent.strawberry_roll_cake_collected else None,
        "Checkerboard Cookies" if persistent.checkerboard_cookies_collected else None,
        "Pudding" if persistent.pudding_collected else None
     ],
    "Cincere" : [
        "Godzilla (1)" if persistent.godzilla_collected else None, 
        "Dos Monjes (954)" if persistent.dos_monjes_collected else None, 
        "The Handmaiden (2016)" if persistent.handmaiden_collected else None
        ],
    "Muse" : [
        "Sense and Sensibility (1811)" if persistent.sense_collected else None, 
        "Dracula (1897)" if persistent.dracula_collected else None, 
        "The Tell-Tale Heart (1843)" if persistent.tell_tale_heart_collected else None
        ],
    "Ghost" : [
        "Love Letter" if persistent.love_letter_collected else None, 
        "Locket" if persistent.locket_collected else None, 
        "Class Ring" if persistent.class_ring_collected else None
        ],
}

# Define each inventory item

# Ame
define strawberry_roll_cake = {
    "name":"Strawberry Roll Cake",
    "description":"A complicated looking recipe for a rolled up strawberry and lemon cake. It smells like fresh lemons.",
    "image" :"strawberry_roll_cake.png"
}
define checkerboard_cookies = {
    "name" : "Checkerboard Cookies",
    "description" : "An advanced recipe for chocolate and vanilla swirled cookies. It's a bit stained.",
    "image" : "checkerboard_cookies.png"
}
define pudding = {
    "name" : "Pudding",
    "description" : "A recipe for Japanese-style pudding. You can only dream of what it tastes like.",
    "image" : "pudding.png"
}

# Cincere
define godzilla = {
    "name" : "Godzilla (1954)",
    "description" : "The original Japanese-language monster movie. You can't get that distinctive roar out of your head.",
    "image" : "godzilla.png"
}
define dos_monjes = {
    "name" : "Dos Monjes (1934)",
    "description" : "An intense, Mexican melodrama about two monks who share a dark secret. It's a thrilling and mysterious film.",
    "image" : "dos_monjes.png"
}
define handmaiden = {
    "name" : "The Handmaiden (2016)",
    "description" : "A mixed-language psychological thriller set during Japanese occupation of Korea. Cincere seems to prefer foreign language films.",
    "image" : "handmaiden.png"
}

# Muse
define sense = {
    "name" : "Sense and Sensibility (1811)",
    "description" : "English author Jane Austen's first published novel. A romantic tale of love, loss, and relationships with gothic elements.",
    "image" : "sense.png"
}
define dracula = {
    "name" : "Dracula (1897)",
    "description" : "A gothic horror novel by Irish author Bram Stoker.",
    "image" : "dracula.png"
}
define tell_tale_heart = { 
    "name" : "The Tell-Tale Heart (1843)",
    "description" : "American gothic poet Edgar Allan Poe's famous short story. Come to think of it, is Muse into gothic stuff? She only ever wears black.",
    "image" : "tell_tale_heart.png"
}

# Ghost
define love_letter = { 
    "name" : "Love Letter",
    "description" : "A crumpled, old love letter found in the film studies classroom. The handwriting is faint but filled with emotion.",
    "image" : "love_letter.png"
}
define locket = {
    "name" : "Locket",
    "description" : "A mysterious locket with a torn photo of a handsome young man. Based on his attire, the photo was probably taken in the 1950s.",
    "image" : "locket.png"
}
define class_ring = {
    "name" : "Class Ring",
    "description" : "A worn, old ring with the initial 'F' engraved into it along with the numbers '1959.'",
    "image" : "class_ring.png"
}
define faith = {
    "name" : "Faith",
    "description" : "You discovered that Ghost's real name is Faith. She can actually look kind of peaceful.",
    "image" : "faith.png"
}

#  ----------------------------------------------------  Systems ---------------------------------------------------------------------------------------------

# Romance Points (RP)

default a_points = 0 # ame points
default c_points = 0 # cincere points
default m_points = 0 # muse points
default max_points = 5 # max RP for each chara

# Ghost Points (GP)

default g_points = 0 # ghost points

# Collectible Items as Keys

# Ame
default persistent.strawberry_roll_cake_collected = False
default persistent.checkerboard_cookies_collected = False
default persistent.pudding_collected = False

# Cincere
default persistent.godzilla_collected = False
default persistent.dos_monjes_collected = False
default persistent.handmaiden_collected = False

# Muse
default persistent.sense_collected = False
default persistent.dracula_collected = False
default persistent.tell_tale_heart_collected = False

# Ghost
default persistent.faith_collected = False
default persistent.love_letter_collected = False
default persistent.locket_collected = False
default persistent.class_ring_collected = False

#  ---------------------------------------------------- Game Start ------------------------------------------------------------------------------------------


# Day 1 ------------------------------------------------------------------------------------------------------------------------------------------------------

label start:
    scene black
    with dissolve
    # play music birds noloop
    f "Hoping that extra beauty sleep will win her affection?"
    p "I feel like I died during that nap. I can't even remember my name..."
    $ p = renpy.input("Enter your name.")
    play music door noloop

    scene bg dorm
    with fade
    # play music moon1
    show frog_teasing
    with dissolve
    f "Your name is [p]."
    f "You go to Deez Nuts University and you have a class in like twenty minutes."
    f "Ha! Your little crush isn't going to like you back if you show up looking like you just rolled out of bed."
    show frog_sad
    with dissolve
    f "Plus, if Ghost catches you alone, you might become her next target."
    p "You know I don't believe in that stuff."
    f "Still, better safe than sorry."
    p "I guess your right."
    show frog_neutral
    with fade
    "You roll out of bed and start getting dressed."
    call screen dress_up

label after_dress_up:
    # Save final outfit selections to variables
    $ mc_shirt = shirt_options[shirt_index]
    $ mc_pants = pants_options[pants_index]
    $ mc_hat = hat_options[hat_index]
    $ mc_shoes = shoes_options[shoes_index]
    # Continue with the story
    "You finalize your outfit and feel ready to go!"
    jump classroom

label classroom:

    scene bg classroom
    with fade
    show screen romance_points
    # play music moon2
    "To your surprise. you arrive to class a few minutes early."
    "Cincere isn't in her usual spot behind you, but you notice a crumpled, yellow piece of paper on her desk."
    menu:
        "Read the paper.":
            $ g_points += 1
            jump find_love_letter
        "Leave the paper alone.":
            jump continue_to_class

label find_love_letter:
    $ persistent.love_letter_collected = True
    $ inventory["Ghost"][0] = "Love Letter"
    call screen inventory_screen # Display updated inventory
    jump continue_to_class

label continue_to_class:
    "The projector whirs as your professor prepares to start class."
    "You notice that your crush, Cincere is running late today..."
    "It couldn't be she was Ghost's next target, could it?"
    "Your fears are assuaged when Cincere storms in, quickly walking to her usual seat behind you."
    show cincere_full
    with dissolve
    c "Hey...can I borrow your pen?"
    "You notice that she's in an unusually good mood, and that you only brought one pen with you in your rush to class."
    menu:
        "Give her the pen":
            $ c_points += 1
            jump pen
        "Keep the pen.":
            jump no_pen

label pen:

    show cincere neutral at right
    with dissolve
    c "Hey... let me use some paper too?"
    # play music notebook_tear noloop
    p "Here... is one page enough?"
    show professor_neutral
    with dissolve
    "Your professor's voice booms:"
    "That's enough talking in my class!"

    scene bg classroom
    with fade
    # play music moon2
    "Some time passes, and a carefully folded note flies over your shoulder."
    "You open the note and it says..."
    # play music notebook_crumple noloop
    "Your shirt is on inside out, and it's distracting me from the movie."
    "You look down at your shirt, and the seams are indeed facing outward."
    "After class, you go back to your dorm to change."
    # play music disappointed noloop

    scene bg dorm
    with fade
    # play music moon1
    p "The first time we ever talk to each other and it's about how I am a mess..."
    p "Maybe it's not too late to drop this class..."
    p "No. I promised myself I would stick it out."
    p "I'll go to the cafe for a pick-me-up."
    jump cafe

label no_pen:

    show cincere neutral at right
    with dissolve
    c "Okay, I'll ask someone else."
    "After class, you notice you've put your shirt on inside out."
    "You go back to your dorm to change."

    scene bg dorm
    with fade
    # play music moon1
    p "Maybe it's not too late to drop this class..."
    p "No. I promised myself I would stick it out."
    p "I'll go to the cafe for a pick-me-up."
    jump cafe

label cafe:

    scene bg cafe
    with fade
    # play music moon3
    "A barista appears behind the counter."
    show ame_frazzled
    with dissolve
    # play music pensive noloop
    p "I don't think I've seen her working here before..."
    "You're struck by her beauty."
    p "Are you new here?"
    a "..."
    p "I did not mean to say that out loud..."
    p "Or that either"
    show ame happy at right
    with dissolve
    a "Name for your order?"
    p "It's [p]." 
    p "A medium roast with two creams and two sugars please." 
    p "Sorry." 
    p "I-I mean thank you."
    "Today is just not your day."
    show ame neutral at right
    with dissolve
    a "[p]?"
    # play music startled noloop
    "The barista hands you your coffee and you notice some writing on the cup."
    p "Oh uhm..."
    show ame happy at right
    with dissolve

    scene bg cafe
    with fade
    "The barista goes to help another customer, but you notice the note she's written on your cup:"
    # play music success noloop
    # play music moon3    
    a "Yes, I'm new! Hope your drink doesn't suck, Ame."
    "You can't make out the rest of it..."
    menu:
        "Wait to get her attention.":
            $ a_points += 1
        "Shrug it off.":
            $ g_points +=1
    "Since the cafe is crowded and Ame looks busy, you head to the library."

label library:

    scene bg library
    with fade
    # play music moon4
    "The entire library is full of students this afternoon."
    play music chatter_spooky noloop
    # play music moon4
    "You look around and notice the girl at the table nearest you has moved her backpack from the seat. She's moving her things around to make room."
    p "She must have noticed my vulturing..."
    p "My winning streak of first impressions is going strong."
    p "I'll ask her if I can sit next to her."
    "You walk up to her. You never thought you were tall before, but wow is this girl tiny."
    p "Hey, is it alright if I sit here?"
    show muse neutral
    with dissolve
    m "Yes! Please do?"
    p "Um, okay."
    "You sit down and get your things to begin studying."
    menu:
        "Tell her your name.":
            $ m_points += 1
            jump shy
        "Say nothing.":
            jump muse

label shy:

    "You glance over and smile at the girl."
    "Her eyes meet yours because she's been staring at you the entire time."
    "You decide to talk first: "
    p "I'm [p]!"
    m "..."
    show muse shy
    with dissolve
    m "I'm shy."
    m "Sorry, I mean Muse." 
    m "My name is Muse."
    jump muse

label muse:

    scene bg library
    with fade
    "After that, you both study at the same table for a while."
    "To your surprise, the silence doesn't feel awkward, but actually kind of..."
    "Nice."
    "The girl leaves first, and you don't look up from your books until she's gone."
    "When you do, you notice she left you a small note: "
    m "If you come a little earlier tomorrow, we can chat before studying."
    "You think of all the notes you've received today and decide that her neat, precise handwriting is the prettiest."
    "Maybe you will try to see her again tomorrow..."
    g "I'd love to see you again tomorrow too."
    # play music startled
    # play music moon4
    "You could have sworn Muse had left already."
    "You look up, but don't see anyone..."
    "It must have been your imagination."
    "You get up and head back to your dorm."

    scene bg dorm
    with fade
    # play music moon1
    # play music door noloop
    # play music moon1
    show frog_neutral at right
    with dissolve
    p "Oh, you're back."
    p "I saw my crush today and I looked like a total dummy with my shirt on inside out..."
    p "Why didn't you say anything?"
    f "Woah, chill dude. I just didn't notice. I'm not your mom!"
    p "Yeah..."
    p "I guess I'm just frustrated..."
    p "It's not really fair of me to take it out on you. Sorry. It's just..."
    p "I looked like a mess seeing Cincere today, and I was already feeling like I made a fool of myself when I met these two other gorgeous girls."
    f "Oh? And what are the names of these gorgeous girls?"
    p "Well there's Cincere, obviously. And then I met a beautiful, hilarious barista named Ame and a studious, petite beauty named Muse."
    "Your eyes start to sparkle as you realize that you got all of their names."
    f "Sounds like you learned a little bit about all of them."
    f "Are you looking to date one of them?"
    # play music startled noloop
    # play music moon1
    p "Are you kidding? I don't have a chance in hell with any of them!"
    show frog_teasing at right
    with dissolve
    f "You're quite the catch, [p]! I'm sure any one of them would be lucky to be your girlfriend..."
    f "Besides, I bet they don't want to run into Ghost either..."
    f "Everyone knows the safest way to avoid her is to cuff it up."
    # play music disappointed noloop
    # play music moon1
    p "Thanks for the vote of confidence..."
    p "I don't know if I'd want to date someone who was just using me to avoid being haunted."
    show frog happy at right
    with dissolve
    f "I thought you didn't believe in that stuff?"
    p "..."
    f "In any case, I'm something of a dating genius..." 
    f "I've been in more relationships than I can count and I'm on good terms with every ex, so ask me for advice when you need it."
    "Frog's eyes pierce yours for a moment."
    f "You could lean on me sometimes, if you want..."
    "It's unusual for Frog to speak so quietly..."
    "You couldn't hear what they said."
    "Before you can ask them to repeat it, their expression turns serious."
    show frog neutral at right
    with dissolve
    f "So, which girl is your favorite so far?"
    p "Um..."
    menu:
        "Cincere":
            $ c_points +=1
            jump cincere_reflection_1
        "Ame":
            $ a_points += 1
            jump ame_reflection_1
        "Muse":
            $ m_points += 1
            jump muse_reflection_1
        "I barely know any of them!":
            $ g_points += 1
            jump day_1_end

label cincere_reflection_1:

    p "I've been crushing on her since classes started last week."
    jump day_1_end

label ame_reflection_1:

    p "She makes me laugh and on top of that, she's a real beauty."
    jump day_1_end

label muse_reflection_1:

    p "She's just so little and shy and cute."
    jump day_1_end

label day_1_end:

    "Frog acknowledges your response with a disinterested 'hm.'"
    "Thinking about it makes your head hurt, so you close your eyes."
    scene black
    with fade
    p "Whatever..."
    p "It's not like Frog would understand."

# Day 2 -------------------------------------------------------------------------------------------------------------------------------------------------------------

label day_2:

    scene bg dorm
    with fade
    # play music birds noloop
    p "Ugh, I slept through dinner again."
    "You hear Frog snoring in the bunk beside yours, so you take a glance at your watch to check the time."
    "It's early for a change... 7am"
    # play music stomach_growl noloop
    "Breakfast doesn't start for another hour..."
    "You decide to head to the cafe in the student center."

    scene bg cafe
    with fade
    # play music moon3
    # play music startled noloop
    show cincere_neutral
    with dissolve
    "Lucky for you, you notice Cincere sitting pensively at one of the cafe tables..."
    "She looks totally absorbed in something..."
    # play music moon2
    menu:
        "Leave Cincere alone.":
            $ g_points += 1
        "Call out to her.":
            $ c_points += 1
    "She spots you first."
    show cincere_happy
    with dissolve
    c "Oh! Hey, you."
    "She waves you over to her table."
    "You walk over as nonchalantly as possible."
    p "Hey Cincere, mind if I sit with you?"
    "You notice dark circles under her eyes and the fact that she's... drawing? something over and over again."
    c "That's why I waved you over here."
    show cincere neutral
    with dissolve
    c "I actually wanted to talk to you about something..."
    "She pulls out the chair beside her, and you take a seat."
    "You glance at the papers Cincere has been drawing on, but can't make sense of her scribbles."
    c "It's about Ghost."
    show cincere_mischievious
    with dissolve
    "Cincere's voice turns serious."
    c "I saw her last night, well, felt her I think..."
    "Her voice gets really low."
    c "In class yesterday, I kept hearing her calling out to me, so I left a bit early to clear my head."
    c "But I just couldn't get this image of a ring out of my head."
    c "I think..."
    c "Nevermind, it's silly."
    menu:
        "Press Cincere to explain.":
            jump explain
        "Comfort Cincere.":
            jump comfort

label explain:

    p "It's not silly."
    p "Tell me what's on your mind."
    jump cafe_continue

label comfort:

    p "It's not silly"
    p "It sounds like a frightening experience."
    c "Thanks."
    c "I'm not as frightened as I'm going to be if I don't get to class."
    c "Here, I made these as handouts, but you can have one because I like you."
    "Your heart skips a beat as she hands you a piece of paper - a movie poster?"
    $ persistent.godzilla_collected = True
    $ inventory["Cincere"][0] = "Godzilla"
    call screen inventory_screen # Display updated inventory
    jump cafe_continue

label cafe_continue:

    "You reach out to squeeze Cincere's hand."
    "Her hand is a bit larger than yours, but a million times softer, and it smells... sweet. Like honey and oatmeal."
    "You notice Cincere's breakfast of oatmeal with honey and a black coffee."
    show cincere neutral
    with dissolve
    c "Are you hungry?"
    p "I'm starving."
    # play music stomach_growl noloop
    c "Listen, I've got to go but rumor has it..."
    "She glances at the cafe counter."
    c "The cafe here has the best apple turnovers on the planet."
    "You can't help but smile at that."
    p "Yeah, I'll give them a try! See you around, Cincere."
    show cincere smile
    with dissolve
    c "See you around, [p]!"
    menu:
        "Splurge on a treat from the cafe.":
            jump cafe_day_2
        "Wait for the dining hall to open, so you can use your meal credits like a responsible adult.":
            jump library_day_2

label cafe_day_2:

    scene bg cafe
    with fade
    # play music moon3
    "You order an apple turnover with a simple latte but..."
    "...You forgot to ask for dairy-free milk."
    "You make to cancel your order when the beautiful barista from yesterday - Ame - appears."
    show ame frazzled
    with dissolve
    a "I'm sorry for being late! I'll take it from here, boss."
    "You didn't realize the person who initially took your order was The Manager\u2122." #unicode trademark (TM) symbol
    "To your surprise, The Manager\u2122 shrugs it off." #unicode trademark (TM) symbol
    show manager_neutral
    with dissolve
    n "It happens." 
    n "That apple turnover has been selling really well..."
    n "I want you to think about what pastry we can sell for the upcoming winter season too."
    n "Here." 
    "He hands Ame a piece of paper - your order - and then turns to leave."
    n "I'll be in the office if you run into any...he looks you up and down... trouble."
    "You want to reply in a cool manner, but what comes out is..."
    menu:
        "Oh, I'm no trouble, boss. I-I mean sir!": 
            $ a_points += 1
        "...":
            "You can't think of what to say."
    "You raise your hand as if to salute, but put it down when you realize The Manager\u2122 has a peg leg." #unicode trademark (TM) symbol
    "What if he really was in the military?"
    "Would it be disrespectful to salute?"
    "To your relief, The Manager\u2122 grunts and walks away." #unicode trademark (TM) symbol
    "As soon as The Manager\u2122 leaves, you can't help but ask Ame if she baked the apple turnovers you've been eyeing." #unicode trademark (TM) symbol
    show ame happy
    with dissolve
    a "Haha...it was my idea to do a 'Pastry of the Season' but, sadly, I'm not licensed to prepare pastries so these are actually just frozen ones from Megman's."
    p "..."
    a "I do love to bake and I can assure you that the apple turnovers I make are way fresher and more delicious, but..."
    a "I just don't have a license to sell my own pastries yet."
    "She looks around the cafe"
    a "Otherwise, I would definitely sell apple turnovers at my own patisserie and not this..."
    "She gestures broadly around."
    show ame sad
    with dissolve
    a "Haunted dump."
    "You linger for a moment before continuing..."
    # play music moon2
    menu:
        "I'm jealous of anyone who gets to try your baking.":
            $ a_points += 1
            jump recipe_1
        "Haunted? You believe in that stuff?":
            $ g_points += 1
            jump haunted

label recipe_1:

    a "In that case..."
    a "Here."
    "She hands you a piece of paper with some writing on it."
    a "It's one of my own personal recipes."
    "You try not to squint as she positively beams at you."
    $ persistent.strawberry_roll_cake_collected = True
    $ inventory["Ame"][0] = "Strawberry Roll Cake"
    call screen inventory_screen # Display updated inventory
    jump cafe_end

label haunted:

    a "Yeah, I always hate working the late shift here."
    "She keeps talking as she prepares the espresso for your latte."
    a "Actually, you know, I did find something weird here the other night but..."
    a "Nah I don't want to keep you."
    p "You can keep me as long as you want."
    "You're not sure if that came out too forward, but you're undeterred."
    jump cafe_end

label cafe_end:

    p "I can't bake at all, so, I'm really impressed!"
    a "You flatter me. I mostly bake for myself since my parents can't eat too many sweets these days."
    a "My freezer is actually chock-full of sweets I've made."
    a "If I was in charge of things, I'd definitely sell them here but..."
    "She sighs."
    # play music success noloop
    a "But you know what? If you come here tomorrow, [p], I'll give you a treat."
    "She winks at you, and you feel your chest melt."
    "You head back to your dorm, grinning the whole way."
    jump day_2_end

label library_day_2:

    scene bg library
    with fade
    # play music startled noloop
    p "It's that girl again from yesterday...Muse?"
    show muse neutral
    with dissolve
    "She's once again elbow-deep in books..."
    "You think she doesn't notice you, but she glances up."
    show muse smile
    with dissolve
    m "Hey, it's you!"
    p "In the flesh."
    "Muse laughs."
    "The sound fills your heart with affection."
    "You could listen to her gentle laugh forever."
    m "Sorry, but, what was your name again?"
    p "It's [p]."
    m "I couldn't say it yesterday, but n-nice to meet you, [p]!"
    p "Um, nice to meet you too, Muse."
    m "Are you here studying today, too?"
    p "Oh, I was just trying to kill time before the dining hall opens..."
    p "Speaking of..."
    menu:
        "What are you studying? It seems intense.":
            jump studying
        "Do you maybe want to get breakfast with me today?":
            $ m_points += 1
            jump breakfast

label studying:

    "Muse gestures at the pile of books on the table, and her eyes light up."
    show muse happy
    with dissolve
    m "It's for an exhibit! We're showcasing student life on campus. I'm looking at old yearbooks, that kind of thing. Trying to decide what to highlight."
    p "Wow, that's really cool, Muse. You work at a museum?"
    m "Yes! I'm thinking about showcasing one of my favorite short stories, but, I'm not sure if it matches the theme."
    p "What are you thinking?"
    m "Tell-Tale Heart, of course!"
    # play music disappointed noloop
    "It saddens you that you've never heard of it."
    # play music moon4
    menu:
        "What's Tell-Tale Heart?":
            jump find_book_1
        "Why do you think it doesn't match the theme?":
            jump haunted_museum

label find_book_1:

    show muse_full
    with dissolve
    m "You've never heard of it?!"
    "She starts rummaging in her backpack."
    m "Here, I actually have a copy of it if you want to borrow it."
    $ persistent.tell_tale_heart_collected = True
    $ inventory["Muse"][0] = "Tell-Tale Heart"
    call screen inventory_screen # Display updated inventory
    jump cafe_end

label haunted_museum:

    m "Well..."
    m "It's supposed to be regarding student life, but..."
    m "I just can't help but think of Ghost and how her hauntings are like..."
    "She stands up, the top of her head barely meeting yours."
    show muse full
    with dissolve
    m "A huge part of student life!"
    "Muse sits back down, her fair features flushing."
    show muse_happy at right
    with dissolve
    m "I just think it might comfort her to see a horror story exhibited."
    "You won't pretend to understand it, but you support Muse's decision."
    jump museum

label breakfast:

    show muse shy
    with dissolve
    m "Th-th-thanks for asking! If it was another time, I'd say yes, but I just can't right now with the exhibit coming up."
    # play music disappointed noloop
    p "Exhibit?"
    jump museum

label museum: 

    p "I'm really impressed, Muse."
    p "You work at a museum?"
    show muse_happy
    with dissolve
    m "Yep! The one right here on campus. Actually...nevermind."
    # play music moon4
    menu:
        "There's a museum on campus?":
            jump library_day_2_end
        "Oh, the one in the student center?":
            $ m_points += 1
            jump library_day_2_end

label library_day_2_end:

    m "Yep, the one in the student center!"
    m "Actually, the exhibition is going to be this Friday."
    m "I could give you my number if you want the details."
    # play music startled noloop
    p "Y-y-yeah!"
    "You pull your phone from out of your pocket and hand it to Muse."
    "When she gives it back to you with her contact, you notice she put a heart at the end of her name."
    p "Is it okay for me to think this is going well?"
    "Muse laughs."
    # play music stomach_growl noloop
    "Neither of you can ignore your stomach anymore..."
    m "Um, I think the dining hall is open now if you're still waiting for breakfast."
    "She points at the clock."
    p "Yeah, I-I'll see you later?"
    m "You know where to find me."

    scene bg dorm
    with fade
    "You go back to your dorm after devouring a meal of plain rice, chive dumplings, and miso soup."
    "You look at the new contact in your phone..."
    "Muse ♡"
    "And you giggle to yourself like an easily excited schoolgirl."
    "Frog stirs in the bed next to yours, and they're immediately chipper:"
    show frog_happy
    with dissolve
    f "Who's got you laughing like that this early in the morning?"
    # play music moon4
    menu:
        "Cincere":
            $ c_points +=1
            jump cincere_reflection_2 
        "Ame":
            $ a_points += 1
            jump ame_reflection_2
        "Muse":
            $ m_points += 1
            jump muse_reflection_2
        "Shut up!":
            $ g_points += 1
            jump day_2_end

label cincere_reflection_2:

    pass # a short reflection of the MC's thoughts on Cincere
    jump day_2_end

label ame_reflection_2:

    pass # a short reflection of the MC's thoughts on Ame
    jump day_2_end

label muse_reflection_2:

    pass # a short reflection of the MC's thoughts on Muse
    jump day_2_end

label day_2_end:

    "You throw a pillow at Frog, and they don't press you any further after that."

    scene black
    with fade
    "Since you don't have any classes today, you decide to take it easy..."
    "You'd give anything to hold on to these carefree days..."
    "Before you know it, night has fallen, and it's time to sleep again."
    jump day_3

# Day 3 -----------------------------------------------------------------------------------------------------------------------------------------------------------------
label day_3:

    scene bg dorm
    with fade
    # play music birds noloop
    show frog teasing
    with dissolve
    f "Better hurry or you'll muck up your chance to see Cincere again."
    p "How many times do I have to tell you not to antagonize me in the morning?"
    f "Ooo! My bad, just trying looking out for my bestie."
    p "Well...I actually did want an early start today..."
    f "...You're welcome."
    menu:
        "Head to your Film Studies class early":
            jump find_locket
        "Take your time picking out an outfit for class":
            $ c_points += 1
            jump classroom_day_3

label find_locket:

    scene bg classroom
    with fade
    "Once again, you find yourself early, before any of the other students arrive."
    "There is a strange item on your desk, some kind of necklace?"
    menu:
        "Pick it up.":
            $ persistent.locket_collected = True
            $ inventory["Ghost"][1] = "Locket"
            call screen inventory_screen # Display updated inventory
        "You don't recognize it, but you pocket it and make a mental note to give it to Cincere.":
            jump classroom_day_3

label classroom_day_3:

    scene bg classroom
    with fade
    show cincere neutral
    with dissolve
    "Cincere looks more tired than usual today, but she seems happy to chat."
    "You decide to start the conversation easy by asking what her major is."
    c "I'm a Film Studies major, but I'm actually..."
    "Her voice drops to a whisper"
    c "I'm retaking this class. I guess I'm what you would call a 'super senior.'"
    show cincere_sad
    with dissolve
    "She sighs."
    "You're surprised, and without thinking, you ask a burning question:"
    # play music moon2 noloop
    menu:
        "Oh, how old are you?!":
            $ c_points += 1
            jump classroom_day_3_end
        "Oh, so, you're retaking this class in order to graduate?": 
            jump find_movie_3

label find_movie_3:

    c "Yeah, pretty much."
    p "Is this class pretty tough?"
    c "Nah, Old Fart over there..."
    "She points to where the professor usually sits."
    c "Just doesn't like my immaculate taste in film."
    p "Isn't that kind of a shitty reason to like..."
    p "Prevent you from graduating?"
    c "It is what it is."
    c "I've been carrying this with me out of spite, but, here."
    c "This is the film Old Fart didn't appreciate my analysis of."
    $ persistent.handmaiden_collected = True
    $ inventory["Cincere"][2] = "The Handmaiden (2016)"
    call screen inventory_screen # Display updated inventory
    c "It'll change your life."
    jump classroom_day_3_end

label classroom_day_3_end:
 
    "To your chagrin, Cincere sighs again."
    c "I don't really like to talk about it."
    "Luckily for you, the bell rings and your professor begins droning on right away."
    "When the lecture is over, you notice that Cincere's seat is empty."
    "She must have left some time during the lecture..."
    "Was it something you said?"
    "You don't want to think about it, so you head to the library to bury yourself in your studies."
    jump library_day_3

label library_day_3: 

    scene bg library
    with fade
    "Muse is sitting very demurely at the same table you studied at on Monday."
    show muse neutral
    with dissolve
    "You didn't know your heart could beat so fast."
    # play music moon3
    menu:
        "Walk over to Muse.":
            $ m_points += 1
            jump library_continue
        "Pretend you don't see her.":
            $ g_points += 1
            jump find_book_2

label find_book_2:
    "You look around the library, but the seat next to Muse is the only place you want to be."
    "You walk over to her and ask what she's reading."
    show muse_happy
    with dissolve 
    m "Oh, it's my favorite book!"
    m "Actually, I have a copy if you want to borrow it..."
    $ persistent.sense_collected = True
    $ inventory["Muse"][0] = "Sense and Sensibility (1811)"
    call screen inventory_screen # Display updated inventory
    "You feel a little heavier."
    jump library_continue

label library_continue:
    show muse_happy
    with dissolve
    "She makes eye contact with you and gestures at the open seat next to her."
    "You oblige and sit down beside her."
    p "I see your still working hard."
    m "Yes, the exhibit is this Friday."
    m "I'm going to be leading the opening tour so..."
    m "I want to make sure I have all my facts straight before Friday and..."
    "She fidgets in her seat, glancing sideways towards you."
    show muse
    with dissolve
    m "Actually, um, I was wondering, and just if you're free..."
    "You notice her wringing her hands together."
    m "Will you come..."
    "She takes a breath and stands up"
    show muse_full
    with dissolve
    m "Will you come see me here again tomorrow morning?!"
    menu: 
        "Oh, sorry. Tomorrow morning, I can't.":
            $ a_points += 1 
            jump muse_no
        "Of course, Muse. I always look forward to seeing you here at the library.":
            $ m_points += 1
            jump muse_yes

label muse_no:

    show muse_sad at right
    with dissolve
    m "Oh, o-of course, I totally get if you're busy."
    m "I'll be here all day tomorrow too, so, even if the morning doesn't work..."
    "She glances up at you with shining eyes."
    m "I still would love to see you."
    jump library_day_3_end

label muse_yes:

    show muse_happy at right
    with dissolve
    m "Thank goodness!"
    p "Thank goodness?"
    m "There's something I want to ask you, so be sure to come early okay?!"
    p "Okay!"
    jump library_day_3_end

label library_day_3_end:

    "You sit there in silence again, studying together for a couple hours until Muse gets up to leave."
    show muse neutral
    with dissolve
    m "It's time for me to head to my job at the museum."
    m "I'll see you later?"
    "It sounds more like a question than a statement."
    "You wave her off."
    p "See you later."

    scene bg library
    with fade
    "You still have some time to kill before your next class, so you decide to stop by the cafe and see if Ame is still there with the promised apple turnovers."
    "You lick your lips just thinking about it."
    jump cafe_day_3

label cafe_day_3:

    scene bg cafe
    with fade
    "Lucky for you, it seems like Ame is always working."
    show ame_sad
    with dissolve
    a "It's alright! I had the afternoon shift today anyway."
    "She sounds cheerful, but you can tell there is something bothering her."
    # play music moon2 
    menu: 
        "Apologize.":
            jump cafe_day_3_end
        "Ask what's on her mind.":
            $ a_points += 1 
            jump find_recipe_2

label find_recipe_2:

    p "Is there something bothering you?"
    "Ame swallows."
    a "Honestly, yeah..."
    "She leans closer to you over the counter."
    "You can smell coffee on her breath."
    a "Actually, here:"
    $ persistent.checkerboard_cookies_collected = True
    $ inventory["Ame"][1] = "Checkerboard Cookies"
    call screen inventory_screen # Display updated inventory
    a "I tried this recipe out for checkerboard cookies, but..."
    a "There's no way I'm going to make them again."
    a "Ugh..."
    jump cafe_day_3_end

label cafe_day_3_end:

    show ame_happy
    with dissolve
    a "It's nothing it's just..."
    a "I really wanted to see you when I wasn't working."
    "It's quiet for a moment, and then Ame laughs."
    a "Hey, you know what. I get off pretty soon actually, in about..."
    "She glances at the analog clock on the wall"
    a "90 minutes? If you want to chat after."
    # play music ticking noloop
    "You wait at a table, smiling and waving at Ame every now and then as you wait for a lull in the afternoon coffee rush."
    "The lull never comes, but Ame sits down across from you at 4:30 on the cup."
    "With glittering eyes, she pushes a foil-wrapped mound in your direction."
    a "It's one of my turnovers, especially for you!"
    "You take a bite."
    p "It's delicious!"
    "Ame laughs."
    a "Better than Megman's?"
    "You nod emphatically."
    p "Way better, holy cow."
    a "You know..."
    a "I still don't have your number. Lend me your phone."
    "You take your phone out of your pocket and hand it to her."
    # play music texting noloop
    a "And, done!"
    a "It's been a long day, so I'm going to head home now. See you later?"
    p "Yeah, see you later."
    "You gather the crumbs and foil, throw them out, and head back to your dorm."
    
    scene bg messenger_app
    with fade
    "On your way there, you get a text notification."
    # play music ping noloop
    "It's from Ame, and it reads:"
    # play music texting
    a "I know this is sudden, and kind of last minute, but, do you want to have a picnic date with me this Friday?"
    a "I'll bring a cheeseplate, and it will be chill. Just let me know by noon on Friday and...do me a favor?"
    a "Don't come to see me at work until you've decided whether you can make the picnic or not..."
    a "Otherwise... my heart just can't take it!"
    # play music moon2 noloop
    menu: 
        "Reply with a flirt.":
            jump day_3_end
        "Reply with a joke.":
            $ a_points += 1 
            jump day_3_end

label day_3_end:

    p "Who knew you could be so...cheesy :x"
    "Ame replies before you make it back to your dorm:"
    a "guh stopppp"
    scene bg dorm
    with fade
    "You lie on your bunk bed grinning in spite of yourself."
    # play music door noloop
    show frog_happy
    with dissolve
    f "Someone looks happy."
    "Without thinking of the consequences, you reply contented:"
    p "So happy :)"
    "Frog laughs."
    f "Who has got you cheesin' this time?"
    menu:
        "Cincere":
            $ c_points +=1
            jump cincere_reflection_3 
        "Ame":
            $ a_points += 1
            jump ame_reflection_3
        "Muse":
            $ m_points += 1
            jump muse_reflection_3
        "Shut it!":
            $ g_points += 1
            jump day_4

label cincere_reflection_3:

    p "My sweet, sweet Cincere of course. I wonder what's troubling her lately."
    jump day_4

label ame_reflection_3:

    p "Actually, Ame asked me on a date. She's really forward, and it's easy to talk with her."
    jump day_4

label muse_reflection_3:

    p "Muse is so serious and hardworking. She really inspires me."
    jump day_4

# Day 4 -----------------------------------------------------------------------------------------------------------------------------------------------------------------

label day_4:

    scene black
    with fade
    # play music birds
    # play music ping noloop

    scene bg messenger_app
    with fade
    # play music texting
    a "Good morning :)"
    p "Morning! This is me making the conscious decision not to go to the cafe for a snack."
    a "There's always the vending machine~"
    p "Ah, definitely not the snack I was talking about ;)"
    a "Flirting when you should be studying?!"
    p "Flirting back when you should be working???"
    "Come to think of it, Muse asked you to meet her in the library today..."
    "You briefly wonder what it is she wanted to ask..."
    "But then you remember you never got the chance to give Cincere that necklace..."
    menu: 
        "Look for Cincere in the film studies classroom.":
            $ c_points += 1
            jump classroom_day_4
        "Head to the library to see Muse.":
            $ m_points += 1
            jump library_day_4

label classroom_day_4:

    scene bg classroom
    with fade
    # play music moon5
    "It's a bit chillier in here than usual."
    "You notice a movie poster near Cincere's usualy seat, so you take a peak."
    $ persistent.dos_monjes_collected = True
    $ inventory["Cincere"][1] = "Dos Monjes (1934)"
    call screen inventory_screen # Display updated inventory
    "Cincere doesn't seem to be here, so you head to the library."
    jump library_day_4

label library_day_4:

    scene bg library
    with fade
    # play music startled noloop
    "You're surprised to see Cincere in the spot where Muse usually sits."
    show cincere_neutral
    with dissolve
    "You jump on the chance to speak with her."
    p "Cincere! I wasn't expecting to see you at the library."
    "Somehow, she looks even more tired than yesterday."
    c "Oh, you think I din't need to study?"
    p "No just, I usually see you in class but not here..."
    c "Oh, that's right."
    "She seems distant."
    c "Sorry, I'm a little out of it today."
    # play music notebook_tear noloop
    "She slides you a note - no - a flyer."
    c "It's for an event tomorrow morning at the Student Center"
    "She's signed it with her phone number and a note - "
    c "Text me tonight if you want to go to my short film premier."
    "You usually have class at that time, but it looks important."
    "When you put the note away, she's already gone."

    scene bg library
    with fade
    p "Come to think of it, Cincere has been constantly disappearing lately..."
    p "Is she...avoiding me?"
    show muse_happy
    with dissolve
    m "You came!"
    p "I stick to my word."
    g "Liar."
    m "That's great. I love that in a partner."
    "Muse is coming on strong today."
    "You don't know what to say."
    p "..."
    show muse muse_full
    with dissolve
    m "Um, I, I wanted to know!"
    m "Will you come to my exhibit tomorrow afternoon?"
    # play music moon4
    menu:
        "For sure, Muse. I wouldn't miss it for the world.":
            $ m_points +=1
            jump muse_reflection_4
        "Actually, I'm busy tomorrow.":
            $ c_points +=1
            jump cincere_reflection_4
        "Sorry. I'm actually going on a date tomorrow.":
            $ a_points += 1
            jump ame_reflection_4

label cincere_reflection_4:

    p "I promised a friend I'd go to her short film premier."
    jump day_4_end

label ame_reflection_4:

    p "I met someone."
    jump day_4_end

label muse_reflection_4:

    p "I thought you'd be happier but it looks like...your thoughts are elsewhere?"
    jump day_4_end

label day_4_end:    

    show muse_sad at right
    with dissolve
    "Muse doesn't acknowledge your answer..."
    m "You don't have to answer me now..." 
    m "Just text me at the end of the day with your decision."
    m "I don't remember if I gave you my number, so let me see your phone."
    "You pull your cell phone out of your pocket and hand it to Muse."
    # play music texting noloop
    "Muse hands your phone back to you."
    "On your way back to your dorm, you realize that all three of the girls you were interested in asked you to go on a date tomorrow."
    "And they all want your answer by tonight..."
    "What are you going to do?"

# Final Night -------------------------------------------------------------------------------------------------------------------------------------------------------------

label final_night: 

    scene bg messenger_app
    with fade
    "Back in your dorm, you open your messaging app"
    "And reply with a simple yes to the date with..."
    # check ghost route 
    if inventory.get("Love Letter") and inventory.get("Locket") and inventory.get("Class Ring"):
        "You feel an eerie presence, and suddenly Ghost appears..."
        jump ghostRoute
    else:
        jump standard_route  # If items aren't collected, go back to a default route

label standard_route:
    # play music moon1
    menu:
        "Cincere":
            jump cincereRoute
        "Ame":
            jump ameRoute
        "Muse":
            jump museRoute
    
# Cincere Route -------------------------------------------------------------------------------------------------------------------------------------------------------------

label cincereRoute:

    # play music texting
    p "Hey Cincere..."
    p "I thought about it..."
    p "And I would love to be there to support you during your short film premier tomorrow."
    # play music ping noloop
    show cincere_happy at right
    with dissolve
    c "Hey, you."
    c "So you want to check out my work? :')"
    # play music moon1
    menu:
        "Yes":
            $ g_points += 1
            jump cincere_yes
        "Actually, I'd rather check out you.":
            jump cincere_yes 

label cincere_yes:

    "Cincere sends you a haha."
    "She always seems weary in class, but at least she is laughing in text..."
    "Maybe she actually likes you?"
    "Yeah, right."
    # play music texting noloop
    c "Actually, there's something I've been wanting to talk to you about."
    "You freeze up in spite of yourself, anxious that Cincere isn't interested in you that way."
    show cincere_sad at right
    with dissolve
    c "Actually, it's about Ghost."
    "Cincere is unusually serious."
    c "I found this...weird ring near my desk when classes started last week..."
    c "Honestly, it freaks me out, and I want to get rid of it."
    c "Will you take it off my hands?"
    # play music moon2 noloop
    menu:
        "Yes":
            $ c_points += 1
            jump find_class_ring
        "No":
            $ g_points += 1 
            jump cincere_date_begin

label find_class_ring:

    p "Sure, Cincere."
    c "Great. Meet me in the Film Studies classroom in twenty minutes."
    c "I'll give it to you there."

    scene bg classroom
    with fade
    show cincere_sad at right 
    with dissolve
    c "Here, I found this in my desk..."
    $ persistent.class_ring_collected = True
    $ inventory["Ghost"][2] = "Class Ring"
    call screen inventory_screen
    c "Honestly, it's been driving me crazy."
    c "Ever since I found it, I haven't been able to sleep."
    c "I feel like you just lifted this huge weight from my shoulders."
    c "Thank you."
    "You're scared, but you don't want to let it show."
    p "You're welcome."
    jump cincere_date_begin

label cincere_date_begin:

    c "You're sweet."
    c "Meet me at the cafe at 9am sharp tomorrow for our date?"
    p "Roger that."

    scene black
    with fade
    # play music birds noloop
    "You take your time deciding on an outfit for your date with Cincere."
    "Choose wisely, you want to look your best."
    call screen dress_up
    pass
    # want to make it so you get RP for choosing a specific shirt (black: m_points += 1, red: a_points += 1, blue: c_points += 1)
    # $ if mc_shirt = shirt: black m_points +=1 elif: mc_shirt = shirt_blue c_points += 1 else: a_points +=1 
    "You're looking sharp."

label cincere_date_continue: 

    scene bg cafe
    with fade
    "When you arrive at the cafe, your face turns absolutely white."
    "Cincere, Ame, and Muse are all sitting at the same table."
    menu:
        "Run away.":
            $ g_points += 1
            jump runaway_ending
        "Confront the girls.":
            jump cincere_date_end

label cincere_date_end:

    show cincere_date_happy at center 
    with dissolve
    show muse_sad at right
    show ame_sad at left
    "Cincere looks especially gorgeous today, but you can't help but notice the somehow even darker circles beneath her eyes."
    "You take the one empty seat at their table."
    p "Uhm, hey... ladies."
    m "..."
    a "..."
    p "So... I take it you all know each other?"
    "Cincere laughs."
    show cincere_date_full
    with dissolve
    c "These are my best friends!"
    c "They're here to support my art."
    "You feel your stomach drop as you glance at Muse and she averts her gaze."
    "Ame whistles."
    show ame_sad at left
    with dissolve
    a "Wow, C. This is the guy you were interested in?"
    "You see tears start to well up in Ame's eyes."
    a "I knew that [p] and [p] had the same name but... the way you described him..."
    "Ame sighs"
    a "I just thought he would be a different [p] than my [p]."
    show cincere_date_neutral at center 
    with dissolve
    c "Wait, you don't mean the guy who makes a fool of himself at the cafe counter?"
    "Ame takes a sip of her rich and steaming cup of joe."
    a "The very same."
    "To your utter horror, Muse pipes up:"
    m "A-actually!"
    show muse_full at right
    with dissolve
    m "This is the guy who's been flirting with me too..."
    "She sits back down, and you start to realize the severity of your situation."
    "You must now face the consequences of your actions."
    "How will you respond?"
    # play music moon1
    menu:
        "I can explain!":
            $ m_points += 1
            jump ends
        "I've done nothing wrong.":
            $ a_points += 1
            jump ends
        "Say nothing.":
            $ c_points += 1 
            jump ends

label ends:
    "Your skin flushes with the heat of embarrassment, but you're filled with resolve."
    p "I-"
    "Cincere stands up suddenly and cuts you off."
    show cincere_date_full at center
    with dissolve
    c "Guys, guys, my film is about to start, let's go!"
    pass # play Cincere's short film about Ghost and the hauntings 
    '''scene black
    with fade
    scene bg seed
    with dissolve
    show bg sprout
    with dissolve 
    scene bg flower
    with dissolve''' 

    scene black
    with fade
    # play music applause noloop

    scene bg student_center
    with fade
    "Cincere turns to look at you, pride smeared across her face."
    show cincere_date_happy at right
    with dissolve
    c "So, what did you think?"
    p "I think your all-nighters really paid off!"
    c "Thanks!"
    c "You actually inspired me to put a little more care into my work."
    c "You probably don't remember but..."
    show cincere_date_neutral at right
    with dissolve
    c "One time, I fell asleep on the bus and someone tried to steal my camera bag."
    c "I was barely awake, but I remember you walking up to the thief and loudly thanking them for looking after my camera."
    c "No one has ever really looked out for me that way before, let alone a stranger."
    show cincere_date_happy at right
    with dissolve
    c "Ever since then, I've basically had a crush on you [p]!"
    p "No way! I didn't realize that was you."
    "Cincere laughs."
    c "I've changed my look quite a bit since then, so I don't blame you."
    p "Haha I'm glad."
    "You feel a bit uneasy, but you have no regrets."
    "Cincere suggests the four of you head back to her dorm after the short film festival."
    "Of course, you oblige."

    scene bg dorm
    with fade
    # play music door noloop
    show cincere_date_neutral
    with dissolve
    c "So, spill. You've been talking to all three of us?"
    if a_points >=5 and c_points >=5 and m_points >=5:
        jump cincereRoute_good_ending
    else:
        jump cincereRoute_bad_ending 

label cincereRoute_good_ending:

    p "Yeah I mean, you're all just so beautiful and interesting..."
    p "Can you really blame me for falling for you?"
    show cincere_date_sad at center
    with dissolve
    show ame_sad at left
    with dissolve
    show muse_sad at right
    with dissolve
    c "I don't blame you but..."
    c "Can you really handle all three of us?"
    show cincere_date_mischievious 
    with dissolve
    c "Ame, you brought some wine right?"
    show ame_neutral at left
    with dissolve
    "Ame nods."
    show cincere_date_happy at center
    with dissolve
    c "Then let's celebrate!"
    show muse_sad at right
    m "Um, I definitely have to work after this, so I will not be partaking."
    m "Also, aren't you all underage?"
    a "Jesus, M, don't be such a prude."
    c "Yeah, now is...really not the time to be prudish."
    "Cincere bites her lip."
    "She leans in close and whispers in your ear:"
    c "Right, [p]?"
    "Shivers run down your neck."
    c "I mean, it's okay if you don't want to..."
    c "But, we've already discussed it and..."
    c "We decided there is really only one reliable way to find out if you're right for one of us."
    p "And how is that?"
    "Ame pours each of you a small plastic cup of blood red wine, except for Muse who gets a small clear cup of water."
    a "You tell us which one of us you enjoy kissing the most."
    p "K-kissing?!"
    "You almost spit out your wine."
    "It's sour, but pleasant."
    m "Yes, kissing."
    p "To be honest, I, I've never kissed anyone before, so..."
    p "I don't know if that would be a good measurement..."
    c "We should play spin the bottle."
    "Your pulse quickens."
    a "Woah, C, calm down."
    p "Yeah can we just um... talk?"
    p "Honestly, I've never hung out like this with anyone before..."
    p "I've never had friends who make art..."
    p "It's cool!"
    p "And honestly..."
    "You feel like your cheeks are on fire."
    p "I just want to be a part of your circle."
    p "All three of you are...really amazing and tbh..."
    p "Really fucking hot."
    p "It's like..."
    p "Do I want to fuck you or do I want to be you?"
    p "I want both and it confuses me..."
    p "Who am I?"
    m "You're [p]."
    p "Yeah, but, is that enough?"
    "Cincere puts her hand on your back."
    c "Always."
    "Your heart feels full, and tears start to well in your eyes."

label cincereRoute_bad_ending:

    p "Yeah I mean, you're all just so beautiful and interesting..."
    p "Can you really blame me for falling for you?"
    show cincere_date_sad at center
    with dissolve
    show ame_sad at left
    with dissolve
    show muse_sad at right
    with dissolve
    c "I don't blame you but..."
    c "The three of us decided it would be better this way."
    p "Better...what way?"
    c "Better for everyone."
    show cincere_date_full
    with dissolve
    c "Ame, get the restraints!"
    c "Muse, you know what to do."
    "Muse opens up a worn book while Ame rummages in her bag."
    show muse_neutral
    with dissolve 
    m "Regna terrae, cantate..."
    m "Deo, psallite Domino..."
    p "Wait, what's going on? What are you saying?"
    m "qui fertis ascendit super caelum"
    m "caeli and Orientem..."
    m "Ecce dabit voci suae vocem virtutis.."
    m "tribuite virtutem deo..."
    m "Exorcizamus te, omnis immundud spiritus..."
    "Ame restrains you to the bed frame."
    "You take a deep breath."
    "It smells like Cincere..."
    p "Muse! Muse, I didn't mean it. Please. Please let me go."
    "Cincere scoffs."
    "Muse doesn't seem to hear you since she continues reading without pause."
    "Ame, where did Ame go?"
    p "Help! Please, help!"
    m "Ergo draco maledicte..."
    m "et omnis legio diabolica adjuramus te!"
    "You try to slip your wrists through the straps, but the knots are tied too tightly."
    p "Please, please just let me go."
    m "The power of Christ compels you!"
    "Your vision blurs..."
    m "The power of Christ compels you!"
    jump logic_puzzle_intro

label logic_puzzle_intro:

    scene black
    with fade
    show ghost_sad
    with dissolve
    g "To escape posession, you must solve this riddle."
    g "Cvm mentior et mentiri me dico, mentior an verum dico?"
    
    "You think about the ghost's words. What is the true meaning?"
    menu:
        "Lying.":
            $ player_choice = "lying"
            jump puzzle_result
        "Telling the truth.":
            $ player_choice = "truth"
            jump puzzle_result

label puzzle_result:

    if player_choice == "lying" and persistent.faith_collected:
        g "Even when lying, you hold onto faith. Proceed."
        jump faithRoute
    elif player_choice == "truth" and persistent.faith_collected:
        g "Truth and faith guide you forward."
        jump faithRoute
    else:
        g "Without faith, neither truth nor lies can save you."
        jump cincereRoute_bad_ending_continued

label cincereRoute_bad_ending_continued:

    g "I guess Cincere thought you would be a suitable replacement"
    "The strange figure looks you up and down and sighs."
    g "As if."
    return

# Ame Route -------------------------------------------------------------------------------------------------------------------------------------------------------------              

label ameRoute:

    # play music texting
    p "Hey Ame..."
    p "I thought about it..."
    p "And I would love to go on a picnic with you tomorrow."
    # play music ping noloop
    show ame_happy at right
    with dissolve
    a "Hey, [p]!"
    a "I'm stoked!"
    a "Actually, want to meet me at the cafe a bit early tomorrow? 9am."
    a "I'm meeting a few friends there for coffee, and then we're going to a short film festival."
    a "It's actually my friend's first premier. She'll be excited I'm sure."
    menu:
        "Totally.":
            $ a_points += 1
            jump find_pudding
        "Actually, I can't.":
            jump ame_date_begin

label find_pudding: 

    a "Awesome! Also... if you meeet me at the cafe in twenty minutes I'll give you something special."
    "You send Ame a sprinting emoji."

    scene bg cafe
    with fade
    show ame_happy
    with dissolve
    a "Ah, you're here!"
    a "The boss has been letting me use some of the equipment here so..."
    a "I've been trying out this recipe..."
    $ persistent.pudding_collected = True
    $ inventory["Ame"][2] = "Pudding"
    call screen inventory_screen
    "Ame hands you a creamy delight wrapped in plastic."
    p "Woah, thanks!"
    a "You're welcome."
    "She laughs, but you can tell her gaze is fixed on your spoon."
    "You start to feel self-conscious."
    "Ame must be thinking about presentation, texture, flavor, bite."
    "Not to mention how many chemical reactions you have to know to make such a perfect treat..."
    "Ame laughs and pulls you out of dessert bliss."
    a "Ha! You always finish my desserts in just one or two bites!"
    p "Oh, they're just incredible."
    p "I could eat them forever."
    a "I love that."
    "Ame looks really content."
    a "See you here bright and early tomorrow?"
    p "Yes m'aam."
    jump ame_date_begin

label ame_date_begin:

    scene black
    with fade
    # play music birds noloop
    "You decided to meet Ame and her friends early for coffee."
    "Take your time deciding on an outfit."
    call screen dress_up
    pass
    # want to make it so you get RP for choosing a specific shirt (black: m_points += 1, red: a_points += 1, blue: c_points += 1)
    # $ if mc_shirt = shirt: black m_points +=1 elif: mc_shirt = shirt_blue c_points += 1 else: a_points +=1 
    "You're looking sharp."
    jump ame_date_continue

label ame_date_continue: 

    scene bg cafe
    with fade
    "When you arrive at the cafe, the color drains from your face."
    "Ame, Cincere, and Muse are all sitting at the same table."
    menu:
        "Run away.":
            $ g_points += 1
            jump runaway_ending
        "Confront the girls.":
            jump ame_date_end

label ame_date_end:

    show ame_date_happy at center 
    with dissolve
    show muse_sad at right
    show cincere_sad at left
    "Ame looks especially beautiful today. It's the first time you've seen her wear her hair down."
    "In fact, it's the first time you've seen her out of her cafe apron."
    "You take the one empty seat at their table."
    p "Uhm, hey... ladies."
    m "..."
    c "..."
    p "So... I take it you all know each other?"
    "Ame laughs."
    show ame_date_full
    with dissolve
    a "These are my best friends."
    a "We're here to support Cincere's short film premier."
    "You feel your stomach drop as you glance at Muse and she averts her gaze."
    "Cincere is visibly shaking and her knuckles are turning white.."
    show cincere_sad at left
    with dissolve
    c "Wow, Ame. This is the guy you were interested in?"
    "You see tears start to well up in Cincere's eyes."
    c "I knew that [p] and [p] had the same name but... the way you described him..."
    "Cincere sighs"
    c "I just thought he would be a different [p] than my [p]."
    show ame_date_neutral at center 
    with dissolve
    a "Your [p]? You mean the classic stud from your film studies class?"
    "Ame looks at Cincere in disbelief."
    c "The very one."
    "To your utter horror, Muse pipes up:"
    m "A-actually!"
    show muse_full at right
    with dissolve
    m "This is the guy who's been flirting with me too..."
    "She sits back down, and you start to realize the severity of your situation."
    "You must now face the consequences of your actions."
    "How will you respond?"
    # play music moon1
    menu:
        "I can explain!":
            $ m_points += 1
            jump ends2
        "I've done nothing wrong.":
            $ a_points += 1
            jump ends2
        "Say nothing.":
            $ c_points += 1 
            jump ends2

label ends2:
    "Your skin flushes with the heat of embarrassment, but you're filled with resolve."
    p "I-"
    "Cincere stands up suddenly and cuts you off."
    show cincere_full
    with dissolve
    c "Guys, guys, my film is about to start, let's go!"
    pass # play Cincere's short film about Ghost and the hauntings 
    '''scene black
    with fade
    scene bg seed
    with dissolve
    show bg sprout
    with dissolve 
    scene bg flower
    with dissolve''' 

    scene black
    with fade
    # play music applause noloop
    a "Wow Cincere, that was beautiful."
    m "Yes Cincere, very sincere. I loved it."
    p "It was beautiful."
    show cincere_happy
    with dissolve
    c "Hey, I've got a great idea."
    c "Let's go back to my dorm and celebrate!"
    "She winks at the other two girls."
    "You feel a bit uneasy, but you know it's time to come clean."

    scene bg dorm
    with fade
    # play music door noloop
    show ame_date_neutral
    with dissolve
    a "It's time for you to talk. You've been flirting with all three of us. Explain."
    if a_points >=5 and c_points >=5 and m_points >=5:
        jump ameRoute_good_ending
    else:
        jump ameRoute_bad_ending 

label ameRoute_good_ending:

    p "Um, yeah I mean, you're all just so beautiful and interesting..."
    p "Can you really blame me for flirting with you?"
    show ame_date_sad at center
    with dissolve
    show cincere_sad at left
    with dissolve
    show muse_sad at right
    with dissolve
    a "I don't blame you but..."
    a "Can you really handle all three of us?"
    show cincere_mischievious at left  
    with dissolve
    c "Ame, you brought some wine right?"
    show ame_date_neutral
    with dissolve
    a "Sure did."
    show cincere_happy at left
    with dissolve
    c "Then let's drink!"
    show muse_sad at right
    m "Um, I definitely have to work after this, so I will not be partaking."
    m "Also, aren't you all underage?"
    a "C'mon, M, don't be such a prude."
    c "Yeah, now is...really not the time to be prudish."
    "Cincere bites her lip."
    "She leans in close and whispers in your ear:"
    c "Right, [p]?"
    "Shivers run down your neck."
    c "I mean, it's okay if you don't want to..."
    c "But, we've already discussed it and..."
    c "We decided there is really only one reliable way to find out if you're right for one of us."
    p "And how is that?"
    "Ame pours each of you a small plastic cup of blood red wine, except for Muse who gets a small clear cup of water."
    "It's a bit sour, but pleasant."
    a "Tell us which one of us you enjoy kissing the most."
    p "K-kissing?!"
    "You almost spit out your wine."
    m "Yes, kissing."
    p "To be honest, I, I've never kissed anyone before, so..."
    p "I don't know if that would be a good measurement..."
    c "We should play spin the bottle."
    "Your pulse quickens."
    a "Woah, C, calm down."
    p "Yeah can we just um... talk?"
    p "Honestly, I've never hung out like this with anyone before..."
    p "I've never had friends who make art..."
    p "It's cool!"
    p "And honestly..."
    "You feel like your cheeks are on fire."
    p "I just want to be a part of your circle."
    p "All three of you are...really amazing and tbh..."
    p "Really fucking hot."
    p "It's like..."
    p "Do I want to fuck you or do I want to be you?"
    p "I want both and it confuses me..."
    p "Who am I?"
    "You put your head in your hands."
    m "You're [p]."
    p "Yeah, but, is that enough?"
    "Ame pats your back with her gentle and firm touch."
    a "Always."
    "Your heart feels full, and tears start to well in your eyes."
    "Ame takes you in her arms and squeezes you tightly."
    a "Always, [p]."
    return

label ameRoute_bad_ending:

    p "Yeah I mean, you're all just so beautiful and interesting..."
    p "Can you really blame me for falling for you?"
    show ame_date_sad at center
    with dissolve
    show cincere_sad at left
    with dissolve
    show muse_sad at right
    with dissolve
    c "I don't blame you but..."
    c "The three of us decided it would be better this way."
    p "Better...what way?"
    a "It's hard to talk about this but..."
    a "We think you and Ghost are the perfect match..."
    a "And if you're together then..."
    a "Maybe she'll stop haunting us."
    p "Wait, wh-what?!"
    show cincere_full
    with dissolve
    c "Ame, get the restraints!"
    c "Muse, you know what to do."
    a "I'm sorry, [p], I really am."
    "Muse opens up a worn book while Ame rummages in her bag."
    show muse_neutral
    with dissolve 
    m "Regna terrae, cantate..."
    m "Deo, psallite Domino..."
    p "Wait, what's going on? What are you saying?"
    m "qui fertis ascendit super caelum"
    m "caeli and Orientem..."
    m "Ecce dabit voci suae vocem virtutis.."
    m "tribuite virtutem deo..."
    m "Exorcizamus te, omnis immundud spiritus..."
    "Ame restrains you to the bed frame."
    "You take a deep breath."
    "It smells like Cincere..."
    p "Muse! Muse, I didn't mean it. Please. Please let me go."
    "Cincere scoffs."
    "Muse doesn't seem to hear you since she continues reading without pause."
    "Ame, where did Ame go?"
    p "Help! Please, help!"
    m "Ergo draco maledicte..."
    m "et omnis legio diabolica adjuramus te!"
    "You try to slip your wrists through the straps, but the knots are tied too tightly."
    "You try to stay calm, but you can't accept how absurd this is."
    p "Please, please just let me go!"
    "You start shouting."
    m "The power of Christ compels you!"
    "Your vision blurs..."
    m "The power of Christ compels you!"
    jump logic_puzzle_intro2

label logic_puzzle_intro2:
    scene black
    with fade
    show ghost_sad
    with dissolve
    g "To escape posession, you must solve this riddle."
    g "Cvm mentior et mentiri me dico, mentior an verum dico?"
    
    "You think about the ghost's words. What is the true meaning?"
    menu:
        "Lying.":
            $ player_choice = "lying"
            jump puzzle_result2
        "Telling the truth.":
            $ player_choice = "truth"
            jump puzzle_result2

label puzzle_result2:

    if player_choice == "Lying." and persistent.faith_collected:
        g "Even when lying, you hold onto faith. Proceed."
        jump faithRoute
    elif player_choice == "Telling the truth." and persistent.faith_collected:
        g "Truth and faith guide you forward."
        jump faithRoute
    else:
        g "Without faith, neither truth nor lies can save you."
        jump ameRoute_bad_ending_continued


label ameRoute_bad_ending_continued:

    g "I guess Cincere thought you would be a suitable replacement for her."
    g "Hmph. Could be interesting."
    "Your limbs grow cold as the relentless elixir of death numbs your bloodstream."
    g "C'mon, [p], don't be shy."
    g "This will hurt you less the less you resist."
    "You wish that sounded more comforting."
    "Your whole body shudders."
    return

# Muse Route -------------------------------------------------------------------------------------------------------------------------------------------------------------

label museRoute:

   # play music texting
    p "Hey Muse..."
    p "I thought about it..."
    p "And I would love to go to your exhibit tomorrow."
    # play music ping noloop
    show muse_happy at right
    with dissolve
    m "Hey, [p]. That's great news!"
    m "Actually, I have a pretty full day tomorrow. Want to join me in the morning?"
    menu:
        "I'm not sure.":
            $ m_points += 1
            jump find_dracula
        "I'd love to.":
            jump muse_date_begin

label find_dracula: 

    m "That's alright..."
    m "I hate to do this to you but it's kind of important."
    m "Meet me in the library in 20 min.?"
    # play music texting noloop
    p "Sure, Muse."

    scene bg library
    with fade
    show muse_neutral
    with dissolve
    m "Hey, [p]."
    p "Hey, Muse! So..."
    "You look around and bring your voice down to a whisper."
    p "What did you want to talk about?"
    "Muse takes you to one of the study rooms and closes the door."
    # play music door noloop
    show muse_full
    with dissolve
    m "Shh just listen."
    m "Tomorrow um..."
    m "I think you're going to get interrogated."
    show muse_sad
    with dissolve
    p "What are you talking about?"
    m "I can't say too much about it, but..."
    m "Do you think you could meet me in the cafe early tomorrow morning, for coffee?"
    p "Uhm, what time?"
    m "9am."
    p "Why so early?"
    m "Just be there. Okay?"
    p "Okay, okay!"
    "You were going to say yes anyway."
    p "I have to admit, I'm feeling a little anxious."
    m "Here, this one always comforts me when I'm feeling scared."
    $ persistent.dracula_collected = True
    $ inventory["Muse"][1] = "Dracula (1897)"
    call screen inventory_screen
    p "Isn't this a horror novel?"
    show muse neutral
    with dissolve
    m "Hm?"
    jump muse_date_begin

label muse_date_begin:

    scene black
    with fade
    # play music birds noloop
    "You decide to meet Muse early for coffee."
    "It seems important, so take your time choosing an outfit."
    call screen dress_up
    pass
    # want to make it so you get RP for choosing a specific shirt (black: m_points += 1, red: a_points += 1, blue: c_points += 1)
    # $ if mc_shirt = shirt: black m_points +=1 elif: mc_shirt = shirt_blue c_points += 1 else: a_points +=1 
    "You're looking clean and fresh."
    jump muse_date_continue

label muse_date_continue: 

    scene bg cafe
    with fade
    "When you arrive at the cafe, you turn pale as a ghost."
    "Muse, Cincere, and Ame are all sitting at the same table."
    menu:
        "Run away.":
            $ g_points += 1
            jump runaway_ending
        "Confront the girls.":
            jump muse_date_end

label muse_date_end:

    show muse_date_happy at center 
    with dissolve
    show ame_sad at right
    show cincere_sad at left
    "Muse looks lovely today. She's wearing all black again, but she's added some accessories."
    "She shines."
    p "Uhm, hey... ladies."
    a "..."
    c "..."
    p "So... I take it you all know each other?"
    "Muse laughs nervously."
    show muse_date_full
    with dissolve
    m "This is him, this is library dude!"
    c "Oooh bummer. Same guy."
    "You're not sure why, but Muse's lips start to quiver."
    "When Ame doesn't say anything, Muse presses her further."
    m "It's weird for you to be quiet Ame. Tell me what's up."
    show ame_sad at right
    with dissolve
    a "Ugh it's the same cafe customer too."
    m "Wait, the guy who always makes a fool of himself at the cafe counter?"
    show cincere_sad at left
    c "It gets worse."
    m "No, no, no, no."
    m "Ugh I really hoped all our [p]s were different people!"
    "Muse sits back down, and you start to realize the severity of your situation."
    "Face the consequences of your actions and respond:"
    # play music moon1
    menu:
        "I can explain!":
            $ m_points += 1
            jump ends3
        "I've done nothing wrong.":
            $ a_points += 1
            jump ends3
        "Say nothing.":
            $ c_points += 1 
            jump ends3

label ends3:
    "Your skin flushes with the heat of embarrassment, but you're filled with resolve."
    p "I-"
    "Cincere stands up suddenly and cuts you off."
    show cincere_full
    with dissolve
    c "Guys, guys, my film is about to start, let's go!"
    "You're swept up in the moment and follow them without thinking."
    pass # play Cincere's short film about Ghost and the hauntings 
    '''scene black
    with fade
    scene bg seed
    with dissolve
    show bg sprout
    with dissolve 
    scene bg flower
    with dissolve''' 

    scene black
    with fade
    # play music applause noloop
    a "Wow Cincere, that was beautiful."
    m "Yes Cincere, very sincere. I loved it."
    p "It was beautiful."
    show cincere_happy
    with dissolve
    c "Hey, I've got a great idea."
    c "Let's go back to my dorm and celebrate!"
    "She winks at the other two girls."
    "You feel a bit uneasy, but you know it's time to come clean."

    scene bg dorm
    with fade
    # play music door noloop
    show muse_date_neutral
    with dissolve
    m "So, were you serious about any of us?"
    if a_points >=5 and c_points >=5 and m_points >=5:
        jump museRoute_good_ending
    else:
        jump museRoute_bad_ending 

label museRoute_good_ending:

    p "Of course! You're all just so beautiful and interesting..."
    p "How could I not take it seriously?"
    show muse_date_sad at center
    with dissolve
    show cincere_sad at left
    with dissolve
    show ame_sad at right
    with dissolve
    m "I don't blame you but..."
    m "Can you really handle all three of us?"
    show cincere_mischievious at left  
    with dissolve
    c "Ame, you brought some wine right?"
    show ame_neutral at right
    with dissolve
    a "Sure did."
    show cincere_happy at left
    with dissolve
    c "Then let's drink!"
    show muse_date_sad at right
    m "Um, I definitely have to work after this, so I will not be partaking."
    m "Also, aren't you all underage?"
    a "C'mon, M, don't be such a prude."
    c "Yeah, now is...really not the time to be prudish."
    "Cincere bites her lip."
    "She leans in close and whispers in your ear:"
    c "Right, [p]?"
    "Shivers run down your neck."
    c "I mean, it's okay if you don't want to..."
    c "But, we've already discussed it and..."
    c "We decided there is really only one reliable way to find out if you're right for one of us."
    p "And how is that?"
    "Ame pours each of you a small plastic cup of blood red wine, except for Muse who gets a small clear cup of water."
    "It's a bit sour, but pleasant."
    a "Tell us which one of us you enjoy kissing the most."
    p "K-kissing?!"
    "You almost spit out your wine."
    m "Yes, kissing."
    p "To be honest, I, I've never kissed anyone before, so..."
    p "I don't know if that would be a good measurement..."
    c "We should play spin the bottle."
    "Your pulse quickens."
    a "Woah, C, calm down."
    p "Yeah can we just um... talk?"
    p "Honestly, I've never hung out like this with anyone before..."
    p "I've never had friends who make art..."
    p "It's cool!"
    p "And honestly..."
    "You feel like your cheeks are on fire."
    p "I just want to be a part of your circle."
    p "All three of you are...really amazing and tbh..."
    p "Really fucking hot."
    p "It's like..."
    p "Do I want to fuck you or do I want to be you?"
    p "I want both and it confuses me..."
    p "Who am I?"
    "You put your head in your hands."
    m "You're [p]."
    p "Yeah, but, is that enough?"
    "Muse rubs your back with her fairy like touch."
    m "You're always enough, [p]."
    return

label museRoute_bad_ending:

    p "Of course! You're all just so beautiful and interesting..."
    p "How could I not take it seriously?"
    show muse_date_sad at center
    with dissolve
    show cincere_sad at left
    with dissolve
    show ame_sad at right
    with dissolve
    c "I don't blame you but..."
    c "The three of us decided it would be better this way."
    p "Better...what way?"
    a "It's hard to talk about this but..."
    a "We think you and Ghost are the perfect match..."
    a "And if you're together then..."
    a "Maybe she'll stop haunting us."
    p "Wait, wh-what?!"
    show cincere_full
    with dissolve
    c "Ame, get the restraints!"
    c "Muse, you know what to do."
    m "I'm sorry, [p]."
    "Muse opens up a worn book while Ame rummages in her bag."
    show muse_neutral
    with dissolve 
    m "Regna terrae, cantate..."
    m "Deo, psallite Domino..."
    p "Wait, what's going on? What are you saying?"
    m "qui fertis ascendit super caelum"
    m "caeli and Orientem..."
    m "Ecce dabit voci suae vocem virtutis.."
    m "tribuite virtutem deo..."
    m "Exorcizamus te, omnis immundud spiritus..."
    "Ame restrains you to the bed frame."
    "You take a deep breath."
    "It smells like Cincere..."
    p "Muse! Muse, I didn't mean it. Please. Please let me go."
    "Cincere scoffs."
    "Muse doesn't seem to hear you since she continues reading without pause."
    "Ame, where did Ame go?"
    p "Help! Please, help!"
    m "Ergo draco maledicte..."
    m "et omnis legio diabolica adjuramus te!"
    "You try to slip your wrists through the straps, but the knots are tied too tightly."
    "You try to stay calm, but you can't accept how absurd this is."
    p "Please, please just let me go!"
    "You start shouting."
    m "The power of Christ compels you!"
    "Your vision blurs..."
    m "The power of Christ compels you!"
    jump logic_puzzle_intro3

label logic_puzzle_intro3:
    scene black
    with fade
    show ghost_sad
    with dissolve
    g "To escape posession, you must solve this riddle."
    g "Cvm mentior et mentiri me dico, mentior an verum dico?"
    
    "You think about the ghost's words. What is the true meaning?"
    menu:
        "Lying.":
            $ player_choice = "lying"
            jump puzzle_result
        "Telling the truth.":
            $ player_choice = "truth"
            jump puzzle_result

label puzzle_result3:

    if player_choice == "lying" and persistent.faith_collected:
        g "Even when lying, you hold onto faith. Proceed."
        jump faithRoute
    elif player_choice == "truth" and persistent.faith_collected:
        g "Truth and faith guide you forward."
        jump faithRoute
    else:
        g "Without faith, neither truth nor lies can save you."
        jump museRoute_bad_ending_continued

label museRoute_bad_ending_continued:

    g "I guess Cincere thought you would be a suitable replacement for her."
    g "Hmph. Could be interesting."
    "Your limbs grow cold as the sweet elixir of death enters your bloodstream."
    g "C'mon, [p], don't be shy."
    g "This will hurt less the less you resist."
    "You wish that sounded more comforting."
    "Your whole body shudders."
    jump credits

# Runaway Route ---------------------------------------------------------------------------------------------------------------------------------------------------------------

label runaway_ending:

    "You ran away."
    jump credits

# Ghost Route ---------------------------------------------------------------------------------------------------------------------------------------------------------------

label ghostRoute:

    scene bg dorm
    with fade
    show ghost_sad
    with dissolve
    g "So you're the person Cincere thinks would be a good partner for me."
    "The strange creature looks you up and down and sighs."
    g "I guess beggars can't be choosers."
    menu:
        "Who are you?":
            $ g_points += 1
            jump ghost_begin
        "What's that supposed to mean?":
            jump ghost_begin

label ghost_begin:

    g "Isn't that the question of the year?"
    g "I thought maybe if I found a partner, I could learn more about who I am..."
    g "But it looks like I might be stuck here forever."
    menu:
        "What happened to you?":
            $ g_points += 2
            g "It was a long time ago... I fell in love, but..."
            g "That's all I remember."
        "There must be a way to help you.": 
            $ g_points += 2
            g "Help? No one's been able to help me for years. What makes you think you can?"
    p "I have a friend who seems like she knows a lot about you..."
    p "And would probably want to meet you to be honest."
    p "Why don't we go to the library? I bet she's there."
    # play music door noloop
    show frog_neutral
    with dossolve
    f "I'm back..."
    f "Who were you talking to just now?"
    "You look around, but don't see anyone."
    p "Um, noone, just talking to myself I guess."
    f "Hm. Maybe you should get some sleep?"
    p "Yeah."
    "Frog drops their things and sits at their desk."
    "They'll probably be up late studying again."
    p "Hey, Frog?"
    f "What?"
    p "Thanks for looking out for me."
    "Frog smiles at their desk."
    f "Now I can tell you're not thinking straight!"
    "You grumble and roll over in your bunkbed."
    p "Good night."
    f "Good night."
    jump ghost_middle

label ghost_middle:

    scene black
    with fade
    "It's so unbearably cold that you clutch your covers to your chest."
    "You're sweating profusely and the covers are wet with your stench."
    show ghost_happy
    with dissolve
    "Ghost is kicking...her...legs over your bed while she watches Frog sleep."
    g "Your roommate seems... nice."
    show ghost_neutral
    with dissolve
    g "But it looks like you forgot about our plans."
    g "Do you want to help me or not?"
    menu:
        "Let me try. I want to help.":
            $ g_points += 3
            g "Aw, you'd do that? For little old me?"
        "I don't know if I can, but I'll do my best.":
            $ g_points += 1
            g "At least you're honest. That's more than I can say for most."
    g "Maybe... maybe there's still hope."
    p "Maybe you and I can both be free of these weights in our chests."
    show ghost_happy
    with dissolve
    g "Let's go to the library."
    jump ghost_end

label ghost_end:

    scene bg library
    with fade 
    "You're surprised the library is open so late, but you don't question it."
    "You also don't question Muse's presence when you find her in her usual spot."
    p "Um, hey Muse! Mind if I sit with you?"
    "Muse looks at all of the empty tables surrounding her."
    show muse_neutral
    with dissolve
    m "You certainly can, [p]."
    "You take a seat besider her, while Ghost sits next to you."
    "Muse doesn't seem able to see Ghost."
    p "I'm here because there's something I want to ask you."
    "Muse doesn't look up from her book."
    m "Continue."
    p "Um well..."
    p "You don't have to believe me but..."
    menu:
        "I'm being haunted by Ghost right now.":
            g "Haunted is a strong word."
        "I have this um, friend, who wants to learn more about Ghost.":
            m "I believe you."
    p "So, do you have any like, references or anything?"
    "Muse pushes her glasses up her nose."
    m "Of course I have references!"
    m "Now that you mention it..."
    m "I was reviewing some of the old school yearbooks for the exhibit tomorrow and I noticed a woman who seemed to match Ghost's description..."
    show muse_full
    with dissolve
    m "Wait here, I'll be right back!"
    scene bg library
    with fade
    show ghost_sad
    with dissolve
    g "I guess you all call me 'Ghost?'"
    p "..."
    show muse_happy
    with dissolve
    m "I got it!"
    m "The class yearbook from 1959."
    m "Let's see, there was a memorial page for her but..."
    m "She tragically passed away her senior year before she could graduate..."
    m "Her name was..."
    m "Faith."
    $ persistent.faith_collected = True
    return

label ghost_end_continued:

    m "This is my best guess as to who Ghost is!"
    m "With everything Cin's been talking about lately, it's got to be her."
    "You look at Ghost who is phasing her hand in and out of books."
    "Maybe 'Faith' doesn't ring a bell?"
    "In any case, you thank Muse for her help."
    p "Thanks, Muse. You're incredible."
    "Muse blushes as she packs up her things."
    m "I'm going to get some sleep."
    m "Good night!"
    p "Night!"

    scene bg library
    with fade
    "You try to get Ghost's attention, but she doesn't seem to care."
    show ghost_neutral
    with dissolve
    g "Huh, so my name was Faith."
    jump credits
    

# Faith Route ---------------------------------------------------------------------------------------------------------------------------------------------------------------

label faithRoute:

    scene bg cemetery
    with fade
    show ghost_sad
    with dissolve
    g "There's something I need to tell you. Something I've never told anyone before."
    menu:
        "I'm listening.":
            $ g_points += 1
            jump faith_discovery
        "This sounds serious.":
            $ g_points += 1
            jump faith_discovery

label faith_discovery:

    g "I was... different. In a way that scared him. We were so close to sharing something beautiful, but when he found out, he... he killed me."
    "The weight of her words hangs heavy in the air." 
    menu:
        "What do you mean?":
            $ g_points += 2
            jump faith_revelation
        "That's horrible...":
            jump faith_revelation

label faith_revelation:

    g "I was born in 1959. Back then, being different wasn't something people could understand, let alone accept."
    g "I was so excited... to share myself fully. But he couldn't handle the truth."
    "Her eyes glisten with unspoken sorrow."
    g "And now, I'm stuck here, searching for someone who can help me move on."
    menu:
        "Faith... I need to tell you something too.":
            $ mc_trans = True
            jump mc_reflection
        "You don't have to do this alone.":
            $ g_points += 2
            jump mc_reflection

label mc_reflection:
    "You take a deep breath, summoning the courage to share your truth."
    p "I'm transgender. Sometimes... I wish I were cisgender. Life would be so much easier."
    p "But I've learned to have faith in the people who love me. They love me for who I am, not what I am."
    "Faith listens intently, her expression softening."
    g "You're brave to share that with me. Thank you."
    jump support_system

label support_system:

    scene bg dorm
    with fade
    "Later, you gather your friends—Frog, Cincere, Muse, and Ame."
    p "There's something I need to tell all of you."
    menu:
        "Tell them the truth.": 
            $ friends_support = True
            jump supportive_friends
        "Stay silent.":
            jump silent_end

label supportive_friends:

    p "I'm transgender. I wanted you all to know because... I trust you."
    f "Thanks for sharing that with us. We're here for you, no matter what."
    c "Absolutely. You're our friend, and we love you."
    m "You're amazing just the way you are."
    a "We've got your back, always."
    "Their words fill you with a warmth you didn't know you needed."
    jump faith_conclusion

label faith_conclusion:

    scene bg cemetery
    with fade
    show ghost_smile
    with dissolve
    "Faith appears, her form shimmering with light."
    g "You've given me something I thought I'd lost forever... hope."
    g "Thank you. For everything."
    "Before your eyes, Faith's spirit is purified, her soul finally at peace."
    return

label silent_end:

    "You decide not to share, the moment passing quietly."
    return

# Credits ---------------------------------------------------------------------------------------------------------------------------------------------------------------

label credits:

    pass # maybe throw in "consider buying me coffee" with a link to my paypal and some sick programming art

#  ---------------------------------------------------- Game End ------------------------------------------------------------------------------------------------------------
