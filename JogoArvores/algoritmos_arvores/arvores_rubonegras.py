# arvores_rubonegras.py


RED = "red"
BLACK = "black"


class RBNode:
    def __init__(self, key=None, color=RED, left=None, right=None, parent=None):
        self.key = key
        self.color = color  # "red" ou "black"
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"RBNode(key={self.key}, color={self.color})"


class RedBlackTree:
    def __init__(self):
        
        self.NIL = RBNode(key=None, color=BLACK)
        self.root = self.NIL

    def insert(self, key):
      
        recolors = 0
        rotations = 0

       
        new_node = RBNode(key=key, color=RED, left=self.NIL, right=self.NIL, parent=None)

       
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.parent = y

        if y is None:
           
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        
        if new_node.parent is None:
            new_node.color = BLACK
            self.root = new_node
            return {"recolor": 1, "rotation": 0}

        if new_node.parent.parent is None:
            
            return {"recolor": 0, "rotation": 0}

       
        r_fix, r_rot = self._fix_insert(new_node)
        recolors += r_fix
        rotations += r_rot

        return {"recolor": recolors, "rotation": rotations}

    # ---------------------------------------------------------
    # rotações
    def _left_rotate(self, x):
        rotations = 1  # contamos uma rotação
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y
        return rotations

    def _right_rotate(self, x):
        rotations = 1
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y
        return rotations

    # ---------------------------------------------------------
    # correção pós-inserção
    def _fix_insert(self, k):
        recolors = 0
        rotations = 0

        while k.parent and k.parent.color == RED:
            # se o pai é vermelho, a gente olha o "tio"
            if k.parent == k.parent.parent.right:
                # pai é filho direito -> tio é esquerda
                u = k.parent.parent.left
                if u and u.color == RED:
                    # caso 1: tio vermelho -> recoloração
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    recolors += 3
                    k = k.parent.parent
                else:
                    # tio preto
                    if k == k.parent.left:
                        # caso 2: triângulo -> rotaciona pra direita no pai
                        rotations += self._right_rotate(k.parent)
                        k = k.parent
                    # caso 3: linha -> rotaciona pra esquerda no avô
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    recolors += 2
                    rotations += self._left_rotate(k.parent.parent)
            else:
                # pai é filho esquerdo -> tio é direita
                u = k.parent.parent.right
                if u and u.color == RED:
                    # caso 1 espelhado: tio vermelho
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    recolors += 3
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # caso 2 espelhado
                        rotations += self._left_rotate(k.parent)
                        k = k.parent
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    recolors += 2
                    rotations += self._right_rotate(k.parent.parent)

            if k == self.root:
                break

        # garante raiz preta
        if self.root.color != BLACK:
            self.root.color = BLACK
            recolors += 1

        return recolors, rotations
