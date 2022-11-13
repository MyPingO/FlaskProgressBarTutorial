from asyncio import sleep
from website import create_app
from flask import render_template, Response
from flask_socketio import SocketIO

app = create_app()
socketio = SocketIO(app)

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/progress/<socketid>", methods = ["POST"])
async def progress(socketid):
    for x in range(1,6):
        socketio.emit("update progress", x * 20, to=socketid)
        await sleep(2)
    return Response(status=204)


if __name__ == "__main__":
    socketio.run(app=app, debug=True, host="0.0.0.0", port = 25565)