# 🚀 DASA Genera AI Assistant - Projeto Funcionando

## ✅ Status Atual
- **API FastAPI**: ✅ Rodando na porta 8789
- **Interface Web**: ✅ Disponível em `demo.html`
- **Serviços Docker**: ⏸️ Parados (podem ser iniciados com `docker-compose up -d api`)

## 🌐 Como Testar o Projeto

### 1. Teste a API (linha de comando)

```bash
# Verificar saúde da API
curl http://localhost:8789/health

# Obter mensagem de boas-vindas
curl http://localhost:8789/

# Fazer uma pergunta sobre relatório genético
curl -X POST http://localhost:8789/ask \
  -H "Content-Type: application/json" \
  -d '{
    "report_id": "test123",
    "question": "Qual é meu risco para diabetes?"
  }'

# Obter recomendações
curl http://localhost:8789/recommendations/test123

# Obter resumo do relatório
curl http://localhost:8789/reports/test123/summary
```

### 2. Interface Web Interativa

Abra o arquivo `demo.html` no seu navegador:

```bash
# Método 1: Abrir diretamente
xdg-open demo.html   # Linux
open demo.html       # macOS
start demo.html      # Windows

# Método 2: Usar servidor Python
python3 -m http.server 8787 &
# Acesse: http://localhost:8787/demo.html
```

### 3. Teste Rápido (script)

Execute o script de teste:

```bash
chmod +x start_api.sh
./start_api.sh

# Em outro terminal:
./testar_api.sh
```

## 📊 Endpoints da API

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/` | GET | Mensagem de boas-vindas |
| `/health` | GET | Status da API |
| `/upload` | POST | Upload de PDF (simulado) |
| `/ask` | POST | Perguntas sobre relatórios |
| `/recommendations/{id}` | GET | Recomendações personalizadas |
| `/reports/{id}/summary` | GET | Resumo do relatório |

## 🧪 Exemplos de Perguntas

1. "O que significa ser portador?"
2. "Quais são meus principais riscos genéticos?"
3. "O que devo fazer com base nos meus resultados?"
4. "Qual é meu risco para diabetes?"
5. "O que são variantes de risco moderado?"

## 🐳 Docker (Opcional)

Para executar toda a stack com banco de dados:

```bash
docker-compose up -d api
```

Isso iniciará:
- PostgreSQL (porta 5433)
- ChromaDB (porta 8002)
- Redis (porta 6380)
- API FastAPI (porta 8789)

## 🔧 Estrutura do Projeto

```
├── src/
│   ├── api/
│   │   ├── main.py          # API FastAPI
│   │   └── models.py        # Modelos Pydantic
│   ├── pdf_processing/
│   │   └── extractor.py     # Processamento de PDF
│   └── config.py            # Configurações
├── examples/
│   └── sample_report_structured.json  # Exemplo de dados
├── demo.html                # Interface web
├── docker-compose.yml       # Orquestração Docker
├── Dockerfile               # Imagem da API
└── requirements.txt         # Dependências Python
```

## 📈 Próximos Passos

1. **Implementar processamento real de PDF**: Integrar PyPDF2/PDFPlumber
2. **Adicionar banco de dados**: Conectar ao PostgreSQL para armazenar relatórios
3. **Integrar IA real**: Conectar à OpenAI/Claude para respostas dinâmicas
4. **Desenvolver frontend React**: Interface completa para usuários
5. **Implementar autenticação**: Sistema de login seguro

## 🛑 Parar os Serviços

```bash
# Parar API
kill $(cat api.pid) 2>/dev/null || true

# Parar servidor web
pkill -f "http.server" 2>/dev/null || true

# Parar Docker
docker-compose down
```

---

**✅ Projeto funcionando e pronto para demonstração!**