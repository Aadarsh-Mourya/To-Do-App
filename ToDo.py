import streamlit as st
import json
from datetime import datetime
from enum import Enum
import os

# Constants
JSON_FILE = "tasks.json"

class TaskStatus(Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    ABORTED = "Aborted"

def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(JSON_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def main():
    st.title("Enhanced To-Do List")
    
    # Set solid background color
    st.markdown("""
        <style>
        .stApp {
            background-color: #010101;
        }
        .task-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
            padding: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'tasks' not in st.session_state:
        st.session_state.tasks = load_tasks()
    if 'show_add_task' not in st.session_state:
        st.session_state.show_add_task = False
    if 'current_filter' not in st.session_state:
        st.session_state.current_filter = "All"

    # Sidebar for filtering tasks
    st.sidebar.header("Task Filters")
    filter_options = ["All"] + [status.value for status in TaskStatus]
    st.session_state.current_filter = st.sidebar.radio("Show tasks:", filter_options)

    # Task statistics in sidebar
    st.sidebar.header("Task Statistics")
    status_counts = {}
    for status in TaskStatus:
        count = len([t for t in st.session_state.tasks if t['status'] == status.value])
        status_counts[status.value] = count
        st.sidebar.text(f"{status.value}: {count}")

    # Main content area with grid layout
    col1, col2, col3, col4 = st.columns(4)
    
    # Add Task button in first column
    with col1:
        if st.button("➕ Add New Task"):
            st.session_state.show_add_task = not st.session_state.show_add_task

    # Add task form
    if st.session_state.show_add_task:
        with st.expander("New Task Form", expanded=True):
            title = st.text_input("Task Title")
            description = st.text_area("Description")
            url = st.text_input("Related URL")
            
            if st.button("Create Task"):
                if title:
                    new_task = {
                        "id": datetime.now().strftime("%Y%m%d%H%M%S"),
                        "title": title,
                        "description": description,
                        "url": url,
                        "status": TaskStatus.TODO.value,
                        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    st.session_state.tasks.append(new_task)
                    save_tasks(st.session_state.tasks)
                    st.session_state.show_add_task = False
                    st.success("Task added successfully!")
                    st.rerun()

    # Display filtered tasks in grid
    st.markdown("<div class='task-grid'>", unsafe_allow_html=True)
    
    filtered_tasks = st.session_state.tasks
    if st.session_state.current_filter != "All":
        filtered_tasks = [t for t in st.session_state.tasks if t['status'] == st.session_state.current_filter]

    for task in filtered_tasks:
        with st.container():
            with st.expander(f"📌 {task['title']}", expanded=False):
                st.text_input("Title", task['title'], key=f"title_{task['id']}")
                st.text_area("Description", task['description'], key=f"desc_{task['id']}")
                st.text_input("URL", task['url'], key=f"url_{task['id']}")
                
                # Status update using radio buttons
                task['status'] = st.radio(
                    "Status",
                    [status.value for status in TaskStatus],
                    index=[status.value for status in TaskStatus].index(task['status']),
                    key=f"status_{task['id']}"
                )
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Save", key=f"save_{task['id']}"):
                        save_tasks(st.session_state.tasks)
                        st.success("Updated!")
                with col2:
                    if st.button("Delete", key=f"delete_{task['id']}"):
                        st.session_state.tasks.remove(task)
                        save_tasks(st.session_state.tasks)
                        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # Clear all tasks button in sidebar
    if st.sidebar.button("Clear All Tasks"):
        if st.session_state.tasks:
            st.session_state.tasks = []
            save_tasks([])
            st.rerun()

if __name__ == "__main__":
    main()