"""Config file for logger."""
import logging
import logging.config

log_config = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': '../data/shared_log.log',  # Path to log file
            'formatter': 'default',
            'level': 'DEBUG',  # Ensure handler level is set to capture all messages
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'DEBUG',  # Ensure handler level is set to capture all messages
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file', 'console'],  # Add both handlers here
    },
}


def setup_logging() -> None:
    logging.config.dictConfig(log_config)
