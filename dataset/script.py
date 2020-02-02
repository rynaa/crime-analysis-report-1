import csv
import os


def merge_dataset(file_list):
    """Merges all the dataset points into a new dataset
    Note: This function assumes that the order of columns of
    all the csv files are same"""

    write_path = open('merged_data.csv', 'w')
    write_csv = csv.writer(write_path)

    header_string = """STATE/UT
    DISTRICT
    Year
    Murder
    Infanticide
    Rape
    Foeticide
    Kidnapping & Abduction
    Abetment of suicide
    Exposure and Abandonment
    Procuration of minor girls
    Selling of girls for prostitution
    Prohibition of child marriage act
    Other Crimes
    Total"""

    write_csv.writerow(header_string.split('\n'))

    for file_path in file_list:
        with open(file_path, 'r') as csv_file:
            csv_data = csv.reader(csv_file)
            write_csv.writerows(csv_data)

    write_path.close()

if __name__ == "__main__":
    csv_list = ['2001.csv', '2013.csv', '2014.csv', '2015.csv']
    merge_dataset(csv_list)
