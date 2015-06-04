
# Built-in
import sys

# Custom
# Add folder "modules" to the locations to import from
sys.path.append(sys.path[0]+"/../modules")
import wmi



w = wmi.WMI(".")


# Function for generating a list of running processes on the target pc
def processes():
    for process in w.Win32_Process():
        print process.ProcessId, process.Name



def services():
    # stopped_services = w.Win32_Service(State="Stopped")
    running_services = w.Win32_Service(State="Running")

    # for ss in stopped_services:
    #     print ss.Caption, "service is not running"

    for rs in running_services:
        print rs.ProcessId, rs.Caption, "service is running"
