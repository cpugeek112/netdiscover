import re
import os
import argparse
from getpass import getpass




def main():
    '''
    Links all classes together
    '''
    args = get_arguments()
    
    #print(args)
    
    
    if args.get:
        print("mode=Getting")
        exit()
    
    if args.file: #opens file to be processed
        filename = str(args.path[0])
        rawtext = loadFile(filename)
        
        if args.audit:
            audit(rawtext)
        
    

    if args.dir: #opens each file in directory to be processed
        directory = str(args.path[0])
        for filename in os.listdir(directory):
            rawtext = loadFile('\\'.join([directory,filename]))
            audit(rawtext)








def get_arguments():
    '''
    gets arguments passed in by user when script is executed
    '''
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('-a','--audit',action='store_true',help='captuers device name, type, model, make , ip address, firmware version, serial number')
    parser.add_argument('-g','--get' ,metavar='commands.txt', default=False,help='Get config from remote devices')
    parser.add_argument('-f','--file', action='store_true', default=False, help='convert file')
    parser.add_argument('-d','--dir', action='store_true', default=False, help='convert directory')
    parser.add_argument('path',nargs='+',help='file or directory to parse')
    return parser.parse_args()


def loadFile(file):
    with open(file, 'r') as file:
        return file.read()


def search(criteria):
    regex, rawtext = criteria
    try:
     
        results = [x.group(1) for x in re.finditer(regex,rawtext,re.MULTILINE)] 
        if len(results) > 1:
            return ','.join(results)
        else:
            return results[0]
        
    except:
        #print("error: <not Defined>")
        return "<Not defined>"
    return "<Not defined>"


    

def audit(rawtext):
    
    hostname = (r'\nhostname\s(.+)',rawtext)
    make = 'Cisco'
    model = (r'\nPID:\s(WS-[A-Z0-9\-]+)',rawtext)  
    ipaddress = (r'\n\s+ip address ([0-9.]+)',rawtext)
    firmware = (r'\nversion\s(.+)',rawtext)
    serialno = (r'\nPID:\sWS-C.+SN:\s(.+)',rawtext)
   
    report = [search(hostname),make,search(model),search(ipaddress),search(firmware),search(serialno)]
    print(';'.join(report))
   
    
    













    
    
    
    



if __name__ == "__main__":
    main()
    
  