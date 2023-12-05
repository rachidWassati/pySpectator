import logging

from monitopy.spectator import FileWatcher

# Configuration du module logging
logging.basicConfig(filename='pySpectator.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Fonction de callback pour la gestion des événements
def on_file_change(event):
    if not event.src_path.endswith("pySpectator.log"):
        log_message = f"Changement détecté : {event.src_path} ({event.event_type})"
        print(log_message)
        logging.info(log_message)

# Créer une instance du FileWatcher
watcher = FileWatcher(r"C:\Users\chid-\Dropbox\mac\DEV\Python\pySpectator", callback=on_file_change)

# Commencer la surveillance
watcher.start()
