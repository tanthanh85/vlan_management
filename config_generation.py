
import yaml
from jinja2 import Environment,FileSystemLoader
from get_vlans import *
from pprint import pprint
import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='./log/config_generation_log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    
with open('vlan.yaml', 'r') as f:
        data = yaml.safe_load(f.read())

def generate_configuration_files():

    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('vlan.j2')
    # vlans_on_device=list_vlans()
    vlans_to_remove=removed_vlans()
    for device, config in data.items():
        logging.info(f'working on {device}')
        output = template.render(vlans=config['vlans'], interfaces=config['interfaces'], removed_vlans=vlans_to_remove[device])
        with open(f'{device}.txt', 'w') as f:
            f.write(output)

def removed_vlans():
    device_data=list_vlans()
    removed_vlan_list={}
    list3 = []
    for dev,vlans in device_data.items():
        list1=[x['id'] for x in vlans]
        list2=[x['id'] for x in data[dev]['vlans']]   
        for i in range(len(list1)):
            if list1[i] not in list2 and list1[i]!='1':
                list3.append(list1[i])
            else:
                pass
        removed_vlan_list[dev]=list3.copy()
        list3.clear()
    return removed_vlan_list

if __name__=='__main__':
    generate_configuration_files()

