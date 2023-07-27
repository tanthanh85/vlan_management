
import yaml
from jinja2 import Environment,FileSystemLoader
    
with open('vlan.yaml', 'r') as f:
        data = yaml.safe_load(f.read())

def generate_configuration_files():

    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('vlan.j2')

    for device, config in data.items():
        output = template.render(vlans=config['vlans'], interfaces=config['interfaces'])
        with open(f'{device}.txt', 'w') as f:
            f.write(output)



