from aenea import *

class VocabularyRule(MappingRule):
    prefix = "vocab "
    mapping = {
        prefix + "linux": Text("linux"),
        prefix + "ubuntu": Text("ubuntu"),
        prefix + "github": Text("github"),
        prefix + "username": Text("mvilim"),
        prefix + "nickname": Text("matt"),
        prefix + "first name": Text("matthew"),
        prefix + "last name": Text("vilim"),
        prefix + "(them|vim)": Text("vim"),
        prefix + "(month|mutt)": Text("mutt"),
        prefix + "github username": Text("matthewvilim"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
