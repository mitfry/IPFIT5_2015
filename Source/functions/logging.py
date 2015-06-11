__author__ = 'Tim D'
"""
Last edited: 11-6-15
Tratidionele Log functie

Deze def zal bij het starten van het programma worden aangeroepen.
Hierna wordt alles wat in het console komt eveneens in een text bestand.

Levels
>DEBUG - 10
>INFO
>WARNING
>ERROR
>CRITICAL - 50

"""
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

filename = "%s.log" % asctime

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
