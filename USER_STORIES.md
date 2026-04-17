# User Stories - DASA Genera AI Assistant

## 📋 User Stories Prioritizadas

### 1. **Como paciente, quero fazer upload do meu relatório PDF** para que o sistema possa processar meus dados genéticos.
**Critérios de Aceitação:**
- Upload de arquivos PDF até 50MB
- Validação de formato (apenas PDF)
- Feedback visual do progresso do upload
- Armazenamento seguro dos arquivos

### 2. **Como paciente, quero visualizar um resumo dos meus principais riscos genéticos** para entender rapidamente as informações mais importantes.
**Critérios de Aceitação:**
- Lista dos 5 principais riscos com classificação de gravidade
- Visualização em cards com cores indicativas (verde/amarelo/vermelho)
- Explicação simplificada de cada risco
- Opção de expandir para detalhes completos

### 3. **Como paciente, quero fazer perguntas sobre meu relatório em linguagem natural** para esclarecer dúvidas sem conhecimento técnico.
**Critérios de Aceitação:**
- Campo de texto para perguntas
- Respostas em linguagem simples e acessível
- Tempo de resposta inferior a 5 segundos
- Histórico das perguntas e respostas

### 4. **Como paciente, quero receber recomendações personalizadas de saúde** baseadas no meu perfil genético.
**Critérios de Aceitação:**
- Lista de recomendações categorizadas (nutrição, exercícios, exames)
- Justificativa baseada nos dados genéticos
- Links para recursos adicionais
- Opção de salvar/exportar recomendações

### 5. **Como médico, quero visualizar o relatório do paciente de forma estruturada** para análise clínica mais eficiente.
**Critérios de Aceitação:**
- Visualização organizada por categorias (riscos, ancestrais, portador)
- Dados técnicos disponíveis sob demanda
- Comparação com dados populacionais
- Exportação para formato médico padrão

### 6. **Como médico, quero gerar um resumo executivo do relatório** para compartilhar com o paciente durante a consulta.
**Critérios de Aceitação:**
- Geração automática de resumo em linguagem clínica
- Destaque dos pontos mais relevantes
- Formato adequado para impressão
- Personalização do nível de detalhe

### 7. **Como paciente, quero visualizar minha ancestralidade de forma interativa** para entender minhas origens genéticas.
**Critérios de Aceitação:**
- Gráfico de pizza ou mapa mostrando composição étnica
- Comparação com populações de referência
- Linha do tempo migratória (se disponível)
- Compartilhamento seguro com familiares

### 8. **Como paciente, quero ser alertado sobre novas pesquisas relacionadas aos meus marcadores genéticos** para me manter atualizado.
**Critérios de Aceitação:**
- Sistema de notificações por e-mail
- Artigos científicos relevantes filtrados
- Resumo em linguagem acessível
- Controle de frequência de notificações

### 9. **Como paciente, quero comparar meus resultados com dados populacionais** para entender meu risco relativo.
**Critérios de Aceitação:**
- Gráficos de comparação com média populacional
- Explicação do significado estatístico
- Contextualização por idade, gênero e etnia
- Visualização clara da posição relativa

### 10. **Como paciente, quero controlar minha privacidade e compartilhamento de dados** para ter segurança sobre minhas informações.
**Critérios de Aceitação:**
- Painel de configurações de privacidade
- Controle granular sobre compartilhamento
- Explicação clara do uso dos dados
- Opção de deletar dados permanentemente

## 🎯 Roadmap de Implementação

### Sprint 1 (Atual)
- [x] Definição das user stories
- [x] Estruturação do projeto
- [x] Arquitetura inicial

### Sprint 2
- [ ] User Stories 1, 2, 3 (Upload, Resumo, Perguntas)
- [ ] Pipeline básico de processamento
- [ ] Interface web inicial

### Sprint 3
- [ ] User Stories 4, 5, 6 (Recomendações, Visualização Médica, Resumo)
- [ ] Integração completa com LLM
- [ ] Sistema de recomendações

### Sprint 4
- [ ] User Stories 7, 8, 9, 10 (Ancestralidade, Alertas, Comparação, Privacidade)
- [ ] Refinamento da interface
- [ ] Testes e validação

## 📊 Métricas de Sucesso

1. **Taxa de conversão**: % de usuários que fazem pelo menos 3 perguntas
2. **Satisfação**: NPS (Net Promoter Score) acima de 40
3. **Tempo reduzido**: Diminuição de 70% no tempo para entender o relatório
4. **Precisão**: 95% de acurácia nas respostas validadas por especialistas
5. **Engajamento**: 60% dos usuários retornam semanalmente

## 🔄 Priorização (MoSCoW)

**MUST HAVE:**
- Upload de PDF (1)
- Resumo de riscos (2)
- Sistema de perguntas (3)

**SHOULD HAVE:**
- Recomendações personalizadas (4)
- Visualização para médicos (5)
- Resumo executivo (6)

**COULD HAVE:**
- Visualização de ancestralidade (7)
- Alertas de pesquisas (8)
- Comparação populacional (9)

**WON'T HAVE (nesta fase):**
- Integração com prontuário eletrônico
- Análise de interação medicamentosa
- Previsão de resposta a tratamentos