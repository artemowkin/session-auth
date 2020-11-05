import logging


logger = logging.getLogger('stream')
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter("%(levelname)s:%(message)s"))

logger.addHandler(handler)

