import streamlit as st
import pandas as pd
import datetime
import os
import random
import time

FILE_NAME = "ket_qua_tro_choi.csv"

QUESTIONS = [
    {"q": "Thủ đô của Việt Nam là gì?", "a": ["Hồ Chí Minh", "Đà Nẵng", "Hà Nội", "Hải Phòng"], "c": "Hà Nội"},
    {"q": "Số nào sau đây là số nguyên tố?", "a": ["4", "6", "9", "7"], "c": "7"},
    {"q": "Hành tinh nào gần Mặt trời nhất?", "a": ["Sao Kim", "Sao Thủy", "Sao Hỏa", "Trái Đất"], "c": "Sao Thủy"},
    {"q": "Tác giả của 'Truyện Kiều' là ai?", "a": ["Nguyễn Khuyến", "Nguyễn Du", "Phan Bội Châu", "Hồ Xuân Hương"], "c": "Nguyễn Du"},
    {"q": "Đại dương nào rộng nhất thế giới?", "a": ["Ấn Độ Dương", "Đại Tây Dương", "Bắc Băng Dương", "Thái Bình Dương"], "c": "Thái Bình Dương"},
    {"q": "Công thức hóa học của nước là gì?", "a": ["CO2", "H2O", "O2", "H2SO4"], "c": "H2O"},
    {"q": "Đỉnh núi nào cao nhất thế giới?", "a": ["Everest", "K2", "Phan Xi Păng", "Lhotse"], "c": "Everest"},
    {"q": "Năm 2024 có bao nhiêu ngày?", "a": ["364", "365", "366", "367"], "c": "366"},
    {"q": "Đơn vị tiền tệ của Nhật Bản là gì?", "a": ["Won", "Yên", "Nhân dân tệ", "Đô la"], "c": "Yên"},
    {"q": "Loài vật nào là chúa sơn lâm?", "a": ["Voi", "Sư tử", "Hổ", "Báo"], "c": "Hổ"},
]

# --- LƯU KẾT QUẢ ---
def save_result(name, score):
    data = {
        "Thời gian": [datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")],
        "Tên": [name],
        "Điểm": [score]
    }
    df_new = pd.DataFrame(data)

    if os.path.exists(FILE_NAME):
        df_old = pd.read_csv(FILE_NAME)
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = df_new

    df.to_csv(FILE_NAME, index=False)

# --- CẤU HÌNH ---
st.set_page_config(page_title="Ai Là Triệu Phú", page_icon="💰", layout="centered")

# --- STYLE ---
st.markdown("""
<style>
.big-title {text-align:center; font-size:40px; font-weight:bold; color:gold;}
.question {font-size:22px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">💰 AI LÀ TRIỆU PHÚ</div>', unsafe_allow_html=True)

# --- SESSION ---
if "step" not in st.session_state:
    st.session_state.step = "start"
    st.session_state.q_list = random.sample(QUESTIONS, len(QUESTIONS))
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.start_time = time.time()

# --- NHẬP TÊN ---
if st.session_state.step == "start":
    name = st.text_input("Nhập tên:")
    if st.button("Bắt đầu"):
        if len(name.strip()) < 3:
            st.warning("Tên không hợp lệ")
        else:
            st.session_state.name = name
            st.session_state.step = "play"
            st.rerun()

# --- GAME ---
elif st.session_state.step == "play":
    q_idx = st.session_state.q_index
    q = st.session_state.q_list[q_idx]

    st.progress((q_idx+1)/10)
    st.markdown(f"<div class='question'>Câu {q_idx+1}: {q['q']}</div>", unsafe_allow_html=True)

    ans = st.radio("Chọn đáp án:", q['a'], key=f"q{q_idx}")

    # TIMER
    time_left = 15 - int(time.time() - st.session_state.start_time)
    st.write(f"⏱️ Thời gian còn lại: {max(time_left,0)}s")

    if time_left <= 0 and not st.session_state.answered:
        st.error("Hết giờ!")
        st.session_state.answered = True

    if st.button("Nộp") and not st.session_state.answered:
        st.session_state.answered = True
        if ans == q['c']:
            st.success("✔ Đúng!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Sai! Đáp án: {q['c']}")

    if st.session_state.answered:
        if st.button("Câu tiếp"):
            st.session_state.q_index += 1
            st.session_state.answered = False
            st.session_state.start_time = time.time()

            if st.session_state.q_index >= 10:
                save_result(st.session_state.name, st.session_state.score)
                st.session_state.step = "end"
            st.rerun()

# --- KẾT QUẢ ---
elif st.session_state.step == "end":
    st.balloons()
    st.header("🎉 Hoàn thành!")
    st.write(f"Người chơi: {st.session_state.name}")
    st.write(f"Điểm: {st.session_state.score}/10")

    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)

        st.subheader("📊 Thống kê")
        col1, col2, col3 = st.columns(3)
        col1.metric("Lượt chơi", len(df))
        col2.metric("Điểm cao nhất", df["Điểm"].max())
        col3.metric("Điểm TB", round(df["Điểm"].mean(),1))

        st.bar_chart(df["Điểm"])

        st.subheader("🏆 Top 5")
        top5 = df.sort_values(by="Điểm", ascending=False).head(5)
        st.dataframe(top5)

        st.download_button("Tải kết quả", df.to_csv(index=False), file_name="ket_qua.csv")

    if st.button("Chơi lại"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
