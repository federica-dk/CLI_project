#imports
from datetime import date
import os
import json
filename = '/Users/federica/Desktop/PFS/python-for-everybody-notes/CLIJournal/journal_entries.json'
#Choices
def choices():
    print('Journal Data Management System')
    print('1. View')
    print('2. Write')
    print('3. Exit')

#option 1 View data
def view_data():
    sort_type = input('Would you like to sort by date (D) or Category (C)')
    if sort_type == "C" or sort_type == 'c':
        with open(filename, 'r') as f:
            temp = json.load(f)
            for entry in temp:
             print(entry)
                date = entry["date"]
                mood = entry['mood']
                reflection = entry['reflection']
                category = entry['category']
                print(f"Date written: {date}")
                print(f"Mood score of entry: {mood}")
                print(f"One line reflection: {reflection}")
                print(f"What category does this belong to?: {category}")
                print("\n\n")
    elif sort_type == 'c' or sort_type == "C":
        pass

# Add Data Function
def add_data():
    item_data = {}
    with open (filename, 'r') as f:
        temp = json.load(f)
    x = 0
    item_data['date'] = str(date.today()),
    item_data['mood'] = input('Enter your mood (1-10): '),
    item_data['reflection']= input("What is today's one line reflection?: ")
    print(item_data)

    value = input('Would you like to comit this entry? (Y or N): ')
    x = 1
    while x ==1:
        if value == 'Y' or value == 'y':
            x=0
            temp.append(item_data)
            with open (filename, 'w') as f:
                json.dump(temp, f, indent = 4)
        else:
            item_data['date'] = str(date.today()),
            item_data['mood'] = input('Enter your mood (1-10): '),
            item_data['reflection']= input("What is today's one line reflection?: ")
            print(item_data)
            value = input('Would you like to comit this entry? (Y or N): ')
            x = 1
    




while True:
    choices()
    choice = input('\nEnter Number:')
    if choice == "1":
        view_data()
    elif choice == "2":
        add_data()
    elif choice == "3":
        break
    else:
        print('The answer is invalid please choose again')



