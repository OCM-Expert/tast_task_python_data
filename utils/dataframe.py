from typing import Any
import pandas as pd
import re


def to_bool(x: Any) -> bool:
    if x in ['Да', 1, 1.0]:
        return True
    return False

def df_edit(df: pd.DataFrame) -> pd.DataFrame:
    df = df[~df['Просрочена, ч'].isnull()]
    df['Организация'] = df['Организация'].map(lambda x: re.search("(?<=городе\s)[ \w-]+", x).group())
    df['Завершен'] = df['Завершен'].map(to_bool)
    df.drop('Unnamed: 0', axis=1, inplace=True)
    return df