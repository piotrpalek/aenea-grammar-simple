from aenea import *

class Rule(MappingRule):
    prefix = ""
    mapping = {
        # general commands
        prefix + "save": Key("space, f, s"),
        prefix + "quit": Key("space, q, q"),
        prefix + "save and quit": Key("space, q, s"),
        prefix + "split": Key("space, w, slash"),
        prefix + "split horizon": Key("space, w, minus"),
        prefix + "nope": Key("c-g"),
        # window / buffer
        prefix + "tree focus": Key("space, f, T"),
        prefix + "tree toggle": Key("space, f, t"),
        prefix + "win close": Key("space, w, d"),
        prefix + "win right": Key("space, w, l"),
        prefix + "win left": Key("space, w, h"),
        prefix + "win up": Key("space, w, k"),
        prefix + "win down": Key("space, w, j"),
        prefix + "win one": Key("space, 1"),
        prefix + "win two": Key("space, 2"),
        prefix + "win three": Key("space, 3"),
        prefix + "swap": Key("space, tab"),
        prefix + "switch": Key("space, w, tab"),
        # carret navigation
        prefix + "jump": Key("space, j, w"),
        prefix + "jump tee": Key("space, j, j"),
        prefix + "jump line": Key("space, j, l"),
        prefix + "jump back": Key("c-o"),
        prefix + "up": Key("c-u"),
        prefix + "down": Key("c-d"),
        prefix + "find [<queryString>]": Key("c-g, slash") + Text("%(queryString)s"),
        prefix + "(begin|beginning)": Key("c-g, g, g"),
        prefix + "end": Key("c-g, s-g"),
        # editing
        prefix + "indent": Key("space, equals"),
        prefix + "copy line": Key("y, y"),
        prefix + "delete line": Key("d, d"),
        prefix + "delete above": Key("m, m, colon, hyphen, d, enter, backtick, m"),
        prefix + "delete below": Key("m, m, colon, plus, d, enter, backtick, m"),
        prefix + "expand [<num>]": Key("%(num)d, space, v"),
        # helm
        prefix + "cow [<queryString>]": Key("c-g, space, p, f") + Text("%(queryString)s"),
        prefix + "suck [<queryString>]": Key("c-g, space, s, p") + Text("%(queryString)s"),
        prefix + "perspective one": Key("space, l, 1"),
        prefix + "perspective two": Key("space, l, 2"),
        prefix + "perspective (three|tree)": Key("space, l, 3"),
        prefix + "perspective four": Key("space, l, 4"),
        prefix + "pick <num>": Key("c-c, %(num)d"),
        prefix + "snippet [<queryString>]": Key("space, i, s") + Text("%(queryString)s"),
        prefix + "nuke <queryString>": Key("c, i, %(queryString)s"),
        prefix + "mini reopen": Key("space, s, l"),
        # misc
        prefix + "no highlight": Key("space, s, c"),
        # ember
        prefix + "handle (curly|currently)": Text("{{}}") + Key("left, left"),
    }
    extras = [
        Dictation("text"),
        Dictation("queryString"),
        IntegerRef("num", 0, 10),
    ]
    defaults = {
        "queryString": "",
    }

RuleContext = ProxyAppContext(title = "emacs@devsys")
