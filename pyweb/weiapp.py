class weiapp:
    map = {}

    def route(self, path):
        def warp(func):
            self.map[path] = func
        return warp

    def __call__(self, environ, start_respone):
        start_respone('200 OK', [('Content-Type', 'text/html')])
        return self.map[environ['PATH_INFO']]()
