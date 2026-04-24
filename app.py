import streamlit as st
import pandas as pd
import datetime, os, random, time, base64
from gtts import gTTS

FILE_NAME = "ket_qua_tro_choi.csv"

QUESTIONS = [
    {"q": "Thủ đô của Việt Nam là gì?", "a": ["A. Hồ Chí Minh", "B. Đà Nẵng", "C. Hà Nội", "D. Hải Phòng"], "c": "C. Hà Nội"},
    {"q": "Số nào là số nguyên tố?", "a": ["A. 4", "B. 6", "C. 9", "D. 7"], "c": "D. 7"},
    {"q": "Hành tinh gần Mặt trời nhất?", "a": ["A. Sao Kim", "B. Sao Thủy", "C. Sao Hỏa", "D. Trái Đất"], "c": "B. Sao Thủy"},
    {"q": "Tác giả Truyện Kiều?", "a": ["A. Nguyễn Khuyến", "B. Nguyễn Du", "C. Phan Bội Châu", "D. Hồ Xuân Hương"], "c": "B. Nguyễn Du"},
    {"q": "Đại dương lớn nhất?", "a": ["A. Ấn Độ Dương", "B. Đại Tây Dương", "C. Bắc Băng Dương", "D. Thái Bình Dương"], "c": "D. Thái Bình Dương"},
]

# ---------- AUDIO ----------
def play_audio(file):
    with open(file, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}">
        </audio>
        """, unsafe_allow_html=True)

# ---------- TEXT TO SPEECH ----------
def speak(text):
    tts = gTTS(text=text, lang="vi")
    tts.save("voice.mp3")
    play_audio("voice.mp3")

# ---------- SAVE ----------
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

# ---------- UI ----------
st.set_page_config(page_title="Ai Là Triệu Phú", page_icon="💰")

st.markdown("""
<style>
body {background: radial-gradient(circle, #001d3d, #000814);}
.title {text-align:center; font-size:40px; color:gold;}
.question {text-align:center; font-size:26px; margin:20px;}
.timer {text-align:center; font-size:20px; color:#00d9ff;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💰 AI LÀ TRIỆU PHÚ</div>', unsafe_allow_html=True)

# ---------- SESSION ----------
if "step" not in st.session_state:
    st.session_state.step = "start"
    st.session_state.q_list = random.sample(QUESTIONS, len(QUESTIONS))
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.start_time = time.time()
    st.session_state.used_audience = False
    st.session_state.voice_played = False

# ---------- START ----------
if st.session_state.step == "start":
    name = st.text_input("Nhập tên:")
    if st.button("▶ BẮT ĐẦU"):
        st.session_state.name = name
        st.session_state.step = "play"
        st.rerun()

# ---------- GAME ----------
elif st.session_state.step == "play":

    q = st.session_state.q_list[st.session_state.q_index]

    st.markdown(f"<div class='question'>{q['q']}</div>", unsafe_allow_html=True)

    # 🎤 GIỌNG ĐỌC (chỉ đọc 1 lần)
    if not st.session_state.voice_played:
        speak(q["q"])
        st.session_state.voice_played = True

    # 👥 KHÁN GIẢ
    if st.button("👥 Hỏi ý kiến khán giả") and not st.session_state.used_audience:
        st.session_state.used_audience = True

        percent = {}
        correct = q["c"]

        for a in q["a"]:
            if a == correct:
                percent[a] = random.randint(40, 70)
            else:
                percent[a] = random.randint(5, 20)

        total = sum(percent.values())
        percent = {k: int(v*100/total) for k,v in percent.items()}

        df = pd.DataFrame({
            "Đáp án": list(percent.keys()),
            "Tỷ lệ (%)": list(percent.values())
        })

        st.bar_chart(df.set_index("Đáp án"))

    # ---- ANSWER ----
    cols = st.columns(2)

    for i, choice in enumerate(q["a"]):
        if cols[i%2].button(choice, key=choice):
            if not st.session_state.answered:
                st.session_state.answered = True

                if choice == q["c"]:
                    st.success("✔ Đúng!")
                    st.session_state.score += 1
                    play_audio("correct.mp3")
                else:
                    st.error(f"❌ Sai! Đáp án: {q['c']}")
                    play_audio("wrong.mp3")

    # ---- TIMER ----
    t = 15 - int(time.time() - st.session_state.start_time)
    st.markdown(f"<div class='timer'>⏱️ {max(t,0)}s</div>", unsafe_allow_html=True)

    if t <= 0 and not st.session_state.answered:
        st.error("⏰ Hết giờ!")
        st.session_state.answered = True
        play_audio("wrong.mp3")

    # ---- NEXT ----
    if st.session_state.answered:
        if st.button("➡ CÂU TIẾP"):
            st.session_state.q_index += 1
            st.session_state.answered = False
            st.session_state.start_time = time.time()
            st.session_state.voice_played = False

            if st.session_state.q_index >= len(QUESTIONS):
                save_result(st.session_state.name, st.session_state.score)
                st.session_state.step = "end"

            st.rerun()

# ---------- END ----------
elif st.session_state.step == "end":
    st.balloons()
    st.header("🎉 HOÀN THÀNH")
    st.write(f"👤 {st.session_state.name}")
    st.write(f"⭐ Điểm: {st.session_state.score}")

    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        st.subheader("🏆 BXH")
        st.dataframe(df.sort_values(by="Điểm", ascending=False).head(10))

    if st.button("🔄 CHƠI LẠI"):
        st.session_state.clear()
        st.rerun()
