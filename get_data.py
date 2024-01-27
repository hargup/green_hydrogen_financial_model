import csv

def process_txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Date', '15-Minute Block Number', 'Price'])

        date = None
        block_number = 0

        for line in infile:
            line = line.strip()
            if line:
                # Check if the line is a date
                if '-' in line and len(line) == 10:
                    date = line
                    block_number = 0
                # Check if the line is a 15-minute block
                elif ':' in line:
                    parts = line.split()
                    price = parts[3]  # Get the first price value after the 15-minute block
                    writer.writerow([date, block_number, price])
                    block_number += 1

# Example usage
input_file = './apr_2023.txt'
output_file = 'your_output_file.csv'
process_txt_to_csv(input_file, output_file)
