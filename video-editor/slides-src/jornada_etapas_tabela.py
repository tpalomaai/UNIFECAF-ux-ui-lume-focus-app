"""Gera a imagem da tabela "Etapas e objetivos em cada interacao"
(docs/01-teorico.md, secao 1.2) pra embutir no documento teorico.
Mesmo formato de saida da jornada-usuario.png: 14,5 x 8,0 cm, 300dpi.

Uso: python jornada_etapas_tabela.py
Saida: docs/screenshots/jornada-etapas-objetivos.png
"""
from playwright.sync_api import sync_playwright

import build as b

ROOT = b.ROOT
PROJ = b.PROJ
OUT = PROJ / "docs" / "screenshots" / "jornada-etapas-objetivos.png"

# 14,5 x 8,0 cm a 300dpi
W, H = 1710, 943

INDIGO = "#3730A3"
TEXTO = "#1d3a8b"
TEXTO_SEC = "#5A5784"
FAIXA = "#EEEDFE"

COLS = [
    ("Etapa", 120),
    ("Objetivo da usuária", 365),
    ("Ação no app", 420),
    ("Tela", 155),
    ("Sentimento", 145),
    ("Oportunidade de design", 433),
]

ROWS = [
    ("1. Primeiro acesso", "Entender que o app não é mais um timer de pressão",
     "Lê “Foque no seu ritmo, sem contagem regressiva” e toca em “Começar”",
     "01 - Boas-vindas", "Desconfiada 😐", "Deixar claro o “sem pressão” logo na primeira frase"),
    ("2. Decidir o que fazer", "Lembrar onde parou",
     "Lê o card “Continuar daqui” (onde parei + próximo passo)",
     "02 - Início", "Aliviada 🙂", "Retomada em 1 toque: botão “Retomar”"),
    ("3. Escolher a tarefa", "Definir o objetivo da sessão",
     "Escreve uma tarefa nova ou escolhe uma recente (com o último tempo)",
     "03 - Escolher tarefa", "Decidida 🙂", "Tarefas recentes evitam redigitar e criam histórico"),
    ("4. Focar", "Trabalhar no próprio ritmo",
     "Acompanha o cronômetro subindo; pode pausar",
     "04 - Sessão em andamento", "Tranquila 😌", "Cronômetro progressivo, sem alarme nem cor de alerta"),
    ("5. Lembrar de outra coisa", "Não esquecer a tarefa paralela sem largar a atual",
     "Toca em “Lembrar depois”, anota e volta",
     "05 - Lembrar depois", "Preocupada →\naliviada 😟🙂", "A tarefa paralela fica guardada, sem culpa"),
    ("6. Concluir", "Ver quanto levou e registrar onde parou",
     "Toca em “Concluir”, vê o tempo e a comparação com a última vez, e preenche “Onde parei” e “Próximo passo”",
     "06 - Sessão concluída", "Orgulhosa 😄", "Comparação gentil: celebra quando melhora e acolhe quando não melhora"),
    ("7. Voltar outro dia", "Retomar sem esforço",
     "Abre o app e toca em “Retomar”",
     "02 - Início", "Confiante 🙂", "O ciclo recomeça com contexto, não do zero"),
]

MARGIN = 36
HEADER_TOP = 76
HEADER_H = 60
ROW_TOP0 = HEADER_TOP + HEADER_H
ROW_H = (H - ROW_TOP0 - 10) / len(ROWS)
CELL_PAD = 10

body = ""
body += f'''<div style="position:absolute; top:22px; left:{MARGIN}px; font-family:'Lexend'; font-weight:700;
  font-size:30px; color:{INDIGO};">Etapas e Objetivos em Cada Interação</div>'''

# cabecalho
x = MARGIN
for label, w in COLS:
    body += f'''<div style="position:absolute; top:{HEADER_TOP}px; left:{x}px; width:{w - CELL_PAD}px; height:{HEADER_H}px;
      background:{INDIGO}; display:flex; align-items:center; padding:0 {CELL_PAD}px;
      font-family:'Lexend'; font-weight:700; font-size:16px; color:#FFFFFF; line-height:1.25;">{label}</div>'''
    x += w

# linhas
for r, row in enumerate(ROWS):
    top = ROW_TOP0 + ROW_H * r
    if r % 2 == 1:
        body += f'<div style="position:absolute; top:{top}px; left:{MARGIN}px; width:{sum(w for _, w in COLS)}px; height:{ROW_H}px; background:{FAIXA};"></div>'
    x = MARGIN
    for c, (label, w) in enumerate(COLS):
        text = row[c].replace(chr(10), "<br>")
        weight = 700 if c == 0 else 400
        color = INDIGO if c == 0 else TEXTO
        body += f'''<div style="position:absolute; top:{top}px; left:{x}px; width:{w - CELL_PAD * 2}px; height:{ROW_H}px;
          display:flex; align-items:center; padding:0 {CELL_PAD}px;
          font-family:'Lexend'; font-weight:{weight}; font-size:15.5px; color:{color}; line-height:1.32;">{text}</div>'''
        x += w
    body += f'<div style="position:absolute; top:{top + ROW_H}px; left:{MARGIN}px; width:{sum(w for _, w in COLS)}px; height:1px; background:#D9D6FF;"></div>'

html = f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>{b.STYLE_CSS}
html, body {{ width: {W}px !important; height: {H}px !important; background: #FFFFFF !important; }}
</style>
</head>
<body>
<div style="position:relative; width:{W}px; height:{H}px; background:#FFFFFF; overflow:hidden;">
{body}
</div>
</body></html>"""

html_path = ROOT / "_tmp_etapas_tabela.html"
html_path.write_text(html, encoding="utf-8")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": W, "height": H})
    page.goto(b.img_src(html_path))
    page.wait_for_timeout(150)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(OUT))
    browser.close()
html_path.unlink()
print("Gerado:", OUT)
