import logging
from logging import handlers

from core.settings import settings


class LoggerSetup:

    def __init__(self) -> None:
        self.logger = logging.getLogger("")
        self.setup_logging()

    def setup_logging(self):
        log_format = settings.log.format
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
        )

        # configure formatter for logger
        formatter = logging.Formatter(log_format)

        # configure console handler
        console = logging.StreamHandler()
        console.setFormatter(formatter)

        # configure TimeRoutingFileHandler
        log_file = "logs/auth-pharmacy.log"
        file = logging.handlers.TimedRotatingFileHandler(
            filename=log_file, when="midnight", backupCount=5
        )
        file.setFormatter(formatter)

        # add handlers to logger
        self.logger.addHandler(console)
        self.logger.addHandler(file)
