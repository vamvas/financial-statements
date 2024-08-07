from src.data_loader.file_loader import load_csv
from src.transformer.google_sheet_entry import GoogleSheetEntry
from src.google_sheets.google_sheets_api import GoogleSheet

# Load Data from csv
transactional_data = load_csv("raw_data/transactional_data.csv")

# Upload Data to Google Sheet
google_sheet_data = GoogleSheetEntry(transactional_data).df

GoogleSheet(
    "credentials/google_service_account.json",
    "1GI3MmJm-vJTPEm1fC5C03JD3i2Riw5d9GWCwiQLsMp4"
    ).write_data_to_google_sheet_tab(
        "Data", google_sheet_data
        )
