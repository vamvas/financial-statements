from src.data_loader.file_loader import load_csv


def test_load_csv_reads_csv_into_a_list_of_dicts(tmp_path):

    csv_path = tmp_path / "test.csv"
    csv_path.write_text("column1,column2\n1,2\n3,4")

    assert load_csv(csv_path) == [
        {"column1": '1', "column2": '2'},
        {"column1": '3', "column2": '4'},
        ]
