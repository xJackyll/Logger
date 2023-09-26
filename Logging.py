import logging
import os

# Configurazione di base 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Aggiungi un handler per scrivere su file
# Crea una cartella per il file di log se non esiste già
log_folder = "C:\\Temp"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

file_handler = logging.FileHandler(log_folder + "\\log.log")
file_handler.setLevel(logging.INFO)  # Scrivi solo WARNING e ERROR su file
logger.addHandler(file_handler)

# Abilita il debug logging?
Enable_Debug = True

# Definisci i livelli di logging
logger.setLevel(logging.DEBUG)   
file_handler.setLevel(logging.INFO)

warn_logger = logging.getLogger('warnings') 
warn_logger.addHandler(file_handler)

error_logger = logging.getLogger('errors')
error_logger.addHandler(file_handler) 

# Definisci la funzione di logging
def log_message(msg, level):
    if level == 'info':
        logger.info(msg) 
    elif level == 'warning':
        warn_logger.warning(msg)
    elif level == 'error':
        error_logger.error(msg)
    elif level == 'debug' and Enable_Debug:
        logger.debug(msg)
        
# Usa la funzione  
log_message('Started program', 'info')  
log_message('Doing something', 'debug')  
log_message('Encountered issue', 'warning')
log_message('Major problem!', 'error')
log_message('Finished', 'info') 