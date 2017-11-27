# This is a command module for Dragonfly. It provides support for several of
# Aenea's built-in capabilities. This module is NOT required for Aenea to
# work correctly, but it is strongly recommended.

# This file is part of Aenea
#
# Aenea is free software: you can redistribute it and/or modify it under
# the terms of version 3 of the GNU Lesser General Public License as
# published by the Free Software Foundation.
#
# Aenea is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with Aenea.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (2014) Alex Roper
# Alex Roper <alex@aroper.net>


# This is an example grammar to demonstrate the use of server plugins. It
# provides a command to call the greet_user rpc added by the example plugin.

import os
import dragonfly
import logging

try:
    import aenea.communications
except ImportError:
    print 'Unable to import Aenea client-side modules.'
    raise

class logHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self, logging.DEBUG)

    def flush(self):
        pass

    def emit(self, record):
        msg = self.format(record)
        asdadsfasfsda
        aenea.communications.server.log("CUSTOM_LOG: %s" % msg)

_log = logging.getLogger("engine")
_log.addHandler(logHandler())

class RecognitionObserverDemo(dragonfly.RecognitionObserver):
    # def on_begin(self):
    #     aenea.communications.server.log("on_begin()")
    def on_recognition(self, res_obj, words):
        aenea.communications.server.log("on_recognition(words): %s" % words)
        #aenea.communications.server.log("on_recognition(res_obj): %s" % dir(res_obj))
        #aenea.communications.server.log("getWords" % res_obj.getWords())
    def on_failure(self, res_obj):
        aenea.communications.server.log("on_failure(res_obj)")

recobs = RecognitionObserverDemo()
recobs.register()

# Unload function which will be called at unload time.
def unload():
    recobs.unregister()
