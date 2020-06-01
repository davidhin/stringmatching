import so_textprocessing as stp
import pandas as pd

# Load textpreprocess with default target word list
tp = stp.TextPreprocess()

# Use longer string match if available
tp.strmatch('symlink following', reformat='summary') # (1, 1, dict_keys(['symlink following']))
tp.strmatch('symlink', reformat='summary') # (1, 1, dict_keys(['symlink']))

# UK/US spelling
tp.strmatch('incorrect synchronization', stem=True, reformat='index') # [(0, 17, 'incorrect synchron')]
tp.strmatch('incorrect synchronisation', stem=True, reformat='index') # [(0, 17, 'incorrect synchron'), (0, 19, 'incorrect synchronis')]
tp.strmatch('incorrect synchronisation', stem=True, reformat='summary') # [(0, 17, 'incorrect synchron'), (0, 19, 'incorrect synchronis')]
tp.strmatch('unauthorized control', stem=True, reformat='index') # [(0, 15, 'unauthor control')]
tp.strmatch('unauthorised control', stem=True, reformat='index') # [(0, 17, 'unauthoris control')]
tp.strmatch('sanitisation', reformat='index') # [(0, 4, 'sanit')]

# Short strings only work when surrounded by non-letters
tp.strmatch('xsss', reformat='summary') # (0, 0, dict_keys([]))
tp.strmatch('.xss.', reformat='summary') # (1, 1, dict_keys(['xss']))
tp.strmatch('.xss ', reformat='summary') # (1, 1, dict_keys(['xss']))

# Stemming is functioning
tp.strmatch('relative path travers', reformat='summary') # (1, 1, dict_keys(['path traversal']))

# When longer string and shorter string are both present, count both if necessary
tp.strmatch('time bomb logic bomb', reformat='summary') # (2, 2, dict_keys(['time bomb', 'logic bomb']))
tp.strmatch('time bomb bomb', reformat='summary') # (2, 2, dict_keys(['time bomb', 'bomb']))
tp.strmatch('time bomb bomb bomb logic bomb', reformat='summary') # (3, 4, dict_keys(['time bomb', 'bomb', 'logic bomb']))
