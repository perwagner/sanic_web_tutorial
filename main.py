from sanic import Sanic
from sanic import response

app = Sanic(name='My Sanic Web App')


async def index(request):
    return response.html("<h1>Hello World</h1>")


app.add_route(index, "/")
app.add_route(index, "/main")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)