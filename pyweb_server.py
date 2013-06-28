#!/usr/bin/env python
# use this if hosting on a linux box, very simple http server 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/cgi-bin"]
 
httpd = server(server_address, handler)
httpd.serve_forever()
