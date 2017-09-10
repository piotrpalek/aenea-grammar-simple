# commands for controlling various programs

from aenea import *
from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
  typeables["semicolon"] = keyboard.get_typeable(char=';')

class WindowManagerRule(MappingRule):
    modKey = "a"
    winPrefix = "win"
    mapping = {
        winPrefix + " [<n>]": Key(modKey + "-%(n)d"),
        winPrefix + " left [<n>]": Key(modKey + "-h:%(n)d"),
        winPrefix + " right [<n>]": Key(modKey + "-l:%(n)d"),
        winPrefix + " up [<n>]": Key(modKey + "-k:%(n)d"),
        winPrefix + " down [<n>]": Key(modKey + "-j:%(n)d"),
        winPrefix + " lock": Key("alt") + Key("s-q"),
        winPrefix + " full": Key(modKey + "-f"),
        winPrefix + " horizontal": Key(modKey + "-semicolon"),
        winPrefix + " vertical": Key(modKey + "-v"),
        winPrefix + " term": Key(modKey + "-enter"),
        winPrefix + " close": Key(modKey + "-q"),
        winPrefix + " launch": Key(modKey + "-d"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 10),
    ]
    defaults = {
        "n": 1,
    }
