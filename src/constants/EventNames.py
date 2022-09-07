########################################################
# EventNames.py
# Xristos Dosis
# August 6, 2022
#
# All event names.
########################################################

from src.lib.jsDictionary import JSDictionary

EVENTS = JSDictionary({
    "CHANGE_FOCUS"   : "change-focus",
    "CHANGE_VIEW"    : "change-view",
    "CHANGE_CONTEXT" : "change-context",
    "CHANGE_VALUE"   : "change-value",
    "ENTER_LINK"     : "enter-link",
    "BREAK_LINK"     : "break-link",
    "RESET"          : "reset"
})
