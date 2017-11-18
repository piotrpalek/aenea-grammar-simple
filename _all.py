# _all.py: main rule for DWK's grammar

from natlink import setMicState
from aenea import *

import Keyboard
import TMux
import Words
import Terminal
import Spacemacs
import WindowManager
release = Key("shift:up, ctrl:up, alt:up")

alternatives = []
alternatives.append(RuleRef(rule=Keyboard.KeyboardRule()))
alternatives.append(RuleRef(rule=TMux.TMuxRule()))
alternatives.append(RuleRef(rule=Words.WordRule()))
alternatives.append(RuleRef(rule=Terminal.TerminalRule()))
alternatives.append(RuleRef(rule=Spacemacs.SpacemacsRule()))
alternatives.append(RuleRef(rule=WindowManager.WindowManagerRule()))
root_action = Alternative(alternatives)

sequence = Repetition(root_action, min=1, max=16, name="sequence")

class RepeatRule(CompoundRule):
    spec = "<sequence>"
    extras = [
        sequence,
    ]

    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]
        for action in sequence:
            action.execute()
        release.execute()

grammar = Grammar("root rule")
grammar.add_rule(RepeatRule())
grammar.load()

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
