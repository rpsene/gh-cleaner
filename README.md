# GitHub Cleaner

GitHub Cleaner is a Python script for managing your GitHub repositories. With it, you can list all your repositories, archive them, or delete them in bulk by providing a file with the repository names.

## Prerequisites

Before you run this script, make sure you have:

- Python 3 installed on your system.
- `requests` library installed in your Python environment (`pip install requests`).
- A GitHub Personal Access Token with appropriate permissions (repo for full control of private repositories). See GitHub documentation on how to generate one.

## Installation

1. Clone this repository or download the `clean.py` script.
2. Ensure you have the necessary Python version and packages installed.
3. Update the script with your GitHub username and personal access token.

## Usage

The script `clean.py` can be run with the following commands:

### List Repositories

To list all your personal GitHub repositories:

```bash
python3 clean.py list
```

### Archive Repositories
To archive repositories:

```bash
python3 clean.py archive -f FILE
```

Replace FILE with the path to a text file containing the full names of the repositories you want to archive, one per line.

### Delete Repositories
To delete repositories:

```bash
python3 clean.py delete -f FILE
```

Replace FILE with the path to a text file containing the full names of the repositories you want to delete, one per line.

### General Options

-h, --help - Show the help message and exit.
-f FILE, --file FILE - File containing the list of repositories to process. This is required for the delete and archive actions.

### Important Notes
Use With Caution: Deletion and archiving are significant actions. Ensure you want to perform these actions before running the script. Always double-check the list of repositories in your file.

Rate Limits: Be aware of GitHub's rate limits. If you have a large number of repositories, you might need to handle pagination or rate limiting in your script.

Error Handling: The script provided is a basic example. In a production environment, you should implement comprehensive error handling to manage different failure scenarios gracefully.
Contributing


### Contributions are welcome :)

If you have a suggestion or improvement, please fork the repository and create a pull request.
