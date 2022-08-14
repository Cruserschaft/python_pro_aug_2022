import settings
import logging


logger = logging.getLogger("mini_shop")
FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
sh.setFormatter(logging.Formatter(FORMAT))
sh.setLevel(logging.DEBUG)
fh = logging.FileHandler(settings.LOG_FILE)
fh.setFormatter(logging.Formatter(FORMAT))
fh.setLevel(logging.INFO)
logger.addHandler(sh)
logger.addHandler(fh)
logger.debug("Logger was start")


    
    
    
