#!/usr/bin/env python
__author__ = "Alec Scott"
__license__ = "Apache 2.0"

import git, os

def main():
    # Get values from ENV Variables
    repo_location = os.environ.get("INPUT_REPO_LOCATION", ".") + "/.git"
    current_commit = os.environ.get("INPUT_CURRENT_COMMIT", "")
    pretty = os.environ.get("INPUT_PRETTY_OUTPUT", "false")

    # Find commit values from Repository.
    if current_commit == "":
        current_commit = git.current_commit(repo_location)

    parent_commits = git.commit_parents(repo_location, current_commit)

    # Define empty commits list to store commits in build history.
    commits = []

    # Get all of the commits in the branch since it seperated from the 
    # current branch.
    if len(parent_commits) > 1:
        merge_base_commit = git.commit_merge_base(
            repo_location, 
            parent_commits[0], 
            parent_commits[1]
        )

        # Iterate over the git history like a linked list
        # adding every commit
        current = parent_commits[1]
        while (current != merge_base_commit):
            commits = commits + [current]
            current = git.commit_parents(repo_location, current)[0]

    print(f"""::set-output name=commits::{" ".join(commits)}""")
    if pretty.lower() == "true":
        print("Merge Commits:")
        for merge_commit in commits:
            print("   --> " + merge_commit)
    

    

if __name__ == "__main__":
    main()