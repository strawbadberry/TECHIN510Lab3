import streamlit as st
from pydantic import BaseModel
import database

# Define Pydantic model for Task
class Task(BaseModel):
    name: str
    description: str
    state: str

def main():
    st.title("Todo App")

    with st.form("Task Form"):
        name = st.text_input("Task Name")
        description = st.text_area("Task Description")
        state = st.selectbox("State", options=["planned", "in-progress", "done"])
        submitted = st.form_submit_button("Submit Task")

        if submitted:
            database.add_task((name, description, state))
            st.success("Task Added Successfully")

    st.subheader("All Tasks")
    tasks = database.get_all_tasks()
    for task in tasks:
        st.write(f"ID: {task[0]}, Name: {task[1]}, Description: {task[2]}, State: {task[3]}")
        if st.button("Delete", key=task[0]):
            database.delete_task(task[0])
            st.experimental_rerun()

if __name__ == "__main__":
    main()
