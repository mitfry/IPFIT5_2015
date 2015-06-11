__author__ = 'Tim Duysens'
"""
Last edited: 9-6-15
Testclasse die alle prints opvangt en logt.

Deze class zal bij het starten van het programma worden aangeroepen.
Hierna wordt alles wat in het console komt eveneens in een text bestand.

"""

import logging
import sys

class LoggingStart():
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def testlog(self):
        print "lol"
        print "lol1"
        print "lol2"

logging.basicConfig(
   level=logging.DEBUG,
   format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
   filename="out.log",
   filemode='a'
)

stdout_logger = logging.getLogger('STDOUT')
sl = LoggingStart(stdout_logger, logging.INFO)
sys.stdout = sl

stderr_logger = logging.getLogger('STDERR')
sl = LoggingStart(stderr_logger, logging.ERROR)
sys.stderr = sl
