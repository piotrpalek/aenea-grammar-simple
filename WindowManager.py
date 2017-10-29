# commands for controlling various programs

from aenea import *
from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
  typeables["semicolon"] = keyboard.get_typeable(char=';')

appCommand = {
    "chrome": "chromium-browser",
    "spotify": "spotify",
    "PDF reader": "zathura",
    "GTK wave": "gtkwave",
}

class WindowManagerRule(MappingRule):
    modKey = "a"
    winPrefix = "pain"
    mapping = {
        winPrefix + " <n>": Key(modKey + "-%(n)d"),
        "lake [<n>]": Key(modKey + "-h:%(n)d"),
        winPrefix + " move left [<n>]": Key(modKey + "s-h:%(n)d"),
        "rake [<n>]": Key(modKey + "-l:%(n)d"),
        winPrefix + " move right [<n>]": Key(modKey + "s-l:%(n)d"),
        winPrefix + " up [<n>]": Key(modKey + "-k:%(n)d"),
        winPrefix + " move up [<n>]": Key(modKey + "s-k:%(n)d"),
        winPrefix + " down [<n>]": Key(modKey + "-j:%(n)d"),
        winPrefix + " move down [<n>]": Key(modKey + "s-j:%(n)d"),
        winPrefix + " lock": Key("alt") + Key("s-q"),
        winPrefix + " max": Key(modKey + "-f"),
        winPrefix + " horizontal": Key(modKey + "-semicolon"),
        winPrefix + " vertical": Key(modKey + "-v"),
        winPrefix + " term": Key(modKey + "-enter"),
        winPrefix + " close": Key(modKey + "-q"),
        winPrefix + " launch": Key(modKey + "-d"),
        winPrefix + " launch <appCommand>": Key(modKey + "-d") + Text("%(appCommand)s") + Key("enter"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 0, 10),
        Choice("appCommand", appCommand),
    ]
    defaults = {
        "n": 1,
    }
