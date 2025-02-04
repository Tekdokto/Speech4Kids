## File: app/routes/__init__.py
```python
from fastapi import APIRouter
from app.routes.nlp import router as nlp_router

__all__ = ["nlp_router"]
```