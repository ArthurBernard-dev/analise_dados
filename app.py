import streamlit as st
import pandas as pd

# ---------- Passos 4, 6 e 7: Olá, mundo + variáveis nome e idade ----------
nome = "Seu Nome"   # <- troque pelo seu nome
idade = 20          # <- troque pela sua idade

# ---------- Passos 11 e 12: título e subtítulo ----------
st.title("Meu primeiro dash")
st.subheader(nome)

st.write("Olá, mundo")
st.write(f"Meu nome é {nome} e eu tenho {idade} anos.")

st.divider()

# ---------- Passo 10: dataframe ----------
df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10],
})

# ---------- Passo 13: df embaixo do título/subtítulo ----------
st.write(df)

st.divider()

# ---------- Passos 16 e 17: supermercado ----------
st.subheader("Supermercado")

precos = {
    "Arroz (5kg)": 28.90,
    "Feijão (1kg)": 8.50,
    "Leite (1L)": 5.20,
    "Pão": 1.20,
    "Café (500g)": 18.75,
    "Ovos (dúzia)": 12.00,
}


def calcular_preco(item, quantidade):
    """Retorna o preço total da compra: preço unitário x quantidade."""
    return precos[item] * quantidade


item = st.selectbox("Escolha um item", list(precos.keys()))
quantidade = st.number_input("Quantidade", min_value=1, value=1, step=1)

total = calcular_preco(item, quantidade)

col1, col2 = st.columns(2)
col1.metric("Preço unitário", f"R$ {precos[item]:.2f}")
col2.metric("Total da compra", f"R$ {total:.2f}")
