# Daily Journal
A simple Command Line Interfacing (CLI) journal to record your daily thoughts, mood, and reflection directly from your terminal. Built using Python, the program saves your prior entires creating a quick, private way to track your reflections.

## Features
* **Add Entries:** Quickly add new journal entries with a date, mood, and reflection.
* **View Entries:** Browse through past journal entries.
* **Search Entries:** Find specific entries by date or mood.
* **Delete Entries:** Remove unwanted journal entries.
* **Persistent Storage:** All data is saved to a local JSON file, ensuring your entries are preserved between sessions.
* **User-Friendly CLI:** Straightforward interaction directly in the terminal.

## Getting started
* Python 3.6 or higher (You can check your Python version with `python --version` or `python3 --version`)
  
### Installation Steps

1.  **Clone the repository (or download the code):**
    ```bash
    git clone [https://github.com/](https://github.com/)[GitHub_Username]/[Repo_Name].git
    cd [Repo_Name]
    

2.  **Navigate to the project directory:**

    ```bash
    cd [Folder_Name]
    ```
    *(Adjust this path to where your `CLI.py` and `journal.json` files are located)*

3.  **No external libraries required:**
    This project primarily uses Python's built-in `json` module, so there are no additional `pip install` steps needed unless you add new features requiring them.

## Usage

Once installed, you can run the journal program from your terminal.

1.  **Run the main program:**

    ```bash
    python CLI.py
    ```
    *(Or `python3 CLI.py` depending on your system's Python setup)*

2.  **Follow the on-screen prompts:**
    The program will present you with options to add, view, search, or delete journal entries.

    ```
    Welcome to your CLI Journal!
    ---------------------------
    [A] Add new entry
    [V] View all entries
    [S] Search for entries by date
    [D] Delete entries by date
    [Q] Quit

    Enter your choice: 
    ```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

