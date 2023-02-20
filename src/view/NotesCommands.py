from enum import Enum, auto


class NotesCommands(Enum):
    CREATE = 'CREATE'
    READ = 'READ'
    UPDATE = 'UPDATE'
    LIST = 'LIST'
    DELETE = 'DELETE'
    EXIT = 'EXIT'
