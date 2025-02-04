## logger.py
This module provides a centralized logging utility for all microservices.

# common/logger.py
import logging
from logging import Logger

def get_logger(name: str) -> Logger:
    """
    Configures and returns a logger with the specified name.
    
    Args:
        name (str): Name of the logger (usually __name__).
    
    Returns:
        Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger