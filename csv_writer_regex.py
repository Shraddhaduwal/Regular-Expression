import csv

def create_csv(filename, string, l):
    """Creating csv files"""
    with open("Results_regex/"+ filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")

        writer.writerow([string])
        for element in sorted(l):
            writer.writerow([element])