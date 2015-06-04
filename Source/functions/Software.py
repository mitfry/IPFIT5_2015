# Built-in
import sys

# Custom
# Add folder "modules" to the locations to import from
sys.path.append(sys.path[0] + "/../modules")
import wmi

w = wmi.WMI(".")

# Generating a list of running processes on the target pc
def processes():
    for process in w.Win32_Process():
        if process.Caption is not None:
            print "ID: ", process.ProcessId, " Name: ", process.Name


# Software installed with any windows installer
# List is incomplete imo
def software_installed():
    for software in w.Win32_Product():
        if software.Caption is not None:
            print "Name: ", software.Caption.replace(u"\u2122", ''), "on version ", software.Version


# Generating a list of services on the target pc
def services():
    for service in w.Win32_Service():
        if service.Caption is not None:
            print "ID: ", service.ProcessId, " Name: ", service.Caption, " Service state:", service.State
