class NoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.altura = 1
        self.esquerda = None
        self.direita = None
    
    def __repr__(self):
        return f"NoAVL(v={self.valor}, h={self.altura})"

class ArvAVL:

    def __init__(self):
        self.raiz = None
        self.acao_necessaria = None
        self.no_desbalanceado = None
    

    def _get_altura(self, no):
        if not no:
            return 0
        return no.altura

    def _get_fb(self, no):
        if not no:
            return 0
        return self._get_altura(no.esquerda) - self._get_altura(no.direita)

    def _atualizar_altura(self, no):
        if no:
            no.altura = 1 + max(self._get_altura(no.esquerda), self._get_altura(no.direita))


    def _rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        self._atualizar_altura(z)
        self._atualizar_altura(y)
        return y

    def _rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        self._atualizar_altura(z)
        self._atualizar_altura(y)
        return y
    

    def _detectar_rebalanceamento(self, raiz_atual, valor):
        fb = self._get_fb(raiz_atual)
        
        if fb > 1:
            if valor < raiz_atual.esquerda.valor:
                return 'RR' 
            else:
                return 'LR'
        
        if fb < -1:
            if valor > raiz_atual.direita.valor:
                return 'LL' 
            else:
                return 'RL'
                
        return None

    def inserir_manual(self, raiz_atual, valor, registro_acoes):
        
        if 'rotacoes_aplicadas' not in registro_acoes:
             registro_acoes['rotacoes_aplicadas'] = 0
             

        if not raiz_atual:
            return NoAVL(valor), registro_acoes
        
        if valor < raiz_atual.valor:
            raiz_atual.esquerda, registro_acoes = self.inserir_manual(raiz_atual.esquerda, valor, registro_acoes)
        elif valor > raiz_atual.valor:
            raiz_atual.direita, registro_acoes = self.inserir_manual(raiz_atual.direita, valor, registro_acoes)
        else:
            return raiz_atual, registro_acoes

        self._atualizar_altura(raiz_atual)

        if self.acao_necessaria is None:
            acao = self._detectar_rebalanceamento(raiz_atual, valor)
            if acao:
                self.acao_necessaria = acao
                self.no_desbalanceado = raiz_atual.valor
                registro_acoes['desbalanceado'] = raiz_atual.valor
                registro_acoes['rotacao_gabarito'] = acao

        fb = self._get_fb(raiz_atual)

        if abs(fb) > 1 and raiz_atual.valor == self.no_desbalanceado:
            
            if fb > 1 and self._get_fb(raiz_atual.esquerda) >= 0:
                registro_acoes['rotacoes_aplicadas'] += 1
                return self._rotacao_direita(raiz_atual), registro_acoes

            if fb < -1 and self._get_fb(raiz_atual.direita) <= 0:
                registro_acoes['rotacoes_aplicadas'] += 1
                return self._rotacao_esquerda(raiz_atual), registro_acoes

            if fb > 1 and self._get_fb(raiz_atual.esquerda) < 0:
                raiz_atual.esquerda = self._rotacao_esquerda(raiz_atual.esquerda)
                registro_acoes['rotacoes_aplicadas'] += 2 # Dupla conta como 2 rotações simples
                return self._rotacao_direita(raiz_atual), registro_acoes

            if fb < -1 and self._get_fb(raiz_atual.direita) > 0:
                raiz_atual.direita = self._rotacao_direita(raiz_atual.direita)
                registro_acoes['rotacoes_aplicadas'] += 2 # Dupla conta como 2 rotações simples
                return self._rotacao_esquerda(raiz_atual), registro_acoes
        
        return raiz_atual, registro_acoes

    def _realizar_rotacao(self, no_raiz, tipo_rotacao):
        if tipo_rotacao == 'RR':
            return self._rotacao_direita(no_raiz)
        elif tipo_rotacao == 'LL':
            return self._rotacao_esquerda(no_raiz)
        elif tipo_rotacao == 'LR':
            no_raiz.esquerda = self._rotacao_esquerda(no_raiz.esquerda)
            return self._rotacao_direita(no_raiz)
        elif tipo_rotacao == 'RL':
            no_raiz.direita = self._rotacao_direita(no_raiz.direita)
            return self._rotacao_esquerda(no_raiz)
        else:
            raise ValueError("Tipo de rotação inválido.")

    def buscar_no(self, valor):
        atual = self.raiz
        while atual is not None:
            if valor == atual.valor:
                return atual
            elif valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None