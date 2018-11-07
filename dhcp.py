###In this example, the script will change the settings for the DNS server for each scope on the router.###
###This is intended for reference and should be modified to fit specific needs.###

from netmiko import ConnectHandler

def Cisco(ip):
    return{
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'USERNAME_HERE',
        'password': 'PASSWORD_HERE',
        }
        
txtFile = open(r'C:\Python\IPaddrs.txt','r')

for line in txtFile:
    ipADDR = line.rstrip('\n')
    
    HOST = Cisco(ipADDR)
    
    try:
        net_connect = ConnectHandler(**HOST)
        pool = net_connect.send_command('sh run | in dhcp pool')
        pool = pool.strip().splitlines()
        if pool:
            for lines in pool:
                cli_cmds = [lines, 'no dns-server', 'dns-server X.X.X.X']
                net_connect.send_config_set(cli_cmds)
            net_connect.send_command('write memory')
            net_connect.disconnect()
            print (ipADDR + ' completed')
        else:
            net_connect.disconnect()
            print (ipADDR + ' no DHCP scope found')
    except:
        print(ipADDR + ' Error, SKIPPED')
        pass
    
txtFile.close()
