"""Just a place for generic testing."""

from .pen import Pen
from .artist import Artist

print("Hey there. Looks like you ran `codestudio` instead of importing it.")
print(Artist().from_json_file('./puzzles/s1level24.json'))

