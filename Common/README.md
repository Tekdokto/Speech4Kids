## README.md
This file provides documentation for the `common` package.

```markdown
# Common Module

The `common` module contains shared libraries and utilities for the `speech4kids` microservices architecture. It includes centralized logging, middleware, and configuration settings.

## Directory Structure
```plaintext
common/
├── __init__.py
├── logger.py
├── middleware.py
├── settings.py
└── README.md
```

## Modules

### logger.py
Provides a centralized logging utility for all microservices.

### middleware.py
Contains middleware for:
- Cross-Origin Resource Sharing (CORS)
- Global error handling
- Validation exception management

### settings.py
Manages configuration using `pydantic.BaseSettings`. Supports environment variables and `.env` files.

## How to Use

### Logger
```python
from common.logger import get_logger
logger = get_logger(__name__)
logger.info("This is a log message.")
```

### Middleware
Add middleware to your FastAPI app:
```python
from common.middleware import add_cors_middleware, add_global_error_handlers

add_cors_middleware(app)
add_global_error_handlers(app)
```

### Settings
Access shared configuration:
```python
from common.settings import settings
print(settings.PROJECT_NAME)
```

## Environment Variables
The following variables can be configured via a `.env` file:
- `PROJECT_NAME`
- `ENVIRONMENT`
- `LOG_LEVEL`
- `DATABASE_URL`
- `REDIS_URL`
- `GOOGLE_API_KEY`
- `JWT_SECRET_KEY`
- `JWT_ALGORITHM`
```