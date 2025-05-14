# determine_commit.py

import datetime
import numpy as np
import random

# Determine if today is a weekend
today = datetime.datetime.today().weekday()
is_weekend = today >= 5

# 85% probability of no commit on weekends
if is_weekend and np.random.randint(0, 11) < 9:
    should_commit = False
else:
    if np.random.randint(0, 11) < 8:
        # Determine random number of commits (0-15).
        num_commits = np.random.randint(0, 15)
        should_commit = True
    else:
        should_commit = False


print(f"::set-output name=should_commit::{should_commit}")
if should_commit:
    print(f"::set-output name=num_commits::{num_commits}")
