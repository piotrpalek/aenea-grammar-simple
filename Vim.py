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
        #prefix + "down": Key("c-d"),
        #prefix + "up": Key("c-u"),
        #prefix + "push": Key("c-rbracket"),
        #prefix + "pop": Key("c-t"),
    }
    extras = [
        Dictation("text"),
    ]
