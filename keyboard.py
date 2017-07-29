# Low-level keyboard input module
#
# Based on the work done by the creators of the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# and _multiedit-en.py found at:
# http://dragonfly-modules.googlecode.com/svn/trunk/command-modules/documentation/mod-_multiedit.html
#
# Modifications by: Tony Grosinger
#
# Licensed under LGPL

from natlink import setMicState
from aenea import (
    Grammar,
    MappingRule,
    Text,
    Key,
    Mimic,
    Function,
    Dictation,
    Choice,
    Window,
    Config,
    Section,
    Item,
    IntegerRef,
    Alternative,
    RuleRef,
    Repetition,
    CompoundRule,
    AppContext,
)

from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')

def cancel_and_sleep(text=None, text2=None):
    """Used to cancel an ongoing dictation and puts microphone to sleep.

    This method notifies the user that the dictation was in fact canceled,
     a message in the Natlink feedback window.
    Then the the microphone is put to sleep.
    Example:
    "'random mumbling go to sleep'" => Microphone sleep.

    """
    print("* Dictation canceled. Going to sleep. *")
    setMicState("sleeping")


# For repeating of characters.
specialCharMap = {
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
    "sing quote": "'",
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

# generate uppercase versions of every letter
upperLetterMap = {}
for letter in letterMap:
    upperLetterMap["sky " + letter] = letterMap[letter].upper()
letterMap.update(upperLetterMap)

numberMap = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

controlKeyMap = {
    "space": "space",
    "tab": "tab",
}

# F1 to F12. (do these actually work?)
functionKeyMap = {
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
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(functionKeyMap)


grammarCfg = Config("multi edit")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(
    {
        # Functional keys.
        "act": Key("escape"),
        "space": Key("space"),
        "space [<n>]": Key("space:%(n)d"),
        "(enter|slap|slop) [<n>]": Key("enter:%(n)d"),
        "tab [<n>]": Key("tab:%(n)d"),
        "select all": Key("c-a/3"),
        # Closures.
        "angle brackets": Key("langle, rangle, left/3"),
        "[square] brackets": Key("lbracket, rbracket, left/3"),
        "[curly] braces": Key("lbrace, rbrace, left/3"),
        "(parens|parentheses)": Key("lparen, rparen, left/3"),
        "quotes": Key("dquote/3, dquote/3, left/3"),
        "backticks": Key("backtick:2, left"),
        "single quotes": Key("squote, squote, left/3"),
        # Punctuation and separation characters, for quick editing.
        "colon [<n>]": Key("colon/2:%(n)d"),
        "semi-colon [<n>]": Key("semicolon/2:%(n)d"),
        "comma [<n>]": Key("comma/2:%(n)d"),
        "(dot|period|dit|point)": Key("dot"),  # cannot be followed by a repeat count
        "(dash|hyphen|minus) [<n>]": Key("hyphen/2:%(n)d"),
        "underscore [<n>]": Key("underscore/2:%(n)d"),
        "<letters>": Text("%(letters)s"),
        "<char>": Text("%(char)s"),

        'langle [<n>]': Key('langle:%(n)d'),
        'lace [<n>]':   Key('lbrace:%(n)d'),
        '(lack|lair) [<n>]':   Key('lbracket:%(n)d'),
        'len [<n>]':    Key('lparen:%(n)d'),
        'rangle [<n>]': Key('rangle:%(n)d'),
        'race [<n>]':   Key('rbrace:%(n)d'),
        '(rack|rare) [<n>]':   Key('rbracket:%(n)d'),
        '(ren|wren) [<n>]':   Key('rparen:%(n)d'),

        'scratch [<n>]':     Key('backspace:%(n)d'),

        '(number|num) <num>': Text("%(num)d"),

        "[<text>] (go to sleep|cancel and sleep) [<text2>]": Function(cancel_and_sleep),  # @IgnorePep8
    },
    namespace={
        "Key": Key,
        "Text": Text,
    }
)


class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 100),
        IntegerRef("num", 0, 1000000),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("letters", letterMap),
        Choice("pressKey", pressKeyMap),
    ]
    defaults = {
        "n": 1,
    }


