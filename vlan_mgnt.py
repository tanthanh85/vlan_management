from config_generation import *
from netmiko import ConnectHandler



conn_info = {'device_type': 'cisco_nxos',
    'host' : '',
    'username' : '',
    'password' : ''
}

def send_config():
    for device,config in data.items():
        conn_info['host']=config['address']
        conn_info['username']=config['username']
        conn_info['password']=config['password']
        conn = ConnectHandler(**conn_info)
        conn.send_config_from_file(f'{device}'+".txt")
    conn.disconnect()
if __name__=='__main__':
    generate_configuration_files()

    send_config()




