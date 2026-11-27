"""Gera a imagem da Jornada do Usuario (docs/01-teorico.md, secao 1.2) pra
embutir no documento teorico. Tamanho impresso: 14,5 x 8,0 cm, a 300dpi.

Uso: python jornada_usuario.py
Saida: docs/screenshots/jornada-usuario.png
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

import build as b

ROOT = b.ROOT
PROJ = b.PROJ
FIGMA = b.FIGMA
SCREENSHOTS = b.SCREENSHOTS
OUT = PROJ / "docs" / "screenshots" / "jornada-usuario.png"

# 14,5 x 8,0 cm a 300dpi
W, H = 1710, 943

INDIGO = "#3730A3"
TEXTO = "#1d3a8b"
TEXTO_SEC = "#5A5784"

STEPS = [
    ("1", "Primeiro acesso", SCREENSHOTS / "tela-01-boas-vindas.png",
     "Lê “sem contagem\nregressiva”", "😐"),
    ("2", "Decidir o que fazer", SCREENSHOTS / "tela-02-inicio.png",
     "Vê “Continuar\ndaqui”", "🙂"),
    ("3", "Escolher a tarefa", FIGMA / "tela-03-escolher-tarefa.png",
     "Tarefa nova\nou recente", "🙂"),
    ("4", "Focar", SCREENSHOTS / "tela-04-sessao.png",
     "Cronômetro sobe,\nsem alarme", "😌"),
    ("5", "Lembrar de\noutra coisa", FIGMA / "tela-05-lembrar-depois.png",
     "Anota e volta\nà sessão", "😟🙂"),
    ("6", "Concluir", SCREENSHOTS / "tela-06-concluida.png",
     "Vê o tempo e\ncompara, gentil", "😄"),
    ("7", "Voltar outro dia", SCREENSHOTS / "tela-02-inicio.png",
     "Toca em\n“Retomar”", "🙂"),
]

MARGIN = 36
COL_W = (W - 2 * MARGIN) / len(STEPS)
PHONE_H = 480
PHONE_W = int(PHONE_H * 390 / 844)
PHONE_TOP = 190

body = ""
body += f'''<div style="position:absolute; top:26px; left:{MARGIN}px; font-family:'Lexend'; font-weight:700;
  font-size:30px; color:{INDIGO};">A Jornada do Usuário</div>'''
body += f'''<div style="position:absolute; top:66px; left:{MARGIN}px; width:{W - 2 * MARGIN}px; font-family:'Lexend';
  font-weight:400; font-size:14px; color:{TEXTO_SEC};">Sete etapas, da desconfiança do primeiro acesso à confiança de quem volta no dia seguinte.</div>'''

for i, (num, title, src, action, emoji) in enumerate(STEPS):
    cx = MARGIN + COL_W * i + COL_W / 2
    phone_left = cx - PHONE_W / 2

    body += f'''<div style="position:absolute; top:{PHONE_TOP}px; left:{phone_left}px; width:{PHONE_W}px; height:{PHONE_H}px;
      border-radius:28px; border:7px solid #0F0D2E; overflow:hidden; background:#000;
      box-shadow:0 10px 20px -6px rgba(27,24,70,.3);">
      <img src="{b.img_src(src)}" style="width:100%; height:100%; object-fit:cover; display:block;" />
      </div>'''

    body += f'''<div style="position:absolute; top:{PHONE_TOP - 36}px; left:{cx - 14}px; width:28px; height:28px;
      border-radius:50%; background:{INDIGO}; color:#FFFFFF; font-family:'Lexend'; font-weight:700; font-size:14px;
      display:flex; align-items:center; justify-content:center;">{num}</div>'''

    title_html = title.replace(chr(10), "<br>")
    action_html = action.replace(chr(10), "<br>")
    body += f'''<div style="position:absolute; top:{PHONE_TOP + PHONE_H + 20}px; left:{MARGIN + COL_W * i + 4}px; width:{COL_W - 8}px;
      text-align:center; font-family:'Lexend'; font-weight:600; font-size:14px; color:{TEXTO}; line-height:1.3;">{title_html}</div>'''
    body += f'''<div style="position:absolute; top:{PHONE_TOP + PHONE_H + 74}px; left:{MARGIN + COL_W * i + 4}px; width:{COL_W - 8}px;
      text-align:center; font-family:'Lexend'; font-weight:400; font-size:12.5px; color:{TEXTO_SEC}; line-height:1.3;">{action_html}</div>'''
    body += f'''<div style="position:absolute; top:{PHONE_TOP + PHONE_H + 122}px; left:{MARGIN + COL_W * i}px; width:{COL_W}px;
      text-align:center; font-size:25px;">{emoji}</div>'''

    if i < len(STEPS) - 1:
        arrow_left = MARGIN + COL_W * (i + 1) - 9
        arrow_top = PHONE_TOP + PHONE_H / 2 - 9
        body += f'<div style="position:absolute; top:{arrow_top}px; left:{arrow_left}px;">{b.icon("arrow-right", INDIGO, 18)}</div>'

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

html_path = ROOT / "_tmp_jornada.html"
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
