import tkinter as tk
import requests
from datetime import datetime


# ============================================================
# CONFIGURAÇÃO
# ============================================================

#INFO_MIC:http://10.41.82.206:8090
#Casa:http://192.168.0.102:8090
STELLARIUM_URL = "http://192.168.0.102:8090"


# ============================================================
# CORES
# ============================================================

BG = "#070A10"
PANEL = "#0D121B"
PANEL_2 = "#111824"
TEXT = "#E8EDF5"
MUTED = "#7E899C"
HOVER = "#182131"


# ============================================================
# STELLARIUM
# ============================================================

class Stellarium:

    def __init__(self, url=STELLARIUM_URL):

        self.url = url

        # Estados iniciais
        self.atmosfera = True
        self.superficie = True

        self.constelacoes = False
        self.arte_constelacoes = False
        self.nomes_constelacoes = False

        self.linha_ecliptica = False

        self.velocidade = 1
            # Coloca o Stellarium em tempo normal ao iniciar o controle
        try:
                requests.post(
                    f"{self.url}/api/main/time",
                    data={"timerate": "1"},
                    timeout=2
                )
                print("[Stellarium] Tempo normal: 1x")

        except Exception as e:
                print("[Stellarium] Não foi possível definir o tempo inicial:", e)

    # ========================================================
    # COMUNICAÇÃO
    # ========================================================

    def set_prop(self, prop, valor):

        try:

            requests.post(
                f"{self.url}/api/stelproperty/set",
                data={
                    "id": prop,
                    "value": str(valor).lower()
                },
                timeout=2
            )

            print(f"[Stellarium] {prop} = {valor}")

        except requests.RequestException as e:

            print("[Stellarium] Erro de conexão:", e)

        except Exception as e:

            print("[Stellarium] Erro:", e)


    # ========================================================
    # TEMPO
    # ========================================================

    def definir_velocidade(self, velocidade):

        try:

            velocidade = float(velocidade)

            self.velocidade = velocidade

            requests.post(
                f"{self.url}/api/main/time",
                data={
                    "timerate": str(velocidade)
                },
                timeout=2
            )

            print(f"[Stellarium] Velocidade: {velocidade}x")

        except requests.RequestException as e:

            print("[Stellarium] Erro na velocidade:", e)

        except Exception as e:

            print("[Stellarium] Erro:", e)

    def tempo_normal(self):
        self.velocidade = 1

        requests.post(
            f"{self.url}/api/main/time",
            data={"timerate": "1"},
            timeout=2
        )
    def pausar_tempo(self):

        self.definir_velocidade(0)

        print("[Stellarium] Tempo pausado")


    def voltar_tempo(self):

        self.definir_velocidade(-100)

        print("[Stellarium] Tempo voltando")


    def continuar_tempo(self):

        # Se estava parado, volta para 1x
        if self.velocidade == 0:
            self.definir_velocidade(1)

        else:
            self.definir_velocidade(self.velocidade)


    def tempo_atual(self):


        try:
            agora = datetime.now()

            data_hora = agora.strftime("%Y-%m-%dT%H:%M:%S")

            requests.post(
                f"{self.url}/api/main/time",
                data={
                    "time": data_hora,
                    "timerate": "1"
                },
                timeout=2
            )

            self.velocidade = 1

            print(
                f"[Stellarium] Tempo sincronizado: "
                f"{agora.strftime('%d/%m/%Y %H:%M:%S')}"
            )

        except Exception as e:
            print("[Stellarium] Erro ao sincronizar tempo:", e)


    # ========================================================
    # ATMOSFERA
    # ========================================================

    def alternar_atmosfera(self):

        self.atmosfera = not self.atmosfera

        self.set_prop(
            "LandscapeMgr.atmosphereDisplayed",
            self.atmosfera
        )

        return self.atmosfera


    # ========================================================
    # SUPERFÍCIE
    # ========================================================

    def alternar_superficie(self):

        self.superficie = not self.superficie

        self.set_prop(
            "LandscapeMgr.landscapeDisplayed",
            self.superficie
        )

        return self.superficie


    # ========================================================
    # LINHAS DAS CONSTELAÇÕES
    # ========================================================

    def alternar_constelacoes(self):

        self.constelacoes = not self.constelacoes

        self.set_prop(
            "ConstellationMgr.linesDisplayed",
            self.constelacoes
        )

        return self.constelacoes


    # ========================================================
    # ARTE DAS CONSTELAÇÕES
    # ========================================================

    def alternar_arte_constelacoes(self):

        self.arte_constelacoes = not self.arte_constelacoes

        self.set_prop(
            "ConstellationMgr.artDisplayed",
            self.arte_constelacoes
        )

        return self.arte_constelacoes


    # ========================================================
    # NOMES DAS CONSTELAÇÕES
    # ========================================================

    def alternar_nomes_constelacoes(self):

        self.nomes_constelacoes = not self.nomes_constelacoes

        self.set_prop(
            "ConstellationMgr.namesDisplayed",
            self.nomes_constelacoes
        )

        return self.nomes_constelacoes


    # ========================================================
    # LINHA ECLÍPTICA
    # ========================================================

    def alternar_linha_ecliptica(self):

        self.linha_ecliptica = not self.linha_ecliptica

        self.set_prop(
            "GridLinesMgr.eclipticLineDisplayed",
            self.linha_ecliptica
        )

        return self.linha_ecliptica


    # ========================================================
    # BUSCAR OBJETO
    # ========================================================

    def buscar_objeto(self, corpo_celeste):

        if not corpo_celeste:
            return

        corpo_celeste = corpo_celeste.strip()

        if not corpo_celeste:
            return

        try:

            requests.post(
                f"{self.url}/api/main/focus",
                data={
                    "target": corpo_celeste
                },
                timeout=2
            )

            print(f"[Stellarium] Focando em: {corpo_celeste}")

        except requests.RequestException as e:

            print("[Stellarium] Erro ao buscar objeto:", e)

        except Exception as e:

            print("[Stellarium] Erro:", e)


    # ========================================================
    # MODO PALESTRA
    # ========================================================

    def modo_palestra(self):

        self.superficie = False
        self.atmosfera = False

        self.constelacoes = True
        self.nomes_constelacoes = True
        self.arte_constelacoes = False

        self.linha_ecliptica = True

        self.set_prop(
            "LandscapeMgr.landscapeDisplayed",
            False
        )

        self.set_prop(
            "LandscapeMgr.atmosphereDisplayed",
            False
        )

        self.set_prop(
            "ConstellationMgr.linesDisplayed",
            True
        )

        self.set_prop(
            "ConstellationMgr.namesDisplayed",
            True
        )

        self.set_prop(
            "ConstellationMgr.artDisplayed",
            False
        )

        self.set_prop(
            "GridLinesMgr.eclipticLineDisplayed",
            True
        )

        print("[Stellarium] Modo palestra ativado")


    # ========================================================
    # CRIAÇÃO DA INTERFACE
    # ========================================================

    def criar_interface(self, parent):

        self.tempo_normal()

        frame = tk.Frame(
            parent,
            bg=BG
        )


        # ====================================================
        # TÍTULO
        # ====================================================

        tk.Label(
            frame,
            text="STELLARIUM",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 2)
        )


        tk.Label(
            frame,
            text="Controle da simulação",
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 9)
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 12)
        )


        # ====================================================
        # FUNÇÃO PARA CRIAR BOTÕES
        # ====================================================

        def botao(parent_botao, texto, comando):

            return tk.Button(
                parent_botao,
                text=texto,
                command=comando,
                bg=PANEL_2,
                fg=TEXT,
                activebackground=HOVER,
                activeforeground=TEXT,
                relief="flat",
                bd=0,
                font=("Segoe UI", 9),
                cursor="hand2",
                padx=6,
                pady=7
            )


        # ====================================================
        # VISUALIZAÇÃO
        # ====================================================

        visual = tk.LabelFrame(
            frame,
            text=" Visualização ",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 9, "bold"),
            bd=1,
            relief="solid"
        )

        visual.pack(
            fill="x",
            padx=15,
            pady=4
        )


        # ----------------------------------------------------
        # ATMOSFERA
        # ----------------------------------------------------

        def atualizar_atmosfera():

            estado = self.alternar_atmosfera()

            botao_atmosfera.config(
                text=f"🌫 Atmosfera: {'ON' if estado else 'OFF'}"
            )


        botao_atmosfera = botao(
            visual,
            "🌫 Atmosfera: ON",
            atualizar_atmosfera
        )

        botao_atmosfera.pack(
            fill="x",
            padx=8,
            pady=3
        )


        # ----------------------------------------------------
        # SUPERFÍCIE
        # ----------------------------------------------------

        def atualizar_superficie():

            estado = self.alternar_superficie()

            botao_superficie.config(
                text=f"🌍 Superfície: {'ON' if estado else 'OFF'}"
            )


        botao_superficie = botao(
            visual,
            "🌍 Superfície: ON",
            atualizar_superficie
        )

        botao_superficie.pack(
            fill="x",
            padx=8,
            pady=3
        )


        # ====================================================
        # CONSTELAÇÕES
        # ====================================================

        const = tk.LabelFrame(
            frame,
            text=" Constelações ",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 9, "bold"),
            bd=1,
            relief="solid"
        )

        const.pack(
            fill="x",
            padx=15,
            pady=4
        )


        # ----------------------------------------------------
        # LINHAS
        # ----------------------------------------------------

        def atualizar_constelacoes():

            estado = self.alternar_constelacoes()

            botao_const.config(
                text=f"✦ Linhas: {'ON' if estado else 'OFF'}"
            )


        botao_const = botao(
            const,
            "✦ Linhas: OFF",
            atualizar_constelacoes
        )

        botao_const.pack(
            fill="x",
            padx=8,
            pady=3
        )


        # ----------------------------------------------------
        # ARTE
        # ----------------------------------------------------

        def atualizar_arte():

            estado = self.alternar_arte_constelacoes()

            botao_arte.config(
                text=f"★ Arte: {'ON' if estado else 'OFF'}"
            )


        botao_arte = botao(
            const,
            "★ Arte: OFF",
            atualizar_arte
        )

        botao_arte.pack(
            fill="x",
            padx=8,
            pady=3
        )


        # ----------------------------------------------------
        # NOMES
        # ----------------------------------------------------

        def atualizar_nomes():

            estado = self.alternar_nomes_constelacoes()

            botao_nomes.config(
                text=f"A Nomes: {'ON' if estado else 'OFF'}"
            )


        botao_nomes = botao(
            const,
            "A Nomes: OFF",
            atualizar_nomes
        )

        botao_nomes.pack(
            fill="x",
            padx=8,
            pady=3
        )


        # ----------------------------------------------------
        # ECLÍPTICA
        # ----------------------------------------------------

        def atualizar_ecliptica():

            estado = self.alternar_linha_ecliptica()

            botao_ecliptica.config(
                text=f"☼ Eclíptica: {'ON' if estado else 'OFF'}"
            )


        botao_ecliptica = botao(
            const,
            "☼ Eclíptica: OFF",
            atualizar_ecliptica
        )

        botao_ecliptica.pack(
            fill="x",
            padx=8,
            pady=3
        )


        # ====================================================
        # TEMPO
        # ====================================================

        tempo = tk.LabelFrame(
            frame,
            text=" Tempo ",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 9, "bold"),
            bd=1,
            relief="solid"
        )

        tempo.pack(
            fill="x",
            padx=15,
            pady=4
        )


        velocidade_label = tk.Label(
            tempo,
            text="Velocidade: 1x",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 9)
        )

        velocidade_label.pack(
            pady=(6, 0)
        )


        # ----------------------------------------------------
        # TRACKBAR
        # ----------------------------------------------------

        def alterar_velocidade(valor):

            valor = float(valor)

            velocidade_label.config(
                text=f"Velocidade: {valor:g}x"
            )

            self.definir_velocidade(valor)


        velocidade = tk.Scale(
            tempo,
            from_=-10,
            to=10,
            resolution=1,
            orient="horizontal",

            bg=BG,
            fg=TEXT,
            troughcolor=PANEL_2,

            highlightthickness=0,
            bd=0,

            showvalue=False,

            command=alterar_velocidade
        )

        velocidade.set(1)

        velocidade.pack(
            fill="x",
            padx=8,
            pady=3
        )


        # ----------------------------------------------------
        # BOTÕES DO TEMPO
        # ----------------------------------------------------

        botoes_tempo = tk.Frame(
            tempo,
            bg=BG
        )

        botoes_tempo.pack(
            fill="x",
            padx=8,
            pady=(2, 6)
        )


        botao(
            botoes_tempo,
            "⏪ Voltar",
            self.voltar_tempo
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=2
        )


        botao(
            botoes_tempo,
            "⏸ Pausar",
            self.pausar_tempo
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=2
        )


        botao(
            botoes_tempo,
            "▶ Continuar",
            self.continuar_tempo
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=2
        )


        # ----------------------------------------------------
        # TEMPO ATUAL
        # ----------------------------------------------------

        botao(
            tempo,
            "🕐 Tempo atual (1x)",
            self.tempo_atual
        ).pack(
            fill="x",
            padx=8,
            pady=(0, 7)
        )


        # ====================================================
        # BUSCAR OBJETO
        # ====================================================

        busca = tk.LabelFrame(
            frame,
            text=" Buscar objeto ",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 9, "bold"),
            bd=1,
            relief="solid"
        )

        busca.pack(
            fill="x",
            padx=15,
            pady=4
        )


        entrada = tk.Entry(
            busca,
            bg=PANEL_2,
            fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            font=("Segoe UI", 9)
        )

        entrada.pack(
            fill="x",
            padx=8,
            pady=(6, 4),
            ipady=5
        )


        botao(
            busca,
            "🔭 Focar objeto",
            lambda: self.buscar_objeto(entrada.get())
        ).pack(
            fill="x",
            padx=8,
            pady=(0, 6)
        )


        # ====================================================
        # MODO PALESTRA
        # ====================================================

        tk.Button(
            frame,
            text="🎤 MODO PALESTRA",
            command=self.modo_palestra,

            bg=PANEL_2,
            fg=TEXT,

            activebackground=HOVER,
            activeforeground=TEXT,

            relief="flat",
            bd=0,

            font=("Segoe UI", 9, "bold"),
            cursor="hand2",

            pady=8
        ).pack(
            fill="x",
            padx=15,
            pady=(6, 12)
        )


        return frame