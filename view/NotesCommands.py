from enum import Enum, auto

# Команды
class NotesCommands(Enum):
    CREATE = 'CREATE'
    READ = 'READ'
    UPDATE = 'UPDATE'
    LIST = 'LIST'
    UNLOADING = 'UNLOAD'
    DELETE = 'DELETE'
    EXIT = 'EXIT'
    TOPIC = 'TOPIC'
    TEXT = 'TEXT'
