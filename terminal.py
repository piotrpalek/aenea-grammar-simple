# commands for controlling various programs

from aenea import *

gitCommandArray = [
    'add',
    'branch',
    'checkout',
    'clone',
    'commit',
    'diff',
    'fetch',
    'init',
    'log',
    'merge',
    'pull',
    'push',
    'rebase',
    'reset',
    'show',
    'stash',
    'status',
    'tag',
]
gitCommand = {}
for command in gitCommandArray:
    gitCommand[command] = command

class TerminalRule(MappingRule):
    prefix = "term "
    mapping = {
        prefix + "vim": Text("vim "),
        prefix + "dir": Text("cd "),
        prefix + "copy": Text("cp "),
        prefix + "list": Text("ls "),
        prefix + "make": Text("make "),
        prefix + "(grep|grip)": Text("grep "),
        prefix + "remove": Text("rm "),
        prefix + "(git|get) <gitCommand>": Text("git %(gitCommand)s "),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('gitCommand', gitCommand),
    ]
    defaults = {
        "n": 1,
    }
