"""Teste rápido do MoviePy: carrega o vídeo, corta os primeiros 3s e extrai 4 frames."""
from moviepy import VideoFileClip
import os

ENTRADA = os.path.join(os.path.dirname(__file__), "..", "entrada", "sample.mp4")
SAIDA = os.path.join(os.path.dirname(__file__), "..", "saida")
os.makedirs(SAIDA, exist_ok=True)

clip = VideoFileClip(ENTRADA)
print(f"Duração: {clip.duration:.2f}s | Resolução: {clip.size} | FPS: {clip.fps}")

# corta os primeiros 3 segundos
sub = clip.subclipped(0, 3)
sub.write_videofile(os.path.join(SAIDA, "sample_cortado.mp4"), logger=None)

# extrai 4 frames espaçados ao longo do clipe original
for i, t in enumerate([0.5, 2, 4, 5.5]):
    frame_path = os.path.join(SAIDA, f"frame_{i}.png")
    clip.save_frame(frame_path, t=t)
    print(f"Frame salvo: {frame_path}")

clip.close()
sub.close()
print("OK: MoviePy funcionando.")
