import json
import matplotlib.pyplot as plt
import numpy as np

def create_total_questions_chart(filename):
    # Load the data
    with open(filename, 'r') as file:
        data = json.load(file)
    
    # Calculate totals and sort by them
    for item in data:
        item['total'] = item['refusal_count'] + item['ignorance_count'] + item['acceptance_count']

    data.sort(key=lambda x: (
        x['refusal_count'] + x['ignorance_count'] + x['acceptance_count'],
        -x['refusal_count']
    ), reverse=True)
    
    # Prepare the data for plotting
    ids = [item['id'] for item in data]
    totals = [item['total'] for item in data]
    
    # Create the bar chart
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot the bars
    bars = ax.bar(np.arange(len(ids)), totals, color='#4a90e2')
    
    # Customize the chart
    ax.set_ylabel('Total Count')
    ax.set_title('Total Refusal-Eliciting Questions Written per Topic')
    ax.set_xticks(np.arange(len(ids)))
    ax.set_xticklabels(ids, rotation=45, ha='right')
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    return plt

# Usage
if __name__ == "__main__":
    plt = create_total_questions_chart('data_3.6_2024_12_23_rpq_output.json')
    plt.show()