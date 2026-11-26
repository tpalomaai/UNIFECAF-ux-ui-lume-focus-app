"""Teste de animacao do mascote (estrela do Lume) - apenas MoviePy + PIL, sem instalar nada novo.

Sequencia (~8s, 1080p, 24fps):
  0.0-0.8s  pop de entrada (Feliz): escala 0 -> 110% -> 100%
  0.8-2.7s  Feliz flutuando (sobe/desce 7px, ciclo de 2s)
  2.7-3.0s  fade curto para Focado
  3.0-5.2s  Focado flutuando
  5.2-5.5s  fade curto para Comemorando
  5.5-8.0s  Comemorando com pulinho (2 saltos amortecidos)

Fundo dividido: metade esquerda creme lunar #FFF8EC, metade direita noite #1B1846,
para comparar o mascote nos dois fundos do app ao mesmo tempo.
"""
import os
import math
import numpy as np
from PIL import Image
from moviepy import VideoClip

RAIZ = os.path.join(os.path.dirname(__file__), "..")
ENTRADA = os.path.join(RAIZ, "entrada", "mascote")
SAIDA = os.path.join(RAIZ, "saida")
os.makedirs(SAIDA, exist_ok=True)

W, H = 1920, 1080
FPS = 24
DURACAO = 8.0

CREME = (0xFF, 0xF8, 0xEC)
NOITE = (0x1B, 0x18, 0x46)

MASCOTE_H = 380  # altura de exibicao em px dentro de cada metade

# --- carrega e pre-redimensiona as 3 expressoes (RGBA) ---
def carregar(nome):
    img = Image.open(os.path.join(ENTRADA, f"{nome}.png")).convert("RGBA")
    w = int(img.width * (MASCOTE_H / img.height))
    return img.resize((w, MASCOTE_H), Image.LANCZOS)

EXPRESSOES = {nome: carregar(nome) for nome in ("feliz", "focado", "comemorando")}

# --- fundo estatico (metade creme / metade noite) ---
fundo = np.zeros((H, W, 3), dtype=np.uint8)
fundo[:, : W // 2] = CREME
fundo[:, W // 2 :] = NOITE
FUNDO_IMG = Image.fromarray(fundo, "RGB")

# limites de tempo
T_POP_FIM = 0.8
T_FADE1_INI, T_FADE1_FIM = 2.7, 3.0
T_FADE2_INI, T_FADE2_FIM = 5.2, 5.5
T_COMEMORA_INI = 5.5


def escala_pop(t):
    """0 -> 110% -> 100% nos primeiros 0.8s; 100% depois."""
    if t >= T_POP_FIM:
        return 1.0
    if t < 0.4:
        frac = t / 0.4
        return 1.1 * math.sin(frac * math.pi / 2)
    frac = (t - 0.4) / 0.4
    return 1.1 - 0.1 * frac


def flutuar_offset(t):
    """Flutuacao continua: +/-7px, ciclo de 2s."""
    return 7 * math.sin(2 * math.pi * t / 2.0)


def pulinho(t):
    """2 saltos amortecidos a partir do inicio da comemoracao. Retorna (offset_y, escala_extra)."""
    if t < T_COMEMORA_INI:
        return 0.0, 1.0
    dt = t - T_COMEMORA_INI
    amplitude = 55 * math.exp(-dt * 1.6)
    salto = abs(math.sin(2 * math.pi * dt / 0.7))
    offset_y = -amplitude * salto
    escala_extra = 1.0 + 0.04 * salto * math.exp(-dt * 1.2)
    return offset_y, escala_extra


def expressao_atual(t):
    """Retorna lista [(nome, peso_alpha)] -- 1 ou 2 entradas durante o crossfade."""
    if t < T_FADE1_INI:
        return [("feliz", 1.0)]
    if t < T_FADE1_FIM:
        frac = (t - T_FADE1_INI) / (T_FADE1_FIM - T_FADE1_INI)
        return [("feliz", 1 - frac), ("focado", frac)]
    if t < T_FADE2_INI:
        return [("focado", 1.0)]
    if t < T_FADE2_FIM:
        frac = (t - T_FADE2_INI) / (T_FADE2_FIM - T_FADE2_INI)
        return [("focado", 1 - frac), ("comemorando", frac)]
    return [("comemorando", 1.0)]


def montar_mascote_frame(t):
    """Compoe a imagem do mascote (com escala e fade) deste instante, como RGBA."""
    camadas = expressao_atual(t)
    offset_y_flutuar = flutuar_offset(t)
    offset_y_pulo, escala_pulo = pulinho(t)
    escala = escala_pop(t) * escala_pulo

    base = Image.new("RGBA", (MASCOTE_H + 40, MASCOTE_H + 40), (0, 0, 0, 0))
    for nome, peso in camadas:
        if peso <= 0:
            continue
        img = EXPRESSOES[nome]
        if escala != 1.0:
            nw, nh = max(1, int(img.width * escala)), max(1, int(img.height * escala))
            img = img.resize((nw, nh), Image.LANCZOS)
        if peso < 1.0:
            r, g, b, a = img.split()
            a = a.point(lambda v: int(v * peso))
            img = Image.merge("RGBA", (r, g, b, a))
        px = (base.width - img.width) // 2
        py = (base.height - img.height) // 2
        base.alpha_composite(img, (px, py))
    return base, offset_y_flutuar + offset_y_pulo


def make_frame(t):
    frame = FUNDO_IMG.copy()
    mascote, offset_y = montar_mascote_frame(t)

    for cx in (W // 4, 3 * W // 4):
        px = int(cx - mascote.width / 2)
        py = int(H / 2 - mascote.height / 2 + offset_y)
        frame.paste(mascote, (px, py), mascote)

    return np.array(frame.convert("RGB"))


if __name__ == "__main__":
    clip = VideoClip(make_frame, duration=DURACAO).with_fps(FPS)
    saida_video = os.path.join(SAIDA, "teste-mascote.mp4")
    clip.write_videofile(saida_video, codec="libx264", audio=False, logger=None)
    print(f"OK: video gerado em {saida_video}")

    # 4 frames: entrada (pop), flutuando, troca de expressao, comemoracao
    momentos = {
        "frame_entrada_pop.png": 0.3,
        "frame_flutuando.png": 1.8,
        "frame_troca_expressao.png": 3.0,
        "frame_comemoracao.png": 6.3,
    }
    for nome_arquivo, t in momentos.items():
        caminho = os.path.join(SAIDA, nome_arquivo)
        Image.fromarray(make_frame(t)).save(caminho)
        print(f"Frame salvo: {caminho} (t={t}s)")
