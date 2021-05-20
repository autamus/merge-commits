# merge-commits
A Simple GitHub Action to Find all of the Commits in a PR/Branch since the last merge.

## Usage
```yaml
name: "Find Commits in Last Merge"

on:
  push:
    branches:
      - main

jobs:
  find-commits:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
        with:
          fetch-depth: '0'
        
      - name: Run Merge Commits
        uses: autamus/merge-commits@master
        with:
          # repo_location: '/github/workspace/'
          # current_commit: 'specify a hash here if you don't want to use latest.'
          # pretty_output: 'disable pretty output'
```
