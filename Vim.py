from aenea import *

class VimRule(MappingRule):
    prefix = "(vim|them) "
    mapping = {
        prefix + "save": Text(":w\n"),
        prefix + "quit": Text(":q\n"),
        prefix + "save and quit": Text(":wq\n"),
        prefix + "force quit": Text(":q!\n"),
        prefix + "vertical split": Text(":vs "),
        prefix + "no highlight": Text(":noh\n"),
    }
    extras = [
        Dictation("text"),
    ]
