from aiohttp import web
from routes.test import get_data, post_data

routes = web.RouteTableDef()


app = web.Application()
app.add_routes([web.get("/", get_data)])
app.add_routes([web.post("/post", post_data)])

web.run_app(app)
