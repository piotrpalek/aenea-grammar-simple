# commands for controlling various programs

from aenea import *

letterMap = {
    "arc": "a",
    "brave": "b",
    "carve": "c",
    "dive": "d",
    "edge": "e",
    "fox": "f",
    "gauge": "g",
    "hit": "h",
    "inch": "i",
    "jab": "j",
    "kick": "k",
    "lime": "l",
    "mike": "m",
    "noun": "n",
    "ork": "o",
    "poke": "p",
    "queen": "q",
    "ram": "r",
    "sink": "s",
    "tear": "t",
    "unit": "u",
    "verge": "v",
    "whisk": "w",
    "xerox": "x",
    "yank": "y",
    "zoo": "z",
}

symbolMap = {
    "spike": "bar",
    "mine": "hyphen",
    "dot": "dot",
    "drip": "comma",
    "crazy": "backslash",
    "score": "underscore",
    "star": "asterisk",
    "coal": "colon",
    "soul": "semicolon",
    "loco": "at",
    "dear": "dquote",
    "seer": "squote",
    "pounder": "hash",
    "dolly": "dollar",
    "percy": "percent",
    "amper": "ampersand",
    "lazy": "slash",
    "equal": "equal",
    "plus": "plus",
    "clamor": "exclamation",
    "quest": "question",
    "carrot": "caret",
    "tilde": "tilde",
    "lang": "langle",
    "rang": "rangle",
    "lace": "lbrace",
    "race": "rbrace",
    "lack": "lbracket",
    "rack": "rbracket",
    "len": "lparen",
    "ren": "rparen",
    "slap": "enter",
    "gap": "space",
    "tab": "tab",
}

def formatGap(symbols, repeat, gap):
    format = "%(s)s:%(r)d"
    if gap == GapTypes.gap or gap == GapTypes.lap:
        format = "space, " + format
    if gap == GapTypes.gap or gap == GapTypes.rap:
        format = format + ", space"
    Key(format).execute({"s": symbols, "r": repeat})

def formatLetter(sky, letters, repeat):
    l = letters
    if sky:
        l = letters.upper()
    Key("%(l)s:%(r)d").execute({"l": l, "r": repeat})

operators = [
    "bar",
    "hyphen",
    "asterisk",
    "percent",
    "slash",
    "equal",
    "plus",
    "caret",
]

keyMap = {
    'F one': 'f1',
    'F two': 'f2',
    'F three': 'f3',
    'F four': 'f4',
    'F five': 'f5',
    'F six': 'f6',
    'F seven': 'f7',
    'F eight': 'f8',
    'F nine': 'f9',
    'F ten': 'f10',
    'F eleven': 'f11',
    'F twelve': 'f12',
    'insert': 'insert',
    'up': 'up',
    'down': 'down',
    'right': 'right',
    'left': 'left',
    'page up': 'pgup',
    'page down': 'pgdown',
}

repeatMap = {
  "wink": 2,
  "blink": 3
}
 
class GapTypes:
    lap = 1
    rap = 2
    gap = 3
    none = 4

gapMap = {
    "lash": GapTypes.lap,
    "rash": GapTypes.rap,
    "gash": GapTypes.gap,
}

skyMap = {
    "yell": True,
}

class KeyboardRule(MappingRule):
    mapping = {
        "[<sky>] <letters> [<repeat>]": Function(formatLetter),
        "<symbols> [<repeat>] [<gap>]": Function(formatGap),
        "numb <num>": Text("%(num)d"),
        "scratch [<n>]": Key("backspace:%(n)d"),
        "break": Key("escape"),
        "key <key>": Key("%(key)s"),
        "train": Key("ctrl:down/3"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
        IntegerRef("num", 0, 10000),
        Choice("letters", letterMap),
        Choice("symbols", symbolMap),
        Choice("key", keyMap),
        Choice("repeat", repeatMap),
        Choice("gap", gapMap),
        Choice("sky", skyMap),
    ]
    defaults = {
        "n": 1,
        "repeat": 1,
        "gap": GapTypes.none,
        "sky": False,
    }
