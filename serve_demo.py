#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os
import threading
import time

PORT = 8787
API_PORT = 8789
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class DemoHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_GET(self):
        # Serve demo.html as index
        if self.path == '/':
            self.path = '/demo.html'
        return super().do_GET()
    
    def log_message(self, format, *args):
        # Custom log format
        print(f"[{self.log_date_time_string()}] {self.address_string()} - {format % args}")

def start_server():
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), DemoHTTPRequestHandler) as httpd:
        print(f"🚀 Servidor de demonstração iniciado na porta {PORT}")
        print(f"📊 API rodando na porta {API_PORT}")
        print(f"🌐 Acesse a demonstração em: http://localhost:{PORT}")
        print(f"🔗 Endpoints da API:")
        print(f"   - http://localhost:{API_PORT}/health")
        print(f"   - http://localhost:{API_PORT}/ask")
        print(f"   - http://localhost:{API_PORT}/upload")
        print(f"   - http://localhost:{API_PORT}/recommendations/{{id}}")
        print(f"\n📁 Arquivos disponíveis:")
        print(f"   - demo.html (interface web)")
        print(f"   - README.md (documentação)")
        print(f"\n📋 Exemplos de curl para testar a API:")
        print(f'   curl http://localhost:{API_PORT}/health')
        print(f'   curl -X POST http://localhost:{API_PORT}/ask -H "Content-Type: application/json" -d \'{{"report_id":"test","question":"Qual é meu risco para diabetes?"}}\'')
        print(f"\n🛑 Pressione Ctrl+C para parar o servidor\n")
        
        # Try to open browser automatically
        try:
            webbrowser.open(f"http://localhost:{PORT}")
            print("🌐 Navegador aberto automaticamente")
        except:
            print("⚠️ Não foi possível abrir o navegador automaticamente")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n⏹️ Servidor parado")

if __name__ == "__main__":
    print("=" * 60)
    print("DASA Genera AI Assistant - Demonstração Interativa")
    print("=" * 60)
    
    # Check if API is running
    import urllib.request
    import urllib.error
    
    try:
        with urllib.request.urlopen(f"http://localhost:{API_PORT}/health", timeout=2) as response:
            if response.getcode() == 200:
                print("✅ API detectada e funcionando")
    except:
        print(f"⚠️  API não encontrada na porta {API_PORT}")
        print("⚠️  Certifique-se de que a API está rodando com: python -m uvicorn src.api.main:app --port 8789")
        print("⚠️  Continuando sem verificação da API...")
    
    start_server()