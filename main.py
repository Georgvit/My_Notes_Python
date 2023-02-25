import  logging
from view.NotesView import NotesView

logging.basicConfig(level=logging.ERROR, filename='py_log.log', filemode='w')
try:
    note = NotesView()
    note.run()
except:
    logging.error('Error startig')


