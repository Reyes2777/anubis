import json

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from controllers.user import UserController
from db import run


async def create_user(request):
    body = json.loads(await request.body())
    name_user = body.get('name_user') or None
    email = body.get('email')
    pwd = body.get('pwd')
    user_controller = UserController(email=email, pwd=pwd)
    ok, message = await user_controller.create_user(username=name_user)
    if ok:
        return JSONResponse({'message': f'user created successfully {email}'}, status_code=200)
    else:
        return JSONResponse({'message': message}, status_code=400)

app = Starlette(
    debug=True,
    routes=[Route(
        '/create_user', create_user)],
    on_startup=[run])
