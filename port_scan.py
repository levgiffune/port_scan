import socket, sys, os, time
from datetime import datetime

host = ''
#max_port = 1000
max_port = 65535
min_port = 1

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def scan(host, port, r_code = 1):
    try:
        s = socket.socket()
    except socket.error:
        print(bcolors.FAIL + "\n[*] Failed to create socket. Exiting...\n\n\n" + bcolors.ENDC)
        sys.exit(2)
    code = s.connect_ex((host, port))
    
    try:
        if code == 0:
            r_code = code
        s.close
    except Exception, e:
        pass
    return r_code
try:
    os.system('clear')
    print(bcolors.HEADER + "Welcome to the port scanner." + bcolors.ENDC)
    try:
        hostname = raw_input(bcolors.WARNING + "\n[*]Enter a hostname or IP to begin: " + bcolors.ENDC + bcolors.OKGREEN)
    except KeyboardInterrupt:
        print(bcolors.WARNING + "\n[*]User requested interrupt. Exiting...\n\n\n" + bcolors.ENDC)
        sys.exit(1)
    try:
        host = socket.gethostbyname(hostname)
    except socket.gaierror:
        print(bcolors.FAIL + "\n[*]Couldn't find host. Exiting...\n\n\n" + bcolors.ENDC)
        sys.exit(3)
    print(bcolors.ENDC + bcolors.WARNING + "\n\n[*]Host: %s IP: %s" % (hostname, host) + bcolors.ENDC )
    print(bcolors.WARNING + "\n[*]Scan started at %s\n\n\n" % (time.strftime('%H:%M:%S' + bcolors.ENDC )))
    start_time = datetime.now()

    try:
        for port in range(min_port, max_port):
            try:
                sys.stdout.write(bcolors.WARNING + "\r" + " [*]scanning port %d/%d (%d%% done)\r" % (port, max_port, 100 * float(port)/max_port) + bcolors.ENDC )
                sys.stdout.flush()
                code = scan(host, port)
                if code == 0:
                    sys.stdout.write(bcolors.HEADER + "\r" + "[+]Port %d open                                         \n " % port + bcolors.ENDC )
            except Exception, e:
                print("error")
            time.sleep(0.01)
    except KeyboardInterrupt:
        print(bcolors.WARNING + "\n[*]Interrupt requested.\n\n" + bcolors.ENDC)   
        stop_time = datetime.now()
        duration = stop_time - start_time
        print(bcolors.WARNING + "\n[*]Scan terminated by user at: %s" % (time.strftime('%H:%M:%S')) + bcolors.ENDC )
        print(bcolors.WARNING + "\n[*]Time elapsed: %s"  % (duration) + bcolors.ENDC )
        print(bcolors.WARNING + "\n[*]Exiting...\n\n\n" + bcolors.ENDC)
        sys.exit(1)
        
        
    stop_time = datetime.now()
    duration = stop_time - start_time

    print(bcolors.WARNING + "\n\n\n[*]Scan finished at: %s" % (time.strftime('%H:%M:%S')) + bcolors.ENDC )
    print(bcolors.WARNING + "\n[*]Time elapsed: %s" % (duration) + bcolors.ENDC )
    print(bcolors.WARNING + "\n[*]Exiting...\n\n\n" + bcolors.ENDC )
    sys.exit(0)
except KeyboardInterrupt:
    print(bcolors.WARNING + "\n[*]User requested interrupt. Exiting..." + bcolors.ENDC )
    sys.exit(1)
