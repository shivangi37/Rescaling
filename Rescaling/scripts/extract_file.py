import sys
import pandas as pd

freq_input = sys.argv[1]
merged_input = sys.argv[2]
output_result = sys.argv[3]

# frequency data
frequency_data = pd.read_csv(freq_input, sep='\t', header=None, names=['Length', 'Frequency'])


reference_data = pd.read_csv('data/reference.hist', sep='\t', header=None, names=['Length', 'NormalizedFrequency'])


max_normalized_frequency = reference_data['NormalizedFrequency'].max()


length_with_max_nfreq = reference_data.loc[reference_data['NormalizedFrequency'] == max_normalized_frequency, 'Length'].values[0]


freq_at_max_nfreq = frequency_data.loc[frequency_data['Length'] == length_with_max_nfreq, 'Frequency'].values[0]


required_counts = {}

for _, row in reference_data.iterrows():
    dna_length = row['Length']
    normalized_freq = row['NormalizedFrequency']
    if dna_length in frequency_data['Length'].values:
        freq_value = frequency_data.loc[frequency_data['Length'] == dna_length, 'Frequency'].values[0]
        required_counts[dna_length] = round((normalized_freq / max_normalized_frequency) * freq_at_max_nfreq)


extracted_lines = []

with open(merged_input, 'r') as merged_file:
    for line in merged_file:
        fields = line.split()
        start_pos = int(fields[1])
        end_pos = int(fields[2])
        dna_length = end_pos - start_pos
        if dna_length in required_counts:
            remaining_count = required_counts[dna_length]
            if remaining_count > 0:
                extracted_lines.append(line)
                required_counts[dna_length] -= 1


with open(output_result, 'w') as result_file:
    result_file.writelines(extracted_lines)