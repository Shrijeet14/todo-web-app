import functions
import streamlit as st
import time
import os

if not os.path.exists("Todos.txt"):
    with open("Todos.txt","w") as file :
        pass

time_now = time.strftime("%b %d , %Y")
st.title("MY TODOs")
st.subheader(time_now)

Todos= functions.file_reader("Todos.txt")

def add_todo():
    new_todo=st.session_state['new_todo']+'\n'
    Todos.append(new_todo)
    functions.file_writer(Todos,'Todos.txt')

st.write("Your Pending Todos are :- ")
for index,todo in enumerate(Todos) :
    checkbox=st.checkbox(todo,key=todo)
    if checkbox :
        Todos.pop(index)
        functions.file_writer(Todos,'Todos.txt')
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo :- ",placeholder="Write Your Todo Here....",on_change=add_todo,key='new_todo')
