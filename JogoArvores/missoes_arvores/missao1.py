import tkinter as tk
from tkinter import ttk

from algoritmos_arvores.arvores_rubonegras import RedBlackTree  


class Missao1:
    """
    Missão 1: Sentinelas de Scarif – Árvore Rubro-Negra
    """
    def __init__(self, root, game_manager, content_frame):
        self.root = root
        self.game_manager = game_manager
        self.base_content_frame = content_frame

        self.fase_atual = 0
        self.max_fases = 3

        self.tree = RedBlackTree()
        self.lista_inseridos = []

        self.dataset_fase = {
            0: [30, 15, 50, 10, 20, 40, 60],
            1: [7, 3, 18, 10, 22, 8, 11],
            2: [20, 15, 25, 10, 5, 1, 30, 28]
        }
        self.idx_dataset = 0

        self.insert_count = 0
        self.recolor_count = 0
        self.rotation_count = 0

        self._carregar_estilos()
        self.canvas = None

    def _carregar_estilos(self):
        try:
            self.cor_fundo = self.game_manager.bg_color_dark
            self.cor_texto = self.game_manager.fg_color_light
            self.cor_titulo = self.game_manager.title_color_accent
            self.font_titulo = self.game_manager.header_font_obj
            self.font_narrativa = self.game_manager.narrative_font_obj
            self.font_subtitulo = self.game_manager.small_bold_font_obj
        except AttributeError:
            self.cor_fundo = "#0b0f14"
            self.cor_texto = "#f5f5f5"
            self.cor_titulo = "#ffd54a"
            self.font_titulo = ("Arial", 20, "bold")
            self.font_narrativa = ("Arial", 12)
            self.font_subtitulo = ("Arial", 10, "bold")

    def _limpar_frame(self):
        for w in self.base_content_frame.winfo_children():
            w.destroy()

    def iniciar_missao_contexto(self, image_to_display=None):
        self._limpar_frame()

        tk.Label(
            self.base_content_frame,
            text="Missão 1: Sentinelas de Scarif – Árvore Rubro-Negra",
            font=self.font_titulo,
            fg=self.cor_titulo,
            bg=self.cor_fundo
        ).pack(pady=(10, 6))

        if image_to_display:
            tk.Label(self.base_content_frame, image=image_to_display, bg=self.cor_fundo).pack(pady=(8, 10))

        contexto = (
            "Inteligência Rebelde: estamos registrando agentes infiltrados. "
            "Cada registro entra na árvore, mas ela precisa continuar equilibrada. "
            "Se pai e tio ficarem vermelhos, recolore. Se não der, rotaciona. "
            "Assim garantimos acesso rápido e o Império não percebe."
        )
        tk.Label(
            self.base_content_frame,
            text=contexto,
            wraplength=800,
            justify=tk.LEFT,
            font=self.font_narrativa,
            fg=self.cor_texto,
            bg=self.cor_fundo
        ).pack(pady=(6, 14), padx=20)

        ttk.Button(
            self.base_content_frame,
            text="Iniciar Missão",
            command=self._iniciar_fase,
            style="Accent.Dark.TButton"
        ).pack(pady=10)

    def _iniciar_fase(self):
        self._reset_fase()
        self._montar_tela_arvore()

    def _reset_fase(self):
        self.tree = RedBlackTree()
        self.lista_inseridos = []
        self.idx_dataset = 0
        self.insert_count = 0
        self.recolor_count = 0
        self.rotation_count = 0

    def _montar_tela_arvore(self):
        self._limpar_frame()

        tk.Label(
            self.base_content_frame,
            text=self._titulo_fase(),
            font=self.font_titulo,
            fg=self.cor_titulo,
            bg=self.cor_fundo
        ).pack(pady=(8, 2))

        tk.Label(
            self.base_content_frame,
            text=self._narrativa_fase(),
            wraplength=820,
            justify=tk.LEFT,
            font=self.font_narrativa,
            fg=self.cor_texto,
            bg=self.cor_fundo
        ).pack(pady=(4, 10), padx=18)

        main = tk.Frame(self.base_content_frame, bg=self.cor_fundo)
        main.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        left = tk.Frame(main, bg=self.cor_fundo, width=340)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left.pack_propagate(False)

        right = tk.Frame(main, bg=self.cor_fundo)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.lbl_inserts = tk.Label(left, text="Inserções: 0", font=self.font_subtitulo, fg=self.cor_texto, bg=self.cor_fundo)
        self.lbl_recolors = tk.Label(left, text="Recolorações: 0", font=self.font_subtitulo, fg=self.cor_texto, bg=self.cor_fundo)
        self.lbl_rotations = tk.Label(left, text="Rotações: 0", font=self.font_subtitulo, fg=self.cor_texto, bg=self.cor_fundo)
        self.lbl_status = tk.Label(left, text="", font=self.font_narrativa, fg="#ffd54a", bg=self.cor_fundo,
                                   wraplength=300, justify=tk.LEFT)

        self.lbl_inserts.pack(anchor="w", pady=(8, 2))
        self.lbl_recolors.pack(anchor="w", pady=2)
        self.lbl_rotations.pack(anchor="w", pady=2)
        self.lbl_status.pack(anchor="w", pady=(8, 10))

        controls = tk.Frame(left, bg=self.cor_fundo)
        controls.pack(fill=tk.X, pady=(6, 2))

        ttk.Button(controls, text="Inserir próximo nó", command=self._inserir_proximo).pack(side=tk.LEFT, padx=4, pady=2)
        ttk.Button(controls, text="Reiniciar fase", command=self._iniciar_fase).pack(side=tk.LEFT, padx=4, pady=2)

        self.btn_prox = ttk.Button(left, text="Próxima Fase", command=self._proxima_fase,
                                   state="disabled", style="Accent.Dark.TButton")
        self.btn_prox.pack(fill=tk.X, pady=(10, 4))

        ttk.Button(left, text="Sair da Missão", command=self._sair, style="Dark.TButton").pack(fill=tk.X, pady=(2, 8))

        self.canvas = tk.Canvas(right, bg=self.cor_fundo, highlightthickness=0, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self._desenhar_arvore()

    def _titulo_fase(self):
        titulos = [
            "Fase 1: Inserções básicas (raiz preta, novos vermelhos)",
            "Fase 2: Conflitos de cor (recoloração)",
            "Fase 3: Rotações para manter equilíbrio"
        ]
        return titulos[self.fase_atual]

    def _narrativa_fase(self):
        if self.fase_atual == 0:
            return "Central Rebelde: observe que a raiz fica preta e os nós novos entram vermelhos."
        elif self.fase_atual == 1:
            return "Central Rebelde: agora vamos provocar pai e tio vermelhos. A árvore vai recolorir sozinha."
        else:
            return "Central Rebelde: nesta fase, se só cor não resolve, a estrutura rotaciona para recuperar o equilíbrio."

    def _inserir_proximo(self):
        dados = self.dataset_fase.get(self.fase_atual, [])
        if self.idx_dataset >= len(dados):
            self.lbl_status.config(text="Todos os registros desta fase foram inseridos. Fase concluída!")
            self.btn_prox.config(state="normal")
            return

        chave = dados[self.idx_dataset]
        self.idx_dataset += 1

        info = self.tree.insert(chave)
        self.lista_inseridos.append(chave)
        self.insert_count += 1

        if isinstance(info, dict):
            self.recolor_count += info.get("recolor", 0)
            self.rotation_count += info.get("rotation", 0)

        self._atualizar_metricas()

        status_msg = f"Registro {chave} inserido."
        if isinstance(info, dict):
            if info.get("recolor", 0) > 0:
                status_msg += f" Recoloração aplicada ({info.get('recolor')})."
            if info.get("rotation", 0) > 0:
                status_msg += f" Rotação aplicada ({info.get('rotation')})."
        self.lbl_status.config(text=status_msg)

        self._desenhar_arvore()

        if self.idx_dataset >= len(dados):
            self.btn_prox.config(state="normal")
            self.lbl_status.config(text=status_msg + " Todos os nós desta fase foram inseridos.")

    def _desenhar_arvore(self):
        if not self.canvas:
            return
        self.canvas.delete("all")

        if self.tree.root is None or self.tree.root == self.tree.NIL:
            self.canvas.create_text(300, 200, text="(Árvore vazia)", fill=self.cor_texto, font=("Arial", 12))
            return

        width = self.canvas.winfo_width() or 700
        start_y = 40
        y_step = 70

        # coletar níveis (BFS)
        levels = {}
        queue = [(self.tree.root, 0)]
        while queue:
            node, depth = queue.pop(0)
            levels.setdefault(depth, []).append(node)
            if node.left and node.left != self.tree.NIL:
                queue.append((node.left, depth + 1))
            if node.right and node.right != self.tree.NIL:
                queue.append((node.right, depth + 1))

        for depth, nodes in levels.items():
            n_nodes = len(nodes)
            gap = width // (n_nodes + 1)
            y = start_y + depth * y_step
            for i, node in enumerate(nodes, start=1):
                x = gap * i

                parent = node.parent
                if parent and parent != self.tree.NIL and (depth - 1) in levels and parent in levels[depth - 1]:
                    parent_list = levels[depth - 1]
                    p_gap = width // (len(parent_list) + 1)
                    px = p_gap * (parent_list.index(parent) + 1)
                    py = start_y + (depth - 1) * y_step
                    self.canvas.create_line(px, py + 15, x, y - 15, fill="#777777")

                fill = "#212121"
                outline = "#eeeeee"
                text_color = "#FFD700"
                if getattr(node, "color", "black") in ("red", "RED", "r", "R"):
                    fill = "#b71c1c"
                    outline = "#ffebee"

                r = 18
                self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=fill, outline=outline, width=2)
                self.canvas.create_text(x, y, text=str(node.key), fill=text_color)

    def _proxima_fase(self):
        if self.fase_atual + 1 < self.max_fases:
            self.fase_atual += 1
            self._iniciar_fase()
        else:
            self._finalizar_missao()

    def _finalizar_missao(self):
        self._limpar_frame()
        tk.Label(
            self.base_content_frame,
            text="Missão Concluída!",
            font=self.font_titulo,
            fg="green",
            bg=self.cor_fundo
        ).pack(pady=(10, 8))

        tk.Label(
            self.base_content_frame,
            text=("As sentinelas de Scarif foram configuradas. A árvore permaneceu balanceada "
                  "e os registros puderam ser acessados rapidamente."),
            wraplength=760,
            justify=tk.CENTER,
            font=self.font_narrativa,
            fg=self.cor_texto,
            bg=self.cor_fundo
        ).pack(pady=10, padx=20)

        ttk.Button(
            self.base_content_frame,
            text="Continuar",
            command=self._encerrar_no_gm,
            style="Accent.Dark.TButton"
        ).pack(pady=16)

    def _encerrar_no_gm(self):
        self.game_manager.mission_completed("Missao1")

    def _sair(self):
        self.game_manager.mission_completed("Missao1")

    def _atualizar_metricas(self):
        self.lbl_inserts.config(text=f"Inserções: {self.insert_count}")
        self.lbl_recolors.config(text=f"Recolorações: {self.recolor_count}")
        self.lbl_rotations.config(text=f"Rotações: {self.rotation_count}")

