
def setup_routes(app, handler, project_root):
    router = app.router
    h = handler
    router.add_get('/', h.mainpage, name='main')
    router.add_post('/poll_info', h.poll_info, name='poll_info')
    router.add_static('/static/', path=str(project_root / 'static'),
                      name='static')
