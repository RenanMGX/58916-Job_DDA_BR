# Job DDA_BR Automation

Este repositório contém uma automação desenvolvida em Python para interagir com o sistema SAP, realizar operações específicas e gerar logs detalhados. A automação foi projetada para ser executada de forma eficiente e segura, utilizando boas práticas de programação e bibliotecas confiáveis.

## 📋 Funcionalidades

1. **Extração de Dados do SAP**:
   - A automação conecta-se ao sistema SAP e extrai informações de empresas utilizando a transação `/n ZFI006`.
   - Os dados extraídos são salvos em um arquivo Excel no diretório de downloads do usuário.

2. **Processamento de Empresas**:
   - Após a extração, a automação processa cada empresa encontrada, utilizando a transação `/n dda_br` no SAP.
   - O processamento inclui a configuração de filtros de data e status para a execução da transação.

3. **Geração de Logs**:
   - Logs detalhados são gerados para cada etapa da execução, incluindo erros e relatórios de progresso.
   - Os logs podem ser salvos localmente em arquivos CSV e enviados para um servidor remoto.

4. **Configuração e Credenciais**:
   - O sistema utiliza um arquivo de configuração (`config.init`) para armazenar parâmetros padrão.
   - As credenciais do SAP são gerenciadas de forma segura utilizando arquivos JSON criptografados.

## 🛠️ Estrutura do Projeto

```plaintext
├── [main.py](http://_vscodecontentref_/0)                     # Arquivo principal para execução da automação
├── Entities/
│   ├── [sap.py](http://_vscodecontentref_/1)                  # Classe SAP para manipulação de transações no SAP
│   ├── dependencies/
│   │   ├── [arguments.py](http://_vscodecontentref_/2)        # Gerenciamento de argumentos de linha de comando
│   │   ├── [config.py](http://_vscodecontentref_/3)           # Gerenciamento de configurações
│   │   ├── [credenciais.py](http://_vscodecontentref_/4)      # Gerenciamento de credenciais criptografadas
│   │   ├── [default_config.py](http://_vscodecontentref_/5)   # Configurações padrão
│   │   ├── [functions.py](http://_vscodecontentref_/6)        # Funções utilitárias
│   │   ├── [logs.py](http://_vscodecontentref_/7)             # Geração e envio de logs
│   │   ├── [navegador_chrome.py](http://_vscodecontentref_/8) # Classe para manipulação do navegador Chrome
│   │   ├── [project_name.py](http://_vscodecontentref_/9)     # Nome do projeto
│   │   ├── [sharepointfolder.py](http://_vscodecontentref_/10) # Gerenciamento de pastas no SharePoint
│   └── [__init__.py](http://_vscodecontentref_/11)             # Inicialização do módulo Entities
├── [requirements.txt](http://_vscodecontentref_/12)            # Dependências do projeto
├── [config.init](http://_vscodecontentref_/13)                 # Arquivo de configuração gerado automaticamente
├── Logs/                       # Diretório para armazenamento de logs
└── .gitignore                  # Arquivo para ignorar arquivos no Git 
```

## 🚀 Como Executar

**Pré-requisitos:**
Python 3.10 ou superior
SAP GUI instalado e configurado
Dependências listadas no arquivo requirements.txt
Instalação

**Clone o repositório:**
Instale as dependências:

**Configure o arquivo config.init:**
O arquivo será gerado automaticamente na primeira execução.
Edite o arquivo para ajustar as configurações padrão, como credenciais e parâmetros de log.

**Adicione as credenciais no diretório especificado:**
As credenciais devem ser salvas no formato JSON no diretório "caminho".

**Para iniciar a automação, execute o seguinte comando:**
Argumentos Disponíveis
start: Inicia a execução completa da automação.

## 📚 Detalhes Técnicos
main.py
O arquivo principal que orquestra a execução da automação. Ele utiliza a classe SAP para interagir com o sistema SAP e processar as empresas.

Entities/sap.py
Contém a classe SAP, que herda de SAPManipulation. Essa classe encapsula a lógica para conectar-se ao SAP, executar transações e manipular sessões.

Entities/dependencies

**Este diretório contém módulos auxiliares, incluindo:**
arguments.py: Gerencia argumentos de linha de comando.
config.py: Lida com configurações do projeto.
credenciais.py: Gerencia credenciais criptografadas.
logs.py: Gera logs locais e remotos.
functions.py: Funções utilitárias para manipulação de arquivos e logs.

## 🧪 Testes
Para testar a automação, você pode usar o argumento start e verificar os logs gerados no diretório Logs/.


Desenvolvido por: Renan Oliveira
Contato: renan.oliveira@patrimar.com.br