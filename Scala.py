# commands for controlling various programs

from aenea import *

commands = {
    'class': 'case class',
    'case class': 'case class',
    'integer': 'Int',
    'define': 'def',
    'value': 'val',
    'detach': 'detach',
    'package': 'package',
    'import': 'import',
    'case': 'case',
    'boolean': 'bool',
    'match': 'match',
    'case': 'case',
    'for each': 'foreach',
}

class ScalaRule(MappingRule):
    prefix = "(scala|scholar) "
    mapping = {
        prefix + "<commands>": Text("%(commands)s"),
    }
    extras = [
        Choice('commands', commands),
    ]
    default = {
        "n": 1,
    }
