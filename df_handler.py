"""df_handler module"""
import pandas as pd

class DataframeHandler():

    def __init__(self, path: str = None, df: pd.DataFrame = None) -> None:
        if df is None:
            if len(path) > 0:
                self.__df = pd.read_csv(path)
                print("Dataframe successfully read")
            else:
                self.__df = pd.DataFrame()
        else: # a Dataframe has been passed
            self.__df = df
    
    @property
    def df(self) -> pd.DataFrame:
        return self.__df
    
    def get_shape(self) -> tuple:
        return self.df.shape
    
    def get_columns(self) -> list:
        return list(self.df.columns)
    
    def get_columns_subset(self, columns: list[str]) -> pd.DataFrame:
        return self.df[columns]
    
    def get_first_n_columns(self, n: int) -> pd.DataFrame:
        return self.df.iloc[:, 0:n]
