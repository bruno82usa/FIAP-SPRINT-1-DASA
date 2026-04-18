# 🎥 Guia para Gravação do Vídeo (5 minutos)

## 📋 Roteiro Sugerido

**Tempo total: 5 minutos** (máximo)

### 0. Introdução (30 segundos)
- "Olá, sou [Seu Nome], aluno FIAP"
- "Este é o Sprint 1 do Challenge DASA: Genera AI Assistant"
- "Nosso objetivo: transformar relatórios genéticos complexos em insights compreensíveis usando IA"

### 1. Problema e Solução (1 minuto)
- **Problema:** Relatórios da DASA Genera são PDFs técnicos difíceis para pacientes entenderem
- **Solução:** Assistente de IA que interpreta relatórios e responde perguntas em linguagem simples
- **Destaque:** Conformidade com LGPD, não dá diagnósticos médicos

### 2. Arquitetura do Sistema (1 minuto)
- Mostrar diagrama em `architecture/architecture.md`
- Pipeline: PDF → Extração → Estruturação → Embeddings → RAG → LLM → Interface
- Componentes: FastAPI, PostgreSQL, ChromaDB, Redis, Docker
- **Demonstração rápida:** Abrir `demo.html` no navegador

### 3. Demonstração Funcional (1,5 minutos)
- **API:** `http://localhost:8789/health` (mostrar resposta JSON)
- **Interface Web:** `http://localhost:8787/demo.html`
  - Mostrar upload simulado de PDF
  - Fazer pergunta: "Qual é meu risco para diabetes?"
  - Mostrar resposta com aviso educativo
  - Mostrar recomendações personalizadas

### 4. User Stories e Governança (30 segundos)
- 10 user stories priorizados (pacientes, médicos, pesquisadores)
- Framework de governança: LGPD, ética, segurança
- Guardrails: IA não diagnostica, apenas educa

### 5. Próximos Passos e Conclusão (1 minuto)
- Processamento real de PDFs com PyPDF2
- Integração com LLMs reais (OpenAI/Claude)
- Frontend React completo
- **Conclusão:** Sistema pronto para escala, impacto na saúde preventiva

## 🚀 Como Demonstrar Rapidamente

### Opção 1 (Recomendada) - Interface Web
```bash
# Terminal 1: Iniciar API
./start_api.sh

# Terminal 2: Iniciar servidor web
python3 -m http.server 8787

# Navegador: http://localhost:8787/demo.html
```

### Opção 2 - Linha de Comando
```bash
# Testar API
./testar_api.sh

# Ou comandos manuais:
curl http://localhost:8789/health
curl -X POST http://localhost:8789/ask -H "Content-Type: application/json" -d '{"report_id":"test","question":"Qual é meu risco para diabetes?"}'
```

### Opção 3 - Docker (se tiver tempo)
```bash
docker-compose up -d api
# Acessar API: http://localhost:8789
```

## 📁 Arquivos Chave para Mostrar
1. `README.md` - Visão geral do projeto
2. `USER_STORIES.md` - Necessidades dos usuários
3. `GOVERNANCE.md` - Governança de dados e ética
4. `architecture/architecture.md` - Arquitetura técnica
5. `demo.html` - Interface de demonstração
6. `examples/sample_report_structured.json` - Exemplo de dados estruturados

## 🎯 Pontos de Destaque para o Vídeo
- ✅ **Problema real:** Dificuldade de entender relatórios genéticos
- ✅ **Solução inovadora:** IA como assistente educativo (não médico)
- ✅ **Conformidade:** LGPD, ética, guardrails
- ✅ **Arquitetura escalável:** Pronta para produção
- ✅ **Demonstração funcional:** API e interface web operacionais
- ✅ **Próximos passos claros:** Roadmap de implementação

## ⏱️ Cronometragem Sugerida
| Seção | Tempo |
|-------|-------|
| Introdução | 30s |
| Problema & Solução | 60s |
| Arquitetura | 60s |
| Demonstração | 90s |
| User Stories & Governança | 30s |
| Próximos Passos & Conclusão | 60s |
| **Total** | **5:00** |

## 💡 Dicas para a Gravação
1. **Teste antes:** Execute `./testar_api.sh` para garantir tudo funciona
2. **Tela dividida:** Mostre código e demonstração simultaneamente
3. **Foco no valor:** Enfatize como o sistema ajuda pacientes
4. **Seja conciso:** 5 minutos passam rápido!
5. **Mostre os guardrails:** Destaque que a IA não substitui médicos

## 🛠️ Troubleshooting Rápido
- API não responde? Execute `./start_api.sh`
- Demo.html não carrega? Inicie `python3 -m http.server 8787`
- Docker não funciona? Use a API local (já está configurada)

**Boa sorte com a gravação! 🎬**