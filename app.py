import streamlit as st
from gemini_agent import generate_plan
from rl import update_strategy

st.set_page_config(page_title="Smart Goal Planner Agent", layout="centered")

st.title("🧠 Smart Goal Planner Agent")
st.write("Plan your goals with Claude AI and refine with feedback.")

goal = st.text_input("Enter your goal (e.g., Learn Python in 5 days):")

if st.button("Generate Plan") and goal:
    subtasks = generate_plan(goal)
    st.session_state['subtasks'] = subtasks
    st.session_state['feedback'] = ["Not Reviewed"] * len(subtasks)

if 'subtasks' in st.session_state:
    st.subheader("📅 N-Day Plan:")
    for i, task in enumerate(st.session_state['subtasks']):
        st.markdown(f"**Day {i+1}:** {task}")

    st.subheader("🗳️ Feedback:")
    for i in range(len(st.session_state['subtasks'])):
        st.session_state['feedback'][i] = st.radio(
            f"Was Day {i+1} helpful?",
            ["Not Reviewed", "Yes", "No"],
            key=f"feedback_{i}",
            index=["Not Reviewed", "Yes", "No"].index(st.session_state['feedback'][i])
        )

    if st.button("Submit Feedback"):
        feedback = [1 if fb == "Yes" else 0 for fb in st.session_state['feedback']]
        update_strategy(feedback)
        st.success("✅ Feedback submitted and learning updated!")
