"""Gera duas imagens explicativas (nao-slide) a partir da tela 02 - Inicio:
1) o celular com o card 'Continuar daqui' destacado
2) o card 'Continuar daqui' ampliado, com setas pra 'Onde parei' / 'Proximo
   passo' e um icone de clique no botao Retomar

Uso: python anotar_tela02.py
Saida: docs/screenshots/tela-02-inicio-destaque.png
       docs/screenshots/continuar-daqui-balao.png
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

import build as b

ROOT = b.ROOT
PROJ = b.PROJ
FIGMA = b.FIGMA
OUT_DIR = PROJ / "docs" / "screenshots"

# Posicao do Card/ContinuarDaqui dentro da tela nativa (do get_metadata, node 43:11)
CARD_X, CARD_Y, CARD_W, CARD_H = 24, 128, 342, 175

# Posicoes internas do card (do get_metadata, node 49:29)
ONDE_X0, ONDE_Y0, ONDE_W0, ONDE_H0 = 17.5, 46.5, 307, 21
PROX_X0, PROX_Y0, PROX_W0, PROX_H0 = 17.5, 75.5, 307, 21
BTN_X0, BTN_Y0, BTN_W0, BTN_H0 = 17.5, 104.5, 109, 53


def render(body, w, h, out_path):
    html = f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>{b.STYLE_CSS}
html, body {{ width: {w}px !important; height: {h}px !important; }}
</style>
</head>
<body>
<div class="slide bg-creme" style="width:{w}px; height:{h}px;">
{body}
</div>
</body></html>"""
    html_path = ROOT / "_tmp_anotar.html"
    html_path.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": w, "height": h})
        page.goto(b.img_src(html_path))
        page.wait_for_timeout(150)
        page.screenshot(path=str(out_path))
        browser.close()
    html_path.unlink()
    print("Gerado:", out_path)


# ---------------------------------------------------------------------------
# Imagem 1: celular com o card destacado
# ---------------------------------------------------------------------------

def build_celular():
    scale = 1.2
    phone_w, phone_h = 390 * scale, 844 * scale
    left, top = 130, 150
    w, h = int(phone_w + left * 2), int(phone_h + top + 100)

    hi_left = left + CARD_X * scale
    hi_top = top + CARD_Y * scale
    hi_w = CARD_W * scale
    hi_h = CARD_H * scale

    body = ""
    body += f'''<div style="position:absolute; top:48px; left:{left}px; font-family:'Lexend'; font-weight:700;
      font-size:38px; color:{b.TEXTO};">Tela 02 — Início</div>'''
    body += f'''<div style="position:absolute; top:{top}px; left:{left}px; width:{phone_w}px; height:{phone_h}px;
      border-radius:{48 * scale}px; border:{12 * scale}px solid #0F0D2E;
      box-shadow:0 50px 100px -20px rgba(15,13,46,.45), 0 20px 40px rgba(15,13,46,.25);
      overflow:hidden; background:#000;">
      <img src="{b.img_src(FIGMA / 'tela-02-inicio-cheia.png')}" style="width:100%; height:100%; object-fit:cover; display:block;" />
      </div>'''
    body += f'''<div style="position:absolute; top:{hi_top}px; left:{hi_left}px; width:{hi_w}px; height:{hi_h}px;
      border-radius:{14 * scale}px; border:4px solid {b.ROSA}; box-shadow:0 0 0 6px rgba(236,111,168,0.22);"></div>'''

    render(body, w, h, OUT_DIR / "tela-02-inicio-destaque.png")


# ---------------------------------------------------------------------------
# Imagem 2: balao "Continuar daqui" ampliado, com setas e icone de clique
# ---------------------------------------------------------------------------

def build_balao():
    card_scale = 2.4
    pad = 24
    card_img_w, card_img_h = CARD_W * card_scale, CARD_H * card_scale
    wrap_w, wrap_h = card_img_w + pad * 2, card_img_h + pad * 2
    wrap_left, wrap_top = 40, 50
    img_left, img_top = wrap_left + pad, wrap_top + pad

    def rel(x0, y0, w0, h0):
        return (img_left + x0 * card_scale, img_top + y0 * card_scale, w0 * card_scale, h0 * card_scale)

    onde_x, onde_y, onde_w, onde_h = rel(ONDE_X0, ONDE_Y0, ONDE_W0, ONDE_H0)
    prox_x, prox_y, prox_w, prox_h = rel(PROX_X0, PROX_Y0, PROX_W0, PROX_H0)
    btn_x, btn_y, btn_w, btn_h = rel(BTN_X0, BTN_Y0, BTN_W0, BTN_H0)

    label_x = wrap_left + wrap_w + 70
    label_w = 420
    w = int(label_x + label_w + 50)
    h = int(wrap_top + wrap_h + 50)

    body = ""
    body += f'''<div style="position:absolute; top:{wrap_top}px; left:{wrap_left}px; width:{wrap_w}px; height:{wrap_h}px;
      background:#FFFFFF; border-radius:28px; box-shadow:0 24px 48px -16px rgba(27,24,70,.28);"></div>'''
    body += f'''<img src="{b.img_src(FIGMA / "card-continuar-daqui.png")}" style="position:absolute; top:{img_top}px; left:{img_left}px;
      width:{card_img_w}px; height:{card_img_h}px; border-radius:10px;" />'''

    hand_size = 72
    body += b.icon_badge(
        btn_y + btn_h - hand_size / 2, btn_x + btn_w - hand_size / 2,
        hand_size, "hand-click", b.ROSA, "#FFFFFF", 34,
    )

    def callout(row_y, row_h, text, color=None):
        color = color or b.INDIGO
        cy = row_y + row_h / 2
        out = b.dashed_line_between(wrap_left + wrap_w - 10, cy, label_x - 20, cy, color, width=3)
        out += f'''<div style="position:absolute; top:{cy - 24}px; left:{label_x}px; width:{label_w}px;
          font-family:'Lexend'; font-weight:700; font-size:32px; color:{color}; line-height:1.15;">{text}</div>'''
        return out

    body += callout(onde_y, onde_h, "Onde parei")
    body += callout(prox_y, prox_h, "Próximo passo")
    body += callout(btn_y, btn_h, "Retomar — 1 toque", color=b.ROSA)

    render(body, w, h, OUT_DIR / "continuar-daqui-balao.png")


if __name__ == "__main__":
    build_celular()
    build_balao()
