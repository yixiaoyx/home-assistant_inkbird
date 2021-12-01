from bluepy.btle import Scanner

scanner = Scanner()
while True:
    print('Scanning')
    scanner.scan()
    results = scanner.getDevices()
    print(len(results))
    for dev in list(results):
        if dev.addr != '49:42:06:00:2e:bd':
            continue
        print(dev.addr)
        print(dev.getScanData())

