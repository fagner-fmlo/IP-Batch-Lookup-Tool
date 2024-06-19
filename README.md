# IP-Batch-Lookup-Tool
Este projeto em Python oferece uma interface gráfica simples para consultar informações de IPs em lote. Utiliza a API do IP-API.com para obter informações como país e ASR (Autonomous System Number) de cada IP, e salva os resultados em uma planilha Excel.

Funcionalidades

    Carregar uma lista de IPs a partir de um arquivo .txt.
    Consultar informações de cada IP utilizando a API do IP-API.com.
    Salvar os resultados em uma planilha Excel.
    Exibir o nome do autor.

Pré-requisitos

Certifique-se de ter as seguintes bibliotecas Python instaladas:

    requests
    pandas
    openpyxl

Você pode instalar estas bibliotecas utilizando o pip:

sh

pip install requests pandas openpyxl

Como usar

    Clone o repositório:

    sh

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Execute o script:

sh

    python consulta_ips_ipapi.py

    Interface Gráfica:
        A interface inicial terá dois botões: "Carregar Arquivo" e "Exibir Autor".
        Clique em "Carregar Arquivo" para selecionar o arquivo de texto com os IPs (um por linha).
        O script consultará os IPs e permitirá que você salve os resultados em uma planilha Excel.
        Clique em "Exibir Autor" para ver o nome do autor.

Estrutura do Projeto

    consulta_ips_ipapi.py: Script principal que contém toda a lógica para carregar arquivos, consultar informações de IPs e salvar resultados.

Exemplo de Uso

    Carregar Arquivo de IPs:
        Selecione um arquivo de texto (.txt) contendo uma lista de IPs. Cada IP deve estar em uma linha separada.

    Consulta e Salvamento:
        O script realizará a consulta para cada IP e abrirá uma janela de diálogo para salvar os resultados em um arquivo Excel (.xlsx).

    Exibir Autor:
        Uma janela pop-up será exibida mostrando o nome do autor: cybersys_br.
Explicação

    consultar_ips: Faz a consulta de cada IP utilizando a API do IP-API.com.
    carregar_arquivo: Abre uma janela de diálogo para selecionar o arquivo de texto com os IPs e chama a função de consulta.
    salvar_resultados: Salva os resultados em uma planilha Excel.
    exibir_autor: Exibe uma mensagem com o nome do autor.
    criar_interface: Configura a interface gráfica inicial com botões para carregar o arquivo de IPs e exibir o autor.
