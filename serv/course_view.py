from aiohttp import web
from .config import db_block, web_routes, render_html


@web_routes.get("/plan")
async def view_xinxi_course(request):
    with db_block() as db:
        db.execute("""
        SELECT sn AS class_sn, classname as class_name FROM class ORDER BY classname
        """)
        classes = list(db)
        
        db.execute("""
        SELECT cl.sn,  
            cl.classname as class_name,
            c.name as cou_name, 
            cs.schedule_year
        FROM class_schedule as cs 
            INNER JOIN class as cl ON cs.class_sn = cl.sn
            INNER JOIN course as c  ON cs.course_sn = c.sn
        WHERE cl.classname='信息'
        ORDER BY schedule_year;
        """)

        items = list(db)

    return render_html(request, 'course_class_choose.html',
                       items=items,
                       classes=classes)

@web_routes.get("/plan/xinxih")
async def view_xinxih_course(request):
    with db_block() as db:
        db.execute("""
        SELECT cl.sn,  
            cl.classname as class_name,
            c.name as cou_name, 
            cs.schedule_year
        FROM class_schedule as cs 
            INNER JOIN class as cl ON cs.class_sn = cl.sn
            INNER JOIN course as c  ON cs.course_sn = c.sn
        WHERE cl.classname='信息H'
        ORDER BY schedule_year;
        """)

        items = list(db)

    return render_html(request, 'course_class_choose.html',
                       items=items)

@web_routes.get("/plan/ruanjian")
async def view_year_course(request):
    with db_block() as db:
        db.execute("""
        SELECT cl.sn,  
            cl.classname as class_name,
            c.name as cou_name, 
            cs.schedule_year
        FROM class_schedule as cs 
            INNER JOIN class as cl ON cs.class_sn = cl.sn
            INNER JOIN course as c  ON cs.course_sn = c.sn
        WHERE cl.classname='软件'
        ORDER BY schedule_year;
        """)

        items = list(db)

    return render_html(request, 'course_class_choose.html',
                       items=items)

@web_routes.get("/plan/ruanjianh")
async def view_year_course(request):
    with db_block() as db:
        db.execute("""
        SELECT cl.sn,  
            cl.classname as class_name,
            c.name as cou_name, 
            cs.schedule_year
        FROM class_schedule as cs 
            INNER JOIN class as cl ON cs.class_sn = cl.sn
            INNER JOIN course as c  ON cs.course_sn = c.sn
        WHERE cl.classname='软件H'
        ORDER BY schedule_year;
        """)

        items = list(db)

    return render_html(request, 'course_class_choose.html',
                       items=items)