import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s.%(msecs)03d |%(levelname)-8s|%(filename)s:%(funcName)s:%(lineno)d|>> %(message)s"
)
handler.setFormatter(formatter)

logger.addHandler(handler)
