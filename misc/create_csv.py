import csv
def create_csv(dict_data,name):
    csv_columns = ['no','link','source','title','date','body','image']
    csv_file = name
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")