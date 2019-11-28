# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define unknown = Character(_("???"), color="ffffff")
define MB = Character(_("Mecha Blob"), color="c8a000")
define mc = Character(_("You"), color="c8c800")
default mcName = "John"

label start:

    scene bg room
    $ mcName = renpy.input("What's your name?")
    menu:
        "Mecha Blob linear arc":
            jump mechablobbegin

label mechablobbegin:
    "The bell rings."
    #play music "bell ring.mp3"
    "Noticing the time, you hurry into your next class."
    "You walk to your desk and sit down."
    "You notice that their is a new resident in the desk next to yours."
    show mc yes
    mc "Hi there, my name is [mcName]. I haven't seen you around before. Are you new here?"
    show mechablob no at right
    MB "Why yes mr manly man, i am new here and i need you to show me around the ropes before i die."
    #GET TO KNOW EACH OTHER SHIT (STILL WAITING ON DIALOGUE CAUSE I CAN'T WRITE FOR SHIT)
    jump end

label study:
    "You go \"study\" at Mecha Blob's house. ;)"
    jump end

label nostudy:
    "You dumbass, no gf for you."
    jump end

label end:

    mc "Ah shit here we go again"

    mc "More pain and suffering while coding to come"

    show mechablob curious at right
    with dissolve

    MB "Fuck me"

    #end game line
    return
