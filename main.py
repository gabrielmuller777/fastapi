import fastapi as FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'Fruta':'Banana'}