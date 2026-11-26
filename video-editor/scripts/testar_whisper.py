"""Teste rápido do faster-whisper: carrega o modelo 'tiny' e transcreve o áudio de teste.

Decodifica o áudio com o FFmpeg (em vez de deixar o faster-whisper usar o PyAV
internamente) porque a versão do PyAV compatível com Python 3.14 removeu o
argumento 'metadata_errors' que o faster-whisper ainda usa.
"""
from faster_whisper import WhisperModel
import numpy as np
import subprocess
import os

ENTRADA = os.path.join(os.path.dirname(__file__), "..", "entrada", "sample.mp4")
FFMPEG = r"C:\Users\Paloma\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.1-full_build\bin\ffmpeg.exe"


def carregar_audio(caminho, sr=16000):
    cmd = [FFMPEG, "-i", caminho, "-f", "f32le", "-ar", str(sr), "-ac", "1", "-"]
    out = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype=np.float32)


print("Decodificando áudio via FFmpeg...")
audio = carregar_audio(ENTRADA)

print("Carregando modelo 'tiny' (download na primeira vez)...")
model = WhisperModel("tiny", device="cpu", compute_type="int8")

segments, info = model.transcribe(audio, language=None)
print(f"Idioma detectado: {info.language} (confianca {info.language_probability:.2f})")

count = 0
for seg in segments:
    count += 1
    print(f"[{seg.start:.1f}s -> {seg.end:.1f}s] {seg.text}")

print(f"OK: faster-whisper funcionando. {count} segmento(s) retornado(s) (video de teste nao tem fala real, por isso pode vir vazio).")
