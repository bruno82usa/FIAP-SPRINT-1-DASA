# ✅ Checklist Final para Entrega

## 📋 Antes da Gravação do Vídeo

### [ ] 1. Testar a Demonstração
- [ ] Executar `./start_api.sh` (API deve iniciar na porta 8789)
- [ ] Executar `python3 -m http.server 8787` (servidor web)
- [ ] Acessar `http://localhost:8787/demo.html` no navegador
- [ ] Testar upload simulado de PDF
- [ ] Fazer pergunta: "Qual é meu risco para diabetes?"
- [ ] Verificar recomendações personalizadas

### [ ] 2. Revisar Documentação
- [ ] README.md está atualizado com instruções de execução
- [ ] USER_STORIES.md com 10 histórias priorizadas
- [ ] GOVERNANCE.md com políticas de LGPD e ética
- [ ] architecture/architecture.md com diagramas claros
- [ ] VIDEO_GUIDE.md com roteiro de 5 minutos

### [ ] 3. Preparar Ambiente de Gravação
- [ ] Fechar aplicações desnecessárias
- [ ] Configurar tela para mostrar código e demonstração
- [ ] Testar áudio e vídeo
- [ ] Cronometrar 5 minutos

## 🎥 Durante a Gravação (Roteiro 5 Minutos)

### [ ] 0:00-0:30 | Introdução
- [ ] Apresentar nome e turma FIAP
- [ ] Contexto: Challenge DASA Genera AI Assistant
- [ ] Problema: Relatórios genéticos complexos em PDF

### [ ] 0:30-1:30 | Solução e Arquitetura
- [ ] Mostrar diagrama de arquitetura
- [ ] Explicar pipeline: PDF → JSON → Embeddings → RAG → LLM
- [ ] Destacar conformidade com LGPD

### [ ] 1:30-3:00 | Demonstração Prática
- [ ] Mostrar API funcionando (`curl` ou navegador)
- [ ] Demonstrar interface web (`demo.html`)
- [ ] Fazer pergunta e mostrar resposta com aviso educativo
- [ ] Mostrar recomendações personalizadas

### [ ] 3:00-4:00 | User Stories e Governança
- [ ] Mostrar 10 user stories priorizados
- [ ] Explicar guardrails éticos (IA não diagnostica)
- [ ] Destacar proteção de dados (LGPD)

### [ ] 4:00-5:00 | Próximos Passos e Conclusão
- [ ] Roadmap: processamento real de PDFs, LLM real, React frontend
- [ ] Impacto: saúde preventiva, empoderamento do paciente
- [ ] Conclusão e agradecimentos

## 📤 Após a Gravação

### [ ] 1. Enviar para GitHub
- [ ] Configurar remote: `git remote add origin https://github.com/bruno82usa/FIAP.git`
- [ ] Fazer push: `git push origin main:SPRINT-1-DASA` ou criar branch
- [ ] Verificar se estrutura de pastas está correta: `/FIAP/SPRINT-1-DASA/`

### [ ] 2. Upload do Vídeo
- [ ] Processar vídeo (cortar para 5 minutos exatos)
- [ ] Upload para plataforma indicada (YouTube, Google Drive, etc.)
- [ ] Adicionar link do vídeo no README.md

### [ ] 3. Entrega Final
- [ ] Enviar link do repositório para o tutor
- [ ] Enviar link do vídeo para o tutor
- [ ] Confirmar recebimento

## 🆘 Suporte Rápido

### Problemas Comuns:
- **API não inicia**: Porta 8789 ocupada → `lsof -ti:8789 | xargs kill -9`
- **Demo.html não carrega**: Iniciar servidor web → `python3 -m http.server 8787`
- **Docker não funciona**: Usar API local (já configurada)

### Comandos Rápidos de Teste:
```bash
# Teste completo
./testar_api.sh

# Teste individual
curl http://localhost:8789/health
curl -X POST http://localhost:8789/ask -H "Content-Type: application/json" -d '{"report_id":"test","question":"Qual é meu risco para diabetes?"}'
```

## 🎯 Pontos Críticos para Destaque no Vídeo

1. **✅ Problema real** - Dificuldade de entender relatórios genéticos
2. **✅ Solução inovadora** - IA como assistente educativo (não médico)
3. **✅ Conformidade legal** - LGPD, ética, guardrails
4. **✅ Arquitetura escalável** - Pronta para produção
5. **✅ Demonstração funcional** - Não é só teoria
6. **✅ Próximos passos claros** - Roadmap de implementação

---

**⏰ TEMPO TOTAL ESTIMADO:**
- Preparação: 15-20 minutos
- Gravação: 5 minutos
- Upload e entrega: 10 minutos
- **Total: ~35 minutos**

**🚀 BOA SORTE NA ENTREGA!**