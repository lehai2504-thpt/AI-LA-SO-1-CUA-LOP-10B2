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
QUESTIONS = [
    {"q": "Thủ đô của Việt Nam là gì?",
     "a": ["A. Hồ Chí Minh", "B. Đà Nẵng", "C. Hà Nội", "D. Hải Phòng"],
     "c": "C. Hà Nội"},

    {"q": "Số nào là số nguyên tố?",
     "a": ["A. 4", "B. 6", "C. 9", "D. 7"],
     "c": "D. 7"},

    {"q": "Hành tinh gần Mặt trời nhất?",
     "a": ["A. Sao Kim", "B. Sao Thủy", "C. Sao Hỏa", "D. Trái Đất"],
     "c": "B. Sao Thủy"},

    {"q": "Tác giả Truyện Kiều?",
     "a": ["A. Nguyễn Khuyến", "B. Nguyễn Du", "C. Phan Bội Châu", "D. Hồ Xuân Hương"],
     "c": "B. Nguyễn Du"},

    {"q": "Đại dương lớn nhất?",
     "a": ["A. Ấn Độ Dương", "B. Đại Tây Dương", "C. Bắc Băng Dương", "D. Thái Bình Dương"],
     "c": "D. Thái Bình Dương"},

    # ======================
    # ✅ ĐÚNG/SAI
    # ======================
    {"q": "Python là ngôn ngữ thông dịch?",
     "a": ["A. Đúng", "B. Sai", "C. Không biết", "D. Tùy trường hợp"],
     "c": "A. Đúng"},

    {"q": "Trái Đất là hành tinh lớn nhất?",
     "a": ["A. Đúng", "B. Sai", "C. Gần đúng", "D. Không xác định"],
     "c": "B. Sai"},

    # ======================
    # ✅ NHIỀU ĐÁP ÁN ĐÚNG
    # ======================
    {"q": "Ngôn ngữ lập trình nào sau đây là ngôn ngữ thông dịch?",
     "a": ["A. Python", "B. Java", "C. C++", "D. JavaScript"],
     "c": ["A. Python", "D. JavaScript"]},

    {"q": "Thiết bị nào là thiết bị nhập?",
     "a": ["A. Bàn phím", "B. Chuột", "C. Màn hình", "D. Máy in"],
     "c": ["A. Bàn phím", "B. Chuột"]},
]

# ======================
# 💾 LƯU
# ======================
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

# ======================
# 🎨 UI
# ======================
st.set_page_config(page_title="Ai Là Triệu Phú", page_icon="💰")

st.markdown("""
<style>
.title {text-align:center; font-size:40px; color: gold; font-weight:bold;}
.question {font-size:26px; margin:20px 0;}
.timer {font-size:22px; color: cyan;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💰 AI LÀ SỐ 1 CỦA LỚP 10B2</div>', unsafe_allow_html=True)

# ======================
# 🔄 SESSION
# ======================
if "step" not in st.session_state:
    st.session_state.step = "start"
    st.session_state.q_list = random.sample(QUESTIONS, len(QUESTIONS))
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.start_time = time.time()

# ======================
# 🚀 START
# ======================
if st.session_state.step == "start":
    name = st.text_input("Nhập tên người chơi:")
    if st.button("BẮT ĐẦU"):
        if len(name.strip()) < 3:
            st.warning("Tên không hợp lệ")
        else:
            st.session_state.name = name
            st.session_state.step = "play"
            st.session_state.start_time = time.time()
            st.rerun()

# ======================
# 🎮 GAME
# ======================
elif st.session_state.step == "play":
    q = st.session_state.q_list[st.session_state.q_index]

    st.progress((st.session_state.q_index+1)/len(st.session_state.q_list))
    st.markdown(f"<div class='question'>{q['q']}</div>", unsafe_allow_html=True)

    # ======================
    # 👉 PHÂN LOẠI CÂU HỎI
    # ======================
    if isinstance(q["c"], list):
        # ---- nhiều đáp án đúng ----
        selected = []
        for choice in q["a"]:
            if st.checkbox(choice, key=f"{choice}_{st.session_state.q_index}"):
                selected.append(choice)

        if st.button("XÁC NHẬN"):
            st.session_state.answered = True

            if set(selected) == set(q["c"]):
                st.success("✔ Chính xác!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Sai! Đáp án đúng: {', '.join(q['c'])}")

    else:
        # ---- 1 đáp án ----
        cols = st.columns(2)
        for i, choice in enumerate(q['a']):
            if cols[i % 2].button(choice, key=f"{choice}_{st.session_state.q_index}") and not st.session_state.answered:
                st.session_state.answered = True
                if choice == q['c']:
                    st.success("✔ Chính xác!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Sai! Đáp án đúng: {q['c']}")

    # ======================
    # ⏱️ TIMER
    # ======================
    elapsed = int(time.time() - st.session_state.start_time)
    remaining = max(15 - elapsed, 0)

    st.markdown(f"<div class='timer'>⏱️ {remaining} giây</div>", unsafe_allow_html=True)

    if remaining <= 0 and not st.session_state.answered:
        st.error("⏰ Hết giờ!")
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

# ======================
# 🏁 END
# ======================
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

# ======================
# 📂 QUẢN LÝ
# ======================
st.markdown("---")
st.subheader("📂 Quản lý kết quả")

col1, col2 = st.columns(2)

with col1:
    if st.button("📊 XEM KẾT QUẢ"):
        if os.path.exists(FILE_NAME):
            df = pd.read_csv(FILE_NAME)
            st.dataframe(df.sort_values(by="Điểm", ascending=False))
        else:
            st.warning("Chưa có dữ liệu!")

with col2:
    st.write("🗑️ XÓA KẾT QUẢ")
    password = st.text_input("Nhập mật khẩu:", type="password")

    if st.button("XÁC NHẬN XÓA"):
        if password == "2504":
            if os.path.exists(FILE_NAME):
                os.remove(FILE_NAME)
                st.success("✅ Đã xóa!")
            else:
                st.warning("Không có file!")
        else:
            st.error("❌ Sai mật khẩu!")
