from aiohttp import web
from .config import db_block, web_routes, render_html


@web_routes.get("/score")
async def view_xinxi_course(request):
    with db_block() as db:
        db.execute("""
        SELECT  s.name as stu_name,
            cl.classname as class_name, 
            c.name as cou_name,
            g.grade,
            cs.schedule_year  
        FROM student as s 
            INNER JOIN course_grade as g ON s.sn = g.stu_sn
            INNER JOIN class as cl  ON g.cou_sn = cl.sn
            INNER JOIN class_schedule as cs  ON cl.sn = cs.class_sn
            INNER JOIN course as c  ON cs.course_sn = c.sn
        WHERE cs.schedule_year='2020春'
        ORDER BY cl.sn;
        """)

        items = list(db)

    return render_html(request, 'score_class_view.html',
                       items=items)

@web_routes.get("/score/2020a")
async def view_xinxi_course(request):
    with db_block() as db:
        db.execute("""
        SELECT  s.name as stu_name,
            cl.classname as class_name, 
            c.name as cou_name,
            g.grade,
            cs.schedule_year  
        FROM student as s 
            INNER JOIN course_grade as g ON s.sn = g.stu_sn
            INNER JOIN class as cl  ON g.cou_sn = cl.sn
            INNER JOIN class_schedule as cs  ON cl.sn = cs.class_sn
            INNER JOIN course as c  ON cs.course_sn = c.sn
        WHERE cs.schedule_year='2020秋'
        ORDER BY cl.sn;
        """)

        items = list(db)

    return render_html(request, 'score_class_view.html',
                       items=items)