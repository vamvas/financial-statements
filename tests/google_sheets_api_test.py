from src.google_sheets.google_sheets_api import GoogleSheet
from unittest.mock import MagicMock, patch
import pandas as pd
import pytest
import gspread


@pytest.fixture
def mock_service_account():
    with patch('gspread.service_account') as mock_service_account:
        yield mock_service_account


@pytest.fixture
def mock_spreadsheet():
    mock_spreadsheet = MagicMock(spec=gspread.Spreadsheet)
    mock_spreadsheet.title = "some-spreadsheet-name"
    mock_spreadsheet.id = "some-spreadsheet-id"
    return mock_spreadsheet


@pytest.fixture
def google_sheet(mock_service_account, mock_spreadsheet):
    mock_service_account.return_value.open_by_key.return_value = (
        mock_spreadsheet
        )
    return GoogleSheet("dummy_path", "dummy_key")


def test_mapping_of_attributes(google_sheet):

    assert google_sheet.credentials_path == "dummy_path"
    assert google_sheet.spreadsheet_key == "dummy_key"


def test_google_sheet_connection(google_sheet):

    sut = google_sheet.open_connection_to_spreadsheet()

    assert sut.title == "some-spreadsheet-name"
    assert sut.id == "some-spreadsheet-id"


def test_write_data_to_google_sheet_tab(google_sheet, mock_spreadsheet):

    mock_worksheet = MagicMock(spec=gspread.Worksheet)
    mock_spreadsheet.worksheet.return_value = mock_worksheet

    data = pd.DataFrame({
        'Date': ['2024-01-01', '2024-01-02'],
        'Description': ['Test1', 'Test2'],
        'Value': [100, 200]
    })

    google_sheet.write_data_to_google_sheet_tab('TestTab', data)

    google_sheet.open_connection_to_spreadsheet = MagicMock(
        return_value=mock_spreadsheet
        )
    mock_spreadsheet.worksheet.assert_called_once_with('TestTab')
    mock_worksheet.clear.assert_called_once()
    mock_worksheet.update.assert_called_once_with(
        [data.columns.values.tolist()] + data.values.tolist()
        )
