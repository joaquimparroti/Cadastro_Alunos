import streamlit as st 
import pandas as pd 
import os 
import datetime
st.set_page_config( 
    page_title=("Tela de Cadastro"), 
    page_icon="👨‍🔧", 
    layout="centered" 
)

st.title("👨‍🔧Cadastro de Alunos") 

nome = st.text_input("Digite o nome do aluno") 
endereco = st.text_input("Digite o endereço do aluno") 
dt_nasc = st.date_input("Selecione a data de nascimento", min_value=datetime.date(2000, 1, 1), max_value=datetime.date(2026, 9, 10), format="DD/MM/YYYY") 
tipo_aluno = st.selectbox("Selecione o aluno", ["Manhã","Tarde","Integral" ]) 
cadastrar = st.button("Cadastrar Aluno") 



if cadastrar: 
    if cadastrar and nome=="" or endereco=="" or dt_nasc=="" or tipo_aluno=="":
     st.error('Usuário inválido!')
    else:
     with open("cad_alunos.csv", "a", encoding="utf8") as arquivo: 
        arquivo.write(f"{nome},{endereco},{dt_nasc},{tipo_aluno}\n") 
        st.success("Aluno cadastrado com sucesso!") 
elif nome=="" or endereco=="" or dt_nasc=="" or tipo_aluno=="":
        st.warning("Preencha todos os campos!")
