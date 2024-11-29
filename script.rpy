# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

screen dressup():
    modal True
    frame:
        yfill True
        xfill True

        grid 3 3:
            xalign 0.5
            textbutton "1":
                action ("start")
            textbutton "2":
                action Jump("start")
            textbutton "3":
                action Jump("start")
            textbutton "4":
                action Jump("start")
            textbutton "5":
                action Jump("start")
            textbutton "6":
                action Jump("start")
            textbutton "7":
                action Jump("start")
            textbutton "8":
                action Jump("start")
            textbutton "9":
                action Jump("start")
        frame:
            textbutton "quit":
                action Hide("dressup")

screen button():
    modal False
    frame:
        textbutton "dressing room":
            action Show("dressup")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    show screen button

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    label repeat:

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    jump repeat

    # This ends the game.

    return
