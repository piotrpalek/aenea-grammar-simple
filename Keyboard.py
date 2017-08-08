# commands for controlling various programs

from aenea import *

letterMap = {
    "(alpha|arch)": "a",
    "(bravo|brav) ": "b",
    "(charlie|turley|char) ": "c",
    "(delta|deal) ": "d",
    "(echo|eck) ": "e",
    "(foxtrot|fox) ": "f",
    "(golf|gang) ": "g",
    "(hotel|hot) ": "h",
    "(india|indigo|ish) ": "i",
    "(juliet|julia) ": "j",
    "(kilo) ": "k",
    "(lima|lion|line|lie) ": "l",
    "(mike) ": "m",
    "(november|noy) ": "n",
    "(Oscar|osh) ": "o",
    "(papa|poppa) ": "p",
    "(quebec|quiche|queen) ": "q",
    "(romeo|ree) ": "r",
    "(sierra|soy) ": "s",
    "(tango|tay) ": "t",
    "(uniform) ": "u",
    "(victor|van) ": "v",
    "(whiskey|wes) ": "w",
    "(x-ray) ": "x",
    "(yankee|yank) ": "y",
    "(zulu|zoo) ": "z",
}

upperLetterMap = {}
for letter in letterMap:
    upperLetterMap["sky " + letter] = letterMap[letter].upper()
letterMap.update(upperLetterMap)

symbolMap = {
    "bar": "bar",
    "dash": "hyphen",
    "(dot|dit)": "dot",
    "comma": "comma",
    "backslash": "backslash",
    "score": "underscore",
    "star": "asterisk",
    "colon": "colon",
    "(semicolon|semi-colon)": "semicolon",
    "at sym": "at",
    "quote": "dquote",
    "sote": "squote",
    "hash": "hash",
    "dollar": "dollar",
    "percent": "percent",
    "ampersand": "ampersand",
    "slash": "slash",
    "equal": "equal",
    "plus": "plus",
    "bang": "exclamation",
    "question": "question",
    "caret": "caret",
    "tilde": "tilde",
    "lang": "langle",
    "rang": "rangle",
    "lace": "lbrace",
    "race": "rbrace",
    "lack": "lbracket",
    "rack": "rbracket",
    "len": "lparen",
    "ren": "rparen",
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
        "(number|num) <num>": Text("%(num)d"),
        "scratch [<n>]": Key("backspace:%(n)d"),
        "act": Key("escape"),
        "ace": Key("space"),
        "slap": Key("enter"),
        "key <key>": Key("%(key)s"),
        "tab": Key("tab"),
        "troll <letters>": Key("ctrl:down/3, %(letters)s"),
        "shift <letters>": Key("shift:down/3, %(letters)s"),
        "alt <letters>": Key("alt:down/3, %(letters)s"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        IntegerRef("num", 0, 1000000),
        Choice("letters", letterMap),
        Choice("key", keyMap),
    ]
    defaults = {
        "n": 1,
    }
