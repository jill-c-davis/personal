# The script of the game goes in this file.

# ---------------------------------------------------- Character Objects -------------------------------------------------------------------------------------------

# Declare characters used by this game. The color argument colorizes the name of the character.

define a = Character("Ame", color="371F76")
define c = Character("Cincere", color="4FB9AF")
define f = Character("Frog", color="5EDD5F")
define g = Character("Ghost")
define m = Character("Muse", color="FF9899")
define n = Character("Manager")
define p = Character("Yugi")


#  ---------------------------------------------------- Images ----------------------------------------------------------------------------------------------------

# Backgrounds 

image bg dorm:
    "images/dorm.png"
    zoom 1.5
image bg classroom:
    "images/classroom.png"
    zoom 1.5
image bg cafe:
    "images/cafe.png"
    zoom 1.25
image bg library:
    "images/library.png"
image bg messenger_app:
    "images/messenger_app.png"

# Characters

# MC
image shirt_black:
    "images/shirt_black.png"
image shirt_blue:
    "images/shirt_blue.png"
image shirt_red:
    "images/shirt_red.png"


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

# Manager
image manager_neutral:
    "images/manager.png"

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
    "images/godzilla.png"
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
    "images/tell_tale_heart.png

# Ghost
image love_letter:
    "images/love_letter.png"
image locket:
    "images/locket.png"
image class_ring:
    "images/class_ring.png"

#  ---------------------------------------------------- Audio ----------------------------------------------------------------------------------------------------

# Music

define audio.moon1 = "music/moonlight_sonata_lofi_pt1.mp3"
define audio.moon2 = "music/moonlight_sonata_lofi_pt2.mp3"
define audio.moon3 = "music/moonlight_sonata_lofi_pt3.mp3"
define audio.moon4 = "music/moonlight_sonata_lofi_pt4.mp3"
define audio.moon5 = "music/moonlight_sonata_lofi_pt5.mp3"
define audio.moon6 = "music/moonlight_sonata_lofi_pt6.mp3"


# SFX

define audio.birds = "music/birds.mp3"
define audio.door = "music/door.mp3"
define audio.startled = "music/startled.mp3"
define audio.notebook_tear = "music/notebook_tear.mp3"
define audio.notebook_crumple = "music/notebook_crumple.mp3"
define audio.pensive = "music/pensive.mp3"
define audio.chatter = "music/chatter.mp3"
define audio.success = "music/success.mp3"
define audio.disappointed = "music/disappointed.mp3"
define audio.stomach_growl = "music/stomach_growl.mp3"
define audio.ticking = "music/ticking.mp3"
define audio.texting = "music/texting.mp3"
define audio.ping = "music/ping.mp3"
#  ---------------------------------------------------- Inventory ------------------------------------------------------------------------------------------------

# Define the inventory as a dictionary to store items

default inventory = {
    "Ame" : [None, None, None],
    "Cincere" : [None, None, None],
    "Muse" : [None, None, None],
    "Ghost" : [None, None, None],
}

# Define each inventory item

# Ame
define strawberry_roll_cake = {
    "name" : "Strawberry Roll Cake",
    "description" : "A complicated looking recipe for a rolled up strawberry and lemon cake. It smells like fresh lemons."
    "image" : "strawberry_roll_cake.png"
}
define checkerboard_cookies = {
    "name" : "Checkerboard Cookies",
    "description" : "An advanced recipe for chocolate and vanilla swirled cookies. It's a bit stained."
    "image" : "checkerboard_cookies.png"
}
define pudding = {
    "name" : "Pudding",
    "description" : "A recipe for Japanese-style pudding. You can only dream of what it tastes like."
    "image" : "pudding.png"
}

# Cincere
define godzilla = {
    "name" : "Godzilla (1954)"
    "description" : "The original Japanese-language monster movie. You can't get that distinctive roar out of your head."
    "image" : "godzilla.png"
}
define dos_monjes = {
    "name" : "Dos Monjes (1934)"
    "description" : "An intense, Mexican melodrama about two monks who share a dark secret. It's a thrilling and mysterious film."
    "image" : "dos_monjes.png"
}
define handmaiden = {
    "name" : "The Handmaiden (2016)"
    "description" : "A mixed-language psychological thriller set during Japanese occupation of Korea. Cincere seems to prefer foreign language films."
    "image" : "handmaiden.png"
}

# Muse
define sense = {
    "name" : "Sense and Sensibility (1811)"
    "description" : "English author Jane Austen's first published novel. A romantic tale of love, loss, and relationships with gothic elements."
    "image" : "sense.png"
}
define dracula = {
    "name" : "Dracula (1897)"
    "description" : "A gothic horror novel by Irish author Bram Stoker."
    "image" : "dracula.png"
}
define tell_tale_heart = { 
    "name" : "The Tell-Tale Heart (1843)"
    "description" : "American gothic poet Edgar Allan Poe's famous short story. Come to think of it, is Muse into gothic stuff? She only ever wears black."
    "image" : "tell_tale_heart.png"
}

# Ghost
define love_letter = { 
    "name" : "Love Letter"
    "description" : "A crumpled, old love letter found in the film studies classroom. The handwriting is faint but filled with emotion."
    "image" : "love_letter.png"
}
define locket = {
    "name" : "Locket"
    "description" : "A mysterious locket with a torn photo of a handsome young man. Based on his attire, the photo was probably taken in the 1950s."
    "image" : "locket.png"
}
define class_ring = {
    "name" : "Class Ring"
    "description" : "A worn, old ring with the initial 'F' engraved into it along with the numbers '1959.'"
    "image" : "class_ring.png"
}
#  ---------------------------------------------------- Point System ---------------------------------------------------------------------------------------

# Romance Points (RP)
default a_points = 0 # ame points
default c_points = 0 # cincere points
default m_points = 0 # muse points

# Ghost Points (GP)
default g_points = 0 # ghost points


#  ---------------------------------------------------- Game Start ------------------------------------------------------------------------------------------


# Day 1 ------------------------------------------------------------------------------------------------------------------------------------------------------

label start:

    scene black
    with dissolve
    play music birds
    f "Hoping that extra beauty sleep will win her affection?"
    p "I feel like I died during that nap. I can't even remember my name..."
    $ p = renpy.input("Enter your name.")
    play music door noloop

    scene bg dorm
    with fade
    show frog_teasing
    with dissolve
    f "Your name is [p]."
    f "You go to Deez Nuts University and you have a class in like twenty minutes."
    play music startled noloop
    f "Ha! Your little crush isn't going to like you back if you show up looking like you just rolled out of bed."
    show frog_sad
    with dissolve
    f "Plus, if Ghost Girl catches you alone, you might become her next target."
    p "You know I don't believe in that stuff."
    f "Still, better safe than sorry."
    p "I guess your right."
    show frog_neutral
    with fade
    "You roll out of bed and start getting dressed."

    call screen dress_up
    "You've selected a [mc_shirt]."
    "After getting dressed as quickly as possible, you head to class."
    jump classroom

label classroom:

    scene bg classroom
    with fade
    "To your surprise. you arrive to class a few minutes early."
    "Cincere isn't in her usual spot behind you, but you notice a crumpled, yellow piece of paper on her desk."
    menu:
        "Read the paper.":
            $ g_points += 1
            jump find_love_letter
        "Leave the paper alone.":
            jump continue_to_class

label find_love_letter:

    $ add_to_inventory("Ghost", "images/love_letter.png")
    show screen inventory_screen # Display updated inventory
    jump continue_to_class

label continue_to_class:

    "The projector whirs as your professor prepares to start class."
    "You notice that your crush, Cincere is running late today..."
    "It couldn't be she was Ghost Girl's next target, could it?
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
    play music notebook_tear noloop
    p "Here... is one page enough?"
    "Your professor's voice booms:"
    "That's enough talking in my class!"

    scene bg classroom
    with fade
    "Some time passes, and a carefully folded note flies over your shoulder.
    "You open the note and it says..."
    play music notebook_crumple noloop
    "Your shirt is on inside out, and it's distracting me from the movie."
    "You look down at your shirt, and the seams are indeed facing outward."
    "After class, you go back to your dorm to change."
    play music disappointed noloop

    scene bg dorm
    with fade
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
    p "Maybe it's not too late to drop this class..."
    p "No. I promised myself I would stick it out."
    p "I'll go to the cafe for a pick-me-up."
    jump cafe

label cafe:

    scene bg cafe
    with fade
    "A barista appears behind the counter."
    show ame_frazzled
    with dissolve
    play music pensive noloop
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
    play music startled noloop
    "The barista hands you your coffee and you notice some writing on the cup."
    p "Oh uhm..."
    show ame happy at right
    with dissolve

    scene bg cafe
    with fade
    "The barista goes to help another customer, but you notice the note she's written on your cup:"
    play music success noloop
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
    "The entire library is full of students this afternoon"
    play music chatter
    "You look around and notice the girl at the table nearest you has moved her backpack from the seat. She's moving her things around to make room."
    p "She must have noticed my vulturing..."
    p "My winning streak of first impressions is going strong. 
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
    m "I'm shy."
    m "Sorry, I mean Muse." 
    m "My name is Muse."
    jump muse

label muse:

    scene bg library
    with fade
    "After that, you both study at the same table for a while."
    "To your surprise, the silence doesn't feel awkward, but actually kind of...nice."
    "The girl leaves first, and you don't look up from your books until she's gone."
    "When you do, you notice she left you a small note: "
    m "If you come a little earlier tomorrow, we can chat a little before studying."
    "You think of all the notes you've received today and decide that her neat, precise handwriting is the prettiest."
    "Maybe you will try to see her again tomorrow..."
    g "I'd love to see you again tomorrow too."
    play music startled
    "You could have sworn Muse had left already."
    "You look up, but don't see anyone..."
    "It must have been your imagination."
    "You get up and head back to your dorm."

    scene bg dorm
    with fade
    play music door noloop
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
    play music startled noloop
    p "Are you kidding? I don't have a chance in hell with any of them!"
    show frog_teasing at right
    with dissolve
    f "You're quite the catch, [p]! I'm sure any one of them would be lucky to be your girlfriend..."
    f "Besides, I bet they don't want to run into Ghost Girl either..."
    f "Everyone knows the safest way to avoid her is to cuff it up."
    play music disappointed noloop
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
    play music moon1
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
        "I barely know any of them!"
            $ g_points += 1
            jump day_1_end

label cincere_reflection_1:

    pass # a short reflection of the MC's thoughts on Cincere
    jump day_1_end

label ame_reflection_1:

    pass # a short reflection of the MC's thoughts on Ame
    jump day_1_end

label muse_reflection_1:

    pass # a short reflection of the MC's thoughts on Muse
    jump day_1_end

label day_1_end:

    "Frog acknowledges your response with a disinterested 'hm.'"
    "Thinking about it makes your head hurt, so you close your eyes."
    scene black
    with fade

# Day 2 -------------------------------------------------------------------------------------------------------------------------------------------------------------

label day_2:

    scene bg dorm
    with fade
    play music birds noloop
    p "Ugh, I slept through dinner again."
    "You hear Frog snoring in the bunk beside yours, so you take a glance at your watch to check the time."
    "It's early for a change... 7am"
    play music stomach_growl noloop
    "Breakfast doesn't start for another hour..."
    "You decide to head to the cafe in the student union."

    scene bg cafe
    with fade
    play music startled noloop
    show cincere_neutral
    with dissolve
    "Lucky for you, you notice Cincere sitting pensively at one of the cafe tables..."
    "She looks totally absorbed in something..."
    menu:
        "Leave Cincere alone.":
            pass
        "Call out to her.":
            $ c_points += 1
            pass
    "She spots you first."
    show cincere_happy
    with dissolve
    c "Oh! Hey, you."
    "She waves you over to her table."
    "You walk over as nonchalantly as possible."
    p "Hey Cincere, mind if I sit with you?"
    "You notice dark circles under her eyes and the fact that she's... drawing? something over and over again."
    c "That's why I invited you over here."
    show cincere neutral
    with dissolve
    c "I actually wanted to talk to you about something..."
    "She pulls out the chair beside her, and you take a seat."
    "You glance at the papers Cincere has been drawing on, but can't make sense of her scribbles."
    c "It's about Ghost Girl."
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
    c "Not as frightened as I'm going to be if I don't get to class."
    c "Here, I made these as handouts, but you can have one because I like you."
    "Your heart skips a beat as she hands you a piece of paper - a movie poster?"
    $ add_to_inventory("Cincere", "images/godzilla.png")
    show screen inventory_screen # Display updated inventory
    jump cafe_continue

label cafe_continue:

    "You reach out to squeeze Cincere's hand."
    "Her hand is a bit larger than yours, but a million times softer, and it smells... sweet. Like honey and oatmeal."
    "You notice Cincere's breakfast of oatmeal with honey and a black coffee."
    play music stomach_growl noloop
    show cincere neutral
    with dissolve
    c "Are you hungry?"
    p "I'm starving."
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
    play music chatter noloop
    "You order an apple turnover with a simple latte but..."
    "...You forgot to ask for dairy-free milk."
    "You make to cancel your order when the beautiful barista from yesterday - Ame - appears."
    show ame frazzled
    with dissolve
    a "I'm sorry for being late! I'll take it from here, boss."
    "You didn't realize the person who initially took your order was The Manager'\u2122'." #unicode trademark (TM) symbol
    "To your surprise, The Manager'\u2122' shrugs it off." #unicode trademark (TM) symbol
    show manager_neutral
    with dissolve
    play music moon2 noloop
    n "It happens." 
    n "That apple turnover has been selling really well..."
    n "I want you to think about what pastry we can sell for the upcoming winter season too."
    n "Here." 
    "He hands Ame a piece of paper - your order - and then turns to leave."
    n "I'll be in the office if you run into any...he looks you up and down... trouble."
    "You want to reply in a cool manner, but what comes out is..."
    play moon2
    menu:
        p "Oh, I'm no trouble, boss. I-I mean sir!": 
            a_points += 1
            pass 
        p "...":
            pass
    "You raise your hand as if to salute, but put it down when you realize The Manager'\u2122' has a peg leg." #unicode trademark (TM) symbol
    "What if he really was in the military?"
    "Would it be disrespectful to salute?"
    "To your relief, The Manager'\u2122' grunts and walks away." #unicode trademark (TM) symbol
    "As soon as The Manager'\u2122' leaves, you can't help but ask Ame if she baked the apple turnovers you've been eyeing." #unicode trademark (TM) symbol
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
    play moon2 
    menu:
        p "I'm jealous of anyone who gets to try your baking.":
            a_points += 1
            jump recipe_1
        p "Haunted? You believe in that stuff?":
            g_points += 1
            jump haunted

label recipe_1:

    a "In that case..."
    a "Here."
    "She hands you a piece of paper with some writing on it."
    a "It's one of my own personal recipes."
    "You try not to squint as she positively beams at you."
    $ add_to_inventory("Ame", "images/strawberry_roll_cake.png")
    show screen inventory_screen # Display updated inventory
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
    play music success noloop
    a "But you know what? If you come here tomorrow, [p], I'll give you a treat."
    "She winks at you, and you feel your chest melt."
    "You head back to your dorm, grinning the whole way."
    jump day_2_end

label library_day_2:

    scene bg library
    with fade
    play music startled noloop
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
    "You could listen to her laugh forever."
    m "Sorry, but, what was your name again?"
    p "It's [p]."
    m "I couldn't say it yesterday, but n-nice to meet you, [p]!"
    p "Um, nice to meet you too, Muse."
    m "Are you here studying today, too?"
    p "Oh, I was just trying to kill time before the dining hall opens..."
    p "Speaking of..."
    menu:
        "What are you studying? It seems intense."
            jump studying
        "Do you maybe want to get breakfast with me today?"
            $m_points += 1
            jump breakfast

label studying:

    "Muse gestures at the pile of books on the table, and her eyes light up."
    show muse happy
    with dissolve
    m "It's for an exhibition! We're showcasing student life on campus. I'm looking at old yearbooks, that kind of thing. Trying to decide what to highlight."
    p "Wow, that's really cool, Muse. You work at a museum?"
    m "Yes! I'm thinking about showcasing one of my favorite short stories, but, I'm not sure if it matches the theme."
    p "What are you thinking?"
    m "Tell-Tale Heart, of course!"
    play music dissapointed noloop
    "It saddens you that you've never heard of it."
    play music moon3
    menu:
        "What's Tell-Tale Heart?":
            jump find_book_1
        "Why do you think it doesn't match the theme?":
            jump haunted_museum

label find_book_1:

    show muse_full
    with dissolve
    m "you've never heard of it?!"
    "She starts rummaging in her backpack."
    m "Here, I actually have a copy of it if you want to borrow it."
    $ add_to_inventory("Muse", "images/tell_tale_heart.png")
    show screen inventory_screen # Display updated inventory
    jump museum

label haunted_museum:

    m "Well..."
    m "It's supposed to be regarding student life, but..."
    m "I just can't help but think of Ghost Girl and how her hauntings are like..."
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
        m "Th-th-thanks for asking! If it was another time, I'd say yes, but I just can't right now with the exhibition coming up."
        play music disappointed noloop
        p "Exhibition?"
        jump museum

label museum: 

    p "I'm really impressed, Muse."
    p "You work at a museum?"
    show muse_happy
    with dissolve
    m "Yep! The one right here on campus. Actually...nevermind."
    play moon3
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
    play music startled noloop
    p "Y-y-yeah!"
    "You pull your phone from out of your pocket and hand it to Muse."
    "When she gives it back to you with her contact, you notice she put a heart at the end of her name."
    p "Is it okay for me to think this is going well?"
    "Muse laughs."
    play music stomach_growl noloop
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
    play moon4
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
    play music birds noloop
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
                $ add_to_inventory("Ghost", "images/locket.png")
                show screen inventory_screen # Display updated inventory
                "You don't recognize it, but you pocket it and make a mental note to give it to Cincere."
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
    menu:
        "Oh, how old are you?!":
            c_points += 1
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
    $ add_to_inventory("Cincere", "images/handmaiden.png")
    show screen inventory_screen # Display updated inventory
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
    play moon3
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
    $ add_to_inventory("Muse", "sense.png")
    show screen inventory_screen # Display updated inventory
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
        "Oh, sorry. Tomorrow morning, I can't."
            $ a_points += 1 
            jump muse_no
        "Of course, Muse. I always look forward to seeing you here at the library."
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
    play music moon2 
        menu: 
            "Apologize.":
                jump cafe_day_3_end
            "Ask what's on her mind.":
                a_points += 1 
                jump find_recipe_2

label find_recipe_2:

    p "Is there something bothering you?"
    "Ame swallows."
    a "Honestly, yeah..."
    "She leans closer to you over the counter."
    "You can smell coffee on her breath."
    a "Actually, here:"
    $ add_to_inventory("Ame", "images/checkerboard_cookies.png")
    show screen inventory_screen # Display updated inventory
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
    play music ticking noloop
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
    play music texting noloop
    a "And, done!"
    a "It's been a long day, so I'm going to head home now. See you later?"
    p "Yeah, see you later."
    "You gather the crumbs and foil, throw them out, and head back to your dorm."
    
    scene bg messenger_app
    with fade
    "On your way there, you get a text notification."
    play music ping noloop
    "It's from Ame, and it reads:"
    play music texting
    a "I know this is sudden, and kind of last minute, but, do you want to have a picnic date with me this Friday?"
    a "I'll bring a cheeseplate, and it will be chill. Just let me know by noon on Friday and...do me a favor?"
    a "Don't come to see me at work until you've decided whether you can make the picnic or not..."
    a "Otherwise... my heart just can't take it!"
    play music moon2 noloop
    menu: 
        "Reply with a flirt.":
            jump day_3_end
        "Reply with a joke.":
            a_points += 1 
            jump day_3_end


label day_3_end:
    p "Who knew you could be so...cheesy :x"
    "Ame replies before you make it back to your dorm:"
    a "guh stopppp"
    scene bg dorm
    with fade
    "You lie on your bunk bed grinning in spite of yourself."
    play music door noloop
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

    pass # a short reflection of the MC's thoughts on Cincere
    jump day_4

label ame_reflection_3:

    pass # a short reflection of the MC's thoughts on Ame
    jump day_4

label muse_reflection_3:

    pass # a short reflection of the MC's thoughts on Muse
    jump day_4

# Day 4 -----------------------------------------------------------------------------------------------------------------------------------------------------------------

label day_4:

    scene black
    with fade
    play music ping noloop

    scene bg messenger_app
    with fade
    play music texting
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
                c_points += 1
                jump classroom_day_4
            "Head to the library to see Muse.":
                m_points += 1
                jump library_day_4

label classroom_day_4:

    scene bg classroom
    with fade
    play music moon5
    "It's a bit chillier in here than usual."
    "You notice a movie poster near Cincere's usualy seat, so you take a peak."
    $ add_to_inventory("Cincere", "images/dos_monjes.png")
    show screen inventory_screen # Display updated inventory
    "Cincere doesn't seem to be here, so you head to the library."
    jump library_day_4

library_day_4:

    scene library bg
    with fade
    play music startled noloop
    "You're surprised to see Cincere in the spot where Muse usually sits."
    show cincere_neutral
    with dissolve
    "You jump on the chance to speak with her."
    p "Cincere! I wasn't expecting to see you at the library."
    "Somehow, she looks even more tired than yesterday."
    c "Oh, do you remember me?"
    p "I just saw you in class yesterday?"
    c "Oh, that's right."
    "She seems distant."
    c "Sorry, I'm a little out of it today."
    play music notebook_tear noloop
    "She slides you a note - no - a flyer."
    c "It's for an event tomorrow afternoon at the Student Union"
    "She's signed it with her phone number and a note - "
    c "Let me know by tonight if you want to my short film premier."
    "When you put the note away, she's already gone."

    scene bg library
    with fade
    p "She seems to be constantly disappearing lately..."
    "Is she...avoiding you?"
    show muse_happy
    with dissolve
    m "You came!"
    p "I like to stick to my word."
    m "That's great. I love that in a partner."
    "Muse is coming on strong today."
    show muse muse_full
    with dissolve
    m "Um, I, I wanted to know!"
    m "Will you come to my exhibit tomorrow?"
    play moon3
    menu:
        "For sure, Muse. I wouldn't miss it for the world.":
        m_points +=1
        jump muse_reflection_4
        "Actually, I'm busy tomorrow.":
        c_points +=1
        jump cincere_reflection_4
        "Sorry. I'm going on a date tomorrow."
        a_points += 1
        jump ame_reflection_4

label cincere_reflection_4:

    "I promised a friend I'd go to her short film premier"
    jump day_4_end

label ame_reflection_4:

    "I actually met someone."
    jump day_4_end

label muse_reflection_4:

    "You thought Muse would be happy, but her thoughts are elsewhere."
    jump day_4_end

label day_4_end:    

    show muse_sad at right
    with dissolve
    "She doesn't acknowledge your answer..."
    m "You don't have to answer me now..." 
    m "Just text me at the end of the day with your decision."
    m "I don't remember if I gave you my number, so let me see your phone."
    "You pull your cell phone out of your pocket and hand it to Muse."
    play music texting noloop
    "Muse hands your phone back to you."
    "On your way back to your dorm, you realize that all three of the girls you were interested in asked you to go on a date tomorrow."
    "And they all want your answer by tonight..."

# Final Day -------------------------------------------------------------------------------------------------------------------------------------------------------------
label final_day: 

    pass # Want to continue the narrative here but change some plot elements including introduce Faith (Ghost Girl)
    scene black
    with fade
    "You have Film Studies today, and with it a chance to see Cincere."
    call screen dress_up
    "You linger in the mirror a bit longer than usual, but decide that you look just as handsome as ever in your [mc_shirt]."

    scene bg classroom
    with fade
    "You look around, but Cincere is nowhere in sight."
    "You know it's not really your business, but you can't help it:"
        menu:
            "Ask your professor about Cincere's absence":
                c_points += 1 
            "Wait until after class to ask your professor about Cincere":
                pass
    "To start the class, your professor begins with an unusual announcement."
    "On the projection screen is the same flyer Cincere handed you yesterday."
    "Your professor continues: "
    "'I'm sure some of you noticed that our class is not as full today...'"
    "'And, no, it's not because it's Friday.'"
    "'It's because we have some excellent students this year showcasing their short films at the Student Film Festival later this afternoon.'"
    "'It's at the Student Center, so be sure to show your support for your fellow classmates, like our very own Cincere, if you're available.'" 
    "'I implore you to participate in any of the student events taking place today to kick of Student Week.'"
    "'That's all for today. Class dismissed.'"
    play music disappointed noloop
    "With no class and no Cincere, you head back to your dorm"

    scene bg dorm
    with fade
    "It's Student Week huh..."
    "So that's why everyone had something to do this afternoon."
    "Come to think of it, shouldn't you reply to Cincere, Ame, and Muse?"
    "You open your messaging app."
        
    scene bg messenger_app
    with fade
    "You reply with a simple 'yes' to the date with..."
    # If all ghost-related items are collected, activate the Faith route

    label check_ghost_route:

    pass # Continue the narrative here... 
    if inventory["Ghost Item 1"] and inventory["Ghost Item 2"] and inventory:  # Add all ghost items
        $ ghost_route_unlocked = True
        "You feel an eerie presence, and suddenly Ghost Girl appears..."
        jump ghostRoute
    else:
        jump standard_route  # If items aren't collected, go back to a default route

label standard_route:

    menu:
        "Cincere":
            jump cincereRoute
        "Ame":
            jump ameRoute
        "Muse":
            jump museRoute
# Ghost Route ---------------------------------------------------------------------------------------------------------------------------------------------------------------

label ghostRoute:

    pass
    "As the story unfolds, you learn that her name was Faith, a girl whose love story met a tragic end."
    $ inventory["Faith"] = True
    $ inventory["Ghost"] = False
    # Proceed with additional Faith story content here

# Cincere Route -------------------------------------------------------------------------------------------------------------------------------------------------------------
label cincereRoute:

    "You can't bear to face Ame or Muse so you reject them over text."
    play music "ping.mp3"
    $ if m_points > 5:
        "Muse sends you a smiley face and says not to worry about it. Mid-terms are coming up, so you know where to find her."
        else:
            "Muse sends you a sad face and you never hear from her again."
    play music "ping.mp3"
    $ if a_points > 5:
        "Ame says she understands, and she asks if you two can stay friends."
        else: 
            "Ame replies that she's busy with work anyway and doesn't have time for frivolous dates."

    scene bg dorm
    with fade
    "Now you can focus on your date with Cincere with a clear conscience."
    "You dress your best and head to the Student Union."

    scene bg student_union
    with fade
    show cincere date smile
    with dissolve
    "You're blown away by how HOT Cincere looks, but you can't help but notice the somehow even darker circlers beneath her eyes."
    "She laughs it off..."
    c "I've been pulling all nighters trying to work in a scene for my short film this afternoon."
    c "Thanks, by the way."
    "You're confused, but you reply anyway:"
        menu:
            "What for?":
            "Oh, am I finally getting my pen back?":
                $ c_points += 1 
    "Cincere laughs before she responds."
    c "I'll tell you after! The film is about to start!"

    scene black
    with fade

    scene bg seed
    with dissolve

    show bg sprout
    with dissolve 

    scene bg flower
    with dissolve

    scene black
    with fade

    play music "applause.mp3"

    scene bg union
    with fade
    "Cincere turns to look at you, pride smeared across her face."
    show cincere smile
    with dissolve
    c "So, what did you think?"
    p "I think your all-nighters really paid off!"
    $ if c_points <= 5:
        c "Actually, this is just the original."
        p "So, you didn't use any of your edits from this week?"
        c "That's right, I didn't"
        p "Isn't that..."
        p "Kind of a waste?"
        c "I don't think so..."
        c "I learned a lot still, and I'm grateful for that."
        p "I'm grateful too. Grateful I got to meet you, Cincere."
        p "And grateful you invited me to this event..."
        p "I hope I don't have the wrong idea but..."
        p "Is it okay if I think of this as a date?"
        play music "startled.mp3"
        show cincere sad
        with dissolve
        c "Even though I think you're cute and I have fun talking with you..."
        c "I'm just too busy with school to date anyone right now."
        c "Thanks for this, by the way."
        "She hands back the pen she borrowed from you on Monday, and you don't say anything more than 'hello' to each other after that."

        scene black
        with fade
        play music "disappointed.mp3"	
        "{b}Bad Ending{/b}"
        return
            else: 
                c "Thanks!"
                c "You actually inspired me to put a little more care into my work."
                c "You probably don't remember but..."
                c "One time, I fell asleep on the bus and someone tried to steal my camera bag."
                c "I was barely awake, but I remember you walking up to the thief and loudly thanking them for looking after my camera."
                c "No one has ever really looked out for me that way before, let alone a stranger."
                show cincere date happy
                with dissolve
                c "Ever since then, I've basically had a crush on you [p]."
                p "No way! I didn't realize that was you."
                "Cincere laughs."
                c "I've changed my look quite a bit since then, so I don't blame you."
                p "Haha I'm glad."
                p "So, is it alright if I think of this as a date?"
                c "Yes, you dork. Hopefully the first of many?"
                p "The first of many it is."
                jump ending_twist

label ending_twist:
    "As you spend time with [love_interest], they reveal a funny secret."
    "[love_interest] \"I have to admit, Ame, Muse, and I had a little wager on who you'd end up with.\""
    "[love_interest] \"Looks like I won, and I get to date you!\"

    scene black
    with fade
    play music success noloop	
    "{b}Good Ending{/b}"
    return
# Ame Route -------------------------------------------------------------------------------------------------------------------------------------------------------------              
label ameRoute:
    "You can't bear to face Cincere or Muse so you reject them over text."
    play music "ping.mp3"
    $ if m_points > 5:
        "Muse sends you a smiley face and says not to worry about it. Mid-terms are coming up, so you know where to find her."
        else:
            "Muse sends you a sad face and you never hear from her again."
        play music "ping.mp3"
    $ if c_points > 5:
            "Cincere says she's dissapointed, but she gets it." 
            "She wanted to show you a film she's been working on, but she'll save it for another time."
            "She tells you to enjoy your date, and that she'll see you in class."
        else: 
            "Cincere says she feels kind of silly since she just assumed you were single this whole time."
            "You reply that you were single until just a few hours ago and the last text you get from her reads:"
            c "I guess I just didn't make the final cut then."
            "You try to reply that you're sorry and you will see her in class but..."
            play music disappointed noloop
            "The message fails to send, and she's already blocked your number."

    scene bg dorm
    with fade
    "Now you can focus on your date with Ame with a clear conscience."
    "You decide to go straight to the cafe to see Ame."

    scene bg cafe
    with fade
    "But she's not working and you feel like an idiot."
    "You send her a text:"

    scene bg messenger_app
    with fade
    p "Bad news. I went all the way to the cafe only to discover that you don't have work today!"
    a "Pro tip: Do NOT start conversations with 'bad news'! MY HEART CANNOT TODAY ;_;"
    p "Good news. I made the bus to Megman's and should be back in time with some fancy cheese to accompany our charcuterie tonight."
    a ":)))))))))))) Good news indeed~"
    a "I just finished my hair, so be prepared for a slay."
    p "You always slay tho??"
    a "BYE you've only seen me in my uniform."
    a "For all you know, I could be bald under that hat."
    p "..."
    p "Are you??"
    a "I guess you'll see for yourself later today~"

    scene bg picnic
    with fade
    show ame date smile
    with dissolve
    "You look dumb with your mouth open, gaping unabashedly at the gorgeous woman in front of you."
    p "This is like...the difference between Clark Kent and Superman. A Kryptonian slay."
    a "So you like what you see?"
    p "Actually..."
    p "I was secretly hoping you were bald."
    show ame date frazzled
    with dissolve
    a "Wait, huh?"
    play music "happy.mp3"
    p "Haha, I'm only teasing. You look stunning. If only these clouds would go away, the scene would be complete."
    show ame data happy
    with dissolve
    a "If we ignore them, maybe they will go away."
    "Ame pulls out a blanket and lays it on the grass."
    "The picnic basket is just a little cooler, and to your surprise, she pulls out a bottle of wine."
    play music "startled.mp3"
    p "Have you been 21 this whole time?!"
    a "Not until next spring, but living with your parents has its benefits."
    p "Oh, I see. So..."
    p "What are your parents like?"
    a "Well...they're older so they're not super active."
    a "But they're really supportive of me and they even rennovated our kitchen a few years ago when I told them I wanted to fo to school and become a full blown pâtissier."
    p "That's incredible! I didn't know you were going down that path, but it totally suits you."
    p "I can picture you already with a poofy hat, all dressed in white."
    show ame date happy
    with dissolve
    a "Can you really? I'd definitely need some color in my chef's uniform."
    a "At first, I was really happy to learn my parents took my dream so seriously but..."
    a "When I asked them how they could afford the rennovations I learned that they took out a second mortgage to pay for it all."
    play music "pensive.mp3"
    p "That must have been bittersweet news..."
    show ame date neutral
    with dissolve
    a "Yes, exactly!"
    a "It made me realize that they would probably do something similar to help me pay for culinary school..."
    a "I love how supportive they are, but I don't want to be even more of a burden on them so..."
    a "I decided to pay my own way through school and I've been working as much as I can to save up for tuition!"
    p "You're an incredible person you know?"
    p "Not everyone would be as considerate to their parents..."
    p "It sounds like they really love you and want to see you happy doing something you love."
    show ame date blushing
    with dissolve
    p "Sorry! I wouldn't be able to rest knowing you might think you're a burden to anyone."
    p "It's just not true and it could never be true!"
    a "..."
    p "Maybe I said too much."
    show ame date happy
    with dissolve
    a "No, not at all."
    a "I guess on some level, everything you said I already knew, but..."
    a "It feels really good to hear it from someone else."
    a "Thank you."
    play music "rain.mp3"
    "It starts to pour and you both pack up the picnic as quickly as you can and run for cover under a bus stop."
    "Neither of you can stop laughing about the ruined picnic."

    scene bg rainy_bus_stop
    with fade
    p "Can we wash the rain off the cheese or is that dumb?"
    show ame date happy
    with dissolve
    a "Please, I'm going to cry or pee my pants. My stomach hurts."
    p "Mine too, I'm so hungry."
    "When the giggles die down, you look at her and she looks at you."
    "You're not thinking and that's perfect."
    "You decide to take a chance."
    p "Do you...want to dry off at my place?"
    show ame date blushing
    with dissolve
    $ if a_points <= 5:
        a "In your dreams."
        scene black
        with fade
        play music disappointed noloop
        "{b}Bad Ending{/b}"
        return
        else:
            a "Yeah, I'd like that."
            scene black
            with fade
            play music "success.mp3"
            "{b}Good Ending{/b}"
            return

# Muse Route -------------------------------------------------------------------------------------------------------------------------------------------------------------
label museRoute: 

    "You can't bear to face Cincere or Ame so you reject them over text."
    play music "ping.mp3"
    $ if a_points > 5:
            "Ame says she understands, and she asks if you two can stay friends."
        else: 
            "Ame replies that she's busy with work anyway and doesn't have time for frivolous dates."
    play music ping noloop
        $ if c_points > 5:
            "Cincere says she's dissapointed, but she gets it." 
            "She wanted to show you a film she's been working on, but she'll save it for another time."
            "She tells you to enjoy your date, and that she'll see you in class."
            else: 
                "Cincere says she feels kind of silly since she just assumed you were single this whole time."
                "You reply that you were single until just a few hours ago and the last text you get from her reads:"
                c "I guess I just didn't make the final cut then."
                "You try to reply that you're sorry and you will see her in class but..."
                play music "error.mp3"
                "The message fails to send, and she's already blocked your number."

    scene bg dorm
    with fade
    "Now you can focus on your date with Muse with a clear conscience."
    "You decide to go straight to the Student Center to see Muse."
    $ if m_points <= 5:
        show museum bg
        with fade
        "Muse is making her way towards you"
        play "shuffling_museum_noises.mp3"
        show muse smile
        with dissolve
        m "You came just in time for the tour!"
        "Muse addresses the group of 4-6 people who showed up for the tour"
        m "Let's begin shall we!"
        "She goes through the evolution of the dormitories, the cultural houses, and eventually lands on the student library."
        m "The library used to me my favorite place but..."
        "She looks in your direction..."
        show muse sad
        with dissolve
        "I don't think I'll be heading back there anytime soon."

        scene black
        with fade
        "{b}Bad Ending{/b}"
        return
        else:
            show museum bg
            with fade
            "Muse is making her way towards you"
            "She looks especially cute today."
            show muse date smile
            with dissolve
            m "You came just in time for the tour!"
            "You look around, but you notice you're the only one here."
            m "I didn't think many people would come, but I'm glad you showed up!"
            p "I wouldn't miss this for the world. You've worked so hard after all."
            "Muse giggles."
            m "I have! You know..."
            m "Since you're the only one here...isn't this sort of like a date?"
            play music success noloop
            "Muse reaches for your hand."
            "She has no intention of letting go."
            "{b}Good Ending{/b}"
            return
#  ---------------------------------------------------- Game End ------------------------------------------------------------------------------------------

