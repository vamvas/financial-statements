import pandas as pd
import gspread


class GoogleSheet():
    def __init__(self, credentials_path: str, spreadsheet_key: str) -> None:
        self.credentials_path = credentials_path
        self.spreadsheet_key = spreadsheet_key

    def open_connection_to_spreadsheet(self) -> gspread.Spreadsheet:
        auth_client = gspread.service_account(filename=self.credentials_path)
        spreadsheet = auth_client.open_by_key(self.spreadsheet_key)

        return spreadsheet

    def write_data_to_google_sheet_tab(self,
                                       tab_name: str,
                                       data: pd.DataFrame,
                                       ):
        spreadsheet = self.open_connection_to_spreadsheet()
        worksheet = spreadsheet.worksheet(tab_name)
        worksheet.clear()
        worksheet.update([data.columns.values.tolist()] + data.values.tolist())
