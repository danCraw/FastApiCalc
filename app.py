import uvicorn as uvicorn
from fastapi import FastAPI, status, Response

from counts import count_str
from models import Expression

app = FastAPI()


@app.get('/index')
@app.get('/')
async def hello() -> str:
    return "Hello world"


@app.get('/eval', status_code=status.HTTP_200_OK)
async def evaluate_get(phrase: str, response: Response):
    try:
        return count_str(phrase)
    except (NameError, SyntaxError) as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return str(e)


@app.post('/eval', status_code=status.HTTP_201_CREATED)
async def evaluate_post(expression: Expression, response: Response):
    try:
        return {'result': count_str(expression.phrase)}
    except (NameError, SyntaxError, TypeError) as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {str(e)}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
