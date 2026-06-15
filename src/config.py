# Configurações centrais do jogo — ajustáveis para a apresentação.
# ====================================================================
# TELA
# ====================================================================
LARGURA_TELA = 800       # Largura da janela do jogo em pixels
ALTURA_TELA = 600        # Altura da janela do jogo em pixels
FPS = 60                 # Quadros por segundo (velocidade do jogo)

TITULO_JOGO = "Projeto Final - Pygame"

# ====================================================================
# CORES — cores fixas (não variam por estado)
# ====================================================================
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (212, 212, 212)

# ====================================================================
# CAMINHOS DE ARQUIVO
# ====================================================================
CAMINHO_RECORDE = "data/recorde.txt"       # Onde o recorde de sequência é salvo
CAMINHO_FONTE = "assets/fontes/Outfit-Bold.ttf"  # Fonte usada em todo o jogo
CAMINHO_PALAVRAS_4 = "data/palavras_4.txt"
CAMINHO_PALAVRAS_5 = "data/palavras_5.txt"
CAMINHO_PALAVRAS_6 = "data/palavras_6.txt"

# ====================================================================
# TERMO — configurações principais do jogo
# ====================================================================

# Número máximo de tentativas por partida (padrão: 6)
MAX_TENTATIVAS = 6

# ====================================================================
# CORES DO TERMO — aplique estas cores nas células e no teclado
# ====================================================================

# Cor de fundo da tela inteira (escuro)
FUNDO = (18, 18, 19)

# Verde: letra certa no lugar certo
VERDE = (83, 141, 78)

# Amarelo: letra certa no lugar errado
AMARELO = (181, 159, 59)

# Cinza: letra ausente da palavra
CINZA_CELULA = (58, 58, 60)

# Borda da célula ativa (linha sendo digitada)
BORDA_ATIVA = (154, 154, 154)

# Cor do texto (títulos, letras, instruções)
TEXTO = (255, 255, 255)

# Cor padrão das teclas do teclado virtual (não pressionadas ainda)
TECLA_PADRAO = (129, 131, 132)

# ====================================================================
# GRADE — tamanho e espaçamento das células
# ====================================================================

# Largura/altura de cada célula da grade em pixels (padrão: 60)
TAMANHO_CELULA = 60

# Espaço entre células em pixels (padrão: 6)
ESPACAMENTO_CELULA = 6