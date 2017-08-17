# commands for controlling various programs

from aenea import *

letterMap = {
    "ark": "a",
    "brave": "b",
    "car": "c",
    "deal": "d",
    "end": "e",
    "fox": "f",
    "gag": "g",
    "hit": "h",
    "itch": "i",
    "jab": "j",
    "kill": "k",
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
    "veil": "v",
    "whisk": "w",
    "xerox": "x",
    "yank": "y",
    "zoo": "z",
}

upperLetterMap = {}
for letter in letterMap:
    upperLetterMap["sky " + letter] = letterMap[letter].upper()
letterMap.update(upperLetterMap)

symbolMap = {
    "bar": "bar",
    "dash": "hyphen",
    "dot": "dot",
    "comma": "comma",
    "blash": "backslash",
    "score": "underscore",
    "star": "asterisk",
    "coal": "colon",
    "soul": "semicolon",
    "at": "at",
    "quote": "dquote",
    "sote": "squote",
    "hash": "hash",
    "doll": "dollar",
    "purse": "percent",
    "amp": "ampersand",
    "slash": "slash",
    "equal": "equal",
    "plus": "plus",
    "bang": "exclamation",
    "quest": "question",
    "carrot": "caret",
    "tile": "tilde",
    "lang": "langle",
    "rang": "rangle",
    "lace": "lbrace",
    "race": "rbrace",
    "lack": "lbracket",
    "rack": "rbracket",
    "lair": "lparen",
    "rare": "rparen",
    "scratch": "backspace",
}
letterMap.update(symbolMap)

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
}

class KeyboardRule(MappingRule):
    mapping = {
        "<letters>": Key("%(letters)s"),
        "num <num>": Text("%(num)d"),
        "scratch [<n>]": Key("backspace:%(n)d"),
        "cape": Key("escape"),
        "ace": Key("space"),
        "slap": Key("enter"),
        "key <key>": Key("%(key)s"),
        "tab": Key("tab"),
        "train <letters>": Key("ctrl:down/3, %(letters)s"),
        "shift <letters>": Key("shift:down/3, %(letters)s"),
        "alt <letters>": Key("alt:down/3, %(letters)s"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        IntegerRef("num", 0, 10000),
        Choice("letters", letterMap),
        Choice("key", keyMap),
    ]
    defaults = {
        "n": 1,
    }
