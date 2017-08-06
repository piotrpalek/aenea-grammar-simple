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
        winPrefix + " <n>": Key(modKey + "-%(n)d"),
        winPrefix + " left": Key(modKey + "-j"),
        winPrefix + " right": Key(modKey + "-semicolon"),
        winPrefix + " up": Key(modKey + "-l"),
        winPrefix + " down": Key(modKey + "-k"),
        winPrefix + " lock": Key(modKey + "-d") + Text("i3lock") + Key("enter"),
        winPrefix + " full": Key(modKey + "-f"),
        winPrefix + " horizontal": Key(modKey + "-h"),
        winPrefix + " vertical": Key(modKey + "-v"),
        winPrefix + " term": Key(modKey + "-enter"),
        winPrefix + " vertical term": Key(modKey + "-v, a-enter"),
        winPrefix + " horizontal term": Key(modKey + "-h, a-enter"),
        winPrefix + " close": Key(modKey + "-q"),
        winPrefix + " launch": Key(modKey + "-d"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
