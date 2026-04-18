#!/bin/bash

echo "🚀 Iniciando Demonstração DASA Genera AI Assistant"
echo "=================================================="

# Parar serviços anteriores
echo "🛑 Parando serviços anteriores..."
lsof -ti:8789 | xargs kill -9 2>/dev/null || true
lsof -ti:8787 | xargs kill -9 2>/dev/null || true

# Iniciar API
echo "📡 Iniciando API na porta 8789..."
nohup .venv/bin/uvicorn src.api.main:app --host 0.0.0.0 --port 8789 > api_demo.log 2>&1 &
API_PID=$!
echo $API_PID > api_demo.pid

# Esperar API iniciar
echo "⏳ Aguardando API iniciar..."
sleep 3

# Verificar API
if curl -s http://localhost:8789/health > /dev/null 2>&1; then
    echo "✅ API iniciada com sucesso!"
    echo "   Health check:"
    curl -s http://localhost:8789/health | python3 -m json.tool 2>/dev/null || curl -s http://localhost:8789/health
else
    echo "❌ Falha ao iniciar API. Verifique api_demo.log"
    exit 1
fi

# Iniciar servidor web
echo "🌐 Iniciando servidor web na porta 8787..."
cd "$(dirname "$0")"
nohup python3 -m http.server 8787 > web_demo.log 2>&1 &
WEB_PID=$!
echo $WEB_PID > web_demo.pid

sleep 2

# Verificar servidor web
if curl -s -o /dev/null -w "%{http_code}" http://localhost:8787/demo.html 2>/dev/null | grep -q "200"; then
    echo "✅ Servidor web iniciado com sucesso!"
else
    echo "⚠️  Servidor web pode não estar acessível. Verifique web_demo.log"
fi

echo ""
echo "=================================================="
echo "🎉 DEMONSTRAÇÃO PRONTA!"
echo ""
echo "📊 API:"
echo "   URL: http://localhost:8789"
echo "   Health: http://localhost:8789/health"
echo "   Teste: curl http://localhost:8789/health"
echo ""
echo "🖥️  Interface Web:"
echo "   URL: http://localhost:8787/demo.html"
echo "   Ou abra manualmente: demo.html no navegador"
echo ""
echo "🧪 Teste Rápido:"
echo '   curl -X POST http://localhost:8789/ask -H "Content-Type: application/json" \'
echo '     -d '\''{"report_id":"demo","question":"Qual é meu risco para diabetes?"}'\'''
echo ""
echo "🛑 Para parar a demonstração:"
echo "   ./stop_demo.sh"
echo "   ou execute: kill $(cat api_demo.pid) && kill $(cat web_demo.pid)"
echo "=================================================="

# Tentar abrir navegador (opcional)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open "http://localhost:8787/demo.html" 2>/dev/null &
elif [[ "$OSTYPE" == "darwin"* ]]; then
    open "http://localhost:8787/demo.html" 2>/dev/null &
elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    start "http://localhost:8787/demo.html" 2>/dev/null &
fi