# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the [Project Name] Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# daily_journal_li_app - Simple terminal-based journaling tool
#                       Stores entries in text or JSON
#                       Skills: file I/O, datetime usage
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import datetime
import json
import os
import sys


# ==========================================================

# --------------------------------------------------
# JOURNAL: MAIN CLI MODULE
# --------------------------------------------------
"""
1. Entry Point: The app starts in the terminal/command-line interface.
2. Command Processing: The application listens for commands, processes 
the input, and calls the appropriate functionality.
"""
def main():
    if len(sys.argv) > 1:
        command_processing(sys.argv)
    else:
        display_help(sys.argv[0])

def command_processing(args):
    if args[1] == "-h" or args[1] == "--help":
        display_help(args[0])
    elif args[1] == "-v" or args[1] == "--version":
        display_version(args[0])
    elif args[1] == "--add" and len(args) == 3:
        add_entry(args[2])
    elif args[1] == "--view" and len(args) == 3:
        view_entry()
    elif args[1] == "--edit" and len(args) == 4:
        edit_entry(args[2], args[3])
    elif args[1] == "--delete" and len(args) == 3:
        delete_entry(args[2])
    elif args[1] == "--list":
        display_list()
    else:
        print("Command not recorgnized. Use -h or --help for help.")

# ==========================================================

# --------------------------------------------------
# JOURNAL ENTRY MODULE
# --------------------------------------------------
"""
Data Model: Each journal entry contains:
    - Date (timestamp)
    - Content (the journal text written by the user)
"""
class JournalEntry:
    def __init__(self, date, content):
        self.date = date
        self.content = content


# ==========================================================

# --------------------------------------------------
# COMMANDS MODULE
# --------------------------------------------------
"""
1. Add Entry: Allows the user to add a new journal entry with a 
    timestamp (date).
2. View Entry: Displays a journal entry based on the date provided 
    by the user.
3. Edit Entry: Modifies an existing journal entry.
4. Delete Entry: Deletes an entry by date.
5. List Entries: Lists all journal entries sorted by date.
6. Help: Displays a list of available commands and their usage.
7. Version: Displays program version details.
"""
# --------------------------------------------------
# 1. add entry
# --------------------------------------------------
"""
1. User enters the command: add "My journal entry for today"
2. App captures the current date and the entry content.
3. The entry is stored in a local file (in JSON format or as
     a text entry).
4. User is notified that the entry was successfully added.
"""
def add_entry(entry):
    if not input_validator(entry):
        print("Journal entry cannot be empty.")
        return
    date_string = datetime.datetime.now().strftime("%Y-%m-%d")
    new_entry = {
        "date": date_string,
        "content": entry
    }
    context = read_file(file="journal_entries.json")
    if not context:
        context = []

    for item in context:
        if item.get("date") == date_string:
            print("An entry for today already exists.")
            return
    context.append(new_entry)
    write_file(file="journal_entries.json",
                content=json.dumps(context))
    print(f"Entry for {date_string} added.")

# --------------------------------------------------
# 2. view entry
# --------------------------------------------------
"""
1. User enters the command: view 2023-12-10 (for example).
2. App checks if there is an entry for the given date.
3. If found, the app displays the content of the entry.
4. If not found, the app displays a "No entry found" message.
"""
def view_entry(date_string):
    if validate_date_format(date_string=date_string) == False:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    context = read_file("journal_entries.json")
    if context == None:
        print("No entries found or the file is missing.")
    else:
        entry_found = False
        for item in context:
            for key in item.keys():
                if key["date"] == date_string:
                    print(f"Date: {key['date']} - ", end="")
                    print(f"Entry: {key['content'][:30]}...")
                    entry_found = True
                    break
        if not entry_found:
            print("Entry not found for the given date.")

# --------------------------------------------------
# 3. edit entry
# --------------------------------------------------
"""
1. User enters the command: edit 2023-12-10 "Updated journal
    entry content".
2. The app locates the existing entry for the given date.
3. The content is replaced with the new input from the user.
4. The file is updated, and the user is notified that the entry
    was edited.
"""
def edit_entry(date_string, entry):
    if validate_date_format(date_string=date_string) == False:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    elif not input_validator(entry):
        print("Journal entry cannot be empty.")
        return
    context = read_file("journal_entries.json")
    if context == None:
        print("No entries found or the file is missing.")
    else:
        entry_found = False
        for item in context:
            if item.get("date") == date_string:
                item.get(["content"]) = entry
                entry_found = True
                break
        if entry_found:
            write_file(file="journal_entries.json", 
                       content=json.dumps(context))
            print(f"Entry for {date_string} updated.")
        else:
            print("Entry not found for the given date.")

# --------------------------------------------------
# 4. delete entry
# --------------------------------------------------
"""
1. User enters the command: delete 2023-12-10.
2. The app checks if the entry exists.
3. If it exists, it deletes the entry from the file and 
    notifies the user of the deletion.
4. If not found, it shows a "No entry found" message.
"""
def delete_entry(date_string):
    if validate_date_format(date_string=date_string) == False:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    context = read_file("journal_entries.json")
    if context == None:
        print("No entries found or the file is missing.")
    else:
        entry_found = False
        for item in context:
            for key in item.keys():
                if key["date"] == date_string:
                    context.remove(item)
                    entry_found = True
                    break
        if entry_found:
            write_file(file="journal_entries.json", 
                       content=json.dumps(context))
            print(f"Entry for {date_string} deleted.")
        else:
            print("Entry not found for the given date.")

# --------------------------------------------------
# 5. list entries
# --------------------------------------------------
"""
1. User enters the command: list.
2. App loads all entries from the file.
3. Entries are sorted by date.
4. A list of entries is displayed, showing the date and 
    part of the content for each entry.
"""
def display_list():
    context = read_file("journal_entries.json")
    if context == None:
        print("No entries found or the file is missing.")
    else:
        print("Journal Entries:")
        print("----------------")
        for item in context:
            for key in item.keys():
                print(f"Date: {key['date']} - ", end="")
                print(f"Entry: {key['content'][:30]}...")
# --------------------------------------------------
# 6. help
# --------------------------------------------------
"""
1. User enters the command: -h or --help.
2. The app displays a brief description of all available 
    commands with examples.
"""
def display_help(string):
    print(f"Usage: {string} [options] <date or string>")
    print("--add <string>\t\tAdd entry")
    print("--delete <date>\t\tDelete entry")
    print("--edit <date> <string>\tEdit entry")
    print(" -h or --help\t\tDisplay program help")
    print("--list \t\t\tList entries")
    print(" -v or --version\tDisplay program version")
    print("--view <date>\t\tView entry")

# --------------------------------------------------
# 6. version
# --------------------------------------------------
"""
1. User enters the command: -v or --version.
2. The app displays the program version
""" 
def display_version(string):
    print(f"{string} version 1.0.0")

# ==========================================================

# --------------------------------------------------
# FILE_IO MODULE
# --------------------------------------------------
"""
File Operations: The app will read from and write to a local file,
either in a structured format like JSON or plain text.
    - Read File: Load all existing entries.
    - Write File: Save a new entry or modifications to existing entries.
"""
def read_file(file):
    if (os.path.exists(file) == True):
            if file.endswith(".txt"):
                with open(file=file, mode="r") as f:
                    content = f.read()
            elif file.endswith(".json"):
                with open(file=file, mode="r") as f:
                    if os.stat(file).st_size == 0:
                        return None
                    content = json.load(f)
            return content
    else:
        print("File not found.")
        return None

def write_file(file, content, mode="w"):
    with open(file=file, mode=mode) as f:
        f.write(content)

# ==========================================================

# --------------------------------------------------
# HELPER MODULE
# --------------------------------------------------
"""
1. Date Format Validator: Ensures the date is in the correct format 
    (e.g., YYYY-MM-DD).
2. Input Validator: Ensures the journal entry text is valid (non-empty).
3. Logging: Log important events like command execution, errors, etc.
"""
def validate_date_format(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def input_validator(entry):
    return bool(len(entry.strip()) > 0)

def logging():
    pass

if __name__ == "__main__":
    main()
