# `teste.py`

import tkinter as tk
from tkinter import filedialog
import os

from model.espera import Espera 

# ============================================================

# CORES

# ============================================================

BG = "#070A10"

PANEL = "#0D121B"
PANEL_2 = "#111824"

TEXT = "#E8EDF5"
MUTED = "#7E899C"
HOVER = "#182131"

TRANSPARENT = "#010101"

# ============================================================

# PLANETARIUM HUB

# ============================================================

class PlanetariumHub(tk.Tk):


    def __init__(self):

        super().__init__()

        self.player_espera = Espera() 

        self.title("Planetarium Hub")

        self.geometry("1400x800")

        self.minsize(
            1000,
            600
        )

        self.configure(
            bg=BG
        )

        # Transparência da área central
        self.attributes(
            "-transparentcolor",
            TRANSPARENT
        )

        # Nenhum vídeo selecionado inicialmente
        self.video_selecionado = None

        self.criar_interface()


# ========================================================
# INTERFACE PRINCIPAL
# ========================================================

def criar_interface(self):

    self.grid_rowconfigure(
        0,
        weight=1
    )

    self.grid_rowconfigure(
        1,
        weight=0
    )

    self.grid_columnconfigure(
        0,
        weight=0
    )

    self.grid_columnconfigure(
        1,
        weight=1
    )

    self.grid_columnconfigure(
        2,
        weight=0
    )

    self.criar_esquerda()

    self.criar_centro()

    self.criar_direita()

    self.criar_rodape()


# ========================================================
# ESQUERDA
# ========================================================

def criar_esquerda(self):

    self.esquerda = tk.Frame(
        self,
        bg=PANEL,
        width=210
    )

    self.esquerda.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    self.esquerda.grid_propagate(
        False
    )


    tk.Label(
        self.esquerda,
        text="PLANETARIUM",
        bg=PANEL,
        fg=MUTED,
        font=("Segoe UI", 9, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(25, 2)
    )


    tk.Label(
        self.esquerda,
        text="HUB",
        bg=PANEL,
        fg=TEXT,
        font=("Segoe UI", 20, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(0, 25)
    )


    opcoes = [
        ("🪐", "Planetário"),
        ("🎵", "Música"),
        ("🎬", "Vídeos"),
        ("🖼", "Imagens"),
        ("📁", "Arquivos")
    ]


    self.botoes_menu = []


    for icone, nome in opcoes:

        botao = tk.Button(
            self.esquerda,

            text=f"  {icone}   {nome}",

            anchor="w",

            bg=PANEL,
            fg=TEXT,

            activebackground=HOVER,
            activeforeground=TEXT,

            relief="flat",
            bd=0,

            cursor="hand2",

            font=("Segoe UI", 11),

            padx=14,
            pady=12,

            command=lambda nome=nome:
                self.selecionar_menu(nome)
        )

        botao.pack(
            fill="x",
            padx=10,
            pady=2
        )

        self.botoes_menu.append(
            botao
        )


    self.botoes_menu[0].configure(
        bg=HOVER
    )


# ========================================================
# CENTRO
# ========================================================

def criar_centro(self):

    self.centro = tk.Frame(
        self,
        bg=TRANSPARENT
    )

    self.centro.grid(
        row=0,
        column=1,
        sticky="nsew"
    )

    self.centro.grid_rowconfigure(
        0,
        weight=1
    )

    self.centro.grid_columnconfigure(
        0,
        weight=1
    )


# ========================================================
# DIREITA
# ========================================================

def criar_direita(self):

    self.direita = tk.Frame(
        self,
        bg=PANEL,
        width=285
    )

    self.direita.grid(
        row=0,
        column=2,
        sticky="nsew"
    )

    self.direita.grid_propagate(
        False
    )


    self.titulo_direita = tk.Label(
        self.direita,

        text="🪐  Planetário",

        bg=PANEL,
        fg=TEXT,

        font=("Segoe UI", 15, "bold")
    )

    self.titulo_direita.pack(
        anchor="w",
        padx=20,
        pady=(28, 20)
    )


    self.card_direita = tk.Frame(
        self.direita,
        bg=PANEL_2
    )

    self.card_direita.pack(
        fill="x",
        padx=16
    )


    self.mostrar_descricao(
        "Controle geral da sessão."
    )


# ========================================================
# LIMPAR PAINEL DIREITO
# ========================================================

def limpar_painel(self):

    for widget in self.card_direita.winfo_children():

        widget.destroy()


# ========================================================
# DESCRIÇÃO PADRÃO
# ========================================================

def mostrar_descricao(self, texto):

    self.limpar_painel()

    self.texto_direita = tk.Label(
        self.card_direita,

        text=texto,

        bg=PANEL_2,
        fg=MUTED,

        justify="left",
        anchor="w",

        font=("Segoe UI", 9),

        padx=15,
        pady=15
    )

    self.texto_direita.pack(
        fill="x"
    )


# ========================================================
# MODO ESPERA / VÍDEOS
# ========================================================

def mostrar_modo_espera(self):

    self.limpar_painel()


    self.video_label = tk.Label(
        self.card_direita,

        text="Nenhum vídeo selecionado.",

        bg=PANEL_2,
        fg=MUTED,

        justify="left",
        anchor="w",

        wraplength=220,

        font=("Segoe UI", 9),

        padx=15,
        pady=15
    )

    self.video_label.pack(
        fill="x"
    )


    botao_escolher = tk.Button(
        self.card_direita,

        text="📂  Escolher vídeo",

        command=self.escolher_video,

        bg=HOVER,
        fg=TEXT,

        activebackground=HOVER,
        activeforeground=TEXT,

        relief="flat",
        bd=0,

        cursor="hand2",

        font=("Segoe UI", 9, "bold"),

        padx=10,
        pady=10
    )

    botao_escolher.pack(
        fill="x",

        padx=15,
        pady=(10, 5)
    )


    botao_reproduzir = tk.Button(
        self.card_direita,

        text="▶  Reproduzir",

        command=self.reproduzir_video,

        bg=PANEL,
        fg=TEXT,

        activebackground=HOVER,
        activeforeground=TEXT,

        relief="flat",
        bd=0,

        cursor="hand2",

        font=("Segoe UI", 9, "bold"),

        padx=10,
        pady=10
    )

    botao_reproduzir.pack(
        fill="x",

        padx=15,
        pady=(5, 15)
    )


# ========================================================
# ESCOLHER VÍDEO
# ========================================================

def escolher_video(self):

    caminho = filedialog.askopenfilename(

        title="Escolher vídeo",

        filetypes=[
            (
                "Vídeos",
                "*.mp4 *.avi *.mkv *.mov"
            ),

            (
                "Todos os arquivos",
                "*.*"
            )
        ]
    )


    if not caminho:

        return


    self.video_selecionado = caminho


    nome_video = os.path.basename(
        caminho
    )


    self.video_label.configure(

        text=f"Vídeo selecionado:\n\n{nome_video}",

        fg=TEXT
    )


    print(
        "Vídeo selecionado:",
        caminho
    )


# ========================================================
# REPRODUZIR VÍDEO
# ========================================================

def reproduzir_video(self):
    if not self.video_selecionado:
        print("Nenhum vídeo selecionado.")
        return

    # ERRADO: sucesso = model.reproduzir_video(...)
    # CORRETO: Usa o objeto 'self.player_espera' que você criou no __init__
    sucesso = self.player_espera.reproduzir_video(self.video_selecionado)

    if sucesso:
        print("Vídeo enviado para reprodução.")


# ========================================================
# MENU
# ========================================================

def selecionar_menu(self, selecionado):

    for botao in self.botoes_menu:

        botao.configure(
            bg=PANEL
        )


    for botao in self.botoes_menu:

        if selecionado in botao.cget("text"):

            botao.configure(
                bg=HOVER
            )


    self.titulo_direita.configure(

        text=f"  {selecionado}"
    )


    descricoes = {

        "Planetário":
            "Controle geral da sessão.",

        "Música":
            "Controle de músicas e fontes externas.",

        "Vídeos":
            "Navegação pelos vídeos disponíveis.",

        "Imagens":
            "Seleção de imagens e PNGs.",

        "Arquivos":
            "Scripts, apresentações e arquivos."
    }


    if selecionado == "Vídeos":

        self.mostrar_modo_espera()

    else:

        self.mostrar_descricao(

            descricoes.get(
                selecionado,
                ""
            )
        )


# ========================================================
# STELLARIUM
# ========================================================

def abrir_stellarium(self):

    pass


# ========================================================
# LIMPAR CENTRO
# ========================================================

def limpar_centro(self):

    for widget in self.centro.winfo_children():

        widget.destroy()


# ========================================================
# TELA CHEIA
# ========================================================

def tela_cheia(self):

    atual = self.attributes(
        "-fullscreen"
    )

    self.attributes(
        "-fullscreen",
        not atual
    )

# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    app = PlanetariumHub()

    app.mainloop()