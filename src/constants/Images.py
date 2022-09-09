########################################################
# Images.py
# Xristos Dosis
# August 6, 2022
#
# All image references.
########################################################

from src.lib.Atlas import Atlas
from src.constants.RaobfNames import *
from src.constants.UI import CONTEXT_POOL
from src.lib.jsDictionary import JSDictionary

BTNS = Atlas("src/art/Buttons/buttons.atlas")

IMAGES = JSDictionary({
    "ATTACK_DISC" : JSDictionary({
        k: 'src/art/FrontSide/{}.png'.format(str(v))
        for k,v in globals().items()
        if type(v).__name__ == "RaobfLabel" and globals()[k].context == CONTEXT_POOL.ATTACK_DISC
    }),

    "SLIDE_RULE_DISC" : JSDictionary({
        k: 'src/art/BackSide/{}.png'.format(str(v))
        for k,v in globals().items()
        if type(v).__name__ == "RaobfLabel" and globals()[k].context == CONTEXT_POOL.SLIDE_RULE_DISC
    }),

    "BUTTONS" : BTNS.CONTROLS,
    "CONTEXT" : BTNS.CONTEXT
})
