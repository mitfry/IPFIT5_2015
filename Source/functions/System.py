__author__ = 'Tim Duysens'
"""
Last edited = 06-7-2015
Dit script geeft alle info die in het systeem tab vraagt terug
- Computernaam
- Accountnaam
- Besturingssysteem
- MAC adres
- Processor
- Local IP adres

systemlog houd bij in het logboek wat er gebeurd in het script,
geprogrammerde niveaus: debug, info
"""

import platform
import getpass
from uuid import getnode as get_mac
import socket
import logging

systemlog = logging.getLogger("THRAM - System")
systemlog.debug("System info imported")
# als deze def wordt aangeroepen zal deze de computernaam teruggeven
def compn():
    computername = platform.node()
    systemlog.info("Computer name: %s" % computername)
    return computername
# als deze def wordt aangeroepen zal deze de accountnaam teruggeven
def accn():
    accountname = getpass.getuser()
    systemlog.info("Accountname: %s" % accountname)
    return accountname
# als deze def wordt aangeroepen zal deze het besturingssysteem teruggeven
def bestu():
    os = platform.system()
    systemlog.info("Opperationsystem: %s" % os)
    return os
# als deze def wordt aangeroepen zal deze het mac-adres teruggeven
def mac():
    macadr = get_mac()
    systemlog.info("MAC-Adress: %s" % macadr)
    return str(macadr)
# als deze def wordt aangeroepen zal deze de processortype teruggeven
def processor():
    proces = platform.processor()
    systemlog.info("Processor: %s" % proces)
    return proces
# als deze def wordt aangeroepen zal deze de lokale ip teruggeven
def locip():
    localip = socket.gethostbyname(socket.gethostname())
    systemlog.info("Local IP: %s" % localip)
    return localip

if __name__ == "__main__":
    print compn()
    print accn()
    print bestu()
    print mac()
    print processor()
    print locip()
