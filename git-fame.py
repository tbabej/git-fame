#!/usr/bin/python3

"""
Usage: git-fame <source> <target>
"""

import os

import docopt
import git

args = docopt.docopt(__doc__)

# Intialize both repos
source_path = os.path.expanduser(args['<source>'])
target_path = os.path.expanduser(args['<target>'])

source_repo = git.Repo(source_path)
target_repo = git.Repo(target_path)

for commit in source_repo.iter_commits('master'):
    print(commit)
