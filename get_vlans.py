from config_generation import *
from netmiko import ConnectHandler
from pprint import pprint
import yaml


conn_info = {'device_type': 'cisco_nxos',
    'host' : '',
    'username' : '',
    'password' : ''
}

vlan_list=[]
device_data={}
vlan={}

with open('vlan.yaml', 'r') as f:
        data = yaml.safe_load(f.read())

def list_vlans():
    for device,config in data.items():    
        vlan_list.clear()   
        conn_info['host']=config['address']
        conn_info['username']=config['username']
        conn_info['password']=config['password']
        conn = ConnectHandler(**conn_info)
        output = conn.send_command('show vlan', use_textfsm=True)
        for v in output:
            vlan1={}
            vlan['id']=v['vlan_id']
            vlan['name']=v['name']
            vlan1.clear()
            vlan1=vlan.copy()
            vlan_list.append(vlan1)
        device_data[device]=vlan_list.copy()
    return device_data
            

if __name__=='__main__':
    vlans=list_vlans()
    pprint(vlans)