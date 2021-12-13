import psutil

def main():
    Interface = psutil.net_if_addrs()
    for interface_name in Interface.keys() :
        print(interface_name)
if __name__ == '__main__':
    main()
    