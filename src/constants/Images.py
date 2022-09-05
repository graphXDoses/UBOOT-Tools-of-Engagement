from kivy.atlas import Atlas
from src.constants.RaobfNames import *
from src.lib.jsDictionary import JSDictionary
from src.lib.fixedASRImage import FixedASRImage

buttons = Atlas("src/art/Buttons/buttons.atlas")

IMAGES = JSDictionary({
    "ATTACK_DISC" : JSDictionary({
        "RB"   : "src/art/FrontSide/{}.png".format("_".join(RB.split(" "))),
        "CR"   : "src/art/FrontSide/{}.png".format("_".join(CR.split(" "))),
        "TG"   : "src/art/FrontSide/{}.png".format("_".join(TG.split(" "))),
        "BALA" : "src/art/FrontSide/{}.png".format("_".join(BALA.split(" "))),
        "ACP"  : "src/art/FrontSide/{}.png".format("_".join(ACP.split(" ")))
    }),

    "SLIDE_RULE_DISC" : JSDictionary({
        "AOB"  : "src/art/BackSide/AOB_Disc.png",
        "DS"   : "src/art/BackSide/Distance_Speed_Disc.png",
        "TM"   : "src/art/BackSide/{}.png".format("_".join(TM.split(" ")))
    }),

    "BUTTONS" : JSDictionary({
        "CR"      : buttons["CR"],
        "TG"      : buttons["TG"],
        "BALA"    : buttons["BALA"],
        "ACP"     : buttons["ACP"],
        "RESET"   : buttons["RESET"],
        "HELP"    : buttons["HELP"]
    }),

    "CONTEXT" : JSDictionary({
        "FRONT" : buttons["FRONT"],
        "BACK"  : buttons["BACK"]
    })
})
