import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from carregar_dados import carregar_vendas


dados = carregar_vendas()


st.title("Dashboard de Vendas")


faturamento_total = dados["Faturamento"].sum()

quantidade_total = dados["Quantidade"].sum()

ticket_medio = dados["Faturamento"].mean()


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Faturamento Total",
        f"R$ {faturamento_total}"
    )


with col2:
    st.metric(
        "Quantidade Vendida",
        f"{quantidade_total} unidades"
    )


with col3:
    st.metric(
        "Ticket Médio",
        f"R$ {ticket_medio:.2f}"
    )


st.subheader("Faturamento por Produto")


faturamento_produto = dados.groupby("Produto")["Faturamento"].sum()


fig, ax = plt.subplots()

faturamento_produto.plot(
    kind="bar",
    ax=ax
)


ax.set_xlabel("Produto")
ax.set_ylabel("Faturamento (R$)")
ax.set_title("Faturamento por Produto")


st.pyplot(fig)

st.subheader("Faturamento por Categoria")


faturamento_categoria = dados.groupby("Categoria")["Faturamento"].sum()


fig, ax = plt.subplots()


faturamento_categoria.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax
)


ax.set_ylabel("")


st.pyplot(fig)

st.subheader("Evolução do Faturamento")


dados["Data"] = pd.to_datetime(dados["Data"])


vendas_por_data = dados.groupby("Data")["Faturamento"].sum()


fig, ax = plt.subplots()


vendas_por_data.plot(
    kind="line",
    marker="o",
    ax=ax
)


ax.set_xlabel("Data")
ax.set_ylabel("Faturamento (R$)")
ax.set_title("Evolução das Vendas")


ax.grid()


st.pyplot(fig)

st.subheader("Dados das vendas")

st.dataframe(dados)