from aenea import *

abbreviation = {
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
    "class": "cls",
    "command": "cmd",
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
    "number": "num",
    "object": "obj",
    "okay": "ok",
    "package": "pkg",
    "parameter": "param",
    "parameters": "params",
    "pixel": "px",
    "position": "pos",
    "point": "pt",
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
    "source": "src",
    "(special|specify|specific|specification)": "spec",
    "standard": "std",
    "standard in": "stdin",
    "standard out": "stdout",
    "string": "str",
    "(synchronize|synchronous)": "sync",
    "system": "sys",
    "tickle": "tcl",
    "utility": "util",
    "utilities": "utils",
    "temporary": "tmp",
    "text": "txt",
    "value": "val",
    "window": "win",
}
class AbbreviateRule(MappingRule):
    mapping = {
      "brief <abbreviation>": Text("%(abbreviation)s"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('abbreviation', abbreviation),
    ]
    defaults = {
        "n": 1,
    }
