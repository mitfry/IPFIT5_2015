# Built-in
import sys

# Custom
# Add folder "modules" to the locations to import from
sys.path.append(sys.path[0] + "/../modules")

import wmi

w = wmi.WMI(".")


# Generating a list of running processes on the target pc
def processes():
    list_processes = []
    for process in w.Win32_Process():
        if process.Caption is not None:
            # print "ID: ", process.ProcessId, " Name: ", process.Name
            list_processes.append([process.ProcessID, process.Name])
    return list_processes


# Software installed with any windows installer
# List is incomplete imo
def software_installed():
    list_software = []
    for software in w.Win32_Product():
        if software.Caption is not None:
            # print "Name: ", software.Caption.replace(u"\u2122", ''), "on version ", software.Version
            list_software.append([software.Caption.replace(u"\u2122", ''), software.Version])
    return list_software

# Generating a list of services on the target pc
def services():
    list_services = []
    for service in w.Win32_Service():
        if service.Caption is not None:
            # print "ID: ", service.ProcessId, " Name: ", service.Caption, " Service state:", service.State
            list_services.append([service.ProcessId, service.Caption, service.State])
    return list_services
