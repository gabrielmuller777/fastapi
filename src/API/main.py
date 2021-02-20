from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return [
            {'Fruta':'Banana'}, {'Salgado':'Coxinha'}
        
            ]