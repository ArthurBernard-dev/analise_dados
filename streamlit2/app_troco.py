import streamlit as st
import pandas as pd

st.set_page_config(page_title="Supermercado", page_icon="🛒", layout="centered")

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
    return precos[item] * quantidade

item = st.selectbox("Escolha um item", list(precos.keys()))
quantidade = st.number_input("Quantidade", min_value=1, value=1, step=1)
total = calcular_preco(item, quantidade)

col1, col2 = st.columns(2)
with col1:
    st.metric("Preço unitário", f"R$ {precos[item]:.2f}")
with col2:
    st.metric("Total da compra", f"R$ {total:.2f}")

st.divider()
st.subheader("Calculadora de Troco")

col1, col2 = st.columns(2)
with col1:
    valor_compra = st.number_input("Valor da compra", value=float(total), step=1.0)
with col2:
    valor_pago = st.number_input("Valor pago em dinheiro", value=0.0, step=1.0)

if st.button("Calcular Troco", type="primary"):
    if valor_pago < valor_compra:
        st.error("O valor pago é menor que o valor da compra.")
    else:
        troco = valor_pago - valor_compra
        st.success(f"**Troco:** R$ {troco:.2f}")
