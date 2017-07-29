from aenea import *

class VocabularyRule(MappingRule):
    prefix = "vocab "
    mapping = {
        prefix + "github": Text("github"),
        prefix + "first name": Text("matthew"),
        prefix + "last name": Text("vilim"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
