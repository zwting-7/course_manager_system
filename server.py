from aiohttp import web


from serv.config import web_routes, home_path

import serv.main_views

import serv.tea_class_views
import serv.try_login
import serv.class_views
import serv.course_actions
import serv.course_view
import serv.error_views
import serv.class_views
import serv.score_view






app = web.Application()
app.add_routes(web_routes)
app.add_routes([web.static("/", home_path / "static")])

if __name__ == "__main__":
    web.run_app(app, port=8080)
