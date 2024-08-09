import pandas as pd
import tkinter as tk
from tkinter import filedialog
from utils import adjust_item_costs, calculate_total_costs, save_to_excel

def main():
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user to select an Excel file
    file_path = filedialog.askopenfilename(
        title="Select the Excel file",
        filetypes=[("Excel files", "*.xlsx *.xls")]  # Limit to Excel files
    )

    # Check if a file was selected
    if not file_path:
        print("No file selected. Exiting.")
        return

    # Load the Excel file
    df = pd.read_excel(file_path)

    # Clean up the DataFrame by keeping only relevant columns
    df = df[['Item', 'Cost', 'nick', 'kevin', 'andy']]

    # Adjust the costs
    df = adjust_item_costs(df)

    # Calculate each person's total cost
    total_costs = calculate_total_costs(df)

    # Save the adjusted DataFrame to a new Excel file
    output_file_path = filedialog.asksaveasfilename(
        title="Save the adjusted Excel file",
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")]
    )

    if not output_file_path:
        print("No file selected for saving. Exiting.")
        return

    save_to_excel(df, output_file_path)

    # Print the total costs for each person
    print(f"Nick's Total Cost: ${total_costs['nick']:.2f}")
    print(f"Kevin's Total Cost: ${total_costs['kevin']:.2f}")
    print(f"Andy's Total Cost: ${total_costs['andy']:.2f}")

if __name__ == "__main__":
    main()
