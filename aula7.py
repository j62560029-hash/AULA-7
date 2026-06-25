import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

# Garante o download correto de todos os recursos necessários
@st.cache_resource
def carregar_recursos_nltk():
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    nltk.download('stopwords', quiet=True)

carregar_recursos_nltk()

st.title("Aula 7 - Processamento de Linguagem Natural")
st.subheader("Desenvolvedor: Entrega das 10 Atividades Práticas")

# Criação das abas (tabs) para organizar as 10 atividades em um único arquivo
abas = st.tabs([f"Atividade {i}" for i in range(1, 11)])

# -------------------------------------------------------------------------
# ATIVIDADE 1: Tokenização simples
# -------------------------------------------------------------------------
with abas[0]:
    st.header("1. Tokenização de Palavras")
    texto_at1 = st.text_area("Mensagem do cliente:", "O suporte técnico resolveu meu problema rapidamente.", key="at1")
    if st.button("Separar em Palavras", key="btn_at1"):
        palavras_at1 = word_tokenize(texto_at1)
        st.write("**Resultado da Tokenização:**", palavras_at1)

# -------------------------------------------------------------------------
# ATIVIDADE 2: Frequência de palavras
# -------------------------------------------------------------------------
with abas[1]:
    st.header("2. Frequência de Palavras")
    texto_at2 = st.text_area("Avaliações dos clientes:", "ótimo produto produto muito bom ótimo atendimento", key="at2")
    if st.button("Contar Frequência", key="btn_at2"):
        palavras_at2 = word_tokenize(texto_at2.lower())
        frequencia_at2 = Counter(palavras_at2)
        st.write("**Frequência de cada palavra:**", dict(frequencia_at2))

# -------------------------------------------------------------------------
# ATIVIDADE 3: Detecção de palavras negativas para prioridade
# -------------------------------------------------------------------------
with abas[2]:
    st.header("3. Detectar Mensagens Negativas")
    texto_at3 = st.text_area("Mensagem de entrada:", "O sistema apresentou um erro terrível e o serviço está péssimo.", key="at3")
    if st.button("Verificar Prioridade", key="btn_at3"):
        texto_min = texto_at3.lower()
        if "ruim" in texto_min or "péssimo" in texto_min or "erro" in texto_min:
            st.error("Alerta: Mensagem com prioridade máxima (Tom Negativo detectado).")
        else:
            st.success("Mensagem normalizada. Sem gatilhos urgentes.")

# -------------------------------------------------------------------------
# ATIVIDADE 4: Remoção de Stopwords
# -------------------------------------------------------------------------
with abas[3]:
    st.header("4. Remoção de Stopwords (Português)")
    texto_at4 = st.text_area("Texto original:", "O produto é bom, mas a entrega atrasou para o cliente.", key="at4")
    if st.button("Remover Stopwords", key="btn_at4"):
        palavras_at4 = word_tokenize(texto_at4.lower())
        palavras_sem_stopwords = [p for p in palavras_at4 if p not in stopwords.words('portuguese')]
        st.write("**Texto filtrado (Apenas palavras com significado):**", palavras_sem_stopwords)

# -------------------------------------------------------------------------
# ATIVIDADE 5: Classificação de sentimento simples (Condicionais)
# -------------------------------------------------------------------------
with abas[4]:
    st.header("5. Classificação de Sentimento Simples")
    texto_at5 = st.text_area("Comentário do cliente:", "Esse produto é excelente, adorei!", key="at5")
    if st.button("Classificar Sentimento", key="btn_at5"):
        texto_min = texto_at5.lower()
        if any(palavra in texto_min for palavra in ["excelente", "ótimo", "recomendo", "bom", "gostei"]):
            st.success("Sentimento: Positivo")
        elif any(palavra in texto_min for palavra in ["ruim", "péssimo", "odiei", "fraco"]):
            st.error("Sentimento: Negativo")
        else:
            st.info("Sentimento: Neutro")

# -------------------------------------------------------------------------
# ATIVIDADE 6: Direcionamento de Chatbot por palavra-chave
# -------------------------------------------------------------------------
with abas[5]:
    st.header("6. Direcionamento de Chatbot")
    texto_at6 = st.text_area("Digite sua dúvida/solicitação:", "Quero efetuar o pagamento do boleto.", key="at6")
    if st.button("Direcionar Cliente", key="btn_at6"):
        texto_min = texto_at6.lower()
        if "cancelar" in texto_min:
            st.warning("Direcionando para o setor de: Retenção e Cancelamentos.")
        elif "erro" in texto_min:
            st.error("Direcionando para o setor de: Suporte Técnico.")
        elif "pagamento" in texto_min or "conta" in texto_min:
            st.success("Direcionando para o setor de: Financeiro.")
        else:
            st.info("Direcionando para o Atendimento Geral.")

# -------------------------------------------------------------------------
# ATIVIDADE 7: Palavras mais frequentes em Reclamações
# -------------------------------------------------------------------------
with abas[6]:
    st.header("7. Termos mais comuns em Reclamações")
    texto_at7 = st.text_area("Histórico de reclamações:", "O aplicativo deu erro. Erro ao logar. Que erro chato.", key="at7")
    if st.button("Analisar Reclamação", key="btn_at7"):
        palavras_at7 = [p.lower() for p in word_tokenize(texto_at7) if p not in string.punctuation]
        mais_comuns = Counter(palavras_at7).most_common(3)
        st.write("**Top 3 palavras mais frequentes:**", mais_comuns)

# -------------------------------------------------------------------------
# ATIVIDADE 8: Classificação Automática (Suporte vs Financeiro)
# -------------------------------------------------------------------------
with abas[7]:
    st.header("8. Classificação: Suporte vs Financeiro")
    texto_at8 = st.text_area("Assunto da mensagem:", "Preciso estornar o valor cobrado errado.", key="at8")
    if st.button("Classificar Mensagem", key="btn_at8"):
        texto_min = texto_at8.lower()
        if any(p in texto_min for p in ["ajuda", "bug", "sistema", "senha", "erro"]):
            st.info("Categoria: Suporte Técnico")
        elif any(p in texto_min for p in ["financeiro", "pagar", "boleto", "estorno", "cobrado"]):
            st.info("Categoria: Financeiro")
        else:
            st.warning("Categoria: Não Identificada (Triagem Manual)")

# -------------------------------------------------------------------------
# ATIVIDADE 9: Limpeza e Normalização de Texto
# -------------------------------------------------------------------------
with abas[8]:
    st.header("9. Limpeza e Normalização")
    texto_at9 = st.text_area("Texto sujo:", "Olá! Tudo bem? O projeto de IA vai funcionar!!!", key="at9")
    if st.button("Limpar Texto", key="btn_at9"):
        texto_minusculo = texto_at9.lower()
        texto_limpo = texto_minusculo.translate(str.maketrans('', '', string.punctuation))
        st.write("**Texto Normalizado:**", texto_limpo)

# -------------------------------------------------------------------------
# ATIVIDADE 10: Tokenização + Condicional (Sentimento Combinado)
# -------------------------------------------------------------------------
with abas[9]:
    st.header("10. Tokenização + Condicional")
    texto_at10 = st.text_area("Insira a avaliação do produto:", "Achei o produto péssimo e quebrou rápido.", key="at10")
    if st.button("Análise Combinada", key="btn_at10"):
        tokens = word_tokenize(texto_at10.lower())
        if "ruim" in tokens or "péssimo" in tokens or "defeito" in tokens:
            st.error("Resultado final: Insatisfeito (Negativo)")
        elif "excelente" in tokens or "bom" in tokens or "satisfeito" in tokens:
            st.success("Resultado final: Satisfeito (Positivo)")
        else:
            st.info("Resultado final: Neutro / Inconclusivo")
        st.write("**Tokens analisados:**", tokens)