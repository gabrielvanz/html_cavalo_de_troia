# Simulador Educacional de Cavalo de Tróia - Python

## 📋 Visão Geral

Este é um simulador educacional desenvolvido em Python para demonstrar conceitos de segurança cibernética relacionados ao Cavalo de Tróia (Trojan Horse). O projeto foi criado exclusivamente para fins educacionais e de conscientização sobre segurança.

## ⚠️ Aviso Importante

**ESTE SIMULADOR É DESTINADO APENAS PARA FINS EDUCACIONAIS E DE PESQUISA EM SEGURANÇA CIBERNÉTICA.**

- ❌ **NÃO** deve ser usado para atividades maliciosas
- ❌ **NÃO** pode causar danos reais (opera em modo sandbox)
- ❌ **NÃO** deve ser usado para atacar sistemas reais
- ✅ **SIM** deve ser usado para aprendizado e conscientização
- ✅ **SIM** opera em ambiente controlado e seguro

## 🎯 Objetivos Educacionais

- Demonstrar conceitos de segurança cibernética
- Explicar como trojans funcionam
- Mostrar técnicas de detecção e prevenção
- Conscientizar sobre riscos e proteções
- Fornecer ferramentas de análise educacional

## 🏗️ Estrutura do Projeto

```
trojan_horse_simulation/
├── trojan_horse_simulation.py      # Simulador principal
├── trojan_education_modules.py     # Módulos educacionais
├── trojan_security_analysis.py     # Análise de segurança
├── requirements.txt                 # Dependências
├── README_PYTHON_SIMULATION.md     # Este arquivo
└── trojan_simulation.log           # Log de execução (gerado automaticamente)
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- Bibliotecas padrão do Python (não são necessárias instalações adicionais)

### Execução

1. **Clone ou baixe os arquivos do projeto**

2. **Execute o simulador principal:**
   ```bash
   python trojan_horse_simulation.py
   ```

3. **Execute módulos específicos:**
   ```bash
   # Módulos educacionais
   python trojan_education_modules.py
   
   # Análise de segurança
   python trojan_security_analysis.py
   ```

## 📚 Funcionalidades

### 1. Simulador Principal (`trojan_horse_simulation.py`)

- **Simulação Educacional**: Demonstra conceitos básicos de trojans
- **Simulação de Detecção**: Mostra como detectar trojans
- **Simulação de Prevenção**: Demonstra medidas de proteção
- **Simulação de Análise**: Análise de amostras de trojans
- **Relatórios de Segurança**: Geração de relatórios detalhados
- **Exportação de Dados**: Exportação em formato JSON

### 2. Módulos Educacionais (`trojan_education_modules.py`)

- **Ciclo de Vida**: Demonstra o ciclo completo de um trojan
- **Técnicas de Detecção**: Explica métodos de detecção
- **Medidas de Prevenção**: Lista estratégias de proteção
- **Cenários de Ataque**: Simula diferentes vetores de ataque
- **Análise de Exemplos**: Analisa trojans famosos
- **Quiz Educacional**: Testa conhecimentos sobre segurança

### 3. Análise de Segurança (`trojan_security_analysis.py`)

- **Análise Estática**: Análise de código e arquivos
- **Análise Dinâmica**: Análise comportamental
- **Análise de Rede**: Monitoramento de tráfego
- **Detecção de Assinaturas**: Identificação de malware conhecido
- **Relatórios de Análise**: Geração de relatórios técnicos

## 🛡️ Recursos de Segurança

### Modo Sandbox
- Todas as simulações operam em ambiente isolado
- Nenhum dano real pode ser causado
- Logs detalhados de todas as atividades

### Modo Ético
- Avisos de segurança em todas as execuções
- Bloqueio de funcionalidades maliciosas
- Foco exclusivo em educação

### Auditoria
- Logs detalhados de todas as atividades
- Rastreamento de eventos de segurança
- Relatórios de auditoria

## 📊 Exemplos de Uso

### Simulação Educacional
```python
from trojan_horse_simulation import TrojanSimulator, SimulationType

simulator = TrojanSimulator()
result = simulator.simulate_trojan_behavior(SimulationType.EDUCATIONAL)
```

### Análise de Segurança
```python
from trojan_security_analysis import TrojanSecurityAnalyzer

analyzer = TrojanSecurityAnalyzer()
findings = analyzer.analyze_file_static("suspicious_file.py")
```

### Módulos Educacionais
```python
from trojan_education_modules import TrojanEducationModules

modules = TrojanEducationModules()
modules.demonstrate_trojan_lifecycle()
```

## 📈 Relatórios e Logs

### Logs de Execução
- Arquivo: `trojan_simulation.log`
- Formato: Timestamp, Nível, Mensagem
- Inclui: Todas as atividades do simulador

### Relatórios de Segurança
- Eventos de segurança registrados
- Estatísticas de ameaças
- Recomendações de proteção

### Exportação de Dados
- Formato: JSON
- Inclui: Resultados de simulações, eventos, configurações
- Uso: Análise posterior, auditoria, relatórios

## 🔧 Configurações

### Configurações de Segurança
```python
# Tempo máximo de simulação (segundos)
max_simulation_time = 300

# Modo sandbox (sempre ativo)
sandbox_mode = True

# Modo ético (sempre ativo)
ethical_mode = True
```

### Configurações de Logging
```python
# Nível de log
logging.basicConfig(level=logging.INFO)

# Arquivo de log
handlers=[logging.FileHandler('trojan_simulation.log')]
```

## 🎓 Conteúdo Educacional

### Conceitos Abordados
- Definição e características de trojans
- Ciclo de vida de infecção
- Técnicas de ocultação e evasão
- Métodos de detecção e prevenção
- Análise de malware
- Aspectos legais e éticos

### Exemplos Reais
- Zeus Trojan (2007-2010)
- Emotet (2014-2021)
- TrickBot (2016-presente)
- NetBus (1998)
- Sub7 (1999)

### Técnicas Demonstradas
- Análise estática e dinâmica
- Detecção por assinatura
- Análise comportamental
- Monitoramento de rede
- Sandboxing

## ⚖️ Aspectos Legais e Éticos

### Legislação Brasileira
- **Lei 12.737/2012**: Crimes Cibernéticos
- **Penalidades**: 3 a 5 anos de prisão
- **Multas**: Indenizações às vítimas
- **Responsabilização**: Civil e criminal

### Uso Ético
- Apenas para fins educacionais
- Não para atividades maliciosas
- Respeito à privacidade
- Conscientização sobre segurança

## 🚨 Avisos de Segurança

### ⚠️ Importante
- Este simulador é apenas para educação
- Não use para atividades maliciosas
- Respeite a legislação local
- Use apenas em ambientes controlados

### 🛡️ Proteções Implementadas
- Modo sandbox obrigatório
- Logs de auditoria
- Avisos de segurança
- Bloqueio de funcionalidades maliciosas

## 📞 Suporte e Contato

### Equipe de Desenvolvimento
- **Diogo Chaves** - Desenvolvimento e Segurança
- **Gabriel Vanz** - Análise e Testes
- **Vitor Badin** - Documentação e Educação

### Instituição
- **Atitus Educação**
- **Disciplina**: Criptografia e Segurança
- **Ano**: 2024

## 📄 Licença

Este projeto é destinado exclusivamente para fins educacionais e de pesquisa em segurança cibernética. O uso malicioso é expressamente proibido e pode resultar em consequências legais severas.

## 🔄 Atualizações e Versões

### Versão Atual: 1.0.0
- Simulador principal funcional
- Módulos educacionais completos
- Análise de segurança implementada
- Documentação completa

### Próximas Versões
- Interface gráfica (opcional)
- Mais exemplos de trojans
- Análise de rede avançada
- Relatórios visuais

## 📚 Referências

### Fontes Acadêmicas
- MITRE ATT&CK Framework
- NIST Cybersecurity Framework
- OWASP Top 10
- Estudos sobre malware

### Legislação
- Lei 12.737/2012 (Brasil)
- Convenção de Budapeste
- GDPR (Europa)

### Organizações
- CERT/CC
- SANS Institute
- Kaspersky Lab
- Symantec

---

**IMPORTANTE**: Este simulador foi desenvolvido exclusivamente para fins educacionais e de conscientização sobre segurança cibernética. O uso malicioso é expressamente proibido e pode resultar em consequências legais severas. Use com responsabilidade e sempre respeite a legislação local.
