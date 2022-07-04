from kivy.atlas import Atlas
from src.constants.RaobfNames import *
from src.lib.jsDictionary import JSDictionary
from src.lib.fixedASRImage import FixedASRImage

buttons = Atlas("src/data/buttons.atlas")

IMAGES = JSDictionary({
    "ATTACK_DISC" : JSDictionary({
        "RB"   : "src/data/FrontSide/{}.png".format("_".join(RB.split(" "))),
        "CR"   : "src/data/FrontSide/{}.png".format("_".join(CR.split(" "))),
        "TD"   : "src/data/FrontSide/{}.png".format("_".join(TD.split(" "))),
        "BALA" : "src/data/FrontSide/{}.png".format("_".join(BALA.split(" "))),
        "ACP"  : "src/data/FrontSide/{}.png".format("_".join(ACP.split(" ")))
    }),

    "SLIDE_RULE_DISC" : JSDictionary({
        "AOB"  : "src/data/BackSide/AOB_Disc.png",
        "DS"   : "src/data/BackSide/Distance_Speed_Disc.png",
        "TM"   : "src/data/BackSide/{}.png".format("_".join(TM.split(" ")))
    }),

    "BUTTONS" : JSDictionary({
        "CR"      : buttons["CR"],
        "TD"      : buttons["TD"],
        "BALA"    : buttons["BALA"],
        "ACP"     : buttons["ACP"],
        "RESET"   : buttons["RESET"]
    }),

    "CONTEXT" : JSDictionary({
        "FRONT" : buttons["FRONT"],
        "BACK"  : buttons["BACK"]
    })
})
