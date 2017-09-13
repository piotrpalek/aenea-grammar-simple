from aenea import *

class FormatTypes:
    camelCase = 1
    pascalCase = 2
    snakeCase = 3
    squash = 4
    upperCase = 5
    lowerCase = 6
    dashify = 7
    dotify = 8
    spokenForm = 9
    sentenceCase = 10


def strip_dragon_info(text):
    newWords = []
    words = str(text).split(" ")
    for word in words:
        if word.startswith("\\backslash"):
            word = "\\"  # Backslash requires special handling.
        elif word.find("\\") > -1:
            word = word[:word.find("\\")]  # Remove spoken form info.
        newWords.append(word)
    return newWords


def extract_dragon_info(text):
    newWords = []
    words = str(text).split(" ")
    for word in words:
        if word.rfind("\\") > -1:
            pos = word.rfind("\\") + 1
            if (len(word) - 1) >= pos:
                word = word[pos:]  # Remove written form info.
            else:
                word = ""
        newWords.append(word)
    return newWords


def format_camel_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText == '':
            newText = word[:1].lower() + word[1:]
        else:
            newText = '%s%s' % (newText, word.capitalize())
    return newText


def format_pascal_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        newText = '%s%s' % (newText, word.capitalize())
    return newText


def format_snake_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = "_" + word  # Adds underscores between normal words.
        newText += word.lower()
    return newText


def format_dashify(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = "-" + word  # Adds dashes between normal words.
        newText += word.lower()
    return newText


def format_dotify(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = "." + word  # Adds dashes between normal words.
        newText += word.lower()
    return newText


def format_squash(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        newText = '%s%s' % (newText, word.lower())
    return newText


def format_sentence_case(text):
    newText = []
    words = strip_dragon_info(text)
    for word in words:
        if newText == []:
            newText.append(word.title())
        else:
            newText.append(word)
    return " ".join(newText)


def format_upper_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = " " + word  # Adds spacing between normal words.
        newText += word.upper()
    return newText


def format_lower_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            if newText[-1:] != "." and word[0:1] != ".":
                word = " " + word  # Adds spacing between normal words.
        newText += word.lower()
    return newText


def format_spoken_form(text):
    newText = ""
    words = extract_dragon_info(text)
    for word in words:
        if newText != "":
            word = " " + word
        newText += word
    return newText


FORMAT_TYPES_MAP = {
    FormatTypes.sentenceCase: format_sentence_case,
    FormatTypes.camelCase: format_camel_case,
    FormatTypes.pascalCase: format_pascal_case,
    FormatTypes.snakeCase: format_snake_case,
    FormatTypes.squash: format_squash,
    FormatTypes.upperCase: format_upper_case,
    FormatTypes.lowerCase: format_lower_case,
    FormatTypes.dashify: format_dashify,
    FormatTypes.dotify: format_dotify,
    FormatTypes.spokenForm: format_spoken_form,
}


def format_brief(brief, formatType=None):
		format_text(brief, formatType)

def format_vocab(vocab, formatType=None):
		format_text(vocab, formatType)

def format_text(text, formatType=None):
    if formatType:
        if type(formatType) != type([]):
            formatType = [formatType]
        result = ""
        method = None
        for value in formatType:
            if not result:
                if formatType == FormatTypes.spokenForm:
                    result = text.words
                else:
                    result = str(text)
            method = FORMAT_TYPES_MAP[value]
            result = method(result)
        Text("%(text)s").execute({"text": result})


def camel_case_text(text):
    """Formats dictated text to camel case.
    Example:
    "'camel case my new variable'" => "myNewVariable".
    """
    newText = format_camel_case(text)
    Text("%(text)s").execute({"text": newText})


def pascal_case_text(text):
    """Formats dictated text to pascal case.
    Example:
    "'pascal case my new variable'" => "MyNewVariable".
    """
    newText = format_pascal_case(text)
    Text("%(text)s").execute({"text": newText})


def snake_case_text(text):
    """Formats dictated text to snake case.
    Example:
    "'snake case my new variable'" => "my_new_variable".
    """
    newText = format_snake_case(text)
    Text("%(text)s").execute({"text": newText})


def squash_text(text):
    """Formats dictated text with whitespace removed.
    Example:
    "'squash my new variable'" => "mynewvariable".
    """
    newText = format_squash(text)
    Text("%(text)s").execute({"text": newText})


def uppercase_text(text):
    """Formats dictated text to upper case.
    Example:
    "'upper case my new variable'" => "MY NEW VARIABLE".
    """
    newText = format_upper_case(text)
    Text("%(text)s").execute({"text": newText})


def lowercase_text(text):
    """Formats dictated text to lower case.
    Example:
    "'lower case John Johnson'" => "john johnson".
    """
    newText = format_lower_case(text)
    Text("%(text)s").execute({"text": newText})

formatMap = {
    "(sentence|sense|since)": FormatTypes.sentenceCase,
    "camel": FormatTypes.camelCase,
    "prop": FormatTypes.pascalCase,
    "snake": FormatTypes.snakeCase,
    "yell snake": [FormatTypes.snakeCase, FormatTypes.upperCase],
    "yell": FormatTypes.upperCase,
    "whisper": FormatTypes.lowerCase,
    "squash": FormatTypes.squash,
    "yell squash": [FormatTypes.squash, FormatTypes.upperCase],
    "dashify": FormatTypes.dashify,
    "yell dashify": [FormatTypes.dashify, FormatTypes.upperCase],
    "dotify": FormatTypes.dotify,
    "yell dotify": [FormatTypes.dotify, FormatTypes.upperCase],
    "say": FormatTypes.spokenForm,
}

abbreviation = {
    "architecture": "arch",
    "administrator": "admin",
    "administrators": "admins",
    "application": "app",
    "applications": "apps",
    "argument": "arg",
    "arguments": "args",
    "attribute": "attr",
    "attributes": "attrs",
    "(authenticate|authentication)": "auth",
    "backup": "bak",
    "binary": "bin",
    "button": "btn",
    "character": "char",
    "class": "cls",
    "command": "cmd",
    "company": "com",
    "(config|configuration)": "cfg",
    "context": "ctx",
    "control": "ctrl",
    "database": "db",
    "(define|definition)": "def",
    "description": "desc",
    "(develop|development)": "dev",
    "(dictionary|dictation)": "dict",
    "(direction|directory)": "dir",
    "dynamic": "dyn",
    "education": "edu",
    "example": "ex",
    "execute": "exec",
    "exception": "exc",
    "expression": "exp",
    "(extension|extend)": "ext",
    "function": "func",
    "framework": "fw",
    "(initialize|initializer)": "init",
    "instance": "inst",
    "integer": "int",
    "iterate": "iter",
    "java archive": "jar",
    "javascript": "js",
    "keyword": "kw",
    "keyword arguments": "kwargs",
    "language": "lng",
    "library": "lib",
    "length": "len",
    "message": "msg",
    "memory": "mem",
    "mount": "mnt",
    "number": "num",
    "object": "obj",
    "okay": "ok",
    "package": "pkg",
    "parameter": "param",
    "parameters": "params",
    "performance": "perf",
    "pixel": "px",
    "position": "pos",
    "point": "pt",
    "pointer": "ptr",
    "previous": "prev",
    "property": "prop",
    "python": "py",
    "query string": "qs",
    "reference": "ref",
    "references": "refs",
    "(represent|representation)": "repr",
    "regular (expression|expressions)": "regex",
    "request": "req",
    "revision": "rev",
    "ruby": "rb",
    "session aidee": "sid",  # "session id" didn't work for some reason.
    "shell": "sh",
    "source": "src",
    "(special|specify|specific|specification)": "spec",
    "standard": "std",
    "standard in": "stdin",
    "standard out": "stdout",
    "string": "str",
    "structure": "struct",
    "(synchronize|synchronous)": "sync",
    "system": "sys",
    "tickle": "tcl",
    "terminal": "term",
    "utility": "util",
    "utilities": "utils",
    "temporary": "tmp",
    "text": "txt",
    "value": "val",
    "window": "win",
}

vocabulary = {
		"linux": "linux",
		"ubuntu": "ubuntu",
		"github": "github",
		"username": "mvilim",
		"name": "matthew vilim",
		"nickname": "matt",
		"first name": "matthew",
		"last name": "vilim",
		"(them|vim)": "vim",
		"(month|mutt)": "mutt",
		"github username": "matthewvilim",
}

class WordRule(MappingRule):
    mapping = {
				"<formatType> <text>": Function(format_text),
				"[<formatType>] brief <brief>": Function(format_brief, formatType=FormatTypes.lowerCase),
				"[<formatType>] vocab <vocab>": Function(format_vocab, formatType=FormatTypes.lowerCase),
    }
    extras = [
        Dictation("text"),
				Choice("formatType", formatMap),
        Choice('brief', abbreviation),
        Choice('vocab', vocabulary),
    ]
