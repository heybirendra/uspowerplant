import pandas as pd
import os

def split_excel_to_csv(excel_file_path: str, output_dir: str):
    all_sheets = pd.read_excel(excel_file_path, sheet_name=None)

    os.makedirs(output_dir, exist_ok=True)

    for sheet_name, df in all_sheets.items():
        safe_sheet_name = sheet_name.replace(" ", "_").replace("/", "_")
        output_path = os.path.join(output_dir, f"{safe_sheet_name}.csv")
        df.to_csv(output_path, index=False)


# Example usage
if __name__ == "__main__":
    excel_path = "givenfile/egrid2023_data_rev1.xlsx"
    output_folder = "sheets_as_csv"
    split_excel_to_csv(excel_path, output_folder)
