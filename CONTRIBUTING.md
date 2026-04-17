# Contribuindo para o DASA Genera AI Assistant

## 📋 Visão Geral

Este projeto é desenvolvido como parte do Challenge DASA da FIAP. Agradecemos seu interesse em contribuir!

## 🚀 Primeiros Passos

### Pré-requisitos
- Python 3.9+
- PostgreSQL 14+
- Docker e Docker Compose (opcional)
- Git

### Configuração do Ambiente

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/dasa-genera-ai.git
   cd dasa-genera-ai
   ```

2. **Configure o ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**
   ```bash
   cp .env.example .env
   # Edite o arquivo .env com suas configurações
   ```

5. **Inicie os serviços**
   ```bash
   docker-compose up -d  # Se usando Docker
   # ou configure PostgreSQL manualmente
   ```

## 🏗️ Estrutura do Projeto

```
.
├── src/
│   ├── pdf_processing/     # Extração e processamento de PDFs
│   ├── nlp/               # Processamento de linguagem natural
│   ├── api/               # API FastAPI
│   └── frontend/          # Interface web (React)
├── tests/                 # Testes automatizados
├── docs/                  # Documentação
└── examples/              # Exemplos de dados
```

## 🔧 Processo de Desenvolvimento

### 1. Escolha uma Issue
- Verifique as issues abertas no GitHub
- Escolha uma issue que corresponda às suas habilidades
- Comente na issue para indicar seu interesse

### 2. Crie uma Branch
```bash
git checkout -b feature/nome-da-feature
# ou
git checkout -b fix/nome-do-fix
```

### 3. Desenvolva sua Feature
- Siga as convenções de código existentes
- Escreva testes para seu código
- Documente suas alterações

### 4. Execute os Testes
```bash
pytest tests/ --cov=src --cov-report=html
```

### 5. Formate seu Código
```bash
black src/ tests/
flake8 src/ tests/
mypy src/
```

### 6. Faça Commit
```bash
git add .
git commit -m "feat: descrição concisa da feature

Descrição mais detalhada se necessário.
Inclui:
- Item 1
- Item 2
- Item 3"
```

### 7. Envie um Pull Request
- Push para sua branch
- Crie um Pull Request no GitHub
- Aguarde revisão da equipe

## 📝 Convenções de Código

### Python
- Use type hints sempre que possível
- Siga o PEP 8
- Docstrings no formato Google Style
- Nomes descritivos para variáveis e funções

### Commits
Use [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` Nova feature
- `fix:` Correção de bug
- `docs:` Documentação
- `style:` Formatação, semântica
- `refactor:` Refatoração de código
- `test:` Adição ou correção de testes
- `chore:` Tarefas de manutenção

### Documentação
- Atualize o README.md se necessário
- Documente APIs com OpenAPI/Swagger
- Comente código complexo

## 🧪 Testes

### Tipos de Testes
1. **Unitários**: Testam funções individuais
2. **Integração**: Testam interação entre componentes
3. **E2E**: Testam fluxos completos do usuário

### Executando Testes
```bash
# Todos os testes
pytest

# Testes específicos
pytest tests/unit/
pytest tests/integration/

# Com cobertura
pytest --cov=src --cov-report=term-missing
```

## 🔒 Segurança

### Dados Sensíveis
- Nunca commit dados reais de pacientes
- Use dados de exemplo/anônimos para desenvolvimento
- Não armazene secrets no código

### Vulnerabilidades
- Reporte vulnerabilidades de segurança para a equipe
- Use dependências atualizadas
- Execute scanners de segurança periodicamente

## 🤝 Código de Conduta

### Nosso Compromisso
Criamos um ambiente aberto e acolhedor para todos.

### Comportamento Esperado
- Seja respeitoso e inclusivo
- Aceite críticas construtivas
- Foque no que é melhor para o projeto
- Mostre empatia com outros colaboradores

### Comportamento Inaceitável
- Linguagem ou imagens sexualizadas
- Assédio público ou privado
- Comentários ofensivos
- Qualquer forma de discriminação

## 📞 Suporte

### Dúvidas Técnicas
- Consulte a documentação no diretório `docs/`
- Verifique issues existentes no GitHub
- Participe das discussões do projeto

### Contato com a Equipe
- Para questões urgentes: [email da equipe]
- Para questões de segurança: [email de segurança]

## 🎉 Reconhecimento

Todos os contribuidores serão reconhecidos no arquivo CONTRIBUTORS.md.

Obrigado por contribuir para tornar a saúde genética mais acessível! 🧬