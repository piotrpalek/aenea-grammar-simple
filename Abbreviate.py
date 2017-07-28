from aenea import *

abbreviation = {
    'temp': 'tmp',
    'binary': 'bin',
    'object': 'obj',
}

class AbbreviateRule(MappingRule):
    mapping = {
      "brief <abbreviation>": Text("%(abbreviation)s"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('abbreviation', abbreviation),
    ]
    defaults = {
        "n": 1,
    }
