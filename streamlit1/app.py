import streamlit as st
import pandas as pd

nome = "Arthur" 
idade = 17        

st.title("Meu primeiro dash")
st.subheader(nome)

st.write("Olá, mundo")
st.write(f"Meu nome é {nome} e eu tenho {idade} anos.")

st.divider()

df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10],
})

st.write(df)

st.divider()

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
