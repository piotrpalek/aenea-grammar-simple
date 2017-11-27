from aenea import *

class Rule(MappingRule):
    prefix = ""
    mapping = {
        prefix + "new": Key("c-t"),
        prefix + "close": Key("c-w"),
        prefix + "reload": Key("c-r"),
        prefix + "open localhost 4000": Key("c-l") + Text("http://localhost:4200/") + Key("enter"),
        prefix + "show [<n>]": Key("c-%(n)d"),
        prefix + "right [<n>]": Key("c-tab:%(n)d"),
        prefix + "left [<n>]": Key("cs-tab:%(n)d"),
        prefix + "inspect": Key("cs-c"),
        prefix + "back": Key("a-left"),
        prefix + "next": Key("a-right"),
        prefix + "reopen": Key("cs-t"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 9),
    ]
    defaults = {
        "n": 1
    }

RuleContext = ProxyAppContext(title = "Google Chrome")
