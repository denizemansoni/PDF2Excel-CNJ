# Script principal da aplicação
import camelot
import pandas as pd
import re

# Normaliza texto (remove quebras e caracteres estranhos)
def normalizar_texto(s):
    if not isinstance(s, str):
        return s
    s = s.replace("\r", " ").replace("\n", " ").replace("cid:13", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Regex CNJ tolerante a espaços/quebras entre blocos, com grupos para reconstrução
CNJ_REGEX_GROUPS = re.compile(
    r"(\d{6,})\s*-\s*(\d{2})\s*\.\s*(\d{4})\s*\.\s*(\d)\s*\.\s*(\d{2})\s*\.\s*(\d{4})"
)

def extrair_cnj_e_nome(row_values):
    # row_values: lista com os textos das colunas da linha
    # 1) Normaliza cada célula e concatena a linha inteira para garantir que o CNJ seja encontrado mesmo se estiver quebrado
    textos = [normalizar_texto(v) for v in row_values if isinstance(v, str) and v.strip()]
    linha_concat = " ".join(textos)

    # 2) Procura CNJs com regex tolerante
    matches = list(CNJ_REGEX_GROUPS.finditer(linha_concat))

    if not matches:
        # Sem CNJ, se houver texto na primeira coluna, use como nome; senão, junta tudo
        nome = textos[0] if textos else None
        return pd.Series([None, nome])

    # 3) Reconstroi os CNJs no formato canônico e remove do texto para sobrar o nome
    cnjs = []
    nome_texto = linha_concat
    for m in matches:
        g1, g2, g3, g4, g5, g6 = m.groups()
        cnj = f"{g1}-{g2}.{g3}.{g4}.{g5}.{g6}"
        cnjs.append(cnj)
        # Remove exatamente o trecho correspondente ao match original (com espaços) do texto para preservar nomes
        nome_texto = (nome_texto[:m.start()] + " " + nome_texto[m.end():]).strip()

    # 4) Limpa espaços extras do nome
    nome_texto = re.sub(r"\s+", " ", nome_texto).strip()

    # Se ficou vazio após remoção, tenta usar a primeira coluna como nome
    if not nome_texto and textos:
        nome_texto = textos[0]

    # 5) Retorna CNJs (se houver mais de um, como lista concatenada) e o nome
    return pd.Series([", ".join(cnjs), nome_texto])

# Caminhos
PDF_PATH = r"C:\Users\denize.cordova\Desktop\EXTRAR PDF PARA XLSX\andamentosbenner.pdf"
OUT_XLSX = r"C:\Users\denize.cordova\Desktop\EXTRAR PDF PARA XLSX\relatorio_processos_simples.xlsx"

# Lê todas as páginas
tables = camelot.read_pdf(PDF_PATH, pages="all", flavor="stream", strip_text="\n")

result_rows = []
for page_idx, table in enumerate(tables, start=1):
    df = table.df.copy()

    # Normaliza célula a célula sem usar applymap (evita FutureWarning)
    for col in df.columns:
        df[col] = df[col].map(normalizar_texto)

    # Extrai por linha, concatenando colunas para garantir que CNJ seja encontrado mesmo quebrado
    for _, row in df.iterrows():
        cnj, nome = extrair_cnj_e_nome(row.tolist())
        # Ignora linhas totalmente vazias
        if not cnj and not nome:
            continue
        result_rows.append({
            "Número do processo": cnj,
            "Nome da parte": nome,
            "Página": page_idx
        })

# Consolida
df_final = pd.DataFrame(result_rows)

# Remove duplicatas óbvias
df_final = df_final.drop_duplicates()

# Exporta
df_final.to_excel(OUT_XLSX, index=False)

print("✅ Extração concluída! Arquivo salvo em:", OUT_XLSX)