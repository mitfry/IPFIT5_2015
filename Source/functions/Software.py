__author__ = 'Mitchell'
# Built-in
import sys
import threading
import pythoncom

# Custom
# Add folder "modules" to the locations to import from
sys.path.append(sys.path[0] + "/../modules")

import wmi

# Submitt column titles for TreeWidget on Software tab. MAX 10!
list_processes = [["Proces ID", "Naam", "", ""]]
list_software = [["Naam", "Versie", "", ""]]
list_services = [["Proces ID", "Naam", "Status", ""]]


def processes():
    return list_processes


def services():
    return list_services


def software_installed():
    return list_software


class WorkerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print 'Gathering information... (0/3)\n'
        pythoncom.CoInitialize()
        w = wmi.WMI(".")

        # Generating a list of running processes on the target pc
        for process in w.Win32_Process():
            if process.Caption is not None:
                # print "ID: ", process.ProcessId, " Name: ", process.Name
                list_processes.append([process.ProcessID, str(process.Name)])
        print 'Process list complete! (1/3)\n'

        from Cloud import cloud_search as cl
        cl()

        # Software installed with any windows installer
        # List is incomplete imo
        for software in w.Win32_Product():
            if software.Caption is not None:
                # print "Name: ", software.Caption.replace(u"\u2122", ''), "on version ", software.Version
                list_software.append([software.Caption.replace(u"\u2122", ''), software.Version])
        print 'Software list complete! (2/3)\n'

        # Generating a list of services on the target pc
        for service in w.Win32_Service():
            if service.Caption is not None:
                # print "ID: ", service.ProcessId, " Name: ", service.Caption, " Service state:", service.State
                list_services.append([service.ProcessId, service.Caption, service.State])
        print 'Service list complete! (3/3)\n'
        print 'Finished gathering information!\n\nSoftware Tab ready for use :)'

