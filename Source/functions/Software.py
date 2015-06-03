from source.modules import wmi


def test():
    w = wmi.WMI()
    for p in w.Win32_Product():
        if 'Box, Inc.' == p.Vendor and p.Caption and 'Box Sync' in p.Caption:
            print 'Installed {}'.format(p.Version)
