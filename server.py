#!/usr/bin/env python3
"""
Server Python phục vụ ứng dụng 'Cố Lên Bro'
Chạy độc lập với thư viện chuẩn Python (Standard Library), không cần cài thêm package nào.
"""
import http.server
import socketserver
import os
import sys

PORT = int(os.environ.get('PORT', 5000))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class WebHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Mặc định phục vụ index.html nếu vào trang chủ hoặc file không tồn tại
        clean_path = self.path.split('?')[0].lstrip('/')
        full_path = os.path.join(DIRECTORY, clean_path)
        if not clean_path or not os.path.exists(full_path):
            self.path = '/index.html'
        return super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run():
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("0.0.0.0", PORT), WebHandler) as httpd:
            print("=" * 60)
            print(f"🚀 CỐ LÊN BRO - Server Python đang chạy trên cổng {PORT}")
            print(f"👉 Local URL: http://localhost:{PORT}")
            print(f"👉 Thư mục: {DIRECTORY}")
            print("=" * 60)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng server.")
        sys.exit(0)

if __name__ == '__main__':
    run()
