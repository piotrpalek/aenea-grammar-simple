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

tmuxCommandArray = [
    'new',
    'list',
    'attach',
]
tmuxCommand = {}
for command in tmuxCommandArray:
    tmuxCommand[command] = command

class TerminalRule(MappingRule):
    prefix = "term "
    mapping = {
        prefix + "sudo": Text("sudo "),
        prefix + "vim": Text("vim "),
        prefix + "direct": Text("cd "),
        prefix + "copy": Text("cp "),
        prefix + "list": Text("ls "),
        prefix + "make": Text("make "),
        prefix + "(grep|grip)": Text("grep "),
        prefix + "move": Text("mv "),
        prefix + "remove": Text("rm "),
        prefix + "(git|get) <gitCommand>": Text("git %(gitCommand)s "),
        prefix + "mux <tmuxCommand>": Text("tmux %(tmuxCommand)s "),
        prefix + "kill": Key("c-c"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('gitCommand', gitCommand),
        Choice('tmuxCommand', tmuxCommand),
    ]
    defaults = {
        "n": 1,
    }
