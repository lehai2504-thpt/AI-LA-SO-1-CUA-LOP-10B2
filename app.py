import streamlit as st
import pandas as pd
import datetime
import os
import random
import time

FILE_NAME = "ket_qua_tro_choi.csv"

# ======================
# 📚 CÂU HỎI
# ======================
QUESTIONS_SINGLE = [
    {"q": "Khi thiết kế một đối tượng đồ họa phức tạp, tại sao ta nên đặt mỗi thành phần trên một lớp ảnh riêng biệt?",
     "a": ["A. Để làm cho dung lượng tệp nhỏ hơn",
           "B. Để phần mềm tự phối màu",
           "C. Để dễ dàng chỉnh sửa riêng từng đối tượng",
           "D. Để tất cả luôn hiển thị cùng lúc"],
     "c": "C. Để dễ dàng chỉnh sửa riêng từng đối tượng"},

    {"q": "GIMP cung cấp các lệnh cơ bản nào để làm việc với lớp ảnh?",
     "a": ["A. Vẽ, tô màu, tẩy",
           "B. Thêm, xoá, nhân đôi, ẩn/hiện, đổi thứ tự",
           "C. Chỉ tạo và xoá lớp",
           "D. Thay đổi font chữ"],
     "c": "B. Thêm, xoá, nhân đôi, ẩn/hiện, đổi thứ tự"},

    {"q": "Để ẩn/hiện lớp ảnh trong GIMP, nhấn biểu tượng nào?",
     "a": ["A. Cái kéo", "B. Dấu +", "C. Thùng rác", "D. Con mắt"],
     "c": "D. Con mắt"},

    {"q": "Thay đổi thứ tự lớp ảnh sẽ dẫn đến điều gì?",
     "a": ["A. Thay đổi kích thước",
           "B. Thay đổi màu sắc",
           "C. Thay đổi hiển thị, lớp trên che lớp dưới",
           "D. Làm đối tượng biến mất"],
     "c": "C. Thay đổi hiển thị, lớp trên che lớp dưới"},

    {"q": "Lớp bóng đổ nên đặt ở đâu?",
     "a": ["A. Trên lớp chữ",
           "B. Dưới lớp chữ",
           "C. Dưới nền",
           "D. Ở file khác"],
     "c": "B. Dưới lớp chữ"},

    {"q": "Thao tác nào giúp di chuyển lớp?",
     "a": ["A. Nút mũi tên lên/xuống",
           "B. Nháy đúp chuột",
           "C. Delete",
           "D. Dùng Text tool"],
     "c": "A. Nút mũi tên lên/xuống"},

    {"q": "Lớp ảnh là gì?",
     "a": ["A. Nơi lưu trữ nhóm đối tượng",
           "B. Nền trắng",
           "C. Công cụ vẽ",
           "D. Thư mục ảnh"],
     "c": "A. Nơi lưu trữ nhóm đối tượng"},

    {"q": "Hướng tập trung vào một lớp dùng để làm gì?",
     "a": ["A. Phóng to lớp",
           "B. Ẩn lớp khác để dễ thao tác",
           "C. Gộp lớp",
           "D. Căn giữa"],
     "c": "B. Ẩn lớp khác để dễ thao tác"},
]

QUESTIONS_MULTI = [
    {"q": "Ban giám hiệu trường Nguyễn Trãi xã Bờ Y hiện tại gồm?",
     "a": ["A. Phạm Đại Cảnh",
           "B. Lê Cao Nguyên",
           "C. Nguyễn Tiến Định",
           "D. Hồ Trung Cang"],
     "c": ["A. Phạm Đại Cảnh", "B. Lê Cao Nguyên", "D. Hồ Trung Cang"]},

    {"q": "Thông tin ĐÚNG về trường Nguyễn Trãi xã Bờ Y là?",
     "a": ["A. Hình thành năm 2004",
           "B. Hình thành năm 2005",
           "C. Đc: 49 Phan Bội Châu",
           "D. Đc: 59 Phan Bội Châu"],
     "c": ["A. Hình thành năm 2004", "C. Đc: 49 Phan Bội Châu"]},
]

QUESTIONS = random.sample(QUESTIONS_SINGLE, len(QUESTIONS_SINGLE)) + \
            random.sample(QUESTIONS_MULTI, len(QUESTIONS_MULTI))

# ======================
# 💾 SAVE
# ======================
def save_result(name, lop, score):
    df_new = pd.DataFrame({
        "Thời gian": [datetime.datetime.now().strftime("%d/%m/%Y %H:%M")],
        "Tên": [name],
        "Lớp": [lop],
        "Điểm": [score]
    })
    if os.path.exists(FILE_NAME):
        df = pd.concat([pd.read_csv(FILE_NAME), df_new])
    else:
        df = df_new
    df.to_csv(FILE_NAME, index=False)

# ======================
# UI
# ======================
st.set_page_config(page_title="Ai Là Triệu Phú", page_icon="💰")

# ======================
# SESSION
# ======================
if "step" not in st.session_state:
    st.session_state.step = "start"
    st.session_state.q_list = QUESTIONS
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.start_time = time.time()

# ======================
# START
# ======================
if st.session_state.step == "start":
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Nhập tên:")
    with col2:
        lop = st.text_input("Nhập lớp:")

    if st.button("BẮT ĐẦU"):
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
    q = st.session_state.q_list[st.session_state.q_index]

    # TIMER
    elapsed = int(time.time() - st.session_state.start_time)
    remaining = max(10 - elapsed, 0)
    time_up = remaining <= 0

    st.write(f"⏱️ {remaining} giây")

    # ======================
    # MULTI
    # ======================
    if isinstance(q["c"], list):
        selected = []
        for choice in q["a"]:
            if st.checkbox(choice, disabled=time_up):
                selected.append(choice)

        if st.button("XÁC NHẬN", disabled=time_up):
            st.session_state.answered = True
            if set(selected) == set(q["c"]):
                st.session_state.score += 1
                st.success("✔ Đúng")
            else:
                st.error("❌ Sai")

    # ======================
    # SINGLE (ĐÃ FIX)
    # ======================
    else:
        cols = st.columns(2)
        for i, choice in enumerate(q['a']):
            if cols[i % 2].button(choice, disabled=time_up) and not st.session_state.answered:
                st.session_state.answered = True
                if choice == q['c']:
                    st.session_state.score += 1
                    st.success("✔ Đúng")
                else:
                    st.error("❌ Sai")

    # HẾT GIỜ
    if time_up and not st.session_state.answered:
        st.error("⏰ Hết giờ!")
        st.session_state.answered = True

    # AUTO REFRESH
    time.sleep(1)
    st.rerun()

    # NEXT
    if st.session_state.answered:
        if st.button("TIẾP TỤC"):
            st.session_state.q_index += 1
            st.session_state.answered = False
            st.session_state.start_time = time.time()

            if st.session_state.q_index >= len(st.session_state.q_list):
                save_result(st.session_state.name, st.session_state.lop, st.session_state.score)
                st.session_state.step = "end"

            st.rerun()

# ======================
# END
# ======================
elif st.session_state.step == "end":
    st.write("🎉 Hoàn thành")
    st.write(st.session_state.score)
