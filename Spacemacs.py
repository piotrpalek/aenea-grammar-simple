from aenea import *

class SpacemacsRule(MappingRule):
    prefix = "(j|jay) "
    mapping = {
        prefix + "save": Key("space, f, s"),
        prefix + "quit": Key("space, q, q"),
        prefix + "save and quit": Key("space, q, s"),
        prefix + "split": Key("space, w, slash"),
        prefix + "split horizon": Key("space, w, minus"),
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
        prefix + "no highlight": Key("space, s, c"),
        prefix + "switch": Key("space, tab"),
        prefix + "indent": Key("space, equals"),
        prefix + "jump": Key("space, j, j"),
        prefix + "jump word": Key("space, j, w"),
        prefix + "jump line": Key("space, j, l"),
        prefix + "jump back": Key("space, j, b"),
        prefix + "pee find": Key("space, p, f"),
        prefix + "clutch": Key("c-g"),
    }
    extras = [
        Dictation("text"),
    ]
