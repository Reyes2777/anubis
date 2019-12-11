import json

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from controllers.user import UserController
from db import run
from utils.crypto import verify_password


async def register(request):
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


async def login(request):
    body = json.loads(await request.body())
    user_controller = UserController(email=body.get('email'), pwd=body.get('pwd'))
    user = await user_controller.get_user()
    if user:
        if verify_password(user.password, body.get('pwd')):
            return JSONResponse({'status': 'logged in'}, status_code=200)
        else:
            return JSONResponse({'status': 'password is wrong'}, status_code=401)
    else:
        return JSONResponse({'status': 'not logged'}, status_code=400)

app = Starlette(
    debug=True,
    routes=[Route(
        '/register', register), Route('/login', login)],
    on_startup=[run])
