"""Gera 3 imagens explicativas (nao-slide) no MESMO estilo visual do slide-06
("Vamos ver na pratica" - fundo noite, celular rotacionado, card-float com
borda rosa, estrelinhas) a partir da tela 02 - Inicio:

1) tela-02-inicio-destaque.png  — celular com o card 'Continuar daqui' destacado
2) continuar-daqui-balao.png    — o card 'Continuar daqui' ampliado, com setas
                                   pra 'Onde parei' / 'Proximo passo' e um
                                   icone de clique no botao Retomar
3) nova-sessao-destaque.png     — celular com o botao 'Nova sessão' destacado

Uso: python anotar_tela02.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

import build as b

ROOT = b.ROOT
PROJ = b.PROJ
FIGMA = b.FIGMA
SCREENSHOTS = b.SCREENSHOTS
OUT_DIR = PROJ / "docs" / "screenshots"

W, H = 1920, 1080

# Posicoes nativas (do get_metadata, node 43:11 / 49:29 do Figma, frame 390x844)
NATIVE_W, NATIVE_H = 390, 844
CARD = (24, 128, 342, 175)          # Card/ContinuarDaqui
NOVA_SESSAO = (24, 319, 342, 56)    # Botão "Nova sessão"
ONDE = (17.5, 46.5, 307, 21)        # dentro do card
PROX = (17.5, 75.5, 307, 21)
BOTAO_RETOMAR = (17.5, 104.5, 109, 53)

# Mesmos parametros de celular do slide 6 (build.slide_06)
PHONE_TOP, PHONE_LEFT, PHONE_HEIGHT, PHONE_ROTATE = 120, 1200, 860, 4
PHONE_BORDER = 14
PHONE_WIDTH = int(PHONE_HEIGHT * NATIVE_W / NATIVE_H)
_c_w = PHONE_WIDTH - 2 * PHONE_BORDER
_c_h = PHONE_HEIGHT - 2 * PHONE_BORDER
_scale = _c_h / NATIVE_H
_rendered_w = NATIVE_W * _scale
_crop_x = (_rendered_w - _c_w) / 2


def to_box(x, y, w, h):
    """Converte coordenada nativa (frame 390x844) pra coordenada dentro do
    conteudo do .phone (que usa object-fit:cover e corta um pouco as laterais)."""
    return (x * _scale - _crop_x, y * _scale, w * _scale, h * _scale)


def phone_with_highlight(src_path, hi_box, hi_color=None):
    hi_color = hi_color or b.ROSA
    hx, hy, hw, hh = hi_box
    return f'''<div class="phone" style="top:{PHONE_TOP}px; left:{PHONE_LEFT}px; width:{PHONE_WIDTH}px;
      height:{PHONE_HEIGHT}px; transform: rotate({PHONE_ROTATE}deg);">
      <img src="{b.img_src(src_path)}" />
      <div style="position:absolute; top:{hy}px; left:{hx}px; width:{hw}px; height:{hh}px;
        border-radius:16px; border:4px solid {hi_color}; box-shadow:0 0 0 6px rgba(236,111,168,0.22);"></div>
      </div>'''


def render(body, out_path):
    html = f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>{b.STYLE_CSS}</style>
</head>
<body>
<div class="slide bg-noite">
{body}
</div>
</body></html>"""
    html_path = ROOT / "_tmp_anotar.html"
    html_path.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": W, "height": H})
        page.goto(b.img_src(html_path))
        page.wait_for_timeout(150)
        page.screenshot(path=str(out_path))
        browser.close()
    html_path.unlink()
    print("Gerado:", out_path)


# ---------------------------------------------------------------------------
# 1) Celular com o card "Continuar daqui" destacado
# ---------------------------------------------------------------------------

def build_celular_continuar():
    body = b.header("NA PRÁTICA", "eyebrow-estrela", "Continuar<br>daqui", "noite")
    body += b.bg_circle(150, 1080, 700, b.FORMA_NOITE, 0.7)
    body += phone_with_highlight(SCREENSHOTS / "tela-02-inicio.png", to_box(*CARD))
    body += b.sparkle(120, 1850, 26, b.ESTRELA)
    body += b.sparkle(980, 1150, 22, "#FFFFFF")
    render(body, OUT_DIR / "tela-02-inicio-destaque.png")


# ---------------------------------------------------------------------------
# 2) Balao "Continuar daqui" ampliado, com setas e icone de clique
# ---------------------------------------------------------------------------

def build_balao():
    body = b.header("NA PRÁTICA", "eyebrow-estrela", "Onde parei e<br>próximo passo", "noite")

    card_scale = 1.85
    cw, ch = CARD[2] * card_scale, CARD[3] * card_scale
    card_left, card_top = 980, 320

    body += b.bg_circle(-150, 1550, 650, b.FORMA_NOITE, 0.6)

    body += f'''<div class="card-float borda-rosa" style="top:{card_top}px; left:{card_left}px;
      width:{cw}px; height:{ch}px; padding:0; overflow:hidden;">
      <img src="{b.img_src(FIGMA / "card-continuar-daqui.png")}" style="width:100%; height:100%; display:block;" />
      </div>'''

    def inner(box):
        x, y, w, h = box
        return (card_left + x * card_scale, card_top + y * card_scale, w * card_scale, h * card_scale)

    onde = inner(ONDE)
    prox = inner(PROX)
    botao = inner(BOTAO_RETOMAR)

    hand_size = 56
    body += b.icon_badge(
        botao[1] + botao[3] - hand_size / 2, botao[0] + botao[2] - hand_size / 2,
        hand_size, "hand-click", b.ROSA, "#FFFFFF", 28,
    )

    label_x = card_left + cw + 40

    def callout(box, text, color):
        x, y, w, h = box
        cy = y + h / 2
        out = b.dashed_line_between(card_left + cw - 6, cy, label_x - 16, cy, color, width=3)
        out += f'''<div style="position:absolute; top:{cy - 22}px; left:{label_x}px; width:260px;
          font-family:'Lexend'; font-weight:700; font-size:27px; color:{color}; line-height:1.2;">{text}</div>'''
        return out

    body += callout(onde, "Onde parei", "#FFFFFF")
    body += callout(prox, "Próximo passo", "#FFFFFF")
    body += callout(botao, "Retomar — 1 toque", b.ROSA)

    body += b.sparkle(220, 1780, 30, b.ESTRELA)
    body += b.sparkle(860, 1120, 24, "#FFFFFF")
    body += b.sparkle(900, 1850, 22, b.ROSA)

    render(body, OUT_DIR / "continuar-daqui-balao.png")


# ---------------------------------------------------------------------------
# 3) Celular com o botao "Nova sessão" destacado
# ---------------------------------------------------------------------------

def build_nova_sessao():
    body = b.header("NA PRÁTICA", "eyebrow-rosa", "Começar uma<br>tarefa nova", "noite")
    body += b.bg_circle(150, 1080, 700, b.FORMA_NOITE, 0.7)
    body += phone_with_highlight(SCREENSHOTS / "tela-02-inicio.png", to_box(*NOVA_SESSAO))
    body += b.card(500, 960, "Nova sessão →", rotate_deg=-3, extra_class="borda-rosa")
    body += b.sparkle(120, 1850, 26, b.ESTRELA)
    body += b.sparkle(980, 1150, 22, "#FFFFFF")
    render(body, OUT_DIR / "nova-sessao-destaque.png")


if __name__ == "__main__":
    build_celular_continuar()
    build_balao()
    build_nova_sessao()
