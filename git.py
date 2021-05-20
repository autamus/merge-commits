import subprocess, sys

##############################################################################
# Global Variables
##############################################################################

# Define SUCCESS for comparing command return codes.
SUCCESS = 0

def run(git_dir, command):
    result = subprocess.run(["git","--git-dir", git_dir] + command.split(), 
        capture_output=True, text=True)
    return result

def current_commit(git_dir):
    """
    Retrieve the current HEAD commit hash from a git repository.

    Parameters:
    git_dir (str) : the location of the git repository .git directory.
    """

    out = run(git_dir, "rev-parse --short HEAD")
    # Check return code for failed command execution.
    if out.returncode == SUCCESS:
        return out.stdout.strip("\n")
    else:
        print("Git Error: " + out.stderr.strip("\n"))
        sys.exit(1)

def commit_parents(git_dir, current_commit):
    """
    Retrive a list of the parents for a given commit hash.

    Parameters:
    git_dir (str) : the location of the git repository .git directory.
    current_commit (str) : the hash of a commit from within the repository.
    """
    out = run(git_dir, f"show -s --pretty=%P {current_commit}")
    if out.returncode == SUCCESS:
        return out.stdout.strip("\n").split()
    else:
        print("Git Error: " + out.stderr.strip("\n"))
        sys.exit(1)

def commit_merge_base(git_dir, parent_commit, branch_commit):
    out = run(git_dir, f"merge-base {parent_commit} {branch_commit}")
    if out.returncode == SUCCESS:
        return out.stdout.strip("\n")
    else:
        print("Git Error: " + out.stderr.strip("\n"))
        sys.exit(1)

def repo_owner(git_dir, upstream):
    out = run(git_dir, f"remote get-url {upstream}")
    if out.returncode == SUCCESS:
        return (*out.stdout.strip(".git\n").split("/")[-2:], )
    else:
        print("Git Error: " + out.stderr.strip("\n"))
        sys.exit(1)