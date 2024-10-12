import pandas as pd 

def excel2csv(filepath: str) -> str:
    df = pd.read_html(filepath)[0]
    csv_filepath = filepath.replace('.xls', '.csv')
    df.to_csv(csv_filepath)
    return csv_filepath