import streamlit as st

# 🎨 Set Page Config
st.set_page_config(page_title="Task Manager ✅", page_icon="📝", layout="centered")

# 🔹 Task List
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# 🎨 Custom CSS for Styling
st.markdown(
    """
    <style>
    body {
        background-color: #F4F4F4;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .title {
        color: #FF5733;
        text-align: center;
        font-size: 40px;
    }
    .task-text {
        font-size: 20px;
    }
    .completed {
        text-decoration: line-through;
        color: green;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🌟 App Title
st.markdown('<h1 class="title">📝 Task Manager</h1>', unsafe_allow_html=True)

# 📌 Input Field for New Task
new_task = st.text_input("➕ Add a new task:", placeholder="Type your task here...")

if st.button("Add Task"):
    if new_task.strip():
        st.session_state["tasks"].append({"task": new_task, "completed": False})
        st.experimental_rerun()
    else:
        st.warning("⚠️ Task cannot be empty!")

# 🔍 Display Tasks
st.markdown("### 🏗️ Your Tasks:")
for i, task in enumerate(st.session_state["tasks"]):
    col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
    
    # 📝 Show Task with Completion Status
    with col1:
        if task["completed"]:
            st.markdown(f'<p class="completed">✔️ {task["task"]}</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="task-text">❌ {task["task"]}</p>', unsafe_allow_html=True)
    
    # ✅ Mark as Completed
    with col2:
        if not task["completed"]:
            if st.button(f"✅ Done {i}", key=f"complete_{i}"):
                st.session_state["tasks"][i]["completed"] = True
                st.experimental_rerun()
    
    # ❌ Delete Task
    with col3:
        if st.button(f"🗑️ Delete {i}", key=f"delete_{i}"):
            del st.session_state["tasks"][i]
            st.experimental_rerun()

# 🆘 Help Section
with st.expander("ℹ️ Help"):
    st.markdown("""
    - **➕ Add Task**: Type in a task and click 'Add Task'  
    - **✅ Mark as Done**: Click the '✅ Done' button  
    - **🗑️ Delete Task**: Click the '🗑️ Delete' button  
    """)

# 🚪 Exit Button
if st.button("🚪 Exit"):
    st.stop()
