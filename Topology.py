import networkx as nx
import matplotlib.pyplot as plt

def input_device_roles(num_hubs, num_spokes):
    devices = {}
    for i in range(num_hubs):
        devices[f'Hub{i + 1}'] = 'Hub'
    for i in range(num_spokes):
        devices[f'Spoke{i + 1}'] = 'Spoke'
    return devices

def create_tunnels(devices):
    tunnels = []
    G = nx.Graph()

    # Create tunnels between Hubs and Spokes
    hubs = [device for device, role in devices.items() if role == 'Hub']
    spokes = [device for device, role in devices.items() if role == 'Spoke']

    for hub in hubs:
        for spoke in spokes:
            tunnels.append(f"Tunnel from {spoke} to {hub}")
            G.add_edge(spoke, hub)

    # Create tunnels between Hubs
    for i, hub1 in enumerate(hubs):
        for hub2 in hubs[i+1:]:
            tunnels.append(f"Tunnel from {hub1} to {hub2}")
            G.add_edge(hub1, hub2)

    return tunnels, G

def visualize_topology(G):
    nx.draw(G, with_labels=True, node_size=700, node_color='lightblue', font_weight='bold')
    plt.show()

# Example usage:
num_hubs = int(input("Enter the number of Hubs: "))
num_spokes = int(input("Enter the number of Spokes: "))

devices = input_device_roles(num_hubs, num_spokes)
tunnels, G = create_tunnels(devices)

for tunnel in tunnels:
    print(tunnel)

visualize_topology(G)
