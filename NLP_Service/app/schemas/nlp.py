## File: app/schemas/nlp.py
```python
from pydantic import BaseModel

class NLPRequest(BaseModel):
    prompt: str

class NLPResponse(BaseModel):
    response: str
```