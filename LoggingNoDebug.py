import logging
import os

# Imposta il livello di log per visualizzare info, warning ed error
logging.basicConfig(level=logging.INFO)

# Crea una cartella per il file di log se non esiste già
log_folder = "C:\\Temp"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Crea un file di log nella cartella e imposta il formato del messaggio di log
log_file = os.path.join(log_folder, "log_file.log")
file_handler = logging.FileHandler(log_file)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logging.getLogger().addHandler(file_handler)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)

# Esempio di utilizzo delle funzioni di log
log_info("Questo è un messaggio di log INFO")
log_warning("Questo è un messaggio di log WARNING")
log_error("Questo è un messaggio di log ERROR")