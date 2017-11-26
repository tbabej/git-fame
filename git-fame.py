#!/usr/bin/python3

"""
Usage: git-fame <source> <target>
"""

import os

import docopt
import git

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S %z'

def record_shadow_commit(shadow_repo, commit):
    """
    Creates a shadow commit in the shadow repo. The actual file content change
    is the commit's hexsha added to the COMMITS file.
    """

    tree_dir = shadow_repo._working_tree_dir
    commits_file = os.path.join(tree_dir, 'COMMITS')

    with open(commits_file, 'a') as f:
        f.write(commit.hexsha)

    shadow_repo.index.commit(
        commit.hexsha,
        author=commit.author,
        committer=commit.committer,
        author_date=commit.authored_datetime.strftime(DATETIME_FORMAT),
        commit_date=commit.committed_datetime.strftime(DATETIME_FORMAT)
    )

args = docopt.docopt(__doc__)

# Intialize both repos
source_path = os.path.expanduser(args['<source>'])
target_path = os.path.expanduser(args['<target>'])

source_repo = git.Repo(source_path)
target_repo = git.Repo(target_path)

for commit in source_repo.iter_commits('master'):
    record_shadow_commit(target_repo, commit)
