# commands for controlling various programs

from aenea import *

gitCommand = {
    'add': 'add',
    '(amen|amend)': 'commit --amend',
    'branch': 'branch',
    'checkout': 'checkout',
    'clone': 'clone',
    'commit': 'commit',
    'diff': 'diff',
    'difftool': 'difftool',
    'fetch': 'fetch',
    'init': 'init',
    'log': 'log',
    'log P': 'log -p',
    'merge': 'merge',
    'pull': 'pull',
    'push': 'push',
    'rebase': 'rebase',
    'reset': 'reset',
    'show': 'show',
    'stash': 'stash',
    'status': 'status',
    'tag': 'tag',
    'remote': 'remote -v',
}

def directoryUp(n=1):
    command = "cd "
    s = "../"
    for i in range(0, n):
        command = command + s
    Text("%(command)s").execute({"command": command})

class Rule(MappingRule):
    prefix = ""
    mapping = {
        prefix + "sudo": Text("sudo "),
        prefix + "(them|vim)": Text("vim "),
        prefix + "direct": Text("cd "),
        prefix + "direct up [<n>]": Function(directoryUp),
        prefix + "copy": Text("cp "),
        prefix + "cat": Text("cat "),
        prefix + "list": Text("ls "),
        prefix + "make": Text("make "),
        prefix + "manual": Text("man "),
        prefix + "age": Text("ag "),
        prefix + "move": Text("mv "),
        prefix + "remove": Text("rm "),
        prefix + "make direct": Text("mkdir "),
        prefix + "remove direct": Text("rmdir "),
        prefix + "(git|get) <gitCommand>": Text("git %(gitCommand)s "),
        prefix + "mount": Text("mount "),
        prefix + "umount": Text("umount "),
        prefix + "SSH": Text("ssh "),
        prefix + "exit": Text("exit"),
        prefix + "change mode": Text("chmod "),
        prefix + "less": Text("less "),
        prefix + "ping": Text("ping "),
        prefix + "working directory": Text("pwd "),
        prefix + "Z shell": Text("zsh "),
        prefix + "secure copy": Text("scp "),
        prefix + "(amber|ember)": Text("ember s"),
        prefix + "commit APP <task>": Text("git commit -am ' [APP-%(task)d]'") + Key('c-b:2, left, left'),
        prefix + "clean line": Key("c-a, c-a, c-k"),
        prefix + "npm I": Text("npm i") + Key("enter"),
        prefix + "pick fast": Text("zz") + Key("enter"),
        prefix + "pick <n>": Text("%(n)d") + Key("enter"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 8),
        DigitsRef("task"),
        Choice('gitCommand', gitCommand),
    ]
    defaults = {
        "n": 1,
    }

RuleContext = ProxyAppContext(title = "tmux")
