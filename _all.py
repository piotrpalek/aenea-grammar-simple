# _all.py: main rule for DWK's grammar

from natlink import setMicState
from aenea import *

import Keyboard
import TMux
import Words
import Terminal
import Spacemacs
import WindowManager
import Browser
release = Key("shift:up, ctrl:up, alt:up")

class RepeatRule(CompoundRule):
    spec = "<sequence>"

    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]
        for action in sequence:
            action.execute()
        release.execute()

alternatives = [Keyboard, TMux, Words, Terminal, Spacemacs, WindowManager, Browser];
grammars = []

for index, RuleConfig in enumerate(alternatives):
    sequence = Repetition(RuleRef(rule=RuleConfig.Rule()), min=1, max=16, name="sequence")
    repeat_rule = RepeatRule(extras = [ sequence ])

    grammar = None
    if hasattr(RuleConfig, 'RuleContext'):
        grammar = Grammar(str(index), context=RuleConfig.RuleContext)
    else:
        grammar = Grammar(str(index))
    grammar.add_rule(repeat_rule)
    grammar.load()
    grammars.append(grammar)
    grammar = None

def unload():
    """Unload function which will be called at unload time."""
    print grammars

    for grammar in grammars:
        if grammar:
            grammar.unload()
        grammar = None
