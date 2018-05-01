#MFLL script!

image park = im.FactorScale("images/park.png", 1.5)
image date = im.FactorScale("images/date.png", 1.5)
image park2 = im.FactorScale("images/park2.png", 1.5)

#piercings
image chin:
        choice (chin == True):
                im.FactorScale("images/piercings/chin.png", .45)
        choice (chin == False):
                im.FactorScale("images/blanc.png", .45)
image cuffs:
        choice (cuffs == True):
                im.FactorScale("images/piercings/cuffs.png", .45)
        choice (cuffs == False):
                im.FactorScale("images/blanc.png", .45)
image ears:
        choice (ears == True):
                im.FactorScale("images/piercings/ears.png", .45)
        choice (ears == False):
                im.FactorScale("images/blanc.png", .45)
image nose:
        choice (nose == True):
                im.FactorScale("images/piercings/nose.png", .45)
        choice (nose == False):
                im.FactorScale("images/blanc.png", .45)
image snakebites:
        choice (snakebites == True):
                im.FactorScale("images/piercings/snakebites.png", .45)
        choice (snakebites == False):
                im.FactorScale("images/blanc.png", .45)

image clothes:
        choice (clothes == 1):
                im.FactorScale("images/clothes/basican.png", .45)
        choice (clothes == 2):
                im.FactorScale("images/clothes/basicfem.png", .45)
        choice (clothes == 3):
                im.FactorScale("images/clothes/basicmasc.png", .45)
        choice (clothes == 4):
                im.FactorScale("images/clothes/prepan.png", .45)
        choice (clothes == 5):
                im.FactorScale("images/clothes/prepfem.png", .45)
        choice (clothes == 6):
                im.FactorScale("images/clothes/prepmasc.png", .45)
        choice (clothes == 7):
                im.FactorScale("images/clothes/punkan.png", .45)
        choice (clothes == 8):
                im.FactorScale("images/clothes/punkfem.png", .45)
        choice (clothes == 9):
                im.FactorScale("images/clothes/punkmasc.png", .45)

image hair:
        choice (hair == 1):
                im.FactorScale("images/hair/curly1.png", .45)
        choice (hair == 2):
                im.FactorScale("images/hair/curly2.png", .45)
        choice (hair == 3):
                im.FactorScale("images/hair/newage1.png", .45)
        choice (hair == 4):
                im.FactorScale("images/hair/newage2.png", .45)
        choice (hair == 5):
                im.FactorScale("images/hair/punk1.png", .45)
        choice (hair == 6):
                im.FactorScale("images/hair/punk2.png", .45)
        choice (hair == 7):
                im.FactorScale("images/hair/straight1.png", .45)
        choice (hair == 8):
                im.FactorScale("images/hair/straight2.png", .45)

image makeup:
        choice (makeup == 1):
                im.FactorScale("images/makeup/gold.png", .45)
        choice (makeup == 2):
                im.FactorScale("images/makeup/green.png", .45)
        choice (makeup == 3):
                im.FactorScale("images/makeup/pink.png", .45)
        choice (makeup == 4):
                im.FactorScale("images/makeup/purple.png", .45)
        choice (makeup == 5):
                im.FactorScale("images/blanc.png", .45)

image body:
        choice (body == 1):
                im.FactorScale("images/body/anbod/1.png", .45)
        choice (body == 2):
                im.FactorScale("images/body/anbod/2.png", .45)
        choice (body == 3):
                im.FactorScale("images/body/anbod/3.png", .45)
        choice (body == 4):
                im.FactorScale("images/body/anbod/4.png", .45)
        choice (body == 5):
                im.FactorScale("images/body/anbod/5.png", .45)
        choice (body == 6):
                im.FactorScale("images/body/anbod/6.png", .45)
        choice (body == 7):
                im.FactorScale("images/body/anbod/7.png", .45)
        choice (body == 8):
                im.FactorScale("images/body/fembod/1.png", .45)
        choice (body == 9):
                im.FactorScale("images/body/fembod/2.png", .45)
        choice (body == 10):
                im.FactorScale("images/body/fembod/3.png", .45)
        choice (body == 11):
                im.FactorScale("images/body/fembod/4.png", .45)
        choice (body == 12):
                im.FactorScale("images/body/fembod/5.png", .45)
        choice (body == 13):
                im.FactorScale("images/body/fembod/6.png", .45)
        choice (body == 14):
                im.FactorScale("images/body/fembod/7.png", .45)
        choice (body == 15):
                im.FactorScale("images/body/mascbod/1.png", .45)
        choice (body == 16):
                im.FactorScale("images/body/mascbod/2.png", .45)
        choice (body == 17):
                im.FactorScale("images/body/mascbod/3.png", .45)
        choice (body == 18):
                im.FactorScale("images/body/mascbod/4.png", .45)
        choice (body == 19):
                im.FactorScale("images/body/mascbod/5.png", .45)
        choice (body == 20):
                im.FactorScale("images/body/mascbod/6.png", .45)
        choice (body == 21):
                im.FactorScale("images/body/mascbod/7.png", .45)

image tillie = im.FactorScale("images/npcs/tillie.png", .45)
image tristan = im.FactorScale("images/npcs/tristan.png", .45)
image taren = im.FactorScale("images/npcs/taren.png", .45)
image fleck = im.FactorScale("images/npcs/fleck.png", .45)

image side tillieside = im.FactorScale("images/npcs/tillieside.png", 0.49)
image side tristanside = im.FactorScale("images/npcs/tristanside.png", 0.49)
image side tarenside = im.FactorScale("images/npcs/tarenside.png", 0.49)
image side fleckside = im.FactorScale("images/npcs/fleckside.png", 0.49)


define y = DynamicCharacter("you", first_indent = 50 , size = 32 , color = "#FFF" , outlines = [(3, "#4D3E3E", 0, 0),  (2, "#1FC527", 0, 0),  (1, "#0E5611", 0, 0) ])
define f = Character("Tillie", image = "tillieside" , first_indent = 50 , size = 32 , color = "#FFF" , outlines = [(3, "#4D3E3E", 0, 0),  (2, "#FF9696", 0, 0),  (1, "#781049", 0, 0) ])
define m = Character("Tristan", image = "tristanside" , first_indent = 50 , size = 32 , color = "#FFF" , outlines = [(3, "#4D3E3E", 0, 0),  (2, "#4d79e5", 0, 0),  (1, "#113386", 0, 0) ])
define n = Character("Taren", image = "tarenside" , first_indent = 50 , size = 32 , color = "#FFF" , outlines = [(3, "#4D3E3E", 0, 0),  (2, "#C637CA", 0, 0),  (1, "#641866", 0, 0) ])
define g = Character("Fleck", image = "fleckside" , first_indent = 50 , size = 32 , color = "#FFF" , outlines = [(3, "#4D3E3E", 0, 0),  (2, "#C7466E", 0, 0),  (1, "#741A36", 0, 0) ])

# The game starts here.

label start:

    $ body = 11
    $ hair = 6
    $ clothes = 2
    $ makeup = 1
    $ snakebites = False
    $ chin = False
    $ nose = False
    $ ears = False
    $ cuffs = False
    $ you = "YOU"
    $ custom = True
    $ gender = "None"
    $ bgb = "Boo"
    $ tilcount = 0
    $ tricount = 0
    $ tarcount = 0
    $ tilclick = 0
    $ triclick = 0
    $ tarclick = 0
    $ fpts = 0
    $ mpts = 0
    $ npts = 0
    scene park
label charactermaking:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show body at left
    show hair at left
    show makeup at left
    show snakebites at left
    show ears at left
    show cuffs at left
    show nose at left
    show chin at left
    show clothes at left
    "Time to create your LoveLife self! (click to next)"
menu:
    "Default or Custom Look?"
    "Default.":
        jump cm7
    "Custom.":
        jump design

label design:

label cm1:
    hide body at left
    hide hair at left
    hide makeup at left
    hide snakebites at left
    hide ears at left
    hide cuffs at left
    hide nose at left
    hide chin at left
    hide clothes at left
    show body at left
    show hair at left
    show makeup at left
    show snakebites at left
    show ears at left
    show cuffs at left
    show nose at left
    show chin at left
    show clothes at left

menu:
    "Choose a body type."
    "Androgynous.":
        $ body = 4
        $ clothes = 1
        jump cm1
    "Feminine.":
        $ body = 11
        $ clothes = 2
        jump cm1
    "Masculine.":
        $ body = 18
        $ clothes = 3
        jump cm1
    "{b}NEXT{/b}":
        jump cm2
label cm2:
    hide body at left
    hide hair at left
    hide makeup at left
    hide snakebites at left
    hide ears at left
    hide cuffs at left
    hide nose at left
    hide chin at left
    hide clothes at left
    show body at left
    show hair at left
    show makeup at left
    show snakebites at left
    show ears at left
    show cuffs at left
    show nose at left
    show chin at left
    show clothes at left  
 
menu:
    "Choose your makeup."
    "Gold.":
        $ makeup = 1
        jump cm2
    "Green.":
        $ makeup = 2
        jump cm2
    "Pink.":
        $ makeup = 3
        jump cm2 
    "Purple.":
        $ makeup = 4
        jump cm2 
    "None.":
        $ makeup = 5
        jump cm2
    "{b}NEXT{/b}":
        jump cm3

label cm3:
    hide body at left
    hide hair at left
    hide makeup at left
    hide snakebites at left
    hide ears at left
    hide cuffs at left
    hide nose at left
    hide chin at left
    hide clothes at left
    show body at left
    show hair at left
    show makeup at left
    show snakebites at left
    show ears at left
    show cuffs at left
    show nose at left
    show chin at left
    show clothes at left

menu:
    "Choose your hair."
    "Curly.":
        menu:
            "Choose length."
            "Short.":
                $ hair = 1
                jump cm3
            "Long.":
                $ hair = 2
                jump cm3
    "Newage.":
        menu:
            "Choose length."
            "Short.":
                $ hair = 3
                jump cm3
            "Long.":
                $ hair = 4
                jump cm3
    "Punk.":
        menu:
            "Choose length."
            "Short.":
                $ hair = 5
                jump cm3
            "Long.":
                $ hair = 6
                jump cm3
    "Straight.":
        menu:
            "Choose length."
            "Short.":
                $ hair = 7
                jump cm3
            "Long.":
                $ hair = 8
                jump cm3
    "{b}NEXT{/b}":
        jump cm4

label cm4:
    hide body at left
    hide hair at left
    hide makeup at left
    hide snakebites at left
    hide ears at left
    hide cuffs at left
    hide nose at left
    hide chin at left
    hide clothes at left
    show body at left
    show hair at left
    show makeup at left
    show snakebites at left
    show ears at left
    show cuffs at left
    show nose at left
    show chin at left
    show clothes at left
 
menu:
    "Choose your clothing."
    "Basic.":
        if body < 8:
            $ clothes = 1
            jump cm4
        if body > 14:
            $ clothes = 3
            jump cm4
        else:
            $ clothes = 2
            jump cm4  
    "Prep.":
        if body < 8:
            $ clothes = 4
            jump cm4
        if body > 14:
            $ clothes = 6
            jump cm4
        else:
            $ clothes = 5
            jump cm4
    "Punk.":
        if body < 8:
            $ clothes = 7
            jump cm4
        if body > 14:
            $ clothes = 9
            jump cm4
        else:
            $ clothes = 8
            jump cm4
    "{b}NEXT{/b}":
        jump cm5

label cm5:
    hide body at left
    hide hair at left
    hide makeup at left
    hide snakebites at left
    hide ears at left
    hide cuffs at left
    hide nose at left
    hide chin at left
    hide clothes at left
    show body at left
    show hair at left
    show makeup at left
    show snakebites at left
    show ears at left
    show cuffs at left
    show nose at left
    show chin at left
    show clothes at left

menu:
    "Choose skin color."
    "Darkest.":
        if body < 8:
            $ body = 1
            jump cm5
        if body > 14:
            $ body = 15
            jump cm5
        else:
            $ body = 8
            jump cm5  
    "Dark.":
        if body < 8:
            $ body = 2
            jump cm5
        if body > 14:
            $ body = 16
            jump cm5
        else:
            $ body = 9
            jump cm5
    "Mid Dark.":
        if body < 8:
            $ body = 3
            jump cm5
        if body > 14:
            $ body = 17
            jump cm5
        else:
            $ body = 10
            jump cm5
    "Medium.":
        if body < 8:
            $ body = 4
            jump cm5
        if body > 14:
            $ body = 18
            jump cm5
        else:
            $ body = 11
            jump cm5  
    "Mid Light.":
        if body < 8:
            $ body = 5
            jump cm5
        if body > 14:
            $ body = 19
            jump cm5
        else:
            $ body = 12
            jump cm5
    "Light.":
        if body < 8:
            $ body = 6
            jump cm5
        if body > 14:
            $ body = 20
            jump cm5
        else:
            $ body = 13
            jump cm5
    "Lightest.":
        if body < 8:
            $ body = 7
            jump cm5
        if body > 14:
            $ body = 21
            jump cm5
        else:
            $ body = 14
            jump cm5
    "{b}NEXT{/b}":
        jump cm6

label cm6:
    hide body at left
    hide hair at left
    hide makeup at left
    hide snakebites at left
    hide ears at left
    hide cuffs at left
    hide nose at left
    hide chin at left
    hide clothes at left
    show body at left
    show hair at left
    show makeup at left
    show snakebites at left
    show ears at left
    show cuffs at left
    show nose at left
    show chin at left
    show clothes at left

menu:
    "Choose your piercings."
    "Chin.":
        if chin == True:
            $ chin = False
            jump cm6
        if chin == False:
            $ chin = True
            jump cm6
    "Cuffs.":
        if cuffs == True:
            $ ears = False
            jump cm6
        if cuffs == False:
            $ cuffs = True
            jump cm6
    "Ears.":
        if ears == True:
            $ ears = False
            jump cm6
        if ears == False:
            $ ears = True
            jump cm6
    "Nose.":
        if nose == True:
            $ nose = False
            jump cm6
        if nose == False:
            $ nose = True
            jump cm6
    "Snake Bites.":
        if snakebites == True:
            $ snakebites = False
            jump cm6
        if snakebites == False:
            $ snakebites = True
            jump cm6
    "None.":
        if snakebites == True:
            $ snakebites = False
        if nose == True:
            $ nose = False
        if ears == True:
            $ ears = False
        if ears == True:
            $ ears = False
        if chin == True:
            $ chin = False
        jump cm6
    "{b}DONE{/b}":
        jump cm7
label cm7:
    hide body at left
    hide hair at left
    hide makeup at left
    hide snakebites at left
    hide ears at left
    hide cuffs at left
    hide nose at left
    hide chin at left
    hide clothes at left
    show body at left
    show hair at left
    show makeup at left
    show snakebites at left
    show ears at left
    show cuffs at left
    show nose at left
    show chin at left
    show clothes at left
menu:
    "What is your gender?"
    "Nonbinary.":
        $ gender = "Nonbinary"
        $ bgb = "Boo"
        jump name
    "Female.":
        $ gender = "Female"
        $ bgb = "Girl"
        jump name
    "Male.":
        $ gender = "Male"
        $ bgb = "Boy"
        jump name

label name:
menu:
    "What is your name?"
    "Jex (Default name)":
        $ you = "Jex"
        jump game
    "Other (You choose)":
        $ you = renpy.input("Type the name you want!")
        $ you = you.strip()

label game: 
    hide body at left
    hide hair at left
    hide makeup at left
    hide snakebites at left
    hide ears at left
    hide cuffs at left
    hide nose at left
    hide chin at left
    hide clothes at left
$ custom = False
jump begin

if custom == False:
    style choice_vbox:
        ypos 500
        yanchor 1.0

menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}KIND{/b} (kind){/color}":
        y "I'm kind!"
    "{color=#866CE7}{b}SNARKY{/b} (snarky){/color}":
        y "I'm snarky!"
    "{color=#E9218F}{b}FLIRTY{/b} (flirty){/color}":
        y "I'm flirty!"

############################################################# GAME

label begin:
menu:
    "Read Intro?"
    "Yes!":
        jump fleck
    "Skip Intro.":
        jump choose
label fleck:
    show fleck
    g "Hello, [you]!"
    g "I’m your guide, as well as your fairygothmother! "
    g "You heard that right!"
    g "I’m Fleck Stormweather, the gothic fae extraordinaire!"
    g "Welcome to the wonderful world of My Future LoveLife!"
    g "I’ll be helping you as you begin."
    g "Making sure you know what to do and where to go!"
    g "I'll always tell you what's going on at the end of a conversation, I got you, [bgb]!"
    g "Anyway, I’m babbling, let’s get back on track." 
    g "This is LoveLife park! Everyone here is single and ready to mingle... so go off and find someone you like!"
    hide fleck

    "{i}Alright, I suppose this is it. Let's see who we have to choose from.{/i}"

label choose:
    hide tristan
    hide tillie 
    hide taren
    if tilcount == 0: 
        show tillie at left
    if tarcount == 0: 
        show taren at right
    if tricount == 0: 
        show tristan

menu:
    "Pick someone to talk to!"
    "The girl on the left." if tilclick == 0: 
        hide tristan
        hide taren
        jump FemaleNPC
    "The boy in the middle" if triclick == 0: 
        hide taren
        hide tillie
        jump MaleNPC
    "The enby on the right." if tarclick == 0: 
        hide tristan
        hide tillie
        jump EnbyNPC

label skip:

jump timeskip

label FemaleNPC:
hide tillie
show tillie
menu:
    "Talk to Tillie?"
    "Yes!":
        f "Hi, there, what’s up?"
        jump tillie
    "No.":
        jump choose

label MaleNPC:
hide tristan
show tristan
menu:
    "Talk to Tristan?"
    "Yes!":
        m "Hey!"
        jump tristan
    "No.":
        jump choose
    
label EnbyNPC:
hide taren
show taren
menu:
    "Talk to Taren?"
    "Yes!":
        n "Oh, hey! I didn’t see you there!"
        jump taren
    "No.":
        jump choose

label tristan:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}Hello!{/b} (kind){/color}":
        $ mpts += 1
        m "What brings you to LoveLife park?"
        jump tristan2
    "{color=#866CE7}{b}Excuse me?{/b} (snarky){/color}":
        $ mpts -= 3
        m "Sorry, I was just trying to be friendly."
        $ tricount = 1
        $ triclick = 1
        "{color=#CC0000}{b}||CONVERSATION END||{/b}{/color}"
        hide tristan
        g "Oof, that was rough. He is out of here."
        jump choose
    "{color=#E9218F}{b}Hel-lo, hot stuff.{/b} (flirty){/color}":
        m "Wow, a little forward, but I’m not complaining."
        y "What can I say, I think you’re cute!"
        if snakebites == True: 
            m "I think you’re cute too! I love your snake bite piercings!"
            $ mpts += 3
            g "Looks like Tristan likes your piercings!" 
            g "Take note that even little changes in your look can make characters see you differently!"
            y "Thanks so much!"
        if snakebites == False:
            m "Well, thank you!"
            y "Welcome!"
        m "I gotta head out, but have a good one!"
        y "You too!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tristan
        g "That went... okay."
        g "Try talking to the others, he will still be available later!"
        $ triclick = 1
        jump choose
label tristan2:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}Just looking to meet people, you know?{/b} (kind){/color}":
        $ mpts += 1
        m "That’s fair, that’s fair. I won’t hold you up though if you want to talk to the others as well! I’ll see you around?"
        jump tristan3
    "{color=#866CE7}{b}Honestly, I have no idea!{/b} (snarky){/color}":
        $ mpts += 3
        m "Hahaha!"
        m "If I’m being real, same here!"
        y "Did it by chance have ANYTHING to do with a fairy?"
        m "….I don’t know what you’re talking about."
        "{i}He says this, but I notice him giving a knowing grin.{/i}"
        g "Hey!"
        g "Don’t rat me out!"
        g "I’m trying to help you here, [bgb]!"
        y "Sorry!"
        m "It’s okay!"
        y "Oh, I wasn’t talking to- uh, um, I gotta go!"
        m "Later!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tristan
        g "That didn't go too shabby with him, but keep quiet about me!"
        g "Try talking to the others, he will still be available later... hmph."
        $ triclick = 1
        jump choose
    "{color=#E9218F}{b}Well, honestly? I was hoping I’d meet good looking guys like you.{/b} (flirty){/color}":
        if snakebites == True:
            $ mpts += 5
            m "Rawr, alright, just getting right to it, huh?"
            y "Yeah, I am… you’re a hottie, who’s like, hot."
            m "So, are you, [bgb], damn."
            if gender == "Male":
                "{i}This is gay. This is hot. Damn.{/i}"
            else:
                "{i}This is hot.{/i}"
            y "Thank you, so..."
            jump tristan4
        if snakebites == False:
            m "Well, I appreciate the honesty, you’re cute too!"
            y "Thanks!"
            m "Now I’ll let you get to the others, but it was nice meeting you!"
            jump tristan3

label tristan3:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}See you!{/b} (kind){/color}":
        $ mpts += 1
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tristan
        g "That didn't go awful!"
        g "Try talking to the others, he will still be available later!"
        $ triclick = 1
        jump choose
    "{color=#866CE7}{b}No, wait!{/b} (snarky){/color}":
        $ mpts += 5
        m "Oh?"
        y "I don’t want to talk to the others, at least not yet. I kinda like you."
        m "I kinda think you’re cool too."
        y "Thanks..."
        m "Did you want to give a date a try? Why not, right? Tomorrow? DateWorld?"
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}Sure! What’s DateWorld?{/b} (kind){/color}":
        $ mpts += 3
        m "It’s only the greatest amusement park in all of the land, and couple who met in LoveLife Park, get to go… for free!"
        y "I’m so in!"
        m "See you then!"
        "{color=#FA2077}{b}||CONVERSATION END||{/b}{/color}"
        hide tristan
        g "So you did it! You have a date! Let’s head home and get some rest for tomorrow!"
        "{color=#FA2077}{b}||YOU HAVE A DATE!||{/b}{/color}"
        jump datetristan
    "{color=#866CE7}{b}Sorry, I don’t know you well enough yet{/b} (snarky){/color}":
        $ mpts -= 3
        m "That’s okay! I’ll still be around!"
        y "Cool, see you!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tristan
        g "That went pretty well!"
        g "Try talking to the others, he will still be available later!"
        $ triclick = 1
        jump choose        
    "{color=#E9218F}{b}Tomorrow day? ...or tomorrow night?{/b} (flirty){/color}":
        $ mpts += 3
        m "Tomorrow day, but maybe the sun will set, and i’ll still be about it."
        y "I feel that. It’s on."
        "{color=#FA2077}{b}||CONVERSATION END||{/b}{/color}"
        hide tristan
        g "So you did it! You have a, possibly fiery, date! Let’s head home and get some rest for tomorrow!"
        "{color=#FA2077}{b}||YOU HAVE A DATE!||{/b}{/color}"
        jump datetristan
        
label tristan4:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}I’ll leave you be, but I’m coming back for you.{/b} (kind){/color}":
        $ mpts += 1
        m "I'll be waiting~"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tristan
        g "That went great!"
        g "Try talking to the others, he will still be available later!"
        $ triclick = 1
        jump choose
    "{color=#866CE7}{b}You’re hot, but there’s other fish in the sea, babe, see you~{/b} (snarky){/color}":
        $ mpts -= 5
        m "Oh, I- ...okay."
        $ tricount = 1
        $ triclick = 1
        "{color=#CC0000}{b}||CONVERSATION END||{/b}{/color}"
        hide tristan
        g "You don’t mess around, you say it like it is, [bgb], but he is goooone. You’ll ‘see him’?, not likely, [you]."
        jump choose
    "{color=#E9218F}{b}No messing around, boy. Give me the digits.{/b} (flirty){/color}":
        $ mpts += 3
        m "Damn, straight."
        "{i}He puts his number into my phone.{/i}"
        y "When we gonna get together?"
        m "Tomorrow at DateWorld, [you]?"
        y "See you, then, Tristan."
        "{color=#FA2077}{b}||CONVERSATION END||{/b}{/color}"
        hide tristan
        g "Wow! Wow! Fire between you guys! No need to even stay, right? Let’s get home and get some rest for your date!"
        "{color=#FA2077}{b}||YOU HAVE A DATE!||{/b}{/color}"
        jump datetristan
        
label tillie:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}Not much, new to the park!{/b} (kind){/color}":
        $ fpts += 1
        f "Same here! I figured it could be a fun way to meet someone, you know?"
        y "Absolutely!"
        f "Meet anyone you like so far?"
        jump tillie2
    "{color=#866CE7}{b}The sky?{/b} (snarky){/color}":
        f "Really?"
        jump tilliey
    "{color=#E9218F}{b}The fact that you’re the most beautiful girl I’ve ever seen, that’s what.{/b} (flirty){/color}":
        if gender == "Female":
            f "Clearly, you’ve never looked in a mirror then."
            "{i}OMG! Did she just say that to me? This is a WLW crisis, what do I say?!{/i}"
            y "Am I dreaming? Okay."
            "{i}Nailed it.{/i}"
            f "No, this is real. You’re beautiful. I wanna get to know you better. I’m already into you."
            y "I’m into you too, oh my…"
            f "You’re so cute!!"
            "{i}I’m pretty sure I’m blushing head to toe.{/i}"
            jump tillie3
        else:
            f "Okay, I’ll admit, that’s actually kind of cute."
            y "Thanks..."
            f "In fact, you’re kind of cute."
            y "Thanks!!"
            f "Of course!"
            jump tilliex

label tilliey:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}Really.{/b} (kind){/color}":
        f "Um… okay. I’m gonna, go. Bye."
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "Oof, awkward much? At least she didn’t leave the park. You might have a second chance if you want."
        g "Try talking to the others first though!"
        $ tilclick = 1
        jump choose
    "{color=#866CE7}{b}No, not really. It never happened.{/b} (snarky){/color}":
        f "I don’t need this sarcasm? Bye."
        $ tilcount = 1
        $ tilclick = 1
        "{color=#CC0000}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "Well, you have no chance with her now. That was a disaster!"
        jump choose
    "{color=#E9218F}{b}I apologize I have no idea how to talk to a pretty girl.{/b} (flirty){/color}":
        f "Oh my gosh, that’s sweet. You're sweet."
        y "Thank you, oh my gosh."
        f "Of course!"
        jump tilliex
    

label tillie2:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}Not yet, but I’m hoping to!{/b} (kind){/color}":
        f "Well, get out there then! I wish you luck!"
        y "Thanks!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "Awhh, what if she was the one! *gasp* haha no worries, looks like she’s sticking around!"
        g "Try talking to the others, she will still be available later!"
        $ tilclick = 1
        jump choose
    "{color=#866CE7}{b}Yeah, actually, but I figured I’d talk to some other people too.{/b} (snarky){/color}":
        $ fpts -= 3
        f "Oh… um, right. Okay? The maybe go find them instead? Bye."
        $ tilcount = 1
        $ tilclick = 1
        "{color=#CC0000}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "Awkward…!!"
        jump choose
    "{color=#E9218F}{b}I think I am meeting them right now o////o{/b} (flirty){/color}":
        $ fpts += 3
        f "Oh… oh, geez that’s me."
        y "Haha, yeah, you’re really cute."
        f "Thank you! So are you!"
        y "Thanks!"
        f "Of course!"
        jump tilliex

label tillie3: 
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}Thanks! So are you!{/b} (kind){/color}":
        $ fpts += 3
        f "Thank you!"
        y "Of course!"
        f "Don’t let me hold you up though! Talk to who you like, but I’ll be around if you want to choose me, okay?"
        y "Sounds good!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "That went really well! We definitely have a date later if we want one! I mean you… you have a date… hah!"
        g "Try talking to the others, she will still be available later!"
        $ tilclick = 1
        jump choose
    "{color=#E9218F}{b}You’re cute, me like you, oh gosh, help.{/b} (flirty){/color}":
        $ fpts += 5
        f "You’re killing me here! Okay please, I want to take you to DateWorld, the greatest free amusement park for lovelife park lovebirds, are you in?!"
        jump tillie4

label tillie4:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}I need a little time to think about it, but it sounds amazing!{/b} (kind){/color}":
        $ fpts -= 1
        f "No problem! Let me know!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "Seems like she is sticking around! Meet up with her later if you want to go on a date!"
        g "Try talking to the others!"
        $ tilclick = 1
        jump choose
    "{color=#866CE7}{b}LOL, no. You’re hot, but like… no.{/b} (snarky){/color}":
        $ fpts -= 10
        f "Wow… rude. Okay, fine. Bye."
        $ tilcount = 1
        $ tilclick = 1
        "{color=#CC0000}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "Welp, no date for you. Damn. Brutal. I wish I was that heartless sometimes, would work with my look."
        jump choose
    "{color=#E9218F}{b}YES!!! Let’s go!{/b} (flirty){/color}":
        $ fpts += 5
        f "Great!! It’s a date, cutie!"
        "{color=#FA2077}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "So you did it! You have a date with Tillie! Let’s head home and get some rest for tomorrow!"
        "{color=#FA2077}{b}||YOU HAVE A DATE!||{/b}{/color}"
        jump datetillie
        
    
label tilliex:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}So… do you like music?{/b} (kind){/color}":
        $ fpts += 1
        f "I mean, yeah, music is good. I listen to the radio."
        y "Cool, cool. Songs…"
        f "Yeah.. Singers… Bands…"
        y "Uh… albums?"
        f "Yeah… I’m sorry this conversation really is small talk, and I’m not super into small talk."
        jump tillie5
    "{color=#866CE7}{b}So… do you like sci-fi?{/b} (snarky){/color}":
        $ fpts += 3
        f "Yeah! I am a big fan of Star Adventure and Solarforces!"
        y "No way! I love Star Adventure!"
        f "Who is your favorite character?"
        jump tillie6
    "{color=#E9218F}{b}So… do you like fandom?{/b} (flirty){/color}":
        $ fpts += 5
        f "Oh my gosh, yes? I run a blog about Star Adventure."
        y "Really? Oh my gosh! I love Star Adventure!"
        "{i}There is a pause and then she looks at me with a wry smile.{/i}"
        f "Do you ‘ship’ characters…?"
        jump tillie7

label tillie5: 
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}Okay, that’s fine, I’ll head out!{/b} (kind){/color}":
        f "See you!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "That got a little bit awk-y, but it wasn’t the end of the world!"
        g "Try talking to the others, she will still be available later!"
        $ tilclick = 1
        jump choose
    "{color=#866CE7}{b}That’s fine… do you like sci-fi?{/b} (snarky){/color}":
        $ fpts += 3
        f "Yeah! I am a big fan of Star Adventure and Solarforces!"
        y "No way! I love Star Adventure!"
        f "Who is your favorite character?"
        jump tillie6
    "{color=#E9218F}{b}That’s fine… do you like fandom?{/b} (flirty){/color}":
        $ fpts += 5
        f "Oh my gosh, yes? I run a blog about Star Adventure."
        y "Really? Oh my gosh! I love Star Adventure!"
        "{i}There is a pause and then she looks at me with a wry smile.{/i}"
        f "Do you ‘ship’ characters…?"
        jump tillie7

label tillie6:  
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}The lead character! Ellen Starlight! She is smart and strong, and while she’s got a lot to learn, her beliefs are in the right place!{/b} (kind){/color}":
        $ fpts += 1
        f "Ellen is great!"
        y "Yeah!"
        f "Do you ‘ship’ characters…?"
        jump tillie7
    "{color=#866CE7}{b}The antagonist of course. Jenson Flare is wickedly lovely. My trash son.{/b} (snarky){/color}":
        $ fpts += 4
        f "Jensen is trash and I love him. Love to hate and hate to love."
        y "Right? He is 100 percent trash baby."
        f "Do you ‘ship’ characters…?"
        jump tillie7
    "{color=#E9218F}{b}I love the sidekick, Kia! She is so sweet and heartfelt, and gah, I love her.{/b} (flirty){/color}":
        $ fpts += 7
        f "Kia!!!! Kia is my favorite too!"
        y "No way!!"
        f "We are Kia stans first and humans second."
        jump tillie8

label tillie7:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}Not really my thing, but I love the show!{/b} (kind){/color}":
        $ fpts -= 2
        f "Fair enough! It’s not for everyone!"
        y "But I respect it, haha."
        f "Good, good. I’m going to go update my Star Adventure blog, but I’ll be around, okay?"
        y "Okay!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "That went pretty well!"
        g "Try talking to the others, she will still be available later!"
        $ tilclick = 1
        jump choose
    "{color=#866CE7}{b}I ship the lead, Ellen, with the villain, Jensen, muahaha. JenEll for life.{/b} (snarky){/color}":
        $ fpts += 5
        f "That is so evil. Omg. That ship is like… A guilty pleasure of mine. I am a terrible Kia stan! L-O-L!"
        y "Omg, I love it!"
        f "New nasty friend maybe date, this is blessed."
        f "I’m going to go update my Star Adventure blog, but I’ll be around, and please hit me up, okay?"
        y "Okay!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "That went so well! I sense a date in your future!"
        g "Try talking to the others, she will still be available later!"
        $ tilclick = 1
        jump choose
    "{color=#E9218F}{b}I ship Ellen and her sidekick Kia! They are so sweet together, and I think EllKia has a chance to be canon!{/b} (flirty){/color}":
        $ fpts += 4
        f "OTP! Love them!"
        y "Me too!!"
        f "In fact.. I have to make a post about them… shoot! I’m going to go update my Star Adventure blog, but I’ll be around, okay?"
        y "Okay!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "That went really well!"
        g "Try talking to the others, she will still be available later!"
        $ tilclick = 1
        jump choose

label tillie8:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}What is a stan?{/b} (kind){/color}":
        f "It used to mean ‘stalker fan’, but now i just means you, like, love a character so much. And I LOVE Kia."
        y "I love Kia too!"
        f "She's great! I’m going to go update my Star Adventure blog, but I’ll be around, okay?"
        y "Okay!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "That went pretty well!"
        g "Try talking to the others, she will still be available later!"
        $ tilclick = 1
        jump choose
    "{color=#866CE7}{b}Oh… you’re one of thooose fans.{/b} (snarky){/color}":
        $ fpts -= 7
        f "Wow… I see. Got it. It’s going to be like that. I don’t need this right now, so like, bye felicia."
        $ tilcount = 1
        $ tilclick = 1
        "{color=#CC0000}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "Well, well, well. You decided to be Judgy McJudgypants, didn’t you? Judge Judy put to shame here folks."
        jump choose
    "{color=#E9218F}{b}Kia Stans for life!{/b} (flirty){/color}":
        $ fpts += 7
        f "Kia stans for life!!!"
        if hair == 2:
            f "You even have the Kia hairdo!"
            g "Looks like Tillie likes the fact that your hair looks like Kia's!" 
            g "Take note that even little changes in your look can make characters see you differently!"
            y "Yeah!"
        f "Hey do you want to go to DateWorld with me? They’re adding a Star Adventure ride!"
        jump tillie9

label tillie9:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}I need a little time to think about it, but it sounds amazing!{/b} (kind){/color}":
        f "No problem! Let me know, fellow Kia stan;)! Here’s my number!"
        "{i}She gave me her number on a sticky note.{/i}"
        y "Thanks!"
        f "See you!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "Seems like she is sticking around! Meet up with her later if you want to go on a date!"
        g "But try talking to the others first!"
        $ tilclick = 1
        jump choose
    "{color=#866CE7}{b}Sorry, I think we’d be better off as friends!{/b} (snarky){/color}":
        $ fpts -= 3
        f "Oh, that’s okay! We can always still hang out sometime! Here’s my number!"
        "{i}She gave me her number on a sticky note.{/i}"
        $ tilcount = 1
        $ tilclick = 1
        "{color=#CC0000}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "She's headed out, but you do have her number, maybe for a friendship!"
        jump choose
    "{color=#E9218F}{b}YES!!! Let’s go!{/b} (flirty){/color}":
        $ fpts += 5
        f "Great!! It’s a date, Kia-cutie! Here’s my number!"
        "{i}She gave me her number on a sticky note.{/i}"
        y "Thanks, Tillie! I’ll see you then, ki-utie? See what I did?"
        f "Hahahaha. See you then!"
        "{color=#FA2077}{b}||CONVERSATION END||{/b}{/color}"
        hide tillie
        g "So you did it, fellow Star Cadet! You have a date with Tillie! Let’s head home and get some rest for tomorrow!"
        "{color=#FA2077}{b}||YOU HAVE A DATE!||{/b}{/color}"
        jump datetillie

label taren:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}I have quiet feet, haha, hi!{/b} (kind){/color}":
        $ npts += 2
        n "It’s okay! I’ve been on the other side of that too when I don’t have a heel on my shoe!"
        y "Fair enough!"
        y "So..."
        jump taren3
    "{color=#866CE7}{b}Did I startle you?{/b} (snarky){/color}":
        n "A little! But it’s fine! I zone out a lot, you’re good!"
        y "Okay, good!"
        jump taren3
    "{color=#E9218F}{b}Do you like what you see?{/b} (flirty){/color}":
        $ npts -= 2
        n "Oh, I am so not into that. Stop it."
        jump taren2

label taren2:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}I’m sorry! I was trying to be smooth but I sounded like a jerk!{/b} (kind){/color}":
        $ npts += 2
        n "Haha, you did, but thanks for owning up to it."
        y "Of course, I, I don’t know what I was thinking."
        n "It’s okay, really! I just hate chat up lines."
        y "Totally valid..."
        jump taren3
    "{color=#866CE7}{b}And now I don’t like what I see{/b} (snarky){/color}":
        $ npts -= 3
        n "Neither do I, bye."
        $ tarcount = 1
        $ tarclick = 1
        "{color=#CC0000}{b}||CONVERSATION END||{/b}{/color}"
        hide taren
        g "That was the definition of trainwreck, good golly!"
        jump choose
    "{color=#E9218F}{b}C’mon, I think you’re cute!{/b} (flirty){/color}":
        $ npts -= 7
        n "I said I’m not into it, respect that, or... or fuck off!"
        $ tarcount = 1
        $ tarclick = 1
        "{color=#CC0000}{b}||CONVERSATION END||{/b}{/color}"
        hide taren
        g "That was not very cool. They told you to stop, and you didn’t respect their boundaries. Please be more mindful!"
        g "They're hurt and gone, and there is no way to mend that bridge."
        jump choose
    
label taren3:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}Are you new to the park?{/b} (kind){/color}":
        $ npts += 3
        n "Eh, not really. I come here from time to time, but I never really meet anybody special."
        y "Been awhile you’ve been searching, huh?"
        n "Yeah, a lot of losers come here."
        y "Hey!"
        n "No, no I didn’t mean you, I-"
        y "I’m joking!"
        n "...OH! Hahaha! You’re funny. I like that."
        jump taren4
    "{color=#866CE7}{b}What are you looking for?{/b} (snarky){/color}":
        $ npts += 1
        n "If I’m being honest, I don’t know."
        y "I don’t know either!"
        n "Haha, maybe you should explore the park a little more and figure out what it is you {i}are{/i} looking for!"
        y "Sounds good!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide taren
        g "The conversation ended, but it seems like they are sticking around!"
        g "Try talking to the others first, but maybe meet up with them later if you want to try again!"
        $ tarclick = 1
        jump choose
    "{color=#E9218F}{b}I love your hair!{/b} (flirty){/color}":
        $ npts += 5
        n "Oh, really? Thank you! I decided to let it grow out a little!"
        y "It looks really nice."
        if hair == 3:
            n "I have to admit, I absolutely ADORE your hair too. It’s so fluffy looking!"
            g "Looks like Taren likes your newage short hair!"
            g "Take note that even little changes in your look can make characters see you differently!"
            y "Really?! Thank you so much!"
            n "You're welcome!"
            jump taren6
        else:
            n "Thank you!"
            jump taren6

label taren4:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}Thank you!{/b} (kind){/color}":
        $ npts += 1
        n "Of course!"
        y "Great!"
        jump taren6
    "{color=#866CE7}{b}I promise you I’m not!{/b} (snarky){/color}":
        $ npts -= 1
        n "Haha… right.. Right… okay uhhh… I’m making a fool of myself, so like, i’m gonna go."
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide taren
        g "That took at turn to awkward town, but it looks like they’re sticking around!"
        g "Try talking to the others first, but maybe meet up with them later if you want to try again!"
        $ tarclick = 1
        jump choose
    "{color=#E9218F}{b}I like your laugh!{/b} (flirty){/color}":
        $ npts += 5
        n "Oh, golly. Really? I sound like a dying alpaca though."
        y "Maybe I like alpacas!"
        n "...Well played, hahaha! You know, I haven’t had a good laugh in a long time."
        y "I’m glad I could help out!"
        n "You know, I don’t normally do this, but, would you like to go on a date?"
        "{i}My heart is beating faster.{/i}"
        n "We can go to DateWorld tomorrow, it’s an all expenses included amusement park for LoveLife Park members, I mean… if you wanted?"
        jump taren5

label taren5:
menu:
    "Make a CHOICE"
    "{color=#46A7E2}{b}I need a little time to think about it, but it sounds like fun!{/b} (kind){/color}":
        $ npts -= 1
        n "No problem! Take your time, I’ll be around!"
        "{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
        hide taren
        g "It’s okay to take time! You totally have an amazing chance for a date if you still are interested!"
        g "Try talking to the others first, but maybe meet up with them later if you want!"
        $ tarclick = 1
        jump choose
    "{color=#866CE7}{b}Oh, I don’t like you like that...{/b} (snarky){/color}":
        $ npts -= 5
        n "Why the one time I like someone, they don’t like me? But, okay. I understand."
        $ tarcount = 1
        $ tarclick = 1
        "{color=#CC0000}{b}||CONVERSATION END||{/b}{/color}"
        hide taren
        g "That was heartbreaking... but you gotta be true to you, [bgb]!"
        jump choose
    "{color=#E9218F}{b}Absolutely! Let’s go on a date!{/b} (flirty){/color}":
        $ npts += 5
        y "Really?! Yay!! It’s a date!"
        "{color=#FA2077}{b}||CONVERSATION END||{/b}{/color}"
        hide taren
        g "Congrats, [you]! You have a date with Taren! Let’s head home and get a good night sleep."
        "{color=#FA2077}{b}||YOU HAVE A DATE!||{/b}{/color}"
        jump datetaren

label taren6:
n "Well, you know, it was nice talking with you."
y "Nice talking with you as well!"
n "I’m going to make a quick phone call to a friend of mine, but I’ll still be around if you want to talk after!"
y "Sounds good!"
n "Bye!"
y "See you!"
"{color=#F1C232}{b}||CONVERSATION END||{/b}{/color}"
hide taren
g "You still have a chance with them, I think that went pretty well!"
g "Try talking to the others first, but maybe meet up with them later if you can!"
$ tarclick = 1
jump choose

label timeskip:
hide tristan
hide tillie
hide taren
scene park2
g "Some time has passed since your first encounters..." 
g "Now let's see who you still have a shot with!"
label choose2:
if tilcount == 0:
    show tillie at left
if tarcount == 0:
    show taren at right
if tricount == 0:
    show tristan
menu:
    "Do you still want a date? Ask some who's left for a date!"
    "The girl on the left." if tilcount == 0: 
        hide tristan
        hide taren
        jump tillast
    "The boy in the middle" if tricount == 0: 
        hide taren
        hide tillie
        jump trilast
    "The enby on the right." if tarcount == 0: 
        hide tristan
        hide tillie
        jump tarlast

label skip2:

jump nodate

label trilast:
show tristan
if mpts >= 5:
    m "You know what? Let's go to DateWorld tomorrow!"
    jump datetristan
else:
    m "I'm not really feeling it, I'm sorry!"
    $ tricount = 1
    hide tristan
    jump choose2

label tillast:
show tillie
if fpts >= 5:
    f "...Yes! Let's go to DateWorld tomorrow!"
    jump datetillie
else:
    f "Awh, sorry, I don't think so!"
    $ tilcount = 1
    hide tillie
    jump choose2

label tarlast:
show taren
if npts >= 5:
    n "...I'm glad you asked. Let's go to DateWorld tomorrow!"
    jump datetaren
else:
    n "I'm sorry, I'm going to pass."
    $ tarcount = 1
    hide taren
    jump choose2

label nodate:
"So... you didn't get a date, but you're fine by yourself!"
return

label datetristan:
    scene date
    show body at left
    show hair at left
    show makeup at left
    show snakebites at left
    show ears at left
    show cuffs at left
    show nose at left
    show chin at left
    show clothes at left
    show tristan
"The next day, you have a great date with Tristan!"
return

label datetillie:
    scene date
    show body at left
    show hair at left
    show makeup at left
    show snakebites at left
    show ears at left
    show cuffs at left
    show nose at left
    show chin at left
    show clothes at left
    show tillie
"The next day, you have a great date with Tillie!"
return

label datetaren:
    scene date
    show body at left
    show hair at left
    show makeup at left
    show snakebites at left
    show ears at left
    show cuffs at left
    show nose at left
    show chin at left
    show clothes at left
    show taren
"The next day, you have a great date with Taren!"
return
