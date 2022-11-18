"""Module providingFunction printing python version."""
import csv
from datetime import datetime


def csv_parser(file):
    """Parsing csv file."""
    # checks if file is csv
    ending = file.split('.')
    if ending[1] != 'csv':
        print('Please upload "csv" file')
    # creates error log
    error = open('errors.log', 'w')
    # reads csv file
    with open(file, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        # creates new csv file with needed output
        with open('new_file.csv', 'w', newline='') as wfile:
            output = csv.writer(wfile)
            output.writerow(['CandidateName', 'PeriodBegining',
                             'PeriodEnding', 'TransactionID',
                             'TransactionType', 'TransactionAmount'])
            for line in reader:
                if line[1] == 'COH':
                    try:
                        start_date = f'{line[35]}'
                        end_date = f'{line[36]}'
                        start = datetime.strptime(
                            start_date, "%m/%d/%Y").strftime("%Y-%m-%d")
                        end = datetime.strptime(
                            end_date, "%m/%d/%Y").strftime("%Y-%m-%d")
                        name = f'{line[6]} {line[7]}'
                        if len(name) > 1 and (len(line[44]) and len(line[48])
                                              and len(line[64])) > 0 and float(line[64]):
                            row = [name, start, end,
                                   line[44], line[48], line[64]]
                            output.writerow(row)
                        else:
                            error.write(f'{line}\n')
                    except:
                        error.write(f'{line}\n')
                else:
                    error.write(f'{line}\n')

    error.close()
