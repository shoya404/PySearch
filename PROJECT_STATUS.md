# PySearch Project Status

## Current Day
Day 4

## Goal
Build a terminal-based search engine using Python and DSA.

## Completed
- Initialized Git repository
- Created project structure
- Created sample text corpus
- Implemented directory traversal
- Implemented text file reading
- Implemented basic keyword search
- Added initial README
- Added argparse-based CLI
- Added --top option
- Added input validation and error handling
- Added pytest test suite
- Added tests for tokenizer, index, and search
- Added pytest configuration via conftest.py

## Current Architecture

Directory
→ File discovery
→ File reading
→ Keyword search
→ Terminal output

## DSA / CS Concepts
- Directory traversal
- Lists
- Strings
- Linear search
- Time complexity of scanning every document

## Git Commits
- Initial setup
- Basic file search

## Next
- Tokenization
- Inverted index
- Hash-based lookup
- Multi-word queries

## Notes
The current search scans every file for every query.
This is intentionally simple and will be replaced by an inverted index on Day 2.