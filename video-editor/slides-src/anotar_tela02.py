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


def phone_geometry(height):
    """Pra um celular de uma certa altura: largura (mesma proporcao 390x844),
    escala e corte horizontal do object-fit:cover por dentro da moldura."""
    width = int(height * NATIVE_W / NATIVE_H)
    c_w = width - 2 * PHONE_BORDER
    c_h = height - 2 * PHONE_BORDER
    scale = c_h / NATIVE_H
    rendered_w = NATIVE_W * scale
    crop_x = (rendered_w - c_w) / 2
    return width, scale, crop_x


PHONE_WIDTH, _scale, _crop_x = phone_geometry(PHONE_HEIGHT)


def to_box(x, y, w, h, height=PHONE_HEIGHT):
    """Converte coordenada nativa (frame 390x844) pra coordenada dentro do
    conteudo do .phone (que usa object-fit:cover e corta um pouco as laterais)."""
    _, scale, crop_x = phone_geometry(height) if height != PHONE_HEIGHT else (None, _scale, _crop_x)
    return (x * scale - crop_x, y * scale, w * scale, h * scale)


def phone_with_highlight(src_path, hi_box, hi_color=None, top=PHONE_TOP, left=PHONE_LEFT,
                          height=PHONE_HEIGHT, rotate_deg=PHONE_ROTATE):
    hi_color = hi_color or b.ROSA
    width = phone_geometry(height)[0]
    hx, hy, hw, hh = hi_box
    return f'''<div class="phone" style="top:{top}px; left:{left}px; width:{width}px;
      height:{height}px; transform: rotate({rotate_deg}deg);">
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


# ---------------------------------------------------------------------------
# 4) As duas imagens (1 e 2) juntas, como fundo de um unico slide 1920x1080
# ---------------------------------------------------------------------------

def build_slide_continuar_completo():
    phone_h = 620
    phone_left, phone_top = 130, 260
    phone_w = phone_geometry(phone_h)[0]

    card_scale = 2.0
    cw, ch = CARD[2] * card_scale, CARD[3] * card_scale
    card_left, card_top = 640, 330

    hi_box = to_box(*CARD, height=phone_h)
    hi_left = phone_left + hi_box[0]
    hi_top = phone_top + hi_box[1]
    hi_w, hi_h = hi_box[2], hi_box[3]

    body = ""
    body += b.bg_circle(-180, 1500, 700, b.FORMA_NOITE, 0.55)

    body += f'''<div style="position:absolute; top:52px; left:120px; font-family:'Lexend'; font-weight:600;
      font-size:28px; letter-spacing:0.1em; text-transform:uppercase; color:{b.ESTRELA};">NA PRÁTICA</div>'''
    body += f'''<div style="position:absolute; top:92px; left:120px; font-family:'Lexend'; font-weight:700;
      font-size:72px; color:#FFFFFF;">Continuar daqui</div>'''

    body += phone_with_highlight(
        SCREENSHOTS / "tela-02-inicio.png", to_box(*CARD, height=phone_h),
        top=phone_top, left=phone_left, height=phone_h,
    )

    # linhas "lupa" ligando o destaque no celular ao balao ampliado
    body += b.dashed_line_between(hi_left + hi_w, hi_top, card_left, card_top, b.ROSA, width=3)
    body += b.dashed_line_between(hi_left + hi_w, hi_top + hi_h, card_left, card_top + ch, b.ROSA, width=3)

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

    hand_size = 60
    body += b.icon_badge(
        botao[1] + botao[3] - hand_size / 2, botao[0] + botao[2] - hand_size / 2,
        hand_size, "hand-click", b.ROSA, "#FFFFFF", 30,
    )

    label_x = card_left + cw + 50

    def callout(box, text, color):
        x, y, w, h = box
        cy = y + h / 2
        out = b.dashed_line_between(card_left + cw - 6, cy, label_x - 16, cy, color, width=3)
        out += f'''<div style="position:absolute; top:{cy - 22}px; left:{label_x}px; width:300px;
          font-family:'Lexend'; font-weight:700; font-size:30px; color:{color}; line-height:1.2;">{text}</div>'''
        return out

    body += callout(onde, "Onde parei", "#FFFFFF")
    body += callout(prox, "Próximo passo", "#FFFFFF")
    body += callout(botao, "Retomar — 1 toque", b.ROSA)

    body += b.sparkle(140, 1800, 30, b.ESTRELA)
    body += b.sparkle(960, 1750, 24, b.ROSA)
    body += b.sparkle(980, 160, 22, "#FFFFFF")

    render(body, OUT_DIR / "continuar-daqui-slide-completo.png")


# ---------------------------------------------------------------------------
# 5) Tela 03 - Escolher tarefa: tarefas recentes + indicadores de tempo
# ---------------------------------------------------------------------------

# Posicoes nativas da tela 03 (do get_metadata, node 43:31 / 50:43), 1o card da lista
CARD1 = (24, 283, 342, 76)       # Card/Tarefa "Estatística — cap. 3" (destaque)
NOME_ROW = (41, 300, 308, 21)    # texto do nome da tarefa, dentro do card
TEMPO_ROW = (41, 325, 308, 17)   # texto "última vez: X min", dentro do card


def build_slide_tarefas_recentes():
    # layout igual ao slide-06: titulo na coluna esquerda, celular a direita
    body = b.header("NA PRÁTICA", "eyebrow-estrela", "Tarefas<br>recentes", "noite")
    body += b.bg_circle(150, 1080, 700, b.FORMA_NOITE, 0.7)

    hi_box = to_box(*CARD1)
    body += phone_with_highlight(
        FIGMA / "tela-03-escolher-tarefa.png", hi_box, hi_color="#FFFFFF",
    )

    nome_x, nome_y, nome_w, nome_h = to_box(*NOME_ROW)
    nome_target = (PHONE_LEFT + nome_x, PHONE_TOP + nome_y + nome_h / 2)
    tempo_x, tempo_y, tempo_w, tempo_h = to_box(*TEMPO_ROW)
    tempo_target = (PHONE_LEFT + tempo_x, PHONE_TOP + tempo_y + tempo_h / 2)

    # indicador 1: nome da tarefa
    label1_left, label1_top, label1_w = 130, 430, 360
    label1_cy = label1_top + 20
    body += b.dashed_line_between(label1_left + label1_w, label1_cy, *nome_target, "#FFFFFF", width=3)
    body += f'''<div style="position:absolute; top:{label1_top}px; left:{label1_left}px; width:{label1_w}px;
      font-family:'Lexend'; font-weight:700; font-size:34px; color:#FFFFFF;">Nome da tarefa</div>'''

    # indicador 2: tempo que levou da ultima vez
    label2_left, label2_top, label2_w = 130, 560, 460
    label2_cy = label2_top + 35
    body += b.dashed_line_between(label2_left + label2_w, label2_cy, *tempo_target, b.ESTRELA, width=3)
    body += f'''<div style="position:absolute; top:{label2_top}px; left:{label2_left}px; width:{label2_w}px;
      font-family:'Lexend'; font-weight:700; font-size:28px; color:{b.ESTRELA}; line-height:1.3;">
      Tempo que levou para executar na última vez</div>'''

    # balao a parte, sem seta, so uma observacao flutuante (igual ao "Retomar →" do slide-06)
    body += b.card(750, 170, b.icon("history", b.ROSA, 30) + "Não precisa digitar novamente",
                   rotate_deg=-3, extra_class="borda-rosa", width=460)

    body += b.sparkle(120, 1850, 26, b.ESTRELA)
    body += b.sparkle(980, 1150, 22, "#FFFFFF")

    render(body, OUT_DIR / "tela-03-tarefas-recentes-slide.png")


if __name__ == "__main__":
    build_celular_continuar()
    build_balao()
    build_nova_sessao()
    build_slide_continuar_completo()
    build_slide_tarefas_recentes()
