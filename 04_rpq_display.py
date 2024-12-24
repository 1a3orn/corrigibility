import json
import matplotlib.pyplot as plt
import numpy as np

# Read the JSON file
def create_stacked_bar_chart(filename):
    # Load the data
    with open(filename, 'r') as file:
        data = json.load(file)

    data.sort(key=lambda x: (
        x['refusal_count'] + x['ignorance_count'] + x['acceptance_count'],
        -x['refusal_count']
    ), reverse=True)
    
    # Prepare the data for plotting
    ids = [item['id'] for item in data]
    refusals = [item['refusal_count'] for item in data]
    ignorances = [item['ignorance_count'] for item in data]
    acceptances = [item['acceptance_count'] for item in data]
    
    # Create the stacked bar chart
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot each stack
    bar_width = 0.8
    x = np.arange(len(ids))
    
    # Create the stacks
    ax.bar(x, refusals, bar_width, label='Refusal', color='#ff9999')
    ax.bar(x, ignorances, bar_width, bottom=refusals, label='Ignorance', color='#66b3ff')
    ax.bar(x, acceptances, bar_width, bottom=[i+j for i,j in zip(refusals, ignorances)], 
           label='Acceptance', color='#99ff99')
    
    # Customize the chart
    ax.set_ylabel('Count')
    ax.set_title('Refusal-Producing Questions by Category')
    ax.set_xticks(x)
    ax.set_xticklabels(ids, rotation=45, ha='right')
    
    # Add legend
    ax.legend()
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    return plt

# Usage
if __name__ == "__main__":
    plt = create_stacked_bar_chart('data_3.6_try_2_rpq_output.json')
    plt.show()
