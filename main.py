import uvicorn

if __name__== "__main__":
    uvicorn.run('app.app:app', port=3002, reload=True)