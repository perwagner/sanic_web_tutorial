from sanic import Sanic
from sanic import response
from sanic_jinja2 import SanicJinja2

app = Sanic(name='Sanic Web Tutorial')
jinja = SanicJinja2(app, pkg_name="main")


@app.route("/")
async def index(request):
    context = {
        "title": "Sanic Web Title",
        "desc": "Something else here",
    }
    return jinja.render("index.html", request, context=context)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)