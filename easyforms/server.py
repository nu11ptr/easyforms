from sanic import Sanic
from sanic.request import Request
from sanic.websocket import WebSocketConnection

app = Sanic(name="Easyforms")


@app.websocket("/ws")
async def ws(request: Request, ws: WebSocketConnection):
    data = "hello!"

    while True:
        print("Sending: " + data)
        await ws.send(data)

        data = await ws.recv()
        print("Received: " + data)

    await ws.close()


def run(ip: str, port: int):
    app.run(host="0.0.0.0", port=8000)
