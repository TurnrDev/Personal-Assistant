import json
from typing import Union, Dict, List


class JSONSettings:
    
    def __init__(self, filename: str):
        self.filename = filename
        self._get_data()
    
    def _get_data(self):
        """Load the settings file into memory.
        If file not found, create file and populate with an empty dict.
        """
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            with open(self.filename, 'w') as f:
                self.data = {}
                json.dump(self.data, f, indent=2)
    
    def set(self, key: str, value: Union[Dict, List, str, int, float, bool, None]):
        """Set a key in the settings file."""
        self._get_data()
        self.data[key] = value
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)
        return self.data.get(key)
    
    def get(self, key: str, default: Union[Dict, List, str, int, float, bool, None] = None, reload: bool = False):
        """Get a key from the settings file."""
        if reload:
            self._get_data()
        return self.data.get(key, default)
    
    def get_or_set(self, key: str, default: Union[Dict, List, str, int, float, bool, None] = None):
        """Get a key from the settings file. If key doesn't exist, set to default."""
        self._get_data()
        if key in self.data:
            return self.data[key]
        else:
            self.set(key, default)
            return self.data[key]

config = JSONSettings('config.json')
DEFAULT_AI_NAME = 'Papy'

def __ai_say(string: str, newline: bool = False) -> str:
    _output = f"{config.get('ai_name', DEFAULT_AI_NAME)}: {string}"
    if newline:
        _output+="\n"
    return _output

def ai_say(string: str) -> None:
    """Prints the text to termianl with the AI name in front of it"""
    print(__ai_say(string))

def ai_ask(string: str) -> str:
    """Prints the text to termianl with the AI name in front of it, then requests input"""
    return input(__ai_say(string, newline=True))
