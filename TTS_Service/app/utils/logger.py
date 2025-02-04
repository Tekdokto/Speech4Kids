#### `app/utils/logger.py`
```python
import logging

def setup_logger():
    logger = logging.getLogger("tts_service")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
```