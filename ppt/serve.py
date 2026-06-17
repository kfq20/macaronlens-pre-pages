#!/usr/bin/env python3
"""
Local server for deck.html — enables in-browser editing with direct save to disk.
Usage: python3 serve.py
Then open http://localhost:8787
"""
import http.server
import json
import os

PORT = 8787
DIR = os.path.dirname(os.path.abspath(__file__))
DECK_FILE = os.path.join(DIR, 'deck.html')


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_POST(self):
        if self.path == '/save':
            length = int(self.headers['Content-Length'])
            body = self.rfile.read(length)
            data = json.loads(body)
            with open(DECK_FILE, 'w', encoding='utf-8') as f:
                f.write(data['html'])
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True}).encode())
            print(f'[saved] deck.html ({len(data["html"])} bytes)')
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == '__main__':
    print(f'Serving deck at http://localhost:{PORT}/deck.html')
    print('Ctrl+S in browser will save directly to disk.')
    http.server.HTTPServer(('', PORT), Handler).serve_forever()
