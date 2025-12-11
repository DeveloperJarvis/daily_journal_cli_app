# **Low-Level Design (LLD)** of a **Daily Journal CLI App in Python**

### 1. **Overview**

The Daily Journal CLI App is a command-line tool that allows users to record daily journal entries. The app will support functionalities such as:

- **Adding a new entry** for the current day.
- **Listing all entries** by date.
- **Viewing a specific entry** by date.
- **Editing an entry** by date.
- **Deleting an entry** by date.
- **Saving entries** in a local file (like a text file or JSON format) for persistence.
- **Displaying help** on available commands and usage.

---

### 2. **Components**

#### 2.1. **Main CLI Application**

- **Entry Point:** The app starts in the terminal/command-line interface.
- **Command Processing:** The application listens for commands, processes the input, and calls the appropriate functionality.

#### 2.2. **Commands**

1. **Add Entry**: Allows the user to add a new journal entry with a timestamp (date).
2. **View Entry**: Displays a journal entry based on the date provided by the user.
3. **Edit Entry**: Modifies an existing journal entry.
4. **Delete Entry**: Deletes an entry by date.
5. **List Entries**: Lists all journal entries sorted by date.
6. **Help**: Displays a list of available commands and their usage.

#### 2.3. **Journal Entry**

- **Data Model:** Each journal entry contains:

  - **Date** (timestamp)
  - **Content** (the journal text written by the user)

#### 2.4. **File Handler**

- **File Operations:** The app will read from and write to a local file, either in a structured format like JSON or plain text.

  - **Read File:** Load all existing entries.
  - **Write File:** Save a new entry or modifications to existing entries.

#### 2.5. **Helper Functions**

- **Date Format Validator:** Ensures the date is in the correct format (e.g., `YYYY-MM-DD`).
- **Input Validator:** Ensures the journal entry text is valid (non-empty).
- **Logging:** Log important events like command execution, errors, etc.

---

### 3. **Data Flow**

#### 3.1. **Add Entry**

1. User enters the command: `add "My journal entry for today"`
2. App captures the current date and the entry content.
3. The entry is stored in a local file (in JSON format or as a text entry).
4. User is notified that the entry was successfully added.

#### 3.2. **View Entry**

1. User enters the command: `view 2023-12-10` (for example).
2. App checks if there is an entry for the given date.
3. If found, the app displays the content of the entry.
4. If not found, the app displays a "No entry found" message.

#### 3.3. **Edit Entry**

1. User enters the command: `edit 2023-12-10 "Updated journal entry content"`.
2. The app locates the existing entry for the given date.
3. The content is replaced with the new input from the user.
4. The file is updated, and the user is notified that the entry was edited.

#### 3.4. **Delete Entry**

1. User enters the command: `delete 2023-12-10`.
2. The app checks if the entry exists.
3. If it exists, it deletes the entry from the file and notifies the user of the deletion.
4. If not found, it shows a "No entry found" message.

#### 3.5. **List Entries**

1. User enters the command: `list`.
2. App loads all entries from the file.
3. Entries are sorted by date.
4. A list of entries is displayed, showing the date and part of the content for each entry.

#### 3.6. **Help**

1. User enters the command: `help`.
2. The app displays a brief description of all available commands with examples.

---

### 4. **Command-Line Interface (CLI)**

The app will use the `argparse` module or `click` module for parsing commands and arguments. Example commands:

1. **Add Entry Command:**

   ```
   python journal.py add "This is my first journal entry!"
   ```

2. **View Entry Command:**

   ```
   python journal.py view 2023-12-10
   ```

3. **Edit Entry Command:**

   ```
   python journal.py edit 2023-12-10 "Updated content of the journal entry."
   ```

4. **Delete Entry Command:**

   ```
   python journal.py delete 2023-12-10
   ```

5. **List Entries Command:**

   ```
   python journal.py list
   ```

6. **Help Command:**

   ```
   python journal.py help
   ```

---

### 5. **File Handling (Persistence)**

#### 5.1. **File Format**

The entries can be saved in either a plain text or structured file format. Two common approaches are:

1. **Text-based file**:

   - Entries can be stored in a plain text file with each entry on a new line, prefixed with the date.

   Example:

   ```
   2023-12-10: This is my first journal entry.
   2023-12-11: Another journal entry.
   ```

2. **JSON-based file**:

   - Entries are stored in a structured JSON file with each entry having a date and content.

   Example:

   ```json
   [
     { "date": "2023-12-10", "content": "This is my first journal entry." },
     { "date": "2023-12-11", "content": "Another journal entry." }
   ]
   ```

#### 5.2. **File Operations**

- **Read:** At the start of the application, the app reads the entire file to load existing journal entries into memory.
- **Write:** When a new entry is added, edited, or deleted, the app writes the updated content back to the file.

---

### 6. **Helper Functions and Validations**

#### 6.1. **Date Format Validator**

- Ensures that the date entered by the user is in the correct format (`YYYY-MM-DD`).
- If invalid, it prompts the user to re-enter the correct date.

#### 6.2. **Input Validator**

- Ensures the journal entry content is not empty and does not contain any invalid characters.

#### 6.3. **Logging**

- Logs actions such as adding, editing, or deleting entries, as well as errors or invalid input.

---

### 7. **Error Handling**

- **Invalid Command:** If the user enters an unrecognized command, the app should display a helpful error message with the available commands.
- **File Not Found:** If the app cannot find the file where the entries are stored, it should prompt the user to create a new file or check the file path.
- **Date Not Found:** If the user tries to view or edit an entry that doesn't exist, an error message should inform the user.

---

### 8. **Use Cases**

#### 8.1. **Add Journal Entry**

- **Input:** `python journal.py add "Today I learned about LLD"`
- **Output:** The entry is added under the current date.

#### 8.2. **View Journal Entry**

- **Input:** `python journal.py view 2023-12-10`
- **Output:** Displays the content of the journal for `2023-12-10`.

#### 8.3. **Edit Journal Entry**

- **Input:** `python journal.py edit 2023-12-10 "Updated entry content"`
- **Output:** The existing entry for `2023-12-10` is updated with the new content.

#### 8.4. **Delete Journal Entry**

- **Input:** `python journal.py delete 2023-12-10`
- **Output:** The entry for `2023-12-10` is deleted from the file.

#### 8.5. **List All Entries**

- **Input:** `python journal.py list`
- **Output:** Displays all journal entries, sorted by date.

---

### 9. **Assumptions**

1. The journal entries are stored in a local file (either plain text or JSON).
2. All journal entries are stored with a date and content.
3. The user will interact with the app through the command-line interface (CLI).
4. The app assumes the user will input valid commands or expects error handling for invalid inputs.

---

### 10. **Future Enhancements**

1. **Password Protection**: Implement a password mechanism to protect the journal from unauthorized access.
2. **Search Functionality**: Add the ability to search for journal entries based on keywords.
3. **Backup/Restore**: Provide a backup and restore functionality for the journal entries.
4. **Synchronization**: Allow synchronization with cloud storage for remote access to journal entries.
