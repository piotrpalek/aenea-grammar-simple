from aenea import *

class VimRule(MappingRule):
    prefix = "vine "
    mapping = {
        prefix + "save": Text(":w"),
        prefix + "quit": Text(":q"),
        prefix + "save and quit": Text(":wq"),
        prefix + "force quit": Text(":q!"),
        prefix + "vertical split": Text(":vs "),
        prefix + "no highlight": Text(":noh"),
    }
    extras = [
        Dictation("text"),
    ]
