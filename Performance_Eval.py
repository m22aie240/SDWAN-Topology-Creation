import time
import networkx as nx
import matplotlib.pyplot as plt

def create_topology(num_hubs, num_spokes):
    devices = ['Hub{}'.format(i+1) for i in range(num_hubs)] + \
              ['Spoke{}'.format(i+1) for i in range(num_spokes)]
    G = nx.Graph()

    # Add edges for Hubs to Spokes
    for hub in devices[:num_hubs]:
        for spoke in devices[num_hubs:]:
            G.add_edge(hub, spoke)

    # Add edges between Hubs
    for i in range(num_hubs):
        for j in range(i+1, num_hubs):
            G.add_edge(devices[i], devices[j])

    return G

def measure_performance(hub_range, spoke_range):
    performance_results = {}

    for num_hubs in hub_range:
        for num_spokes in spoke_range:
            start_time = time.time()
            create_topology(num_hubs, num_spokes)
            end_time = time.time()
            performance_results[(num_hubs, num_spokes)] = end_time - start_time

    return performance_results

def plot_performance(performance_results):
    hubs, spokes, times = zip(*[(k[0], k[1], v) for k, v in performance_results.items()])
    plt.figure(figsize=(12, 6))
    
    for num_hubs in set(hubs):
        # Extract performance times for the current number of hubs
        times_for_hub = [times[i] for i in range(len(times)) if hubs[i] == num_hubs]
        plt.plot(spokes[:len(times_for_hub)], times_for_hub, '-o', label=f'Hubs: {num_hubs}')
        
    plt.xlabel('Number of Spokes')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Topology Creation Performance by Number of Hubs and Spokes')
    plt.legend()
    plt.grid(True)
    plt.show()

# Define the range for the number of hubs and spokes
hub_range = range(1, 11)  # From 1 to 5 hubs
spoke_range = range(10, 100, 10)  # From 10 to 50 spokes, in increments of 10

performance_results = measure_performance(hub_range, spoke_range)
plot_performance(performance_results)
