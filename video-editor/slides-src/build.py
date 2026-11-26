"""Monta e renderiza os slides do video pitch (HTML/CSS -> PNG 1920x1080) via Playwright.

Uso:
  python build.py style-test      # so os slides 5 e 10 (teste de estilo)
  python build.py all             # os 11 slides
  python build.py contact-sheet   # grade com os PREVIEW dos 11 (depois de 'all')
"""
import os
import sys
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
PROJ = ROOT.parent.parent
SCREENSHOTS = PROJ / "docs" / "screenshots"
FIGMA = ROOT.parent / "entrada" / "figma"
ICONS = ROOT / "icons"
OUT_FINAL = ROOT.parent / "entrada" / "slides"
OUT_PREVIEW = OUT_FINAL / "preview"
STYLE_CSS = (ROOT / "style.css").read_text(encoding="utf-8")

W, H = 1920, 1080

# cores
CREME = "#FFF8EC"
NOITE = "#1B1846"
INDIGO = "#3730A3"
ESTRELA = "#FFD43B"
ROSA = "#EC6FA8"
TEXTO = "#1B1846"
TEXTO_SEC = "#5A5784"
FORMA_CREME = ["#EEEDFE", "#FFF3BF", "#FBEAF0"]
FORMA_NOITE = "#2E2A6E"


def icon(name, color, size=36):
    svg = (ICONS / f"{name}.svg").read_text(encoding="utf-8")
    svg = re.sub(r'width="\d+"', f'width="{size}"', svg, count=1)
    svg = re.sub(r'height="\d+"', f'height="{size}"', svg, count=1)
    return f'<span class="icon-inline" style="color:{color}">{svg}</span>'


def img_src(path: Path) -> str:
    return "file:///" + str(path.resolve()).replace("\\", "/")


def phone(src_path: Path, top, left, height, rotate_deg=0, width=None):
    w = width or int(height * 390 / 844)
    return f'''<div class="phone" style="top:{top}px; left:{left}px; width:{w}px; height:{height}px; transform: rotate({rotate_deg}deg);">
      <img src="{img_src(src_path)}" />
    </div>'''


def card(top, left, html, rotate_deg=0, extra_class="", width=None):
    w_style = f"width:{width}px;" if width else ""
    return f'''<div class="card-float {extra_class}" style="top:{top}px; left:{left}px; {w_style} transform: rotate({rotate_deg}deg);">
      {html}
    </div>'''


def bg_circle(top, left, size, color, opacity=1):
    return f'<div class="bg-circle" style="top:{top}px; left:{left}px; width:{size}px; height:{size}px; background:{color}; opacity:{opacity};"></div>'


def sparkle(top, left, size, color):
    return f'<div class="sparkle" style="top:{top}px; left:{left}px; width:{size}px; height:{size}px;">{icon_raw("star-filled", color, size)}</div>'


def icon_raw(name, color, size):
    svg = (ICONS / f"{name}.svg").read_text(encoding="utf-8")
    svg = re.sub(r'width="\d+"', f'width="{size}"', svg, count=1)
    svg = re.sub(r'height="\d+"', f'height="{size}"', svg, count=1)
    return f'<span style="color:{color}; display:block;">{svg}</span>'


def mascot_area(top, left, preview, on_noite=False):
    cls = "mascot-area preview" + (" on-noite" if on_noite else "") if preview else "mascot-area"
    label = "mascote" if preview else ""
    return f'<div class="{cls}" style="top:{top}px; left:{left}px;">{label}</div>'


def header(eyebrow_text, eyebrow_color_cls, title_text, bg, subtitle_text=None):
    title_cls = "title-noite" if bg == "noite" else "title-creme"
    sub_cls = "subtitle-noite" if bg == "noite" else "subtitle-creme"
    sub_html = f'<div class="subtitle {sub_cls}">{subtitle_text}</div>' if subtitle_text else ""
    return f'''<div class="header">
      <div class="eyebrow {eyebrow_color_cls}">{eyebrow_text}</div>
      <div class="title {title_cls}">{title_text}</div>
      {sub_html}
    </div>'''


# ---------------------------------------------------------------------------
# Definicao dos slides (so 5 e 10 por enquanto, para o teste de estilo)
# ---------------------------------------------------------------------------

def slide_05(preview):
    body = header(
        "A SOLUÇÃO", "eyebrow-rosa",
        "O Lume mede,<br>não cobra.", "creme",
        "Cronômetro progressivo: sem prazo, sem alarme.",
    )
    body += bg_circle(140, 1040, 760, FORMA_CREME[0])
    body += phone(SCREENSHOTS / "tela-04-sessao.png", 130, 1240, 860, rotate_deg=-5)
    body += card(230, 1120, "última vez · 42 min", rotate_deg=-3)
    body += card(430, 1660, icon("bell-off", INDIGO, 34) + "sem alarme", rotate_deg=3)
    body += card(760, 1130, "Onde parei · Exercícios 4 a 6", rotate_deg=-2, extra_class="borda-rosa", width=460)
    body += sparkle(90, 1700, 44, ESTRELA)
    body += sparkle(980, 1120, 30, ROSA)
    body += sparkle(680, 1860, 26, ESTRELA)
    return body


def slide_10(preview):
    body = header("O DIFERENCIAL", "eyebrow-estrela", "Sem contagem<br>regressiva.", "noite")

    def diff_card(top, left, icon_name, bg_color, text_color, title_txt, sub_txt):
        return f'''<div class="card-float" style="top:{top}px; left:{left}px; width:460px; height:200px; background:{bg_color}; flex-direction:column; align-items:flex-start; justify-content:center; gap:10px;">
          {icon(icon_name, text_color, 40)}
          <div style="font-weight:700; font-size:34px; color:{text_color};">{title_txt}</div>
          <div style="font-weight:400; font-size:24px; color:{text_color}; opacity:0.85;">{sub_txt}</div>
        </div>'''

    body += diff_card(470, 120, "clock", ESTRELA, "#1B1846", "Cronômetro progressivo", "mede, não cobra")
    body += diff_card(470, 640, "history", "#FFFFFF", "#1B1846", "Histórico por tarefa", "melhora no seu ritmo")
    body += diff_card(730, 120, "bell", "#FFFFFF", "#1B1846", "Lembrar depois", "a outra tarefa fica guardada")
    body += diff_card(730, 640, "player-play", ROSA, "#1B1846", "Continuar daqui", "retomar em 1 toque")
    body += bg_circle(-200, 1500, 700, FORMA_NOITE, 0.6)
    body += sparkle(140, 1250, 36, ESTRELA)
    body += sparkle(300, 1680, 26, "#FFFFFF")
    body += mascot_area(500, 1430, preview, on_noite=True)
    return body


def dashed_line_between(x1, y1, x2, y2, color, width=3):
    import math
    length = math.hypot(x2 - x1, y2 - y1)
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return f'''<div style="position:absolute; top:{y1}px; left:{x1}px; width:{length}px; height:0;
      border-top:{width}px dashed {color}; transform: rotate({angle}deg); transform-origin: left center;"></div>'''


def icon_badge(top, left, size, icon_name, bg_color, icon_color, icon_size=44):
    return f'''<div style="position:absolute; top:{top}px; left:{left}px; width:{size}px; height:{size}px; border-radius:50%;
      background:{bg_color}; display:flex; align-items:center; justify-content:center; box-shadow:0 16px 32px -8px rgba(27,24,70,.25);">
      {icon(icon_name, icon_color, icon_size)}
      </div>'''


def big_card(top, left, width, height, bg_color, html, rotate_deg=0):
    return f'''<div style="position:absolute; top:{top}px; left:{left}px; width:{width}px; height:{height}px; border-radius:28px;
      background:{bg_color}; box-shadow:0 24px 48px -16px rgba(27,24,70,.22); transform: rotate({rotate_deg}deg);
      display:flex; flex-direction:column; align-items:flex-start; justify-content:center; padding:0 44px; gap:14px;">
      {html}
      </div>'''


def logo_lume(top, left, size=220, color=ESTRELA):
    return f'''<div style="position:absolute; top:{top}px; left:{left}px; font-family:'Sniglet',sans-serif; font-weight:800; font-size:{size}px; color:{color}; line-height:1;">Lume</div>'''


import random as _random


def star_field(seed, n, x0, x1, y0, y1, color, size_range=(8, 22), avoid=None):
    rnd = _random.Random(seed)
    out = ""
    for _ in range(n):
        x = rnd.randint(x0, x1)
        y = rnd.randint(y0, y1)
        if avoid and avoid[0] <= x <= avoid[2] and avoid[1] <= y <= avoid[3]:
            continue
        s = rnd.randint(*size_range)
        out += sparkle(y, x, s, color)
    return out


# ---------------------------------------------------------------------------
# Slide 1
# ---------------------------------------------------------------------------

def slide_01(preview):
    body = ""
    body += star_field(1, 28, 60, 1900, 40, 1040, ESTRELA, (6, 16), avoid=(1300, 250, 1920, 950))
    body += logo_lume(400, 160, 220, ESTRELA)
    body += f'<div class="subtitle subtitle-noite" style="position:absolute; top:640px; left:168px; font-size:40px;">foque no seu ritmo</div>'
    body += mascot_area(330, 1460, preview, on_noite=True)
    return body


# ---------------------------------------------------------------------------
# Slide 2
# ---------------------------------------------------------------------------

def slide_02(preview):
    body = header("O PROBLEMA", "eyebrow-rosa", "Estudar sozinho<br>é difícil", "creme")
    body += dashed_line_between(1375, 600, 1565, 630, TEXTO_SEC)
    body += dashed_line_between(1735, 600, 1565, 630, TEXTO_SEC)
    body += icon_badge(360, 1300, 150, "home", "#FFFFFF", INDIGO, 56)
    body += f'<div class="subtitle subtitle-creme" style="position:absolute; top:525px; left:1290px; width:170px; text-align:center; font-size:26px;">em casa</div>'
    body += icon_badge(630, 1480, 170, "device-laptop", ROSA, "#FFFFFF", 64)
    body += f'<div class="subtitle subtitle-creme" style="position:absolute; top:815px; left:1455px; width:220px; text-align:center; font-size:26px;">no notebook</div>'
    body += icon_badge(360, 1660, 150, "device-mobile", "#FFFFFF", INDIGO, 56)
    body += f'<div class="subtitle subtitle-creme" style="position:absolute; top:525px; left:1650px; width:170px; text-align:center; font-size:26px;">no celular</div>'
    body += card(180, 1480, icon("bell", ROSA, 32) + "3 tarefas paralelas", rotate_deg=-3)
    body += sparkle(140, 1250, 28, ESTRELA)
    body += sparkle(900, 1750, 24, ROSA)
    return body


# ---------------------------------------------------------------------------
# Slide 3
# ---------------------------------------------------------------------------

def slide_03(preview):
    body = header("PARA QUEM", "eyebrow-rosa", "Para quem é<br>o Lume", "creme")
    cols = [
        (120, "school", "EAD"),
        (690, "briefcase", "Home office"),
        (1260, "language", "Idiomas"),
    ]
    for left, ic, label in cols:
        bg = ESTRELA if ic == "briefcase" else "#FFFFFF"
        body += big_card(500, left, 540, 280, bg, (
            icon(ic, INDIGO, 52) +
            f'<div style="font-weight:700; font-size:38px; color:{TEXTO};">{label}</div>'
        ))
    body += card(840, 560, "30 min a 1h para retomar", rotate_deg=-2, extra_class="borda-rosa", width=820)
    body += sparkle(440, 1780, 30, ESTRELA)
    body += sparkle(1000, 150, 24, ROSA)
    return body


# ---------------------------------------------------------------------------
# Slide 4
# ---------------------------------------------------------------------------

def slide_04(preview):
    body = header("O PROBLEMA", "eyebrow-rosa", "Contagem regressiva<br>gera ansiedade", "creme")
    body += f'''<div style="position:absolute; top:430px; left:1180px; width:560px; height:560px; border-radius:50%;
      border:28px solid #E4E1F0;"></div>'''
    body += f'''<div style="position:absolute; top:620px; left:1180px; width:560px; text-align:center;
      font-family:'Lexend',sans-serif; font-weight:700; font-size:120px; color:#8A87A6; letter-spacing:0.04em;">25:00</div>'''
    body += card(300, 1420, icon("bell-off", "#8A87A6", 32) + "o tempo acabou…", rotate_deg=3)
    body += sparkle(900, 1680, 26, ROSA)
    return body


# ---------------------------------------------------------------------------
# Slide 6
# ---------------------------------------------------------------------------

def slide_06(preview):
    body = header("NA PRÁTICA", "eyebrow-estrela", "Vamos ver<br>na prática", "noite")
    body += bg_circle(150, 1080, 700, FORMA_NOITE, 0.7)
    body += phone(SCREENSHOTS / "tela-02-inicio.png", 120, 1200, 860, rotate_deg=4)
    body += card(430, 1080, "Retomar →", rotate_deg=-3, extra_class="borda-rosa")
    body += mascot_area(640, 150, preview, on_noite=True)
    body += sparkle(120, 1850, 26, ESTRELA)
    body += sparkle(980, 1150, 22, "#FFFFFF")
    return body


# ---------------------------------------------------------------------------
# Slide 7
# ---------------------------------------------------------------------------

def slide_07(preview):
    body = header("UI", "eyebrow-rosa", "Cada cor tem<br>uma função", "creme")
    body += f'''<div style="position:absolute; top:430px; left:120px; width:820px; border-radius:28px; overflow:hidden;
      box-shadow:0 24px 48px -16px rgba(27,24,70,.22);">
      <img src="{img_src(FIGMA / 'paleta.png')}" style="width:100%; display:block;" />
      </div>'''

    def color_tag(top, dot_color, label):
        return f'''<div style="position:absolute; top:{top}px; left:1040px; display:flex; align-items:center; gap:18px;">
          <div style="width:44px; height:44px; border-radius:50%; background:{dot_color};"></div>
          <div style="font-weight:600; font-size:30px; color:{TEXTO};">{label}</div>
          </div>'''

    body += color_tag(460, INDIGO, "Ação")
    body += color_tag(560, ESTRELA, "Progresso")
    body += color_tag(660, ROSA, "Retomar")
    body += big_card(770, 1040, 640, 170, "#FFFFFF", (
        f'<div style="font-family:\'Lexend\'; font-weight:700; font-size:40px; color:{TEXTO};">Aa</div>'
        f'<div style="font-weight:400; font-size:26px; color:{TEXTO_SEC};">Lexend — leitura fácil</div>'
    ))
    body += sparkle(360, 1700, 28, ESTRELA)
    return body


# ---------------------------------------------------------------------------
# Slide 8
# ---------------------------------------------------------------------------

def slide_08(preview):
    body = header("COMPONENTES", "eyebrow-rosa", "Um ajuste,<br>sete telas", "creme")
    body += f'''<div style="position:absolute; top:480px; left:120px; width:760px; border-radius:24px; overflow:hidden;
      box-shadow:0 24px 48px -16px rgba(27,24,70,.22);">
      <img src="{img_src(FIGMA / 'botao-variantes.png')}" style="width:100%; display:block;" />
      </div>'''
    body += f'<div style="position:absolute; top:640px; left:940px; transform:rotate(18deg);">{icon("arrow-right", INDIGO, 64)}</div>'
    body += phone(SCREENSHOTS / "tela-02-inicio.png", 300, 1120, 560, rotate_deg=-8)
    body += phone(SCREENSHOTS / "tela-04-sessao.png", 260, 1350, 600, rotate_deg=3)
    body += phone(SCREENSHOTS / "tela-06-concluida.png", 300, 1600, 560, rotate_deg=12)
    body += sparkle(900, 1150, 24, ESTRELA)
    return body


# ---------------------------------------------------------------------------
# Slide 9
# ---------------------------------------------------------------------------

def slide_09(preview):
    body = header("ACESSIBILIDADE", "eyebrow-rosa", "Acessível<br>por padrão", "creme")
    items = [
        (120, "contrast", "AA", "contraste WCAG"),
        (690, "hand-click", "48px", "área de toque"),
        (1260, "eye", "Cor + texto", "nada só por cor"),
    ]
    for left, ic, num, label in items:
        body += big_card(500, left, 540, 320, "#FFFFFF", (
            icon(ic, INDIGO, 52) +
            f'<div style="font-weight:700; font-size:40px; color:{TEXTO};">{num}</div>'
            f'<div style="font-weight:400; font-size:26px; color:{TEXTO_SEC};">{label}</div>'
        ))
    body += sparkle(440, 1780, 26, ESTRELA)
    body += sparkle(900, 150, 22, ROSA)
    return body


# ---------------------------------------------------------------------------
# Slide 11
# ---------------------------------------------------------------------------

def slide_11(preview):
    body = ""
    body += logo_lume(230, 150, 170, ESTRELA)
    body += f'<span style="position:absolute; top:255px; left:620px;">{icon("star-filled", ESTRELA, 70)}</span>'
    body += f'<div class="subtitle subtitle-noite" style="position:absolute; top:400px; left:158px; font-size:36px;">no seu ritmo</div>'
    body += big_card(540, 150, 560, 130, "#FFFFFF", (
        icon("brand-figma", INDIGO, 40) +
        f'<div style="font-weight:600; font-size:30px; color:{TEXTO};">Protótipo no Figma</div>'
    ))
    body += big_card(700, 150, 560, 130, "#FFFFFF", (
        icon("brand-github", INDIGO, 40) +
        f'<div style="font-weight:600; font-size:30px; color:{TEXTO};">GitHub</div>'
    ))
    body += f'''<div style="position:absolute; bottom:90px; left:158px; font-family:'Lexend'; font-weight:400; font-size:26px; color:#D9D6FF;">
      Paloma Ai Tsuchinaga · UniFECAF · UX/UI</div>'''
    body += star_field(11, 10, 60, 1900, 40, 980, ESTRELA, (6, 14), avoid=(1350, 250, 1920, 950))
    body += mascot_area(330, 1460, preview, on_noite=True)
    return body


SLIDE_BUILDERS = {
    1: slide_01, 2: slide_02, 3: slide_03, 4: slide_04, 5: slide_05,
    6: slide_06, 7: slide_07, 8: slide_08, 9: slide_09, 10: slide_10, 11: slide_11,
}
SLIDE_BG = {
    1: "noite", 2: "creme", 3: "creme", 4: "creme", 5: "creme",
    6: "noite", 7: "creme", 8: "creme", 9: "creme", 10: "noite", 11: "noite",
}


def render_slide(num, preview, out_dir):
    bg_cls = "bg-creme" if SLIDE_BG[num] == "creme" else "bg-noite"
    body = SLIDE_BUILDERS[num](preview)
    html = f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>{STYLE_CSS}</style>
</head>
<body>
<div class="slide {bg_cls}">
{body}
</div>
</body></html>"""
    html_path = ROOT / f"_tmp_slide_{num:02d}.html"
    html_path.write_text(html, encoding="utf-8")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"slide-{num:02d}.png"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": W, "height": H})
        page.goto(img_src(html_path))
        page.wait_for_timeout(150)
        page.screenshot(path=str(out_path))
        browser.close()
    html_path.unlink()
    print(f"Gerado: {out_path}")


def build_contact_sheet():
    from PIL import Image
    cols, rows = 3, 4
    tw, th = 480, 270
    pad = 10
    grid = Image.new("RGB", (cols * tw + (cols + 1) * pad, rows * th + (rows + 1) * pad), (230, 230, 230))
    for i in range(1, 12):
        p = OUT_PREVIEW / f"slide-{i:02d}.png"
        img = Image.open(p).convert("RGB").resize((tw, th))
        col, row = (i - 1) % cols, (i - 1) // cols
        grid.paste(img, (pad + col * (tw + pad), pad + row * (th + pad)))
    out = OUT_PREVIEW / "contact-sheet.png"
    grid.save(out)
    print(f"Gerado: {out}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "style-test"
    if mode == "style-test":
        for n in (5, 10):
            render_slide(n, preview=True, out_dir=OUT_PREVIEW)
    elif mode == "all":
        for n in range(1, 12):
            render_slide(n, preview=False, out_dir=OUT_FINAL)
            render_slide(n, preview=True, out_dir=OUT_PREVIEW)
    elif mode == "contact-sheet":
        build_contact_sheet()
    else:
        print("Modo nao implementado ainda:", mode)
