import csv

def preprocess_play(filepath):
    out_str = []
    unique_names = set()
    with open(filepath) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            unique_names.add(row[0])
            out_str.append([row[0], row[1]])
    return (out_str, unique_names)