from aiohttp import web
import json


# TEST GET API
async def get_data(request):
    data = [{"name": "Maruf hosen"}]
    response_data = json.dumps(data)
    return web.Response(body=response_data)


# TEST POST API
async def post_data(request):
    req_data = await request.content.read()
    req_data_dict = json.loads(req_data)
    print(req_data_dict["name"])
    return web.Response(body=req_data, content_type="application/json")