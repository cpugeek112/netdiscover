import re
import sys



def main():
    
    if len(sys.argv) < 2:
        print(f'usage: {sys.argv[0]} device_output.txt')
        exit()
    
    
    with open(sys.argv[1], 'r') as file:
        rawtext = file.read()
        

    
    deviceName = re.search(r'hostname (.+)', rawtext).group(1)
    vendor = 'Cisco'
    model = re.search(r'\nPID: (WS-C[A-Z0-9\-]+)\s.+', rawtext).group(1)
    ipAddress = re.search(r'\n\s+ip address ([0-9\.]+)', rawtext).group(1)
    firmware = re.search(r'version ([0-9\.]+)',rawtext).group(1)
    serialNumber = re.search(r'\nPID: WS-C[A-Z0-9\-]+.+\s+SN: (.+)',rawtext).group(1)
    
    
    
    report = ';'.join([deviceName,vendor,model,ipAddress,firmware,serialNumber])
    
    print(report)
    
    
    






if __name__ == '__main__':
    main()
    