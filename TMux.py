from aenea import *

class Rule(MappingRule):
    prefix = "tea "
    tmuxPrefix = "c-a"
    mapping = {
        prefix + "next": Key(tmuxPrefix + ", n"),
        prefix + "previous": Key(tmuxPrefix + ", p"),
        prefix + "new": Key(tmuxPrefix + ", c"),
        prefix + "kill": Key(tmuxPrefix + ", x"),
        prefix + "detach": Key(tmuxPrefix + ", d"),
        prefix + "<n>": Key(tmuxPrefix + ", %(n)d"),
        prefix + "pains": Key(tmuxPrefix + ", q"),
        prefix + "pain <n>": Key(tmuxPrefix + ", q, %(n)d"),
        prefix + "max": Key(tmuxPrefix + ", z"),
        prefix + "split": Key(tmuxPrefix + ", hyphen"),
        prefix + "horizontal split": Key(tmuxPrefix + ", bar"),
        prefix + "switch": Key(tmuxPrefix + ", o"),
        prefix + "scroll": Key(tmuxPrefix + ", lbracket"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 0, 5),
    ]
    defaults = {
        "n": 1,
    }
