import pandas as pd
import os
import convert
import argparse

def combine_data(folder_path, data_type):
    combined_df = None

    for filename in os.listdir(folder_path):
        if data_type not in filename.lower():
            print(f"Skipping {filename}")
            continue

        if filename.endswith('.xls'):
            filename = convert.excel2csv(os.path.join(folder_path, filename))
            print(f"Converted {filename}")

        if filename.endswith('.csv'):
            path = filename if "data" in filename else os.path.join(folder_path, filename)

            country_name = filename.replace('.csv', '').replace(f'data/{data_type}s/usa/', '').replace(f'_{data_type.capitalize()}', "").capitalize()

            df = pd.read_csv(path)

            df = df.iloc[:, [1, 2, 3]]
            df = df.drop(index=[0, 1])

            try:
                df.iloc[:, 0] = df.iloc[:, 0].apply(lambda x: x[1:])
            except:
                pass

            df.columns = ['Product Code', 'Product Label', f'Total {data_type.capitalize()} {"from" if data_type == "import" else "to"} {country_name} (in USD)']

            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

            if combined_df is None:
                combined_df = df
            else:
                combined_df = pd.merge(combined_df, df, on=['Product Code', 'Product Label'], how='outer')

    combined_df.columns = [col.replace("_x", "") for col in combined_df.columns]

    output_path = f'data/{data_type}s/usa/combined_{data_type}.csv'
    combined_df.to_csv(output_path, index=False)

    print(f"Data combined successfully and saved to '{output_path}'")

def main():
    parser = argparse.ArgumentParser(description="Combine Import/Export Data")
    parser.add_argument('type', choices=['import', 'export'], help="Specify whether to combine import or export data")
    parser.add_argument('country', choices=['usa'], help="Specify the home base country")
    
    args = parser.parse_args()

    folder_path = f'data/{args.type}s/{args.country}'
    
    combine_data(folder_path, args.type)

if __name__ == "__main__":
    main()
