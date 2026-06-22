from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

""" じゃんけんすんじゃねえのかよ... """
from random import randint

table = {
    "rock": "グー",
    "scissors": "チョキ",
    "paper": "パー"
}

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request, "index.html", {}
    )

@app.post("/", response_class=HTMLResponse)
async def rsp(request: Request):
    form_data = await request.form()
    hand = form_data.get("hand")

    if (type(hand) == str) and (hand in table.keys()):
        print("判定")
        random = randint(0, 2)
        your_hand = table[hand]
        enemy_hand = list(table.values())[random]
        result = list(table.keys()).index(hand) - random

        return templates.TemplateResponse(
            request, "index.html", { "your_hand": your_hand, "enemy_hand": enemy_hand, "result": ["あいこ", "勝ち", "負け"][result] }
        )
    else:
        return templates.TemplateResponse(
            request, "index.html", {}
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)