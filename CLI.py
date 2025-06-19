#imports
from datetime import date
import os
import json
filename = '/Users/federica/Desktop/PFS/CLIJournal/CLI_project/journal_entries.json'
#Choices
def choices():
    print('Journal Data Management System')
    print('1. View')
    print('2. Write')
    print('3. Delete Entry')
    print('4. Exit')

#option 1 View data
def view_data():
    searching = input('Would you like to search for a specific entry?(Y / N): ')
    if searching == 'N' or searching == 'n':
        with open(filename, 'r') as f:
            temp = json.load(f)
            for entry in temp:
                date = entry["date"]
                mood = entry['mood']
                reflection = entry['reflection']
                print(f"Date written: {date}")
                print(f"Mood score of entry: {mood}")
                print(f"One line reflection: {reflection}")
                print("\n\n")
                print("\n\n")
    else:
        search()

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
    

#Sorting data
def search():
    item_data = {}
    with open (filename, 'r') as f:
        temp = json.load(f)
    x = 0
    item_data = temp
    value = input('What date are you searching for? (Year-month-day): ')
    found_entry = False
    for entry in item_data:
        if entry['date'] == value:
            date = entry["date"]
            mood = entry['mood']
            reflection = entry['reflection']
            print(f"Date written: {date}")
            print(f"Mood score of entry: {mood}")
            print(f"One line reflection: {reflection}")
            print("\n\n")
            print("\n\n")
            found_entry = True
            remove = input('Would you like to delete this entry? (Y / N)')
            if remove == 'Y' or remove == 'y':
                delete()
        if not found_entry:
            print(f"No journal entries found for the date: {value}")


#Delete entry function
def delete():
    # 1. Load existing data
    with open(filename, 'r') as f:
        journal_entries = json.load(f) # journal_entries will be a list

    date_to_delete = input('Enter the date of the entry/entries you want to delete (Year-month-day): ')

    initial_count = len(journal_entries)
    updated_entries = [entry for entry in journal_entries if entry.get("date") != date_to_delete]

    if len(updated_entries) == initial_count:
        print(f"No entries found for date '{date_to_delete}'. Nothing was deleted.")
    else:
        deleted_count = initial_count - len(updated_entries)
        print(f"Found and deleting {deleted_count} entr(y/ies) for date '{date_to_delete}'.")
            
        
        with open(filename, 'w') as f: # Open in 'w' (write) mode to overwrite the file
            json.dump(updated_entries, f, indent=4) # Use indent for pretty printing
        print("Deletion successful and journal updated.")

while True:
    choices()
    choice = input('\nEnter Number:')
    if choice == "1":
        view_data()
    elif choice == "2":
        add_data()
    elif choice == "4":
        break
    elif choice == '3':
        delete()
    else:
        print('The answer is invalid please choose again')



