#!/bin/bash

echo "🧪 Testando DASA Genera AI Assistant API"
echo "========================================"

API_URL="http://localhost:8789"

# Função para testar endpoint
test_endpoint() {
    local method=$1
    local endpoint=$2
    local data=$3
    local description=$4
    
    echo -n "🔍 $description... "
    
    if [ "$method" = "POST" ]; then
        response=$(curl -s -X POST "$API_URL$endpoint" \
            -H "Content-Type: application/json" \
            -d "$data" 2>/dev/null)
    else
        response=$(curl -s "$API_URL$endpoint" 2>/dev/null)
    fi
    
    if echo "$response" | grep -q "error\|Error\|Exception\|Not Found"; then
        echo "❌ ERRO"
        echo "   Resposta: $response"
    else
        echo "✅ OK"
        if [ "$1" != "GET" ] || [ "$endpoint" = "/health" ]; then
            echo "$response" | python3 -m json.tool 2>/dev/null || echo "   $response"
        fi
    fi
    echo
}

# Testar endpoints
test_endpoint GET "/" "Página inicial"
test_endpoint GET "/health" "" "Health check"

# Testar upload simulado
test_endpoint POST "/upload" '{"file": "simulado"}' "Upload de PDF (simulado)"

# Testar perguntas
test_endpoint POST "/ask" '{"report_id": "test123", "question": "Qual é meu risco para diabetes?"}' "Pergunta sobre diabetes"
test_endpoint POST "/ask" '{"report_id": "test123", "question": "O que significa ser portador?"}' "Pergunta sobre portador"

# Testar recomendações
test_endpoint GET "/recommendations/test123" "" "Recomendações personalizadas"

# Testar resumo
test_endpoint GET "/reports/test123/summary" "" "Resumo do relatório"

echo "========================================"
echo "📊 Todos os testes concluídos!"
echo "🌐 Acesse a interface web: file://$(pwd)/demo.html"
echo "🔗 API disponível em: $API_URL"