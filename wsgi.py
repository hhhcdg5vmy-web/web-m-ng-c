"""
WSGI Application cho PythonAnywhere hoặc bất kỳ máy chủ WSGI (Gunicorn, uWSGI).
Dùng trực tiếp trong trang cấu hình 'Web' của PythonAnywhere.
"""
import os
import sys

# Đảm bảo đường dẫn thư mục dự án nằm trong PYTHONPATH
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

HTML_FILE = os.path.join(CURRENT_DIR, 'index.html')

def application(environ, start_response):
    path = environ.get('PATH_INFO', '/')

    if os.path.exists(HTML_FILE):
        with open(HTML_FILE, 'rb') as f:
            content = f.read()
        status = '200 OK'
        headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
            ('Content-Length', str(len(content))),
            ('Cache-Control', 'no-cache, no-store, must-revalidate')
        ]
        start_response(status, headers)
        return [content]
    else:
        status = '404 Not Found'
        content = b'<h1>File index.html not found! Vui long dat index.html cung thu muc voi wsgi.py</h1>'
        headers = [('Content-Type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        return [content]
