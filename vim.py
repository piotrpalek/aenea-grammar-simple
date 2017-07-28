# commands for controlling various programs

from aenea import *

class VimRule(MappingRule):
    prefix = "vim "
    mapping = {
        prefix + "save": Text(":w"),
        prefix + "quit": Text(":q"),
        prefix + "save and quit": Text(":wq"),
        prefix + "force quit": Text(":q!"),
        prefix + "vertical split": Text(":vs "),
        prefix + "no highlight": Text(":noh"),

        prefix + "up": Key('c-u'),
        prefix + "down": Key('c-d'),
        prefix + "toggle": Key('c-w, c-w'),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
