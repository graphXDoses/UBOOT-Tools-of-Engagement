########################################################
# RaobfNames.py
# Xristos Dosis
# August 6, 2022
#
# All RAOBF names, as labels.
########################################################

from src.lib.Utils import Label
from src.constants.UI import CONTEXT_POOL

class RaobfLabel(Label):

    def __init__(self, extended, compact, context=None):
        super(RaobfLabel, self).__init__(extended, compact)
        self.__context = context

    @property
    def context(self):
        return self.__context

# Front Side

RB   = RaobfLabel("Relative Bearing",       "Relative_Bearing",       CONTEXT_POOL.ATTACK_DISC)
CR   = RaobfLabel("Compass Rose",           "Compass_Rose",           CONTEXT_POOL.ATTACK_DISC)
TG   = RaobfLabel("Target Disc",            "Target_Disc",            CONTEXT_POOL.ATTACK_DISC)
BALA = RaobfLabel("Bearing and Lead Angle", "Bearing_and_Lead_Angle", CONTEXT_POOL.ATTACK_DISC)
ACP  = RaobfLabel("Attack Course Pointer",  "Attack_Course_Pointer",  CONTEXT_POOL.ATTACK_DISC)

# Back Side

AOB  = RaobfLabel("Angle-on-Bow Disc",     "AOB_Disc",            CONTEXT_POOL.SLIDE_RULE_DISC)
DS   = RaobfLabel("Distance & Speed Disc", "Distance_Speed_Disc", CONTEXT_POOL.SLIDE_RULE_DISC)
TM   = RaobfLabel("Time Disc",             "Time_Disc",           CONTEXT_POOL.SLIDE_RULE_DISC)

del Label
del RaobfLabel
