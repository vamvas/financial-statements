from src.transformer.google_sheet_entry import GoogleSheetEntry


def test_mapping():

    input_data = [
        {
            "Date": "02 Jan 2024",
            "Type": "DPC",
            "Description": "some_description",
            "Value": "-100.35",
            "Balance": "2540.50",
            "Account Name": "some_name",
            "Account Number": "some_account_name"
        },
        {
            "Date": "03 Apr 2024",
            "Type": "BAC",
            "Description": "another_description",
            "Value": "280.00",
            "Balance": "2640.50",
            "Account Name":
            "another_name",
            "Account Number":
            "another_account_name"
        }
    ]

    sut = GoogleSheetEntry(input_data).df

    assert sut.columns.to_list() == ["Date", "Description", "Value"]
    assert sut.loc[0, "Date"] == "2024-01-02"
    assert sut.loc[1, "Date"] == "2024-04-03"
    assert sut.loc[0, "Description"] == "some_description"
    assert sut.loc[1, "Description"] == "another_description"
    assert sut.loc[0, "Value"] == -100.35
    assert sut.loc[1, "Value"] == 280.00
