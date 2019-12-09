import json

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from controllers.user import UserController
from db import run


async def homepage(request):
    body = json.loads(await request.body())
    print(body)
    user_controller = UserController()
    user_controller.create_user(email=body.get('email'), pwd=body.get('pwd'))
    return JSONResponse({'hello': 'world'})

app = Starlette(debug=True, routes=[Route('/', homepage)], on_startup=[run])
