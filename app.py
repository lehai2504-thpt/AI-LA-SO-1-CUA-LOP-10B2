import streamlit as st
import pandas as pd
import datetime
import os
import random
import time

FILE_NAME = "ket_qua_tro_choi.csv"

# ======================
# 📚 CÂU HỎI 1 ĐÁP ÁN (8 CÂU)
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

# ======================
# 📚 CÂU HỎI NHIỀU ĐÁP ÁN (2 CÂU)
# ======================
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
# 💾 LƯU (THÊM LỚP)
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
    st.session_state.q_list = QUESTIONS
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.start_time = time.time()

# ======================
# 🚀 START (THÊM Ô LỚP)
# ======================
if st.session_state.step == "start":
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Nhập tên người chơi:")

    with col2:
        lop = st.text_input("Nhập lớp:")

    if st.button("BẮT ĐẦU"):
        if len(name.strip()) < 3 or len(lop.strip()) < 2:
            st.warning("Nhập thiếu thông tin!")
        else:
            st.session_state.name = name
            st.session_state.lop = lop
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

    if isinstance(q["c"], list):
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
        cols = st.columns(2)
        for i, choice in enumerate(q['a']):
            if cols[i % 2].button(choice, key=f"{choice}_{st.session_state.q_index}") and not st.session_state.answered:
                st.session_state.answered = True
                if choice == q['c']:
                    st.success("✔ Chính xác!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Sai! Đáp án đúng: {q['c']}")

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
                save_result(st.session_state.name, st.session_state.lop, st.session_state.score)
                st.session_state.step = "end"

            st.rerun()

# ======================
# 🏁 END
# ======================
elif st.session_state.step == "end":
    st.balloons()
    st.header("🎉 HOÀN THÀNH")
    st.write(f"Người chơi: {st.session_state.name}")
    st.write(f"Lớp: {st.session_state.lop}")
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
