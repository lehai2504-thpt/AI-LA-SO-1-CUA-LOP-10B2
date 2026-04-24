import streamlit as st
import pandas as pd
import datetime
import os
import random
import time

FILE_NAME = "ket_qua_tro_choi.csv"
TIME_LIMIT = 10

# ======================
# CÂU HỎI
# ======================
QUESTIONS_SINGLE = [
    {"q": "Lớp ảnh dùng để làm gì?",
     "a": ["A. Lưu đối tượng", "B. Nền trắng", "C. Công cụ vẽ", "D. Thư mục"],
     "c": "A. Lưu đối tượng"},
]

QUESTIONS_MULTI = [
    {"q": "Thiết bị nhập?",
     "a": ["A. Bàn phím", "B. Chuột", "C. Màn hình", "D. Máy in"],
     "c": ["A. Bàn phím", "B. Chuột"]},
]

QUESTIONS = QUESTIONS_SINGLE + QUESTIONS_MULTI

# ======================
# SESSION
# ======================
if "step" not in st.session_state:
    st.session_state.step = "start"
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.start_time = time.time()

# ======================
# START
# ======================
if st.session_state.step == "start":
    name = st.text_input("Tên")
    lop = st.text_input("Lớp")

    if st.button("Bắt đầu"):
        if name and lop:
            st.session_state.name = name
            st.session_state.lop = lop
            st.session_state.step = "play"
            st.session_state.start_time = time.time()
            st.rerun()

# ======================
# GAME
# ======================
elif st.session_state.step == "play":
    q = QUESTIONS[st.session_state.q_index]

    timer_placeholder = st.empty()

    # tính thời gian
    elapsed = time.time() - st.session_state.start_time
    remaining = int(TIME_LIMIT - elapsed)
    time_up = remaining <= 0

    timer_placeholder.markdown(f"## ⏱️ {max(remaining,0)} giây")

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
    # TIẾP TỤC
    # ======================
    if st.session_state.answered:
        if st.button("Tiếp tục"):
            st.session_state.q_index += 1
            st.session_state.start_time = time.time()
            st.session_state.answered = False

            if st.session_state.q_index >= len(QUESTIONS):
                st.session_state.step = "end"

            st.rerun()

    # ======================
    # REFRESH NHẸ (KHÔNG TREO)
    # ======================
    if not st.session_state.answered:
        time.sleep(1)
        st.rerun()

# ======================
# END
# ======================
elif st.session_state.step == "end":
    st.success("🎉 Hoàn thành")
    st.write("Điểm:", st.session_state.score)
