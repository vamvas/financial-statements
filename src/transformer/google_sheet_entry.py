import pandas as pd


class GoogleSheetEntry():

    def __init__(self, list_of_dict: list[dict[str, str]]):
        self.list_of_dict = list_of_dict
        self.df = self.__create_df_from_list_of_dict()

    def __create_df_from_list_of_dict(self) -> pd.DataFrame:

        transactions_df = pd.DataFrame(
            data=self.list_of_dict,
            columns=[keys for keys in self.list_of_dict[0]],
            index=range(len(self.list_of_dict))
            ).astype(
                {
                    "Date": "datetime64[ns]",
                    "Value": "float64"
                }
            )

        transactions_df = transactions_df.loc[
            :, ["Date", "Description", "Value"]
            ]

        transactions_df["Date"] = transactions_df[
            "Date"
            ].dt.strftime('%Y-%m-%d')

        return transactions_df
