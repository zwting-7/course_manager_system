from aiohttp import web
import psycopg2.errors
from urllib.parse import urlencode

from .config import db_block, web_routes

@web_routes.post('/action/course_add')
async def action_course_add(request):
    params = await request.post()
    class_sn= params.get("class_sn")
    cou_name = params.get("cou_name")
    schedule_year = params.get("schedule_year")

    if class_sn is None or cou_name is None or schedule_year is None:
        return web.HTTPBadRequest(text="class_sn, course_sn, schedule_year must be required")

    try:
        class_sn = int(class_sn)
        cou_name= int(cou_name)
        schedule_year= int(schedule_year)
    except ValueError:
        return web.HTTPBadRequest(text="invalid value")

    try:
        with db_block() as db:
            db.execute("""
            INSERT INTO class_schedule(class_sn,schedule_year) 
            VALUES ( %(class_sn)s,  %(schedule_year)s);
            INSERT INTO course(name) 
            VALUES ( %(cou_name)s)
            """, dict(class_sn=class_sn, cou_name=cou_name, schedule_year=schedule_year))
    except psycopg2.errors.UniqueViolation:
        query = urlencode({
            "message": "已经添加该课程信息",
            "return": "/plan"
        })
        return web.HTTPFound(location=f"/error?{query}")
    except psycopg2.errors.ForeignKeyViolation as ex:
        return web.HTTPBadRequest(text=f"无此班级或课程: {ex}")

    return web.HTTPFound(location="/plan")