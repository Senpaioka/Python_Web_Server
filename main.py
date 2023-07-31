import asyncio
import tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello , World !")

class WebPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class QueryParameterHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument('num')

        if num.isdigit():
            r = 'odd' if int(num) % 2 else 'even'
            self.write(f'{num} is {r}') 
        else:
            self.write(f'{num} is not a valid integer !')

class ResourceHandler(tornado.web.RequestHandler):
    def get(self, user_name, user_age):
        self.write(f'welcome {user_name}, as your age {user_age} - you allowed to be here !!')



def main_app():
    return tornado.web.Application([
        (r"/", MainHandler), # http://localhost:8888/
        (r"/page", WebPageHandler), # http://localhost:8888/page
        (r"/is_int", QueryParameterHandler), # http://localhost:8888/is_int?num=5
        (r"/name/([a-z]+)/([0-9]+)", ResourceHandler), # http://localhost:8888/name/senpaioka/26
    ])

async def main():
    app = main_app()
    app.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())