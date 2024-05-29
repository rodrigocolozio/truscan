#!/bin/python3
# Port scanning performed in Python
# Any suggestions contact me 

import socket
import sys

def banner_grabbing(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((target, port))
        banner = s.recv(1024).decode().strip()
        return banner
    except Exception as e:
        return None
    finally:
        s.close()

def scan_ports(target, ports):
    print("    PORT          STATUS            SERVICE")
    print("-------------------------------------------------")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        con = s.connect_ex((target, port))
        if con == 0:
            banner = banner_grabbing(target, port)
            if banner:
                print(f"Port {port}        Open         {banner}")
            else:
                print(f"Port {port}        Open         No banner")
        else:
            print(f"Port {port}        Closed")
        s.close()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 truscan.py <IP> [Port]")
        sys.exit()

    ip = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else None
    
    common_ports = [
        1, 3, 4, 5, 7, 9, 11, 13, 15, 17, 18, 19, 20, 21, 22, 23, 25, 37, 42, 43, 49,
        53, 67, 68, 69, 70, 79, 80, 81, 82, 83, 84, 85, 88, 89, 90, 99, 100, 106, 109, 110,
        111, 113, 115, 117, 119, 123, 135, 137, 138, 139, 143, 144, 161, 162, 163, 179, 194, 199,
        201, 202, 204, 206, 209, 213, 220, 226, 230, 233, 234, 236, 237, 239, 243, 245, 246, 347,
        363, 369, 370, 372, 389, 427, 443, 444, 445, 464, 465, 481, 497, 500, 512, 513, 514, 515,
        520, 521, 525, 530, 531, 532, 533, 540, 543, 544, 546, 547, 548, 554, 556, 563, 587, 591,
        593, 604, 623, 631, 636, 639, 646, 648, 666, 667, 668, 683, 687, 690, 691, 700, 705, 711,
        712, 749, 750, 751, 752, 754, 760, 782, 783, 808, 843, 873, 880, 888, 898, 900, 901, 902,
        903, 911, 981, 987, 990, 992, 993, 995, 999, 1000, 1001, 1002, 1007, 1009, 1010, 1021, 1022,
        1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038,
        1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054,
        1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070,
        1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086,
        1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1433, 1434, 1521,
        1723, 2049, 2082, 2083, 2181, 3306, 3389, 3690, 5432, 5900, 6379, 8080, 8081, 8443, 8888, 9200,
        9300, 10000
    ]

    if port:
        print(f"Scanning {ip} on port {port}.")
        scan_ports(ip, [port])
    else:
        menu = input("Choose an option (1 or 2):\n1. Top ports\n2. Specific ports\n\noption -> ")
        if menu == "1":
            print(f"Starting scanning on {ip} for the top ports.\n")
            scan_ports(ip, common_ports)
        elif menu == "2":
            ports = input("Enter the ports to scan (comma-separated): ")
            port_list = list(map(int, ports.split(',')))
            print(f"Start scanning on {ip} for specific ports")
            scan_ports(ip, port_list)
        else:
            print("Please choose one of the two options displayed (1 or 2)...")
            sys.exit()

if __name__ == "__main__":
    print(
        """ 
          __________  __  ______________   __________  ____  __   _____
        /_  __/ __ \/ / / / ____/ ____/  /_  __/ __ \/ __ \/ /  / ___/
        / / / /_/ / / / / __/ /___ \     / / / / / / / / / /   \__ \ 
        / / / _, _/ /_/ / /_______/ /    / / / /_/ / /_/ / /______/ / 
        /_/ /_/ |_|\____/_____/_____/    /_/  \____/\____/_____/____/  
            \n                                                   
        """
    )
    print(
        """
        ===================================================
        =                                                   =
        =                                                   =
        =           :.        TRUSCAN        .:             =
        =                                                   =
        =                                                   =
        =                                                   =
        =       by: TRUE5                                   =
        =                                                   =
        ====================================================

        Usage ---->   Menu : python3 truscan.py <IP> 
                      Specific port : python3 truscan.py <IP> <Port>
        truscan v1.01
        Last update: May, 28, 2024
        Contact: true5mail _at_ proton.me
        """
    )
    main()
