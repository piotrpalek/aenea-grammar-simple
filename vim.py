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

        prefix + "file": Key('c-g'),
        prefix + "redo": Key('c-r'),
        prefix + "up": Key('c-u'),
        prefix + "down": Key('c-d'),
        prefix + "toggle": Key('c-w, c-w'),
        prefix + "push": Key('c-rbracket'),
        prefix + "pop": Key('c-t'),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
