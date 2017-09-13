# commands for controlling various programs

from aenea import *

letterMap = {
    "ark": "a",
    "brave": "b",
    "carve": "c",
    "dive": "d",
    "edge": "e",
    "fox": "f",
    "gag": "g",
    "hit": "h",
    "inch": "i",
    "jab": "j",
    "kin": "k",
    "lime": "l",
    "mike": "m",
    "noy": "n",
    "osh": "o",
    "poke": "p",
    "queen": "q",
    "ram": "r",
    "soy": "s",
    "tay": "t",
    "unit": "u",
    "verge": "v",
    "whisk": "w",
    "xerox": "x",
    "yarn": "y",
    "zoo": "z",
}

upperLetterMap = {}
for letter in letterMap:
    upperLetterMap["sky " + letter] = letterMap[letter].upper()
letterMap.update(upperLetterMap)

symbolMap = {
    "spike": "bar",
    "mine": "hyphen",
    "dot": "dot",
    "comma": "comma",
    "blash": "backslash",
    "score": "underscore",
    "star": "asterisk",
    "coal": "colon",
    "soul": "semicolon",
    "loco": "at",
    "quote": "dquote",
    "sote": "squote",
    "hash": "hash",
    "dolly": "dollar",
    "percy": "percent",
    "amper": "ampersand",
    "slash": "slash",
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
    "ace": "space",
    "tab": "tab",
}

def formatGap(symbols, repeat, gap):
    format = "%(s)s:%(r)d"
    if gap:
        if symbols in operators:
            format = "space, " + format
        format = format + ", space"
    Key(format).execute({"s": symbols, "r": repeat})

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
 
gapMap = {
    "gap": True,
}

class KeyboardRule(MappingRule):
    mapping = {
        "<letters> [<repeat>]": Key("%(letters)s:%(repeat)d"),
        "<symbols> [<repeat>] [<gap>]": Function(formatGap),
        "numb <num>": Text("%(num)d"),
        "scratch [<n>]": Key("backspace:%(n)d"),
        "cape": Key("escape"),
        "key <key>": Key("%(key)s"),
        "train": Key("ctrl:down/3"),
        "alt": Key("alt:down/3"),
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
    ]
    defaults = {
        "n": 1,
        "repeat": 1,
        "gap": False,
    }
