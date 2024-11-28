import sys
import pandas as pd
import matplotlib.pyplot as plt

input_file = sys.argv[1]
output_plot = sys.argv[2]

extracted_data = pd.read_csv(input_file, sep='\t', header=None, names=['chrom', 'start', 'end', 'length_a', 'length_b', 'alignment'], usecols=['chrom', 'start', 'end'])
reference_data = pd.read_csv('data/reference.hist', sep='\t', header=None, names=['length', 'normalized_freq'])

extracted_data['length'] = extracted_data['end'] - extracted_data['start']
length_frequency = extracted_data['length'].value_counts().sort_index()

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

axes[0].bar(length_frequency.index, length_frequency.values, color='skyblue')
axes[0].set_title('DNA Length vs Frequency from Extracted Data')
axes[0].set_xlabel('DNA Length')
axes[0].set_ylabel('Frequency')

axes[1].bar(reference_data['length'], reference_data['normalized_freq'], color='salmon')
axes[1].set_title('DNA Length vs Normalized Frequency from Reference Data')
axes[1].set_xlabel('DNA Length')
axes[1].set_ylabel('Normalized Frequency')

plt.tight_layout()
plt.savefig(output_plot)
plt.show()
