import pandas as pd
import gspread


class GoogleSheet():
    def __init__(self, credentials_path: str) -> None:
        self.credentials_path = credentials_path

    def __open_connection_to_spreadsheet(self):
        gc = gspread.service_account(filename=self.credentials_path)
        sh = gc.open("Financial Statements")
        return sh

    def write_data_to_google_sheet_tab(self,
                                       tab_name: str,
                                       data: pd.DataFrame
                                       ):
        sh = self.__open_connection_to_spreadsheet()
        worksheet = sh.worksheet(tab_name)
        worksheet.clear()
        worksheet.update([data.columns.values.tolist()] + data.values.tolist())
