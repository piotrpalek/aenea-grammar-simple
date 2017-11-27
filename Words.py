from aenea import *
import Keyboard

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


def format_brief(brief, formatType, gap):
		format_text(brief, formatType, gap)

def format_vocab(vocab, formatType, gap):
		format_text(vocab, formatType, gap)

def format_exception(exception, formatType, gap):
		format_text(exception, formatType, gap)

lastFormatLength = 0
def format_text(text, formatType, gap):
    global lastFormatLength
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
        if gap == Keyboard.GapTypes.gap or gap == Keyboard.GapTypes.lap:
            result = " " + result
        if gap == Keyboard.GapTypes.gap or gap == Keyboard.GapTypes.rap:
            result = result + " "
        Text("%(text)s").execute({"text": result})
        lastFormatLength = len(result)

def format_scratch():
    global lastFormatLength
    Key("backspace:" + str(lastFormatLength)).execute()


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
    "sentence": FormatTypes.sentenceCase,
    "camel": FormatTypes.camelCase,
    "pacify": FormatTypes.pascalCase,
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
    "dictate": FormatTypes.spokenForm,
}

abbreviation = {
    "architecture": "arch",
    "asynchronous": "async",
    "administrator": "admin",
    "address": "addr",
    "application": "app",
    "approximate": "approx",
    "argument": "arg",
    "arguments": "args",
    "attribute": "attr",
    "attributes": "attrs",
    "(authenticate|authentication)": "auth",
    "backup": "bak",
    "binary": "bin",
    "bibliography": "bib",
    "boolean": "bool",
    "button": "btn",
    "ceiling": "ceil",
    "character": "char",
    "class": "cls",
    "command": "cmd",
    "company": "com",
    "(config|configuration)": "cfg",
    "context": "ctx",
    "control": "ctrl",
    "see plus plus": "cpp",
    "copy": "cpy",
    "database": "db",
    "debug": "dbg",
    "(define|definition)": "def",
    "dequeue": "deq",
    "description": "desc",
    "(develop|development)": "dev",
    "(dictionary|dictation)": "dict",
    "(direction|directory)": "dir",
    "dynamic": "dyn",
    "education": "edu",
    "enable": "en",
    "enqueue": "enq",
    "environment": "env",
    "example": "ex",
    "execute": "exec",
    "exception": "exc",
    "expression": "exp",
    "(extension|extend)": "ext",
    "function": "func",
    "framework": "fw",
    "fraction": "frac",
    "(generate|general)": "gen",
    "homework": "hw",
    "(initialize|initializer)": "init",
    "in out": "io",
    "(instance|instruction)": "inst",
    "integer": "int",
    "iterate": "iter",
    "java archive": "jar",
    "javascript": "js",
    "keyword": "kw",
    "language": "lang",
    "latex": "tex",
    "library": "lib",
    "line": "ln",
    "length": "len",
    "message": "msg",
    "memory": "mem",
    "mount": "mnt",
    "modify": "mod",
    "multiplexer": "mux",
    "number": "num",
    "object": "obj",
    "okay": "ok",
    "operating system": "os",
    "package": "pkg",
    "parameter": "param",
    "parameters": "params",
    "performance": "perf",
    "pixel": "px",
    "position": "pos",
    "point": "pt",
    "pointer": "ptr",
    "power": "pow",
    "previous": "prev",
    "property": "prop",
    "python": "py",
    "read": "rd",
    "reference": "ref",
    "register": "reg",
    "(represent|representation)": "repr",
    "regular (expression|expressions)": "regex",
    "request": "req",
    "response": "resp",
    "revision": "rev",
    "select": "sel",
    "shell": "sh",
    "simulate": "sim",
    "source": "src",
    "(special|specify|specific|specification)": "spec",
    "square root": "sqrt",
    "standard": "std",
    "standard in": "stdin",
    "standard out": "stdout",
    "string": "str",
    "structure": "struct",
    "(synchronize|synchronous)": "sync",
    "synthesize": "synth",
    "system": "sys",
    "tickle": "tcl",
    "terminal": "term",
    "utility": "util",
    "utilities": "utils",
    "temp": "tmp",
    "temporary": "temp",
    "text": "txt",
    "value": "val",
    "valid": "vld",
    "variable": "var",
    "vector": "vec",
    "window": "win",
    "write": "wr",
}

vocabulary = {
		"bit": "bit",
		"byte": "byte",
		"ram": "ram",
		"D ram": "dram",
		"S ram": "sram",
		"(linux|lenox|the next)": "linux",
		"ubuntu": "ubuntu",
		"github": "github",
		"username": "piotrpalek",
		"name": "Piotr Palek",
		"nickname": "peter",
		"first name": "Piotr",
		"last name": "Palek",
		"(them|vim)": "vim",
		"(get|git)": "git",
		"(month|mutt)": "mutt",
		"github username": "piotrpalek",
		"argon": "argon",
		"spatial": "spatial",
		"(scala|scholar)": "scala",
		"fifoe": "fifo",
		"tucson": "tucson",
		"(lou|laura|lula)": "lua",
		"null": "null",
		"let": "let",
		"nil": "nil",
		"class": "class",
		"true": "true",
		"false": "false",
		"case": "case",
		"write": "write",
		"new": "new",
		"if": "if",
		"then": "then",
		"end": "end",
		"else": "else",
		"for": "for",
		"in": "in",
		"function": "function",
		"while": "while",
		"break": "break",
		"continue": "continue",
		"extends": "extends",
		"match": "match",
		"override": "override",
		"for each": "foreach",
		"float": "float",
		"auto": "auto",
		"do": "do",
		"double": "double",
		"static": "static",
		"void": "void",
		"go to": "goto",
		"return": "return",
		"switch": "switch",
		"union": "union",
		"abstract": "abstract",
		"import": "import",
		"private": "private",
		"public": "public",
		"protected": "protected",
		"module": "module",
		"wire": "wire",
		"bundle": "bundle",
		"interface": "interface",
		"package": "package",
		"this": "this",
		"super": "super",
		"catch": "catch",
		"try": "try",
		"boolean": "boolean",
		"assert": "assert",
		"global": "global",
		"local": "local",
		"self": "self",
}

css = {
    "flex": "flex"
}

exception = {
  "phil": "fill",
  "pear": "pair",
}

class Rule(MappingRule):
    mapping = {
				"<formatType> <text> [stop] [<gap>]": Function(format_text),
				"<formatType> <exception> [<gap>]": Function(format_exception),
				"[<formatType>] brief <brief> [<gap>]": Function(format_brief),
				"[<formatType>] cab <vocab> [<gap>]": Function(format_vocab),
				"CSS <css>": Text("%(css)s"),
				"scratch that": Function(format_scratch),
    }
    extras = [
        Dictation("text"),
        Choice("formatType", formatMap),
        Choice('brief', abbreviation),
        Choice('exception', exception),
        Choice('vocab', vocabulary),
        Choice('css', css),
        Choice('gap', Keyboard.gapMap),
    ]
    defaults = {
        "formatType": FormatTypes.lowerCase,
        "gap": Keyboard.GapTypes.none,
    }
