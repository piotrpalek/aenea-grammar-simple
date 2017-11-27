# commands for controlling various programs

from aenea import *
from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
  typeables["semicolon"] = keyboard.get_typeable(char=';')

appCommand = {
    "chrome": "google chrome",
    "fox": "firefox",
    "spotify": "spotify",
    "emacs": "emacs",
    "term": "terminal",
    "gedit": "gedit",
}

class Rule(MappingRule):
    modKey = "cs"
    winKey = "cw"
    winPrefix = "pain"
    mapping = {
        "lake [<n>]": Key(modKey + "-h:%(n)d"),
        "rake [<n>]": Key(modKey + "-n:%(n)d"),
        winPrefix + " <n>": Key(winKey + "-%(n)d"),
        winPrefix + " last": Key(winKey + "-end"),
        winPrefix + " switch": Key("a-tab"),
        winPrefix + " stick lake": Key("w-left"),
        winPrefix + " stick rake": Key("w-right"),
        winPrefix + " launch": Key("a-f2/10"),
        winPrefix + " launch <appCommand>": Key("a-f2/0:1/100000") + Text("%(appCommand)s") + Key("enter"),
        winPrefix + " move lake": Key("csa-left"),
        winPrefix + " move rake": Key("csa-right"),
        winPrefix + " kill": Key("a-f4"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 0, 10),
        Choice("appCommand", appCommand),
    ]
    defaults = {
        "n": 1,
    }
