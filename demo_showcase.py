#!/usr/bin/env python3
import json
import requests
import time
import os
import subprocess
import sys

API_URL = "http://localhost:8789"
DEMO_URL = "http://localhost:8787/demo.html"

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def print_step(step, text):
    print(f"\n[{step}] {text}")

def test_api():
    print_step("1", "Testando conexão com a API...")
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ API online: {data['status']}")
            print(f"   📅 Versão: {data['version']}")
            print(f"   ⏰ Última verificação: {data['timestamp']}")
            return True
        else:
            print(f"   ❌ API retornou código {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("   ❌ Não foi possível conectar à API")
        print("   ℹ️  Certifique-se de que a API está rodando com:")
        print("      ./start_api.sh")
        return False
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def test_endpoints():
    print_step("2", "Testando endpoints da API...")
    
    endpoints = [
        ("GET", "/", "Página inicial"),
        ("POST", "/ask", "Perguntas sobre relatórios"),
        ("GET", "/recommendations/test123", "Recomendações"),
        ("GET", "/reports/test123/summary", "Resumo do relatório"),
    ]
    
    for method, endpoint, description in endpoints:
        print(f"   🔍 {description} ({method} {endpoint})... ", end="")
        try:
            if method == "POST" and endpoint == "/ask":
                response = requests.post(
                    f"{API_URL}{endpoint}",
                    json={"report_id": "test123", "question": "Qual é meu risco para diabetes?"},
                    timeout=5
                )
            else:
                response = requests.get(f"{API_URL}{endpoint}", timeout=5)
            
            if response.status_code in [200, 201]:
                print("✅ OK")
                if endpoint == "/ask":
                    data = response.json()
                    print(f"      Resposta: {data['answer'][:80]}...")
                    print(f"      Confiança: {data['confidence']*100:.1f}%")
                    print(f"      Aviso: {data['disclaimer'][:80]}...")
            else:
                print(f"❌ Código {response.status_code}")
        except Exception as e:
            print(f"❌ Erro: {e}")

def start_web_server():
    print_step("3", "Iniciando servidor web para interface...")
    
    # Verificar se porta 8787 já está em uso
    try:
        response = requests.get("http://localhost:8787", timeout=2)
        print("   ⚠️  Servidor já está rodando na porta 8787")
        return True
    except:
        pass
    
    # Tentar iniciar servidor
    try:
        # Usar http.server em background
        import http.server
        import socketserver
        import threading
        
        def run_server():
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("", 8787), handler) as httpd:
                httpd.serve_forever()
        
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        time.sleep(2)
        
        # Testar se servidor está respondendo
        try:
            response = requests.get("http://localhost:8787/demo.html", timeout=3)
            if response.status_code == 200:
                print("   ✅ Servidor web iniciado na porta 8787")
                return True
            else:
                print(f"   ❌ Servidor retornou código {response.status_code}")
                return False
        except:
            print("   ❌ Não foi possível iniciar servidor web")
            print("   ℹ️  Você pode abrir demo.html manualmente no navegador")
            return False
            
    except Exception as e:
        print(f"   ❌ Erro ao iniciar servidor: {e}")
        return False

def show_demo_instructions():
    print_step("4", "Instruções para a demonstração")
    print("\n   🌐 URLs para acesso:")
    print(f"      API: {API_URL}")
    print(f"      Interface Web: {DEMO_URL}")
    print(f"      Arquivo local: file://{os.path.abspath('demo.html')}")
    
    print("\n   🧪 Testes rápidos (linha de comando):")
    print(f'      curl {API_URL}/health')
    print(f'      curl -X POST {API_URL}/ask -H "Content-Type: application/json" \\')
    print('        -d \'{"report_id":"test","question":"Qual é meu risco para diabetes?"}\'')
    
    print("\n   🖥️  Interface Web (demo.html):")
    print("      1. Verificar status da API")
    print("      2. Simular upload de relatório PDF")
    print("      3. Fazer perguntas sobre resultados genéticos")
    print("      4. Obter recomendações personalizadas")
    print("      5. Visualizar resumo do relatório")
    
    print("\n   📋 Exemplos de perguntas para testar:")
    print("      • 'O que significa ser portador?'")
    print("      • 'Quais são meus principais riscos genéticos?'")
    print("      • 'O que devo fazer com base nos meus resultados?'")
    print("      • 'Qual é meu risco para diabetes?'")

def interactive_demo():
    print_step("5", "Demonstração interativa")
    
    print("\n   Vamos interagir com o sistema!")
    
    # Simular upload
    print("\n   1. 📤 Simulando upload de relatório genético...")
    try:
        response = requests.post(
            f"{API_URL}/upload",
            files={"file": ("relatorio.pdf", b"conteudo simulado", "application/pdf")},
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            report_id = data["report_id"]
            print(f"      ✅ Relatório enviado! ID: {report_id}")
            print(f"      📝 Status: {data['status']}")
            print(f"      ⏱️  Tempo estimado: {data['estimated_processing_time']} segundos")
        else:
            report_id = "test123"
            print(f"      ⚠️  Usando ID de teste: {report_id}")
    except:
        report_id = "test123"
        print(f"      ⚠️  Usando ID de teste: {report_id}")
    
    # Fazer perguntas
    print("\n   2. ❓ Fazendo perguntas sobre o relatório...")
    questions = [
        "Qual é meu risco para diabetes?",
        "O que significa ser portador?",
        "Quais são meus principais riscos genéticos?"
    ]
    
    for question in questions:
        print(f"\n      Pergunta: '{question}'")
        try:
            response = requests.post(
                f"{API_URL}/ask",
                json={"report_id": report_id, "question": question},
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                print(f"      ✅ Resposta: {data['answer'][:100]}...")
                print(f"      🔍 Confiança: {data['confidence']*100:.1f}%")
            else:
                print(f"      ❌ Erro: Código {response.status_code}")
        except Exception as e:
            print(f"      ❌ Erro: {e}")
    
    # Obter recomendações
    print("\n   3. 💡 Obtendo recomendações personalizadas...")
    try:
        response = requests.get(f"{API_URL}/recommendations/{report_id}", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"      ✅ {len(data['recommendations'])} recomendações encontradas")
            print(f"      📊 Prioridade: {data['priority']}")
            print(f"      🏷️  Categorias: {', '.join(data['categories'])}")
            print("\n      Principais recomendações:")
            for i, rec in enumerate(data['recommendations'][:3], 1):
                print(f"        {i}. {rec}")
        else:
            print(f"      ❌ Erro: Código {response.status_code}")
    except Exception as e:
        print(f"      ❌ Erro: {e}")

def main():
    print_header("DASA Genera AI Assistant - Demonstração")
    
    # Verificar API
    if not test_api():
        print("\n⚠️  API não está disponível. Inicie-a com:")
        print("   ./start_api.sh")
        print("\nDeseja tentar iniciar a API automaticamente? (s/N): ", end="")
        choice = input().strip().lower()
        if choice == 's':
            print("\nIniciando API...")
            subprocess.run(["./start_api.sh"], cwd=os.path.dirname(__file__))
            time.sleep(3)
            if not test_api():
                print("\n❌ Não foi possível iniciar a API. Encerrando.")
                return
    
    # Testar endpoints
    test_endpoints()
    
    # Tentar iniciar servidor web
    web_ok = start_web_server()
    
    # Mostrar instruções
    show_demo_instructions()
    
    # Demonstração interativa
    print("\n" + "="*60)
    print("Deseja ver uma demonstração interativa? (s/N): ", end="")
    choice = input().strip().lower()
    if choice == 's':
        interactive_demo()
    
    print_header("Demonstração Concluída")
    print("\n🎯 O DASA Genera AI Assistant está funcionando!")
    print("\n📚 Próximos passos:")
    print("   1. Acesse a interface web para explorar todas as funcionalidades")
    print("   2. Consulte a documentação em README.md para detalhes técnicos")
    print("   3. Implemente processamento real de PDFs com PyPDF2/PDFPlumber")
    print("   4. Integre com banco de dados PostgreSQL para armazenamento")
    print("\n👨‍⚕️  Lembrete: Este é um sistema de demonstração para fins educacionais.")
    print("   Sempre consulte um profissional de saúde para orientações médicas.")

if __name__ == "__main__":
    main()