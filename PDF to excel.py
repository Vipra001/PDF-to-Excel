pip install tabula-py pandas
import tabula
import pandas as pd
import os

# Path to your PDF file
pdf_path = r"C:\users\seema\OneDrive\Documents\Desktop\odf to excel\Conditional Formatting Lab (1).pdf"

# Check if the file exists and is not empty
if not os.path.isfile(pdf_path):
    raise ValueError(f"The file at {pdf_path} does not exist.")
if os.path.getsize(pdf_path) == 0:
    raise ValueError(f"The file at {pdf_path} is empty. Check the file, or download it manually.")

try:
    # Extract tables from the PDF
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

    if not tables:
        raise ValueError("No tables found in the PDF file.")

    # Combine all tables into a single DataFrame
    combined_df = pd.concat(tables, ignore_index=True)

    # Save the combined DataFrame to an Excel file
    combined_df.to_excel('output.xlsx', index=False)

    print("Tables extracted and saved to output.xlsx")
except Exception as e:
    print(f"An error occurred: {e}")
