# commands for controlling various programs

from aenea import *

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
        winPrefix + " full-screen": Key(modKey + "-f"),
        winPrefix + " horizontal": Key(modKey + "-h"),
        winPrefix + " vertical": Key(modKey + "-v"),
        winPrefix + " term": Key(modKey + "-enter"),
        winPrefix + " vertical term": Key(modKey + "-v, a-enter"),
        winPrefix + " horizontal term": Key(modKey + "-h, a-enter"),
        winPrefix + " close": Key(modKey + "s-q"),
        winPrefix + " launch": Key(modKey + "-d"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
