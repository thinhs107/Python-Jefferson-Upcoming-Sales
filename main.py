import pandas as pd
import re
from pathlib import Path

pd.options.display.max_columns = None
pd.options.display.max_rows = None


def extract_from_csv(file_to_process, number_rows):
    dataframe = pd.read_csv(file_to_process, nrows=number_rows)
    return dataframe


def transformer(_extract_df, column_to_be_rename, new_column_name):
    # Rename Columns
    transform_df = _extract_df.rename(columns={column_to_be_rename: new_column_name})
    return transform_df


def formatText(parseValue):
    pattern = "vs.\s*[\n\r\a-z]*"
    string_pattern = re.search(pattern, parseValue).group(0)
    string_pattern = str(string_pattern).replace('vs.', '')
    return string_pattern


# def etl_process():
#     table1 = [['foo', 'bar', 'baz'],
#               ['A', '2.4', 12],
#               ['B', '5.7', 34],
#               ['C', '1.2', 56]]
#     table5 = etl.convert(table1, 'foo', 'replace', 'A', 'AA')
#     print(table5)


# x = conn.conn_to_db();
# print(x)

if __name__ == '__main__':
    input_file_to_process = 'http://jeffcomm.org/docs/webPush.csv'

    output_df = extract_from_csv(input_file_to_process, 100)

    # Rename Columns
    # transform_df = output_df.rename(columns={'DIV': 'DIV_rename'})
    output_transform_df = transformer(output_df, 'DIV', 'Div_rename')

    # print(output_transform_df)

    format_text_list = []
    # format_text_list.append('a')
    print(type(format_text_list))

    for index, row in output_transform_df.iterrows():
        format_records = formatText(row['expr5'])
        format_text_list.append(format_records)
        # output_transform_df.insert('Parse_value', value=(formatText(['expr5'])))
        # conn.conn_to_db(row['CASE'])
    # print(row['CASE'])

    # Adding new columns to dataframe to contain format text
    output_transform_df['Parse_Value'] = format_text_list
    # print(output_transform_df)

    # Write DF to CSV
    filepath = Path('D:\\PycharmProjects\\Output\\fileFormat.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    output_transform_df.to_csv(filepath, index=False)

    print(f'output located in {filepath}')

    # Count how many rows
    number_of_rows = output_transform_df[output_transform_df.columns[0]].count()
    # or
    len_number_of_rows = len(output_transform_df.index)

