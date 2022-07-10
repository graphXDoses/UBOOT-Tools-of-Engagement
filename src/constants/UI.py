from src.lib.jsDictionary import JSDictionary

active_button   = "active_button"
not_assigned    = "None"
CONTEXT_POOL = JSDictionary({
    "ATTACK_DISC"     : "Attack Disc",
    "SLIDE_RULE_DISC" : "Slide Rule Disc"
})
VIEWS_POOL   = JSDictionary({
    "MAINVIEW"        : "main",
    "SETTINGSVIEW"    : "settings"
})
default_view    = VIEWS_POOL.MAINVIEW
# default_view    = VIEWS_POOL.SETTINGSVIEW
default_context = CONTEXT_POOL.ATTACK_DISC
# currentContext  = not_assigned
