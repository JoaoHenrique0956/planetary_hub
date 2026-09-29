# ============================================================
# montanha_russa.py
# ============================================================

import tkinter as tk
from tkinter import messagebox
import os
import ctypes


# ============================================================
# CONFIGURAÇÕES
# ============================================================

# ALTERE SEU CAMINHO PARA A PASTA DA MONTANHA-RUSSA
PASTA_VIDEOS = r"D:\planetary_hub\videos\montanha_russa"


EXTENSOES = (
    ".mp4",
    ".avi",
    ".mkv",
    ".mov",
    ".wmv",
    ".webm"
)


# ============================================================
# CORES
# ============================================================

BG = "#070A10"
PANEL = "#0D121B"
PANEL_2 = "#111824"

TEXT = "#E8EDF5"
MUTED = "#7E899C"
HOVER = "#182131"

ACCENT = "#4EA1FF"


# ============================================================
# MONTANHA-RUSSA
# ============================================================

class Montanha_Russa:

    def __init__(self, parent):

        self.parent = parent

        self.frame = tk.Frame(
            parent,
            bg=BG
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        self.criar_interface()

        self.carregar_videos()


    # ========================================================
    # INTERFACE
    # ========================================================

    def criar_interface(self):

        # ----------------------------------------------------
        # CABEÇALHO
        # ----------------------------------------------------

        header = tk.Frame(
            self.frame,
            bg=BG
        )

        header.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )


        titulo = tk.Label(
            header,
            text="🎢  MONTANHA-RUSSA",
            font=("Segoe UI", 20, "bold"),
            bg=BG,
            fg=TEXT
        )

        titulo.pack(
            anchor="w"
        )


        subtitulo = tk.Label(
            header,
            text="Selecione um vídeo para iniciar a apresentação",
            font=("Segoe UI", 10),
            bg=BG,
            fg=MUTED
        )

        subtitulo.pack(
            anchor="w",
            pady=(4, 0)
        )


        # ----------------------------------------------------
        # ÁREA PRINCIPAL
        # ----------------------------------------------------

        conteudo = tk.Frame(
            self.frame,
            bg=BG
        )

        conteudo.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )


        # ----------------------------------------------------
        # PAINEL DE VÍDEOS
        # ----------------------------------------------------

        painel = tk.Frame(
            conteudo,
            bg=PANEL
        )

        painel.pack(
            fill="both",
            expand=True
        )


        # ----------------------------------------------------
        # TÍTULO DA LISTA
        # ----------------------------------------------------

        topo = tk.Frame(
            painel,
            bg=PANEL
        )

        topo.pack(
            fill="x",
            padx=18,
            pady=15
        )


        tk.Label(
            topo,
            text="VÍDEOS DISPONÍVEIS",
            font=("Segoe UI", 10, "bold"),
            bg=PANEL,
            fg=MUTED
        ).pack(
            anchor="w"
        )


        # ----------------------------------------------------
        # LISTA
        # ----------------------------------------------------

        lista_container = tk.Frame(
            painel,
            bg=PANEL
        )

        lista_container.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=(0, 12)
        )


        self.canvas = tk.Canvas(
            lista_container,
            bg=PANEL,
            highlightthickness=0
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )


        scrollbar = tk.Scrollbar(
            lista_container,
            orient="vertical",
            command=self.canvas.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )


        self.canvas.configure(
            yscrollcommand=scrollbar.set
        )


        self.lista = tk.Frame(
            self.canvas,
            bg=PANEL
        )


        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.lista,
            anchor="nw"
        )


        self.lista.bind(
            "<Configure>",
            lambda event: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )


        self.canvas.bind(
            "<Configure>",
            self.ajustar_largura_lista
        )


        # ----------------------------------------------------
        # MOUSE WHEEL
        # ----------------------------------------------------

        self.canvas.bind_all(
            "<MouseWheel>",
            self.rolar
        )


    # ========================================================
    # AJUSTAR LARGURA DA LISTA
    # ========================================================

    def ajustar_largura_lista(self, event):

        self.canvas.itemconfig(
            self.canvas_window,
            width=event.width
        )


    # ========================================================
    # SCROLL
    # ========================================================

    def rolar(self, event):

        self.canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )


    # ========================================================
    # CARREGAR VÍDEOS
    # ========================================================

    def carregar_videos(self):

        for widget in self.lista.winfo_children():
            widget.destroy()


        # ----------------------------------------------------
        # VERIFICAR PASTA
        # ----------------------------------------------------

        if not os.path.exists(PASTA_VIDEOS):

            tk.Label(
                self.lista,
                text="Pasta de vídeos não encontrada.",
                font=("Segoe UI", 11),
                bg=PANEL,
                fg=MUTED
            ).pack(
                pady=30
            )

            return


        videos = []


        # ----------------------------------------------------
        # PROCURAR VÍDEOS
        # ----------------------------------------------------

        for arquivo in os.listdir(PASTA_VIDEOS):

            caminho = os.path.join(
                PASTA_VIDEOS,
                arquivo
            )


            if (
                os.path.isfile(caminho)
                and arquivo.lower().endswith(EXTENSOES)
            ):

                videos.append(caminho)


        videos.sort()


        # ----------------------------------------------------
        # NENHUM VÍDEO
        # ----------------------------------------------------

        if not videos:

            tk.Label(
                self.lista,
                text="Nenhum vídeo encontrado.",
                font=("Segoe UI", 11),
                bg=PANEL,
                fg=MUTED
            ).pack(
                pady=30
            )

            return


        # ----------------------------------------------------
        # CRIAR ITENS
        # ----------------------------------------------------

        for numero, caminho in enumerate(
            videos,
            start=1
        ):

            self.criar_item_video(
                numero,
                caminho
            )


    # ========================================================
    # ITEM DE VÍDEO
    # ========================================================

    def criar_item_video(
        self,
        numero,
        caminho
    ):

        nome = os.path.basename(
            caminho
        )


        item = tk.Frame(
            self.lista,
            bg=PANEL_2,
            height=70
        )

        item.pack(
            fill="x",
            padx=6,
            pady=5
        )

        item.pack_propagate(
            False
        )


        # ----------------------------------------------------
        # NÚMERO
        # ----------------------------------------------------

        numero_label = tk.Label(
            item,
            text=str(numero),
            font=("Segoe UI", 12, "bold"),
            bg=PANEL_2,
            fg=ACCENT,
            width=4
        )

        numero_label.pack(
            side="left",
            fill="y"
        )


        # ----------------------------------------------------
        # NOME
        # ----------------------------------------------------

        nome_label = tk.Label(
            item,
            text=nome,
            font=("Segoe UI", 11),
            bg=PANEL_2,
            fg=TEXT,
            anchor="w"
        )

        nome_label.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )


        # ----------------------------------------------------
        # BOTÃO
        # ----------------------------------------------------

        botao = tk.Button(
            item,
            text="▶  ABRIR",
            font=("Segoe UI", 9, "bold"),
            bg=PANEL_2,
            fg=TEXT,
            activebackground=HOVER,
            activeforeground=TEXT,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda: self.abrir_video(
                caminho
            )
        )

        botao.pack(
            side="right",
            padx=12
        )


        # ----------------------------------------------------
        # HOVER
        # ----------------------------------------------------

        widgets = [
            item,
            numero_label,
            nome_label
        ]


        def entrar(event):

            for widget in widgets:

                widget.configure(
                    bg=HOVER
                )


        def sair(event):

            for widget in widgets:

                widget.configure(
                    bg=PANEL_2
                )


        for widget in widgets:

            widget.bind(
                "<Enter>",
                entrar
            )

            widget.bind(
                "<Leave>",
                sair
            )


        # ----------------------------------------------------
        # CLICAR NO ITEM
        # ----------------------------------------------------

        for widget in widgets:

            widget.bind(
                "<Button-1>",
                lambda event, c=caminho:
                    self.abrir_video(c)
            )


    # ========================================================
    # REPRODUZIR VÍDEO
    # ========================================================

    def reproduzir_tela_cheia(
        self,
        caminho
    ):

        # ----------------------------------------------------
        # ABRIR VÍDEO
        # ----------------------------------------------------

        os.startfile(
            caminho
        )


        # ----------------------------------------------------
        # ESPERAR PLAYER ABRIR
        # ----------------------------------------------------

        self.frame.after(
            1500,
            self.maximizar_player
        )


    # ========================================================
    # ENCONTRAR PLAYER
    # ========================================================

    def maximizar_player(self):

        user32 = ctypes.windll.user32

        SW_MAXIMIZE = 3

        player_encontrado = [False]


        # ----------------------------------------------------
        # PROCURAR JANELAS DO WINDOWS
        # ----------------------------------------------------

        def enum_callback(
            hwnd,
            lParam
        ):

            if not user32.IsWindowVisible(
                hwnd
            ):

                return True


            tamanho = user32.GetWindowTextLengthW(
                hwnd
            )


            if tamanho == 0:

                return True


            titulo_buffer = ctypes.create_unicode_buffer(
                tamanho + 1
            )


            user32.GetWindowTextW(
                hwnd,
                titulo_buffer,
                tamanho + 1
            )


            titulo = (
                titulo_buffer.value.lower()
            )


            # ------------------------------------------------
            # IDENTIFICAR PLAYER
            # ------------------------------------------------

            if (
                "media player" in titulo
                or "filmes e tv" in titulo
                or "filmes" in titulo
            ):

                # --------------------------------------------
                # MAXIMIZAR
                # --------------------------------------------

                user32.ShowWindow(
                    hwnd,
                    SW_MAXIMIZE
                )


                # --------------------------------------------
                # TRAZER PLAYER PARA FRENTE
                # --------------------------------------------

                user32.SetForegroundWindow(
                    hwnd
                )


                player_encontrado[0] = True


                return False


            return True


        # ----------------------------------------------------
        # CALLBACK
        # ----------------------------------------------------

        CALLBACK = ctypes.WINFUNCTYPE(
            ctypes.c_bool,
            ctypes.c_void_p,
            ctypes.c_void_p
        )


        user32.EnumWindows(
            CALLBACK(enum_callback),
            0
        )


        # ----------------------------------------------------
        # ENTRAR EM FULLSCREEN
        # ----------------------------------------------------

        if player_encontrado[0]:

            self.frame.after(
                500,
                self.ativar_fullscreen
            )


    # ========================================================
    # FULLSCREEN
    # ========================================================

    def ativar_fullscreen(self):

        user32 = ctypes.windll.user32


        VK_MENU = 0x12
        VK_RETURN = 0x0D

        KEYEVENTF_KEYUP = 0x0002


        # ----------------------------------------------------
        # ALT
        # ----------------------------------------------------

        user32.keybd_event(
            VK_MENU,
            0,
            0,
            0
        )


        # ----------------------------------------------------
        # ENTER
        # ----------------------------------------------------

        user32.keybd_event(
            VK_RETURN,
            0,
            0,
            0
        )


        # ----------------------------------------------------
        # SOLTAR ENTER
        # ----------------------------------------------------

        user32.keybd_event(
            VK_RETURN,
            0,
            KEYEVENTF_KEYUP,
            0
        )


        # ----------------------------------------------------
        # SOLTAR ALT
        # ----------------------------------------------------

        user32.keybd_event(
            VK_MENU,
            0,
            KEYEVENTF_KEYUP,
            0
        )


        # ----------------------------------------------------
        # ESPERAR FULLSCREEN
        # ----------------------------------------------------

        self.frame.after(
            1000,
            lambda: self.focar_menu(
                self.frame.winfo_toplevel()
            )
        )


    # ========================================================
    # COLOCAR PLANETARY HUB POR CIMA
    # ========================================================

    def focar_menu(
        self,
        janela
    ):

        # ----------------------------------------------------
        # GARANTIR QUE O HUB ESTÁ VISÍVEL
        # ----------------------------------------------------

        janela.deiconify()


        # ----------------------------------------------------
        # COLOCAR NA FRENTE
        # ----------------------------------------------------

        janela.lift()


        # ----------------------------------------------------
        # TOPMOST TEMPORÁRIO
        # ----------------------------------------------------

        janela.attributes(
            "-topmost",
            True
        )


        janela.focus_force()


        # ----------------------------------------------------
        # DEPOIS DE 1 SEGUNDO,
        # REMOVE TOPMOST
        # ----------------------------------------------------

        janela.after(
            1000,
            lambda: janela.attributes(
                "-topmost",
                False
            )
        )


    # ========================================================
    # ABRIR VÍDEO
    # ========================================================

    def abrir_video(
        self,
        caminho
    ):

        # ----------------------------------------------------
        # VERIFICAR EXISTÊNCIA
        # ----------------------------------------------------

        if not os.path.exists(
            caminho
        ):

            messagebox.showerror(
                "Erro",
                "O vídeo não foi encontrado."
            )

            return


        try:

            # ------------------------------------------------
            # MONTANHA-RUSSA
            # ------------------------------------------------

            if "montanha" in caminho.lower():

                self.reproduzir_tela_cheia(
                    caminho
                )


            # ------------------------------------------------
            # OUTROS VÍDEOS
            # ------------------------------------------------

            else:

                os.startfile(
                    caminho
                )


        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível abrir o vídeo.\n\n{erro}"
            )


# ============================================================
# TESTE INDEPENDENTE
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()


    root.title(
        "Planetary Hub - Montanha-Russa"
    )


    root.geometry(
        "900x600"
    )


    root.configure(
        bg=BG
    )


    Montanha_Russa(
        root
    )


    root.mainloop()