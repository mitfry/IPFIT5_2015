__author__ = 'Tim Duysens'
"""
Last edited: 29-6-15

Deze class zal bij het starten van het programma worden aangeroepen.
Hierna wordt alles wat in het console komt eveneens in een text bestand opgeslagen.

"""

import os
import logging
import logging.handlers
import time

LOG_FILENAME = 'THRAM Log'

formatter = '%(asctime)s - %(name)s - [%(levelname)s] - %(message)s'
formatlog = '%(message)s'

# Set up a specific logger with our desired output level
logger = logging.getLogger('THRAM')
logger.setLevel(logging.INFO)

# Check if log exists and should therefore be rolled
needRoll = os.path.isfile(LOG_FILENAME)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, backupCount=50)

forhand = logging.StreamHandler()

forhand.setFormatter(formatlog)

logger.addHandler(handler)
logger.addHandler(forhand)

# This is a stale log, so roll it
if needRoll:
    # Add timestamp
    logger.info('\n---------\nLog closed on %s.\n---------\n' % time.asctime())


    # Roll over on application start
    logger.handlers[0].doRollover()

# Add timestamp
logger.info('\n---------\nLog started on %s.\n---------\n' % time.asctime())

logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format=formatter)

loggerlog = logging.getLogger("THRAM - Log")
loggerlog.debug("Logger module imported")

mainlog = logging.getLogger("THRAM - Main")
mainlog.info("Program has started, Let the search begin")
