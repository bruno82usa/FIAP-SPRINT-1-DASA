#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8787
DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(DIR)

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/demo.html'
        return super().do_GET()
    
    def log_message(self, format, *args):
        print(f"[HTTP] {self.address_string()} - {format % args}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"✅ Servidor rodando em http://localhost:{PORT}")
    print(f"📊 API rodando em http://localhost:8789")
    print(f"📁 Servindo diretório: {DIR}")
    print("\n📋 Endpoints para testar:")
    print("   curl http://localhost:8789/health")
    print('   curl -X POST http://localhost:8789/ask -H "Content-Type: application/json" -d \'{"report_id":"test","question":"Qual é meu risco para diabetes?"}\'')
    print("\n🛑 Pressione Ctrl+C para parar")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n⏹️ Servidor parado")