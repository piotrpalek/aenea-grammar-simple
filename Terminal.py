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

tmuxCommand= {
    'new': 'new',
    'list': 'ls',
    'attach': 'attach',
}

aptCommandArray = [
    'update',
    'install',
    'remove',
]
aptCommand = {}
for command in aptCommandArray:
    aptCommand[command] = command

class TerminalRule(MappingRule):
    prefix = "term "
    mapping = {
        prefix + "sudo": Text("sudo "),
        prefix + "apt <aptCommand>": Text("apt %(aptCommand)s "),
        prefix + "vim": Text("vim "),
        prefix + "direct": Text("cd "),
        prefix + "copy": Text("cp "),
        prefix + "list": Text("ls "),
        prefix + "make": Text("make "),
        prefix + "man": Text("man "),
        prefix + "mutt": Text("mutt "),
        prefix + "(grep|grip)": Text("grep "),
        prefix + "move": Text("mv "),
        prefix + "remove": Text("rm "),
        prefix + "make direct": Text("mkdir "),
        prefix + "remove direct": Text("rmdir "),
        prefix + "(git|get) <gitCommand>": Text("git %(gitCommand)s "),
        prefix + "see tags": Text("ctags"),
        prefix + "teamux <tmuxCommand>": Text("tmux %(tmuxCommand)s "),
        prefix + "mount": Text("mount "),
        prefix + "umount": Text("umount "),
        prefix + "i three message": Text("i3-msg "),
        prefix + "secure shell": Text("ssh "),
        prefix + "exit": Text("exit "),
    }
    extras = [
        Dictation("text"),
        Choice('aptCommand', aptCommand),
        Choice('gitCommand', gitCommand),
        Choice('tmuxCommand', tmuxCommand),
    ]
