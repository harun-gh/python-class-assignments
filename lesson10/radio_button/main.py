from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

templates = Jinja2Templates(directory="templates")

app = FastAPI()

table = {
    "apple": "りんご",
    "banana": "バナナ",
    "grape": "ぶどう"
}

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request, "index.html", {}
    )

@app.post("/", response_class=HTMLResponse)
async def echo(request: Request):
    form_data = await request.form()
    fruit = form_data.get("fruit")

    if type(fruit) == str:
        return templates.TemplateResponse(
            request, "index.html", {"fruit": table[fruit]}
        )
    else:
        return templates.TemplateResponse(
            request, "index.html", {}
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)