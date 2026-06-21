import os

# configura pygame para modo sem janela antes de qualquer importação de src/
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
