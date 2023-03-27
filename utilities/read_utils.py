import pandas

"""method to get Excel as list"""


def get_excel_as_list(file_path, sheet_name):
    df = pandas.read_excel(io=file_path, sheet_name=sheet_name)
    return df.values.tolist()


def get_csv_as_list(filepath, delimeter):
    df=pandas.read_csv(filepath_or_buffer=filepath, delimiter=delimeter)
    return df.values.tolist()