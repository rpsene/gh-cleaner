import requests
import argparse

# Constants
USERNAME = ""  # Replace with your GitHub username
TOKEN = ""  # Replace with your GitHub token
GITHUB_API = "https://api.github.com"

def list_repos():
    """List all personal repositories of the user, handling pagination."""
    repos = []
    page = 1
    per_page = 100  # Max allowed value to minimize the number of requests

    while True:
        url = f"{GITHUB_API}/user/repos"
        params = {
            'type': 'owner',
            'sort': 'created',
            'per_page': per_page,
            'page': page
        }
        response = requests.get(url, auth=(USERNAME, TOKEN), params=params)
        if response.status_code == 200:
            current_repos = response.json()
            if not current_repos:
                break  # If no more repos, exit the loop
            repos.extend(current_repos)
            page += 1
        else:
            print("Failed to fetch repositories")
            break

    return [repo['full_name'] for repo in repos]

def archive_repo(repo_name):
    """Archive a specified repository."""
    url = f"{GITHUB_API}/repos/{repo_name}"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    payload = {
        'archived': True,
    }
    response = requests.patch(url, auth=(USERNAME, TOKEN), headers=headers, json=payload)
    if response.status_code == 200:
        print(f"Successfully archived {repo_name}")
    else:
        print(f"Failed to archive {repo_name}: {response.content}")

def delete_repo(repo_name):
    """Delete a specified repository."""
    url = f"{GITHUB_API}/repos/{repo_name}"
    response = requests.delete(url, auth=(USERNAME, TOKEN))
    if response.status_code == 204:
        print(f"Successfully deleted {repo_name}")
    else:
        print(f"Failed to delete {repo_name}")

def bulk_archive(file_path):
    """Read repository names from a file and archive them."""
    with open(file_path, 'r') as file:
        repos_to_archive = file.read().splitlines()
        for repo in repos_to_archive:
            archive_repo(repo)

def bulk_delete(file_path):
    """Read repository names from a file and delete them."""
    with open(file_path, 'r') as file:
        repos_to_delete = file.read().splitlines()
        for repo in repos_to_delete:
            delete_repo(repo)

def main():
    parser = argparse.ArgumentParser(description="Manage your GitHub repositories.")
    parser.add_argument('action', choices=['delete', 'archive', 'list'], help="Action to perform: delete, archive, or list")
    parser.add_argument('-f', '--file', help="File containing the list of repositories to process", default=None)
    args = parser.parse_args()

    if args.action == 'list':
        # List all personal repositories
        print("Listing all personal repositories:")
        for repo in list_repos():
            print(repo)
    elif args.action == 'delete':
        if not args.file:
            print("Error: 'delete' action requires a file argument.")
            return
        # Bulk delete from file
        print("Deleting repositories listed in " + args.file)
        bulk_delete(args.file)
    elif args.action == 'archive':
        if not args.file:
            print("Error: 'archive' action requires a file argument.")
            return
        # Bulk archive from file
        print("Archiving repositories listed in " + args.file)
        bulk_archive(args.file)

if __name__ == "__main__":
    main()