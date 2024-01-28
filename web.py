import streamlit as st
import functions

todos = functions.read_myList()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo.capitalize())
    functions.write_myList(todos)
    
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_myList(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="New to-do items", placeholder="Type in a new todo here to add...",
              on_change=add_todo, key='new_todo')