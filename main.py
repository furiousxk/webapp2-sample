import webapp2
from webapp2_extras import json

class HelloWebApp2(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'application/json'
		response = {
			'message': 'Hello, webapp2!'
		}
		self.response.out.write(json.encode(response))

app = webapp2.WSGIApplication([
	('/', HelloWebApp2),
], debug=True)

def main():
	from paste import httpserver
	httpserver.serve(app, host='127.0.0.1', port='9090')

if __name__ == '__main__':
	main()
