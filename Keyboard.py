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
    "bar": "|",
    "dash": "-",
    "(dot|dit)": ".",
    "comma": ",",
    "backslash": "\\",
    "score": "_",
    "star": "*",
    "colon": ":",
    "(semicolon|semi-colon)": ";",
    "at sym": "@",
    "quote": '"',
    "sote": "'",
    "hash": "#",
    "dollar": "$",
    "percent": "%",
    "ampersand": "&",
    "slash": "/",
    "equal": "=",
    "plus": "+",

    "bang": "!",
    "question": "?",
    "caret": "^",
    "tilde": "~",
}

bracketMap = {
    "langle": "langle",
    "lace": "lbrace",
    "lack": "lbracket",
    "len": "lparen",
    "rangle": "rangle",
    "race": "rbrace",
    "rack": "rbracket",
    "ren": "rparen",
}

class KeyboardRule(MappingRule):
    mapping = {
        "<letters>": Text("%(letters)s"),
        "<symbols>": Text("%(symbols)s"),
        "<brackets>": Key("%(brackets)s"),
        "(number|num) <num>": Text("%(num)d"),
        "scratch [<n>]": Key("backspace:%(n)d"),
        "act": Key("escape"),
        "space": Key("space"),
        "slap": Key("enter"),
        "tab": Key("tab"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        IntegerRef("num", 0, 1000000),
        Choice("letters", letterMap),
        Choice("symbols", symbolMap),
        Choice("brackets", bracketMap),
    ]
    defaults = {
        "n": 1,
    }
