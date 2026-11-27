"""Gera uma imagem explicativa (nao-slide) da tela 02 - Inicio, destacando o
card 'Continuar daqui': area ampliada, setas pra 'Onde parei' / 'Proximo passo'
e icone de clique no botao Retomar.

Uso: python anotar_tela02.py
Saida: docs/screenshots/tela-02-continuar-daqui-anotada.png
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

import build as b

ROOT = b.ROOT
PROJ = b.PROJ
FIGMA = b.FIGMA
OUT = PROJ / "docs" / "screenshots" / "tela-02-continuar-daqui-anotada.png"

W, H = 2300, 1080

PHONE_NATIVE_W, PHONE_NATIVE_H = 390, 844
PHONE_SCALE = 1.0
PHONE_W = PHONE_NATIVE_W * PHONE_SCALE
PHONE_H = PHONE_NATIVE_H * PHONE_SCALE
PHONE_TOP = 190
PHONE_LEFT = 120

# Posicao do Card/ContinuarDaqui dentro da tela nativa (do get_metadata)
CARD_X, CARD_Y, CARD_W, CARD_H = 24, 128, 342, 175

# Caixa de destaque sobre o card, na tela (escalada)
HI_LEFT = PHONE_LEFT + CARD_X * PHONE_SCALE
HI_TOP = PHONE_TOP + CARD_Y * PHONE_SCALE
HI_W = CARD_W * PHONE_SCALE
HI_H = CARD_H * PHONE_SCALE

# Card ampliado (recorte renderizado em alta fidelidade, nao upscale de pixel)
CARD_SCALE = 2.339
CARD_IMG_W = CARD_W * CARD_SCALE
CARD_IMG_H = CARD_H * CARD_SCALE
PAD = 24
WRAP_W = CARD_IMG_W + PAD * 2
WRAP_H = CARD_IMG_H + PAD * 2
WRAP_LEFT = 900
WRAP_TOP = 240
IMG_LEFT = WRAP_LEFT + PAD
IMG_TOP = WRAP_TOP + PAD

# Posicoes internas do card (do get_metadata de 49:29), escaladas + offset
def card_rel(x, y, w, h):
    return (IMG_LEFT + x * CARD_SCALE, IMG_TOP + y * CARD_SCALE, w * CARD_SCALE, h * CARD_SCALE)

ONDE_X, ONDE_Y, ONDE_W, ONDE_H = card_rel(17.5, 46.5, 307, 21)
PROX_X, PROX_Y, PROX_W, PROX_H = card_rel(17.5, 75.5, 307, 21)
BTN_X, BTN_Y, BTN_W, BTN_H = card_rel(17.5, 104.5, 109, 53)

body = ""

# fundo: duas formas suaves
body += b.bg_circle(-150, -150, 600, b.FORMA_CREME[0])
body += b.bg_circle(700, 1850, 500, b.FORMA_CREME[2], 0.7)

# titulo (desenhado por cima de tudo no final, pra nunca ficar atras do celular)

# celular (moldura escura, igual ao resto do material)
body += f'''<div style="position:absolute; top:{PHONE_TOP}px; left:{PHONE_LEFT}px; width:{PHONE_W}px; height:{PHONE_H}px;
  border-radius:48px; border:12px solid #0F0D2E; box-shadow:0 50px 100px -20px rgba(15,13,46,.45), 0 20px 40px rgba(15,13,46,.25);
  overflow:hidden; background:#000;">
  <img src="{b.img_src(FIGMA / 'tela-02-inicio-cheia.png')}" style="width:100%; height:100%; object-fit:cover; display:block;" />
  </div>'''

# destaque (contorno) sobre o card dentro do celular
body += f'''<div style="position:absolute; top:{HI_TOP}px; left:{HI_LEFT}px; width:{HI_W}px; height:{HI_H}px;
  border-radius:{14 * PHONE_SCALE}px; border:4px solid {b.ROSA}; box-shadow:0 0 0 6px rgba(236,111,168,0.22);"></div>'''

# linhas conectando o destaque ao card ampliado (estilo "lupa")
body += b.dashed_line_between(HI_LEFT + HI_W, HI_TOP, WRAP_LEFT, WRAP_TOP, b.ROSA, width=3)
body += b.dashed_line_between(HI_LEFT + HI_W, HI_TOP + HI_H, WRAP_LEFT, WRAP_TOP + WRAP_H, b.ROSA, width=3)

# cartao branco com o recorte ampliado do Card/ContinuarDaqui
body += f'''<div style="position:absolute; top:{WRAP_TOP}px; left:{WRAP_LEFT}px; width:{WRAP_W}px; height:{WRAP_H}px;
  background:#FFFFFF; border-radius:28px; box-shadow:0 24px 48px -16px rgba(27,24,70,.28);"></div>'''
body += f'''<img src="{b.img_src(FIGMA / "card-continuar-daqui.png")}" style="position:absolute; top:{IMG_TOP}px; left:{IMG_LEFT}px;
  width:{CARD_IMG_W}px; height:{CARD_IMG_H}px; border-radius:10px;" />'''

# icone de clique (mao) no canto do botao Retomar, em badge circular pra contrastar
HAND_SIZE = 72
body += b.icon_badge(
    BTN_Y + BTN_H - HAND_SIZE / 2, BTN_X + BTN_W - HAND_SIZE / 2,
    HAND_SIZE, "hand-click", b.ROSA, "#FFFFFF", 34,
)

label_x = WRAP_LEFT + WRAP_W + 70

LABEL_W = W - label_x - 60

def callout(row_y, row_h, text, color=None):
    color = color or b.INDIGO
    cy = row_y + row_h / 2
    out = b.dashed_line_between(WRAP_LEFT + WRAP_W - 10, cy, label_x - 20, cy, color, width=3)
    out += f'''<div style="position:absolute; top:{cy - 24}px; left:{label_x}px; width:{LABEL_W}px;
      font-family:'Lexend'; font-weight:700; font-size:32px; color:{color}; line-height:1.15;">{text}</div>'''
    return out

body += callout(ONDE_Y, ONDE_H, "Onde parei")
body += callout(PROX_Y, PROX_H, "Próximo passo")
body += callout(BTN_Y, BTN_H, "Retomar — 1 toque", color=b.ROSA)

# titulo, por cima de tudo
body += f'''<div style="position:absolute; top:48px; left:120px; font-family:'Lexend'; font-weight:700;
  font-size:44px; color:{b.TEXTO};">Tela 02 — Início: como funciona o<br>"Continuar daqui"</div>'''

html = f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>{b.STYLE_CSS}
html, body {{ width: {W}px !important; height: {H}px !important; }}
</style>
</head>
<body>
<div class="slide bg-creme" style="width:{W}px; height:{H}px;">
{body}
</div>
</body></html>"""

html_path = ROOT / "_tmp_anotar_tela02.html"
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
