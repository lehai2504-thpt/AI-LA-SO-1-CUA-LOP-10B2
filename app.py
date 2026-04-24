import streamlit as st
import time
import random

TIME_LIMIT = 10

QUESTIONS = [
    {"q": "Lớp ảnh dùng để làm gì?",
     "a": ["A. Lưu đối tượng", "B. Nền trắng", "C. Công cụ", "D. Thư mục"],
     "c": "A. Lưu đối tượng"},

    {"q": "Thiết bị nhập?",
     "a": ["A. Bàn phím", "B. Chuột", "C. Màn hình", "D. Máy in"],
     "c": ["A. Bàn phím", "B. Chuột"]},
]

# ======================
# INIT
# ======================
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.answered = False

q = QUESTIONS[st.session_state.q_index]

# ======================
# TIMER
# ======================
elapsed = time.time() - st.session_state.start_time
remaining = int(TIME_LIMIT - elapsed)
time_up = remaining <= 0

st.write(f"⏱️ {max(remaining,0)} giây")

# ======================
# SINGLE
# ======================
if isinstance(q["c"], str):
    for choice in q["a"]:
        if st.button(choice, disabled=time_up or st.session_state.answered):
            st.session_state.answered = True
            if choice == q["c"]:
                st.success("✔ Đúng")
                st.session_state.score += 1
            else:
                st.error("❌ Sai")

# ======================
# MULTI
# ======================
else:
    selected = []
    for choice in q["a"]:
        if st.checkbox(choice, disabled=time_up or st.session_state.answered):
            selected.append(choice)

    if st.button("XÁC NHẬN", disabled=time_up or st.session_state.answered):
        st.session_state.answered = True
        if set(selected) == set(q["c"]):
            st.success("✔ Đúng")
            st.session_state.score += 1
        else:
            st.error("❌ Sai")

# ======================
# HẾT GIỜ
# ======================
if time_up and not st.session_state.answered:
    st.session_state.answered = True
    st.error("⏰ Hết giờ!")

# ======================
# NEXT
# ======================
if st.session_state.answered:
    if st.button("Tiếp tục"):
        st.session_state.q_index += 1
        st.session_state.start_time = time.time()
        st.session_state.answered = False

        if st.session_state.q_index >= len(QUESTIONS):
            st.success(f"🎉 Hoàn thành - Điểm: {st.session_state.score}")
            st.stop()

        st.rerun()

# ======================
# AUTO REFRESH AN TOÀN
# ======================
if not st.session_state.answered:
    st.experimental_set_query_params(t=int(time.time()))
