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
    'detach': 'detach',
    'kill session': 'kill-session',
}

aptCommandArray = [
    'update',
    'install',
    'remove',
]
aptCommand = {}
for command in aptCommandArray:
    aptCommand[command] = command

def directoryUp(n=1):
    command = "cd "
    s = "../"
    for i in range(0, n):
        command = command + s
    Text("%(command)s").execute({"command": command})

class TerminalRule(MappingRule):
    prefix = "shell "
    mapping = {
        prefix + "sudo": Text("sudo "),
        prefix + "apt <aptCommand>": Text("apt %(aptCommand)s "),
        prefix + "(them|vim)": Text("vim "),
        prefix + "direct": Text("cd "),
        prefix + "direct up [<n>]": Function(directoryUp),
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
        prefix + "tea (mucks|box|monks) <tmuxCommand>": Text("tmux %(tmuxCommand)s "),
        prefix + "mount": Text("mount "),
        prefix + "umount": Text("umount "),
        prefix + "i three message": Text("i3-msg "),
        prefix + "SSH": Text("ssh "),
        prefix + "exit": Text("exit"),
        prefix + "change mode": Text("chmod "),
        prefix + "VPN": Text("vpn"),
        prefix + "less": Text("less "),
        prefix + "GTK wave": Text("gtkwave "),
        prefix + "ping": Text("ping "),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 8),
        Choice('aptCommand', aptCommand),
        Choice('gitCommand', gitCommand),
        Choice('tmuxCommand', tmuxCommand),
    ]
    default = {
        "n": 1,
    }
