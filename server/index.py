from http.server import BaseHTTPRequestHandler, HTTPServer

class IntroHandler(BaseHTTPRequestHandler):
  
  def do_GET(self):
    if "png" in self.path:
      self.send_response(200)
      self.send_header('Content-type', 'image/png')
      self.end_headers()
      self.wfile.write(open(self.path[1:], 'rb').read())
    elif "css" in self.path:
      self.send_response(200)
      self.send_header('Content-type', 'text/css')
      self.end_headers()
      self.wfile.write(open(self.path[1:]).read().encode('utf-8'))
    elif "/" == self.path:
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write(
        '''
        <html>
          <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="author" content="colorlib.com">
            <link rel="icon" herf="/resource/image/favicon.png" />
            <link rel="shortcut icon" href="/resource/image/favicon.png" />
            <link href="https://fonts.googleapis.com/css?family=Montserrat:500" rel="stylesheet" />
            <link href="/resource/css/main.css" rel="stylesheet" />
          </head>
          <body>
            <div class="s129">
              <form>
                <div class="inner-form">
                  <div class="input-field">
                    <button class="btn-search" type="button">
                      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                        <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path>
                      </svg>
                    </button>
                    <input id="search" type="text" placeholder="What are you looking for?" />
                  </div>
                </div>
              </form>
            </div>
          </body><!-- This templates was made by Colorlib (https://colorlib.com) -->
        </html>
        '''.encode('utf-8')
      )
    else:
      self.send_response('404')

if __name__ == '__main__':
  httpd = HTTPServer(('', 9003), IntroHandler)
  print('Starting 9003 httpd...')
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass
  httpd.server_close()
  print('Stopping httpd...\n')

  server.serve_forever()
