import streamlit as st
import pandas as pd
import datetime
import os
import random
import time

st.experimental_set_query_params(t=int(time.time()))

FILE_NAME = "ket_qua_tro_choi.csv"
TIME_LIMIT = 15

QUESTIONS = [
    {"q": "Thủ đô của Việt Nam là gì?", "a": ["A. Hồ Chí Minh", "B. Đà Nẵng", "C. Hà Nội", "D. Hải Phòng"], "c": "C. Hà Nội"},
    {"q": "Số nào là số nguyên tố?", "a": ["A. 4", "B. 6", "C. 9", "D. 7"], "c": "D. 7"},
    {"q": "Hành tinh gần Mặt trời nhất?", "a": ["A. Sao Kim", "B. Sao Thủy", "C. Sao Hỏa", "D. Trái Đất"], "c": "B. Sao Thủy"},
    {"q": "Tác giả Truyện Kiều?", "a": ["A. Nguyễn Khuyến", "B. Nguyễn Du", "C. Phan Bội Châu", "D. Hồ Xuân Hương"], "c": "B. Nguyễn Du"},
    {"q": "Đại dương lớn nhất?", "a": ["A. Ấn Độ Dương", "B. Đại Tây Dương", "C. Bắc Băng Dương", "D. Thái Bình Dương"], "c": "D. Thái Bình Dương"},
    {"q": "Trong các phát biểu sau, đâu là phát biểu ĐÚNG?", "a": ["A. Python là ngôn ngữ lập trình bậc thấp","B. Trái Đất có 2 Mặt Trăng","C. Nước sôi ở 100°C (điều kiện thường)","D. Con người không cần oxy để sống"], "c": "C. Nước sôi ở 100°C (điều kiện thường)"},
    {"q": "Trong các phát biểu sau, đâu là phát biểu SAI?", "a": ["A. 1 giờ = 60 phút","B. Cá voi là động vật có vú","C. Ánh sáng truyền chậm hơn âm thanh","D. Con người có 5 giác quan cơ bản"], "c": "C. Ánh sáng truyền chậm hơn âm thanh"},
]

def save_result(name, score):
    df_new = pd.DataFrame({
        "Thời gian": [datetime.datetime.now().strftime("%d/%m/%Y %H:%M")],
        "Tên": [name],
        "Điểm": [score]
    })
    if os.path.exists(FILE_NAME):
        df = pd.concat([pd.read_csv(FILE_NAME), df_new])
    else:
        df = df_new
    df.to_csv(FILE_NAME, index=False)

st.set_page_config(page_title="Ai Là Triệu Phú", page_icon="💰")

st.markdown("""
<style>
body {background-color: #000814; color: white;}
.title {text-align:center; font-size:40px; color: gold; font-weight:bold;}
.question {font-size:26px; margin:20px 0;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💰 AI LÀ SỐ 1 CỦA LỚP 10B2</div>', unsafe_allow_html=True)

if "step" not in st.session_state:
    st.session_state.step = "start"
    st.session_state.q_list = random.sample(QUESTIONS, len(QUESTIONS))
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.start_time = time.time()

if st.session_state.step == "start":
    name = st.text_input("Nhập tên người chơi:")
    if st.button("BẮT ĐẦU"):
        if len(name.strip()) < 3:
            st.warning("Tên không hợp lệ")
        else:
            st.session_state.name = name
            st.session_state.step = "play"
            st.rerun()

elif st.session_state.step == "play":
    q = st.session_state.q_list[st.session_state.q_index]
    st.progress((st.session_state.q_index+1)/len(st.session_state.q_list))

    st.markdown(f"<div class='question'>{q['q']}</div>", unsafe_allow_html=True)

    cols = st.columns(2)
    for i, choice in enumerate(q['a']):
        if cols[i%2].button(choice, key=choice) and not st.session_state.answered:
            st.session_state.answered = True
            if choice == q['c']:
                st.success("✔ Chính xác!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Sai! Đáp án đúng: {q['c']}")

    # TIMER ĐẾM NGƯỢC MƯỢT
    t = TIME_LIMIT - int(time.time() - st.session_state.start_time)
    st.markdown(f"## ⏱️ {max(t,0)} giây")

    if t > 0 and not st.session_state.answered:
        time.sleep(1)
        st.rerun()

    if t <= 0 and not st.session_state.answered:
        st.error("Hết giờ!")
        st.session_state.answered = True

    if st.session_state.answered:
        if st.button("TIẾP TỤC"):
            st.session_state.q_index += 1
            st.session_state.answered = False
            st.session_state.start_time = time.time()

            if st.session_state.q_index >= len(st.session_state.q_list):
                save_result(st.session_state.name, st.session_state.score)
                st.session_state.step = "end"
            st.rerun()

elif st.session_state.step == "end":
    st.balloons()
    st.header("🎉 HOÀN THÀNH")
    st.write(f"Người chơi: {st.session_state.name}")
    st.write(f"Điểm: {st.session_state.score}")

    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        st.subheader("🏆 BXH")
        st.dataframe(df.sort_values(by="Điểm", ascending=False).head(10))

    if st.button("CHƠI LẠI"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
