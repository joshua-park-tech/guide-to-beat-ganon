import random
from appjar import gui

app = gui("Guide to wiping out Ganon from this Universe", "1000x550")
print("Guide to demolish Ganon")

def press():
    pass
def launch(win):
    app.showSubWindow(win)


if __name__ == "__main__":
    app.addFlashLabel("die", "You wanna kick Ganon out of Hyrule Castle with a tree branch and stuff?")
    #app.addImage("memes", "ezgif-2-e07e7cb62724.gif")

    # these go in the main window

    app.addButtons(["Thunderblight Ganon", "Windblight Ganon", "Waterblight Ganon", "Fireblight Ganon", "Calamity Ganon", "Dark Beast Ganon"], launch)

    # app.addImage("stasis zelda", "zelda-being-great-for-the-first-time-in-her-life.gif")
    # app.setImageSize("stasis zelda", 100, 100)
    # # app.addImage("bad zelda", "zelda-is-bad.gif")
    # # app.addImage("scared zelda", "zelda-is-scared.gif")
    # # app.addImage("frog zelda", "zelda-makes-link-eat-a-frog.gif")

    # this is a pop-up
    app.startSubWindow("Thunderblight Ganon", modal=True)
    app.addLabel("sed", "kill")
    app.addImage("gif", "tumblr_ou8k3q8gex1unzyd3o1_500.gif")
    app.addTextArea('t1')
    app.setTextArea("t1", "if you are good at parries, parry thunderblight and smack the shield before stunning him again. feel free to attack while stunned."
                          "if you are good at flurry rushes, continue flurry rushing"
                          "second phrase, if thunderblight chuchs metal pillars at you, magnesis them and attack them at thunderblight and resume attacking, parrying, flurry rushing after"
                    , end=True, callFunction=True)

    app.stopSubWindow()

    # this is another pop-up
    app.startSubWindow("Windblight Ganon")
    app.addLabel("aptn", "SubWindow Two")
    app.stopSubWindow()

    # this is another pop-up
    app.startSubWindow("Waterblight Ganon")
    app.addLabel("btq", "SubWindow Two")
    app.stopSubWindow()

    # this is another pop-up
    app.startSubWindow("Fireblight Ganon")
    app.addLabel("bsg", "SubWindow Two")
    app.stopSubWindow()

    # this is another pop-up
    app.startSubWindow("Calamity Ganon")
    app.addLabel("qwert", "SubWindow Two")
    app.stopSubWindow()

    # this is another pop-up
    app.startSubWindow("Dark Beast Ganon")
    app.addLabel("sdf", "SubWindow Two")
    app.stopSubWindow()

    app.setLabelBg("die", "red")
    # app.addButton("Thunderblight Ganon3", press)
    # app.addButton("Windblight Ganon3", press)
    # app.addButton("Waterblight Ganon3", press)
    # app.addButton("Firebllight Ganon3", press)
    # app.addButton("Calamity Ganon3", press)
    # app.addButton("Dark Beast Ganon3", press)

    list_names = ["zelda-being-great-for-the-first-time-in-her-life.gif", "zelda-is-bad.gif", "zelda-is-scared.gif"]
    ran_name = random.choice(list_names)
    app.addImage( "abc",ran_name)

    # app.addImage("stasis zelda", "zelda-being-great-for-the-first-time-in-her-life.gif")
    app.setImageSize("abc", 400, 500)


    app.go()