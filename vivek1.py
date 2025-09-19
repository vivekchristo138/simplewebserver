from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>
            device specification - 25013444
        </title>
    </head>
    <body>
        <h1>DEVICE SPECIFICATION = 25013444</h1>
        <table border="3" cellspacing = "5" cellpadding ="5">
            <tr bgcolor ="yellow">
                <th>si.no</th>
                <th>device specification</th>
                <th>description</th>
            </tr>
            <tr>
                <td>1</td>
                <td>storage</td>
                <td>477gb</td>
            </tr>
            <tr>
                <td>2</td>
                <td>processor</td>
                <td>AMD rtzen 7 series</td>
            </tr>
            <tr>
                <td>3</td>
                <td>graphics card</td>
                <td>4GB</td>
            </tr>
            <tr>
                <td>4</td>
                <td>version</td>
                <td>24HS</td>
            </tr>
            <tr>
                <td>5</td>
                <td>windows</td>
                <td>11</td>
            </tr>
        </table>
    </body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()