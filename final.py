import csv

def split_csv_by_keyword(filename, keyword):
  # Open the CSV file
  with open(filename, "r") as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Initialize a list to store the data
    data = []
    # Iterate over the rows in the CSV
    for row in reader:
      # Append the row to the data list
      data.append(row)
    # Initialize a counter for the number of files
    file_count = 1
    # Initialize a list to store the rows for the current file
    current_file_rows = []
    # Iterate over the rows in the data list
    for row in data:
      # If the keyword is found in the first column, create a new CSV file with the current rows and reset the current file rows
      if keyword in row[0]:
        # Create the new CSV file
        with open(f"{filename.split('.')[0]}_{file_count}.csv", "w") as outfile:
          # Create a CSV writer object
          writer = csv.writer(outfile)
          # Write the rows to the CSV file
          writer.writerows(current_file_rows)
        # Increment the file count
        file_count += 1
        # Reset the current file rows
        current_file_rows = []
      # If the keyword is not found, add the row to the current file
      else:
        current_file_rows.append(row)
    # If there are any remaining rows, create a new CSV file with those rows
    if current_file_rows:
      # Create the new CSV file
      with open(f"{filename.split('.')[0]}_{file_count}.csv", "w") as outfile:
        # Create a CSV writer object
        writer = csv.writer(outfile)
        # Write the rows to the CSV file
        writer.writerows(current_file_rows)

# Example usage:
split_csv_by_keyword("may_2022.csv", "Total")
