from aiohttp import web
from pathlib import Path
from cryptography.fernet import InvalidToken
from cryptography.fernet import Fernet
from aiohttp import web
from .config import db_block, web_routes, render_html

secret_key = Fernet.generate_key()
print(f"Generated Secure Key: {secret_key}")
fernet = Fernet(secret_key)





passwords1={'101':'101'}
passwords2={'101':'101'}
passwords3={'manager':'888'}

@web_routes.get("/loginpage")
async def login_choose_page(request):
    return render_html(request, 'login_.html')


@web_routes.get("/login")##学生
async def login_form_page(request):
    return web.Response(text=f"""
    <html><body>
    <form action="/login" method="post">
        学号: <input type="text" name="username">
        密码: <input type="password" name="password">
        <input type="submit" value="登录">
    </form>
    <form action="/" method="get">
            <input type="submit" value="退出,返回身份选择界面">
    </form>
    </body></html>
    """, content_type="text/html")


@web_routes.get("/login2")#####教师
async def login_form_page2(request):
    return web.Response(text=f"""
    <html><body>
    <form action="/login2" method="post">
        教工号: <input type="text" name="username">
        密码: <input type="password" name="password">
        <input type="submit" value="登录">
    </form>
    <form action="/" method="get">
            <input type="submit" value="退出,返回身份选择界面">
    </form>
    </body></html>
    """, content_type="text/html")

@web_routes.get("/login3")
async def login_form_page3(request):
    return web.Response(text=f"""
    <html><body>
    <form action="/login3" method="post">
        账号: <input type="text" name="username">
        密码: <input type="password" name="password">
        <input type="submit" value="登录">
    </form>
    <form action="/" method="get">
            <input type="submit" value="退出,返回身份选择界面">
    </form>
    </body></html>
    """, content_type="text/html")

@web_routes.post("/login")###学生
async def handle_login(request):
    parmas = await request.post()  # 获取POST请求的表单字段数据
    global username
    username = parmas.get("username")
    password = parmas.get("password")

    if passwords1.get(username) != password:  # 比较密码
        return web.HTTPFound('/login')  # 比对失败重新登录
    resp = web.HTTPFound('/course')
    set_secure_cookie(resp, "session_id", username)
    return resp





@web_routes.post("/login2")#####教师
async def handle_login2(request):
    parmas = await request.post()  # 获取POST请求的表单字段数据
    username2 = parmas.get("username")
    password = parmas.get("password")
    if passwords2.get(username2) != password:  # 比较密码
        return web.HTTPFound('/login2')  # 比对失败重新登录
    resp = web.HTTPFound('/teacher')
    set_secure_cookie(resp, "session_id", username2)
    return resp

@web_routes.post("/login3")
async def handle_login3(request):
    parmas = await request.post()  # 获取POST请求的表单字段数据
    username = parmas.get("username")
    password = parmas.get("password")
    if passwords3.get(username) != password:  # 比较密码
        return web.HTTPFound('/login3')  # 比对失败重新登录
    resp = web.HTTPFound('/plan')
    set_secure_cookie(resp, "session_id", username)
    return resp


@web_routes.get("/logout")
async def handle_logout(request):
    resp = web.HTTPFound('/login')
    resp.del_cookie("session_id")
    return resp 

def get_current_user(request):
    user_id = get_secure_cookie(request, "session_id")
    return user_id


def get_secure_cookie(request, name):
    value = request.cookies.get(name)
    if value is None:
        return None
    try:
        buffer = value.encode('utf-8')  # 将文本转换成字节串
        buffer = fernet.decrypt(buffer)
        secured_value = buffer.decode('utf-8')  # 将加密的字节串转换成文本
        return secured_value
    except InvalidToken:
        print("Cannot decrypt cookie value")
        return None

def set_secure_cookie(response, name, value, **kwargs):
    value = fernet.encrypt(value.encode('utf-8')).decode('utf-8')
    response.set_cookie(name, value, **kwargs)

