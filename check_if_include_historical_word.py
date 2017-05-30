import csv
import pandas as pd

historical_people = []
historical_event = []
with open('historical_people.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        historical_people.append(row[0])

with open('historical_event.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        historical_event.append(row[0])

df = pd.read_csv("historicalbooks_milanz.csv")

df['description'] = df['description'].fillna("")

f = lambda x: True if any(name in x['description'] for name in historical_people) | any(name in x['description'] for name in historical_event) else False

# x = '(' + '|'.join(list(dataframe2['Japanese Era Names in Kanji'])) + ')'
# dataframe1['has_era'] = dataframe1['description'].str.contains(x)

df['includes_historical_words'] = df.apply(f, axis=1)

df.to_csv("historicalbooks_flag_historical_words.csv")

