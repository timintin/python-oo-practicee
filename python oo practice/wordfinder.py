# wordfinder.py

import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    
    def __init__(self, filepath):
        """Reads words from a file and reports the number of words read."""
        with open(filepath) as file:
            self.words = self.parse(file)
        print(f"{len(self.words)} words read")
    
    def parse(self, file):
        """Parse the file to get the list of words."""
        return [word.strip() for word in file]
    
    def random(self):
        """Return a random word from the list."""
        return random.choice(self.words)


# special_wordfinder.py

class SpecialWordFinder(WordFinder):
    """Specialized Word Finder that excludes blank lines and comments."""
    
    def parse(self, file):
        """Parse the file to get the list of words, excluding blanks and comments."""
        return [word.strip() for word in file if word.strip() and not word.startswith('#')]
