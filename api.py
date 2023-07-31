import asyncio
import tornado
import json


class IndexHandler(tornado.web.RequestHandler):
    def get(self):  # http://localhost:8880
        self.write("Hello, go to /list to see the api output !")


class ApiHandler(tornado.web.RequestHandler):
    def get(self):  # http://localhost:8880/list
        api_file = open('api.txt', 'r')
        all_text = api_file.read().splitlines()
        api_file.close()
        self.write(json.dumps(all_text))

    def post(self): # http://localhost:8880/list?add=apple [postman call]
        new_item = self.get_argument('add')
        api_file = open('api.txt', 'a')
        api_file.write(f'{new_item}\n')
        api_file.close()
        self.write(json.dumps({'message': 'New Item Added !'}))

async def main():
    application = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/list', ApiHandler),
    ])

    application.listen(8880)
    await asyncio.Event().wait()



if __name__ == '__main__':
    asyncio.run(main())