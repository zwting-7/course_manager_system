from aiohttp import web
from .config import db_block, web_routes, render_html


@web_routes.get("/teacher")
async def view_list_course(request):
    with db_block() as db:
        db.execute("""
        SELECT cs.course_sn, cs.class_sn, 
            c.name as cou_name, 
            cl.classname as class_name,
            cs.weeks,
            cs.lessons,
            cs.remark 
        FROM class_schedule as cs 
            INNER JOIN class as cl ON cs.class_sn = cl.sn
            INNER JOIN course as c  ON cs.course_sn = c.sn
        
        """)

        items = list(db)

    return render_html(request, 'tea_class_view.html',
                       items=items)

@web_routes.get("/teacher/course/year/2020s")
async def view_year_course(request):
    with db_block() as db:
        db.execute("""
        SELECT cs.course_sn, cs.class_sn, 
            c.name as cou_name, 
            cl.classname as class_name,
            cs.weeks,
            cs.lessons,
            cs.remark 
        FROM class_schedule as cs 
            INNER JOIN class as cl ON cs.class_sn = cl.sn
            INNER JOIN course as c  ON cs.course_sn = c.sn
            WHERE schedule_year = '2020春'
        ORDER BY teacher_sn, course_sn;
        """)

        items = list(db)

    return render_html(request, 'tea_class_past_choose.html',
                       items=items)

@web_routes.get("/teacher/course/year/2020a")
async def view_year_course(request):
    with db_block() as db:
        db.execute("""
        SELECT cs.course_sn, cs.class_sn, 
            c.name as cou_name, 
            cl.classname as class_name,
            cs.weeks,
            cs.lessons,
            cs.remark 
        FROM class_schedule as cs 
            INNER JOIN class as cl ON cs.class_sn = cl.sn
            INNER JOIN course as c  ON cs.course_sn = c.sn
            WHERE schedule_year = '2020秋'
        ORDER BY teacher_sn, course_sn;
        """)

        items = list(db)

    return render_html(request, 'tea_class_past_choose.html',
                       items=items)