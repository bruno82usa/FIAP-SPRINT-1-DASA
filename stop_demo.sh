#!/bin/bash

echo "🛑 Parando Demonstração DASA Genera AI Assistant"
echo "================================================"

# Parar API
if [ -f api_demo.pid ]; then
    API_PID=$(cat api_demo.pid)
    if kill -0 $API_PID 2>/dev/null; then
        kill -9 $API_PID
        echo "✅ API parada (PID: $API_PID)"
    else
        echo "⚠️  API já estava parada"
    fi
    rm -f api_demo.pid
else
    echo "ℹ️  Arquivo api_demo.pid não encontrado"
fi

# Parar servidor web
if [ -f web_demo.pid ]; then
    WEB_PID=$(cat web_demo.pid)
    if kill -0 $WEB_PID 2>/dev/null; then
        kill -9 $WEB_PID
        echo "✅ Servidor web parado (PID: $WEB_PID)"
    else
        echo "⚠️  Servidor web já estava parado"
    fi
    rm -f web_demo.pid
else
    echo "ℹ️  Arquivo web_demo.pid não encontrado"
fi

# Limpar arquivos temporários
rm -f api_demo.log web_demo.log 2>/dev/null || true

# Matar processos nas portas (garantia)
lsof -ti:8789 | xargs kill -9 2>/dev/null || true
lsof -ti:8787 | xargs kill -9 2>/dev/null || true

echo ""
echo "✅ Todos os serviços foram parados."
echo "🔗 Portas liberadas: 8789 (API) e 8787 (Web)"
echo "================================================"