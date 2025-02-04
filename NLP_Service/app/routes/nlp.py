## File: app/routes/nlp.py
```python
from fastapi import APIRouter, HTTPException
from app.schemas.nlp import NLPRequest, NLPResponse
from app.services.gpt_handler import GPTHandler

router = APIRouter()
gpt_handler = GPTHandler()

@router.post("/generate", response_model=NLPResponse)
async def generate_response(request: NLPRequest):
    try:
        response_text = gpt_handler.generate_response(request.prompt)
        return NLPResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```