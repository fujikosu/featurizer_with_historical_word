import json
import csv
import wikipedia

wikipedia.set_lang("jp")
japanese_historical_people_page = wikipedia.page("Wikipedia:すべての言語版にあるべき項目の一覧/日本史の人物")
japanese_historical_event_page = wikipedia.page("日本史の出来事一覧")


historical_people_list = japanese_historical_people_page.links
historical_event_list = japanese_historical_event_page.links

historical_people_list_for_write = [[historical_people_list[i]] for i in range(len(historical_people_list))]
historical_event_list_for_write = [[historical_event_list[i]] for i in range(len(historical_event_list))]

header = ['historical_people',]
with open('historical_people.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') 
    writer.writerow(header)
    writer.writerows(historical_people_list_for_write)

header = ['historical_event',]
with open('historical_event.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') 
    writer.writerow(header)
    writer.writerows(historical_event_list_for_write)