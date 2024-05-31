"""Config file for logger."""
import logging
import logging.config

log_config = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': '../data/shared_log.log',
            'formatter': 'default',
            'level': 'DEBUG',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        'fileLogger': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'consoleLogger': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'combinedLogger': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file', 'console'],
    },
}


def setup_logging() -> None:
    logging.config.dictConfig(log_config)
