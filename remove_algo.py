import pandas as pd

def remove_algorithm_column(input_file, output_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Drop the 'Algorithm/Technique' column
    df = df.drop(columns=['Algorithm/Technique'])
    
    # Save the DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Column 'Algorithm/Technique' removed and saved to {output_file}")

# Usage
input_file = 'shuffled_new_main.csv'  # Replace with your input file name
output_file = 'output_file_without_algorithm.csv'  # Replace with desired output file name
remove_algorithm_column(input_file, output_file)
