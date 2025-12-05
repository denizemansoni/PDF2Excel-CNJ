# 📄 PDF2Excel-CNJ  

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green)](#-licença)  

Aplicação desenvolvida para resolver um problema cotidiano de **extração de dados de relatórios em PDF**.  
O objetivo é **converter informações jurídicas** — como **números de processo CNJ** e **nomes das partes** — em uma planilha Excel organizada e pronta para análise.  

---

## 📑 Índice  

- [🚀 Motivação](#-motivação)  
- [🛠️ Tecnologias utilizadas](#-tecnologias-utilizadas)  
- [📂 Estrutura de pastas](#-estrutura-de-pastas)  
- [📦 Instalação das dependências](#-instalação-das-dependências)  
- [▶️ Uso](#️-uso)  
- [📊 Exemplo de saída](#-exemplo-de-saída)  
- [🤝 Contribuição](#-contribuição)  
- [📜 Licença](#-licença)  

---

## 🚀 Motivação  

Relatórios jurídicos em PDF, frequentemente disponibilizados sem linhas de grade, dificultam a manipulação e análise dos dados.  
Para otimizar o trabalho e garantir maior eficiência, foi desenvolvida uma aplicação que **automatiza a extração e organização** das informações jurídicas, como números de processo CNJ e nomes das partes.  

---

## 🛠️ Tecnologias utilizadas  

- 🐍 [Python 3](https://www.python.org/) → linguagem principal  
- 📑 [Camelot](https://camelot-py.readthedocs.io/) → leitura de tabelas em PDF  
- 📊 [Pandas](https://pandas.pydata.org/) → manipulação e exportação dos dados  
- 🔎 [Regex](https://docs.python.org/3/library/re.html) → identificação e separação de números de processo CNJ  
- 📈 [OpenPyXL](https://openpyxl.readthedocs.io/) → exportação para Excel  

---

## 📂 Estrutura de pastas  

```plaintext
PDF2Excel-CNJ/
│
├── extrairpdf.py          # Script principal da aplicação
├── requirements.txt       # Lista de dependências do projeto
├── README.md              # Documentação completa do projeto
│
├── input/                 # PDFs de entrada (relatórios originais)
│   └── exemplo.pdf
│
├── output/                # Arquivos Excel gerados pela aplicação
│   └── relatorio_processos.xlsx
│
└── docs/                  # Documentação extra (prints, exemplos)
    └── exemplo_saida.png
```

---

## 📦 Instalação das dependências  

Este projeto utiliza um arquivo `requirements.txt` para facilitar a instalação das bibliotecas necessárias.  

**Conteúdo do `requirements.txt`:**  
```plaintext
camelot-py[cv]==0.11.0
pandas==2.2.2
openpyxl==3.1.5
```

**Como instalar:**  
```bash
pip install -r requirements.txt
```

---

## ▶️ Uso  

1. Coloque o arquivo PDF na pasta `input/`.  
2. Execute o script:  
   ```bash
   python extrairpdf.py
   ```  
3. O resultado será salvo na pasta `output/` com o nome:  
   ```plaintext
   relatorio_processos.xlsx
   ```

---

## 📊 Exemplo de saída  

| Número do processo        | Nome da parte     | Página |
|---------------------------|------------------|--------|
| 0001234-56.2020.8.21.0001 | João da Silva    | 1      |
| 0005678-90.2021.8.21.0002 | Maria Oliveira   | 2      |

---

## 📜 Licença  

Este projeto está sob a licença **MIT**.  

---