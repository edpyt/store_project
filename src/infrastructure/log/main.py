import logging.config


def configure_logging(logging_config: dict) -> None:
    logging.config.dictConfig(logging_config)
