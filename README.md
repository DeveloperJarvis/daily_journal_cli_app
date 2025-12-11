# daily_journal_cli_app - Simple Terminal-based Journaling Tool

## Overview

**daily_journal_cli_app** is a simple terminal-based journaling tool that allows users to record daily journal entries. The tool can store entries in either a text file or a JSON file, providing a simple way to keep track of your thoughts, ideas, and daily events.

## Features

- **Add new journal entries** for the current day or any specific date.
- **View journal entries** by date.
- **Edit journal entries** if you need to update them.
- **Delete journal entries** if no longer needed.
- **List all journal entries** in a simple, chronological order.
- **Store entries in JSON or plain text** formats.
- **Command-line interface** for easy interaction.

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/DeveloperJarvis/daily_journal_cli_app.git
cd daily_journal_cli_app
```

### Step 2: Set up the environment (Optional but recommended)

You can create a virtual environment to isolate dependencies:

```bash
python -m venv .env
source .env/bin/activate  # On Windows use .env\Scripts\activate
```

### Step 3: Install required dependencies

If you have a `requirements.txt` file, install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Commands:

Once the app is installed, you can use it through the command line. Below are the available commands:

- **Add Entry**: Add a new journal entry for today or a specific date:

  ```bash
  python main.py add "Today I learned about journaling."
  ```

- **View Entry**: View a journal entry for a specific date:

  ```bash
  python main.py view 2023-12-10
  ```

- **Edit Entry**: Edit an existing journal entry by date:

  ```bash
  python main.py edit 2023-12-10 "Updated content of the journal entry."
  ```

- **Delete Entry**: Delete an entry by its date:

  ```bash
  python main.py delete 2023-12-10
  ```

- **List Entries**: List all journal entries, sorted by date:

  ```bash
  python main.py list
  ```

- **Help**: Get more help or see all available commands:

  ```bash
  python main.py help
  ```

### Example Usage:

#### Add a Journal Entry

```bash
python main.py add "Today was a productive day."
```

#### View a Journal Entry

```bash
python main.py view 2023-12-10
```

#### Edit an Existing Journal Entry

```bash
python main.py edit 2023-12-10 "Updated the entry content."
```

#### Delete a Journal Entry

```bash
python main.py delete 2023-12-10
```

#### List All Journal Entries

```bash
python main.py list
```

## File Storage

### Supported Formats

- **Text format**: Stores each journal entry as a simple text file, each one dated appropriately.
- **JSON format**: Stores entries in a structured format, making it easier to handle, process, or export data programmatically.

### Default Storage Location

- **JSON**: By default, journal entries are saved to `journal_entries.json` in the same directory as the script.
- **Text files**: Each journal entry is saved as a separate text file, with the filename as the date (e.g., `2023-12-10.txt`).

Example of `journal_entries.json`:

```json
[
  {
    "date": "2023-12-10",
    "content": "Today was a productive day."
  },
  {
    "date": "2023-12-11",
    "content": "Started learning about CLI apps in Python."
  }
]
```

### File Structure:

```
daily_journal_cli_app/
│
├── main.py              # Journal script for the CLI app
├── journal_entries.json # JSON file to store journal entries
├── requirements.txt     # (Optional) Dependency list for the app
├── README.md            # Project documentation
└── LICENSE              # License information (GPL-3.0-or-later)
```

## License

This project is licensed under the **GNU General Public License, version 3** (GPL-3.0-or-later). See the [LICENSE](LICENSE) file for details.

## Author

**Developer Jarvis** (Pen Name)
[GitHub Profile](https://github.com/DeveloperJarvis)

## Creating tag

```bash
# 1. Check existing tags
git tag
# 2. Create a valid tag
git tag -a v1.0.0 -m "Release version 1.0.0"
# or lightweight tag
git tag v1.0.0
# push tag to remote
git push origin v1.0.0
```
