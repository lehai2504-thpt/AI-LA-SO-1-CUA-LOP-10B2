<!doctype html>
<html lang="vi" style="height: 100%;">
 <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ai Là Triệu Phú</title>
  <script src="https://cdn.jsdelivr.net/npm/lucide@0.263.0/dist/umd/lucide.min.js"></script>
  <script src="/_sdk/element_sdk.js"></script>
  <script src="/_sdk/data_sdk.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700;900&amp;display=swap" rel="stylesheet">
  <style>
* { box-sizing: border-box; }
html, body { height: 100%; margin: 0; padding: 0; }
body { font-family: 'Be Vietnam Pro', sans-serif; background: #000814; color: #f1f5f9; }

@keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@keyframes pulse-glow { 0%, 100% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.3); } 50% { box-shadow: 0 0 40px rgba(255, 215, 0, 0.6); } }
@keyframes confetti-fall { 0% { transform: translateY(-100%) rotate(0deg); opacity: 1; } 100% { transform: translateY(800px) rotate(720deg); opacity: 0; } }
@keyframes shimmer { 0% { background-position: -200% center; } 100% { background-position: 200% center; } }
@keyframes correctFlash { 0% { background: #065f46; } 50% { background: #10b981; } 100% { background: #065f46; } }
@keyframes wrongShake { 0%,100% { transform: translateX(0); } 20%,60% { transform: translateX(-8px); } 40%,80% { transform: translateX(8px); } }
@keyframes timerPulse { 0%,100% { transform: scale(1); } 50% { transform: scale(1.15); } }

.fade-up { animation: fadeUp 0.5s ease-out forwards; }
.fade-up-delay { animation: fadeUp 0.5s ease-out 0.1s forwards; opacity: 0; }
.fade-up-delay2 { animation: fadeUp 0.5s ease-out 0.2s forwards; opacity: 0; }
.fade-up-delay3 { animation: fadeUp 0.5s ease-out 0.3s forwards; opacity: 0; }
.pulse-glow { animation: pulse-glow 2s infinite; }
.correct-flash { animation: correctFlash 0.6s ease; }
.wrong-shake { animation: wrongShake 0.4s ease; }
.timer-critical { animation: timerPulse 0.5s infinite; color: #ef4444 !important; }

.answer-btn {
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
  padding: 9px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 600;
  text-align: center;
  cursor: pointer;
  border: 2px solid #334155;
  background: #1e293b;
  color: #e2e8f0;
  width: 100%;
  min-height: 45px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.answer-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.3);
  border-color: #f59e0b;
}
.answer-btn:disabled { cursor: not-allowed; opacity: 0.7; }
.answer-btn.correct { background: #065f46 !important; border-color: #10b981 !important; }
.answer-btn.wrong { background: #7f1d1d !important; border-color: #ef4444 !important; }

.confetti-piece {
  position: fixed;
  width: 10px;
  height: 10px;
  top: -20px;
  animation: confetti-fall linear forwards;
  z-index: 100;
  pointer-events: none;
}

.shimmer-text {
  background: linear-gradient(90deg, #fbbf24, #fef3c7, #f59e0b, #fbbf24);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmer 3s linear infinite;
}

.progress-fill { transition: width 0.5s ease; }

#app { height: 100%; width: 100%; display: flex; flex-direction: column; }
.screen { height: 100%; width: 100%; display: flex; flex-direction: column; }
.hidden { display: none !important; }
  </style>
  <style>body { box-sizing: border-box; }</style>
  <script src="https://cdn.tailwindcss.com/3.4.17" type="text/javascript"></script>
 </head>
 <body>
  <div id="app" style="height: 100%; width: 100%; background: #000814;">
   <!-- START SCREEN -->
   <div id="screen-start" class="screen" style="align-items: center; justify-content: center; padding: 20px;">
    <div style="text-align: center; max-width: 500px; width: 100%;" class="fade-up">
     <div style="font-size: 60px; margin-bottom: 20px;">
      💰
     </div>
     <h1 id="title-display" class="shimmer-text" style="font-size: 48px; font-weight: 900; margin: 0 0 10px 0;">AI LÀ TRIỆU PHÚ</h1>
     <p style="color: #94a3b8; margin: 0 0 40px 0; font-size: 14px;">Trả lời đúng để chinh phục đỉnh cao tri thức!</p>
     <div style="margin-bottom: 20px;" class="fade-up-delay">
      <label for="player-name" style="display: block; text-align: left; font-weight: 600; font-size: 14px; margin-bottom: 8px; color: #e2e8f0;">Tên người chơi</label> <input id="player-name" type="text" placeholder="Nhập tên của bạn..." style="width: 100%; padding: 16px 20px; border-radius: 12px; font-size: 16px; font-weight: 600; outline: none; background: #1e293b; color: #f1f5f9; border: 2px solid #334155;" onfocus="this.style.borderColor='#f59e0b'" onblur="this.style.borderColor='#334155'">
      <p id="name-error" style="text-align: left; font-size: 13px; color: #f87171; margin: 8px 0 0 0; display: none;">Tên phải có ít nhất 3 ký tự</p>
     </div><button id="btn-start" class="fade-up-delay2" style="width: 100%; padding: 16px; border-radius: 12px; font-size: 18px; font-weight: 700; cursor: pointer; border: 0; background: linear-gradient(135deg, #f59e0b, #d97706); color: #000814;" onclick="startGame()">BẮT ĐẦU</button>
    </div>
   </div><!-- PLAY SCREEN -->
   <div id="screen-play" class="screen hidden" style="display: flex; flex-direction: column; padding: 20px; gap: 12px; overflow-y: auto;">
    <!-- Top Bar -->
    <div style="display: flex; align-items: center; justify-content: space-between; gap: 10px;">
     <div style="display: flex; align-items: center; gap: 8px; font-size: 14px; color: #94a3b8;">
      <span>Câu</span> <span id="q-counter" style="font-size: 18px; font-weight: 700; color: #fbbf24;">1/5</span>
     </div>
     <div id="timer-display" style="display: flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 20px; font-size: 18px; font-weight: 700; background: #1e293b; color: #fbbf24;">
      <i data-lucide="clock" style="width: 18px; height: 18px;"></i> <span id="timer-text">15</span>
     </div>
     <div style="display: flex; align-items: center; gap: 8px; font-size: 14px; color: #94a3b8;">
      <span>Điểm</span> <span id="score-display" style="font-size: 18px; font-weight: 700; color: #10b981;">0</span>
     </div>
    </div><!-- Progress Bar -->
    <div style="width: 100%; height: 6px; border-radius: 3px; background: #1e293b;">
     <div id="progress-bar" class="progress-fill" style="height: 6px; border-radius: 3px; background: linear-gradient(90deg, #f59e0b, #10b981); width: 20%;"></div>
    </div><!-- Question Card -->
    <div id="question-card" style="border-radius: 16px; padding: 28px 20px; background: rgba(15, 23, 42, 0.95); border: 2px solid #1e293b; text-align: center; flex: 0.5; display: flex; flex-direction: column; justify-content: center;">
     <p id="question-text" style="font-size: 20px; font-weight: 700; margin: 0; color: #f1f5f9; line-height: 1.6;"></p>
    </div><!-- Answer Buttons Grid (2x2) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; flex: 0.5;">
     <button id="answer-0" class="answer-btn fade-up-delay"></button> <button id="answer-1" class="answer-btn fade-up-delay"></button> <button id="answer-2" class="answer-btn fade-up-delay"></button> <button id="answer-3" class="answer-btn fade-up-delay"></button>
    </div><!-- Feedback -->
    <div id="feedback" style="text-align: center; font-size: 16px; font-weight: 700; min-height: 28px; display: none; color: #10b981;"></div><!-- Continue button -->
    <div id="continue-wrap" style="display: none; text-align: center;">
     <button id="btn-continue" style="padding: 12px 32px; border-radius: 12px; font-size: 16px; font-weight: 700; cursor: pointer; background: #1e293b; color: #fbbf24; border: 2px solid #fbbf24;" onclick="nextQuestion()">TIẾP TỤC →</button>
    </div>
   </div><!-- END SCREEN -->
   <div id="screen-end" class="screen hidden" style="align-items: center; justify-content: center; padding: 20px; overflow-y: auto;">
    <div style="text-align: center; max-width: 500px; width: 100%;" class="fade-up">
     <div style="font-size: 60px; margin-bottom: 20px;">
      🎉
     </div>
     <h2 style="font-size: 32px; font-weight: 900; margin: 0 0 10px 0; color: #fbbf24;">HOÀN THÀNH!</h2>
     <p id="end-player" style="font-size: 18px; margin: 0 0 20px 0; color: #94a3b8;"></p>
     <p style="font-size: 56px; font-weight: 900; margin: 20px 0; color: #10b981;"><span id="end-score">0</span><span style="font-size: 24px; color: #94a3b8;">/5</span></p>
     <div id="end-message" style="font-size: 18px; font-weight: 600; margin-bottom: 30px; color: #e2e8f0;"></div><!-- Leaderboard -->
     <div style="border-radius: 20px; padding: 20px; margin-bottom: 30px; text-align: left; background: #0f172a; border: 1px solid #1e293b;">
      <h3 style="font-size: 18px; font-weight: 700; margin: 0 0 20px 0; display: flex; align-items: center; gap: 8px; color: #fbbf24;"><i data-lucide="trophy" style="width: 20px; height: 20px;"></i> Bảng Xếp Hạng</h3>
      <div id="leaderboard" style="display: flex; flex-direction: column; gap: 8px;">
       <p style="font-size: 14px; color: #64748b; margin: 0;">Chưa có dữ liệu</p>
      </div>
     </div><button style="width: 100%; padding: 16px; border-radius: 12px; font-size: 18px; font-weight: 700; cursor: pointer; border: 0; background: linear-gradient(135deg, #f59e0b, #d97706); color: #000814;" onclick="restartGame()">CHƠI LẠI 🔄</button>
    </div>
   </div>
  </div>
  <script>
const QUESTIONS = [
  {q:"Thủ đô của Việt Nam là gì?", a:["A. Hồ Chí Minh","B. Đà Nẵng","C. Hà Nội","D. Hải Phòng"], c:"C. Hà Nội"},
  {q:"Số nào là số nguyên tố?", a:["A. 4","B. 6","C. 9","D. 7"], c:"D. 7"},
  {q:"Hành tinh gần Mặt trời nhất?", a:["A. Sao Kim","B. Sao Thủy","C. Sao Hỏa","D. Trái Đất"], c:"B. Sao Thủy"},
  {q:"Tác giả Truyện Kiều?", a:["A. Nguyễn Khuyến","B. Nguyễn Du","C. Phan Bội Châu","D. Hồ Xuân Hương"], c:"B. Nguyễn Du"},
  {q:"Đại dương lớn nhất?", a:["A. Ấn Độ Dương","B. Đại Tây Dương","C. Bắc Băng Dương","D. Thái Bình Dương"], c:"D. Thái Bình Dương"},
];

let state = { name:'', qList:[], qIndex:0, score:0, answered:false, timer:15, timerInterval:null };
let allRecords = [];

const defaultConfig = {
  game_title: 'AI LÀ TRIỆU PHÚ',
  start_button_text: 'BẮT ĐẦU',
  background_color: '#000814',
  surface_color: '#0f172a',
  text_color: '#f1f5f9',
  primary_action_color: '#f59e0b',
  secondary_action_color: '#10b981'
};

function applyConfig(config) {
  const bg = config.background_color || defaultConfig.background_color;
  const surface = config.surface_color || defaultConfig.surface_color;
  const text = config.text_color || defaultConfig.text_color;
  const primary = config.primary_action_color || defaultConfig.primary_action_color;
  const secondary = config.secondary_action_color || defaultConfig.secondary_action_color;
  const font = config.font_family;
  const fontSize = config.font_size;

  document.getElementById('app').style.background = bg;
  document.getElementById('title-display').textContent = config.game_title || defaultConfig.game_title;
  document.getElementById('btn-start').textContent = config.start_button_text || defaultConfig.start_button_text;
  document.getElementById('btn-start').style.background = `linear-gradient(135deg, ${primary}, ${primary}dd)`;

  document.getElementById('question-text').style.color = text;
  document.getElementById('end-message').style.color = text;

  const scoreEl = document.getElementById('score-display');
  if (scoreEl) scoreEl.style.color = secondary;
  const endScore = document.getElementById('end-score');
  if (endScore) endScore.style.color = secondary;

  if (font) {
    const stack = `${font}, 'Be Vietnam Pro', sans-serif`;
    document.body.style.fontFamily = stack;
  }
  if (fontSize) {
    const base = fontSize;
    document.querySelectorAll('h1').forEach(el => el.style.fontSize = `${base * 2.5}px`);
    document.querySelectorAll('h2').forEach(el => el.style.fontSize = `${base * 2}px`);
  }
}

window.elementSdk.init({
  defaultConfig,
  onConfigChange: async (config) => applyConfig(config),
  mapToCapabilities: (config) => ({
    recolorables: [
      { get: () => config.background_color || defaultConfig.background_color, set: v => { config.background_color = v; window.elementSdk.setConfig({background_color:v}); }},
      { get: () => config.surface_color || defaultConfig.surface_color, set: v => { config.surface_color = v; window.elementSdk.setConfig({surface_color:v}); }},
      { get: () => config.text_color || defaultConfig.text_color, set: v => { config.text_color = v; window.elementSdk.setConfig({text_color:v}); }},
      { get: () => config.primary_action_color || defaultConfig.primary_action_color, set: v => { config.primary_action_color = v; window.elementSdk.setConfig({primary_action_color:v}); }},
      { get: () => config.secondary_action_color || defaultConfig.secondary_action_color, set: v => { config.secondary_action_color = v; window.elementSdk.setConfig({secondary_action_color:v}); }},
    ],
    borderables: [],
    fontEditable: {
      get: () => config.font_family || defaultConfig.font_family || 'Be Vietnam Pro',
      set: v => { config.font_family = v; window.elementSdk.setConfig({font_family:v}); }
    },
    fontSizeable: {
      get: () => config.font_size || defaultConfig.font_size || 16,
      set: v => { config.font_size = v; window.elementSdk.setConfig({font_size:v}); }
    }
  }),
  mapToEditPanelValues: (config) => new Map([
    ['game_title', config.game_title || defaultConfig.game_title],
    ['start_button_text', config.start_button_text || defaultConfig.start_button_text]
  ])
});

const dataHandler = {
  onDataChanged(data) {
    allRecords = data;
    renderLeaderboard();
  }
};

(async () => {
  const r = await window.dataSdk.init(dataHandler);
  if (!r.isOk) console.error('Data SDK init failed');
})();

function renderLeaderboard() {
  const container = document.getElementById('leaderboard');
  if (!allRecords.length) {
    container.innerHTML = '<p style="font-size:14px;color:#64748b;margin:0;">Chưa có dữ liệu</p>';
    return;
  }
  const sorted = [...allRecords].sort((a,b) => (b.score||0) - (a.score||0)).slice(0, 10);
  const medals = ['🥇','🥈','🥉'];
  container.innerHTML = sorted.map((r, i) => `
    <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 12px;border-radius:8px;background:${i<3?'#1e293b':'transparent'}">
      <div style="display:flex;align-items:center;gap:8px;">
        <span style="font-size:18px;">${medals[i]||`<span style="color:#64748b;font-size:14px;">#${i+1}</span>`}</span>
        <span style="font-weight:600;color:#e2e8f0;font-size:14px;">${r.player_name||'?'}</span>
      </div>
      <span style="font-weight:700;color:#fbbf24;font-size:14px;">${r.score||0}/5</span>
    </div>
  `).join('');
}

function shuffle(arr) { const a=[...arr]; for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];} return a; }

function showScreen(id) {
  ['screen-start','screen-play','screen-end'].forEach(s => document.getElementById(s).classList.toggle('hidden', s!==id));
}

function startGame() {
  const name = document.getElementById('player-name').value.trim();
  if (name.length < 3) {
    document.getElementById('name-error').style.display = 'block';
    return;
  }
  document.getElementById('name-error').style.display = 'none';
  state.name = name;
  state.qList = shuffle(QUESTIONS);
  state.qIndex = 0;
  state.score = 0;
  state.answered = false;
  showScreen('screen-play');
  renderQuestion();
}

function startTimer() {
  clearInterval(state.timerInterval);
  state.timer = 15;
  const timerText = document.getElementById('timer-text');
  const timerDisplay = document.getElementById('timer-display');
  timerText.textContent = state.timer;
  timerDisplay.classList.remove('timer-critical');

  state.timerInterval = setInterval(() => {
    state.timer--;
    timerText.textContent = Math.max(state.timer, 0);
    if (state.timer <= 5) timerDisplay.classList.add('timer-critical');
    if (state.timer <= 0) {
      clearInterval(state.timerInterval);
      if (!state.answered) timeOut();
    }
  }, 1000);
}

function timeOut() {
  state.answered = true;
  const fb = document.getElementById('feedback');
  fb.textContent = '⏰ Hết giờ!';
  fb.style.color = '#f87171';
  fb.style.display = 'block';
  highlightCorrect();
  document.getElementById('continue-wrap').style.display = 'block';
  document.querySelectorAll('.answer-btn').forEach(b => b.disabled = true);
}

function renderQuestion() {
  const q = state.qList[state.qIndex];
  document.getElementById('q-counter').textContent = `${state.qIndex+1}/${state.qList.length}`;
  document.getElementById('score-display').textContent = state.score;
  document.getElementById('progress-bar').style.width = `${((state.qIndex+1)/state.qList.length)*100}%`;
  document.getElementById('question-text').textContent = q.q;
  document.getElementById('feedback').style.display = 'none';
  document.getElementById('continue-wrap').style.display = 'none';

  for (let i = 0; i < 4; i++) {
    const btn = document.getElementById(`answer-${i}`);
    btn.textContent = q.a[i];
    btn.disabled = false;
    btn.className = 'answer-btn fade-up-delay';
    btn.onclick = function() { selectAnswer(this, q.a[i]); };
  }

  startTimer();
  setTimeout(() => lucide.createIcons(), 100);
}

function selectAnswer(btn, answer) {
  if (state.answered) return;
  state.answered = true;
  clearInterval(state.timerInterval);

  const q = state.qList[state.qIndex];
  const fb = document.getElementById('feedback');
  fb.style.display = 'block';

  document.querySelectorAll('.answer-btn').forEach(b => b.disabled = true);

  if (answer === q.c) {
    state.score++;
    document.getElementById('score-display').textContent = state.score;
    btn.classList.add('correct','correct-flash');
    fb.textContent = '✅ Chính xác!';
    fb.style.color = '#10b981';
  } else {
    btn.classList.add('wrong','wrong-shake');
    fb.textContent = `❌ Sai! Đáp án: ${q.c}`;
    fb.style.color = '#f87171';
    highlightCorrect();
  }

  document.getElementById('continue-wrap').style.display = 'block';
}

function highlightCorrect() {
  const q = state.qList[state.qIndex];
  document.querySelectorAll('.answer-btn').forEach(b => {
    if (b.textContent.trim() === q.c) {
      b.classList.add('correct');
    }
  });
}

async function nextQuestion() {
  state.qIndex++;
  state.answered = false;
  if (state.qIndex >= state.qList.length) {
    await endGame();
  } else {
    renderQuestion();
  }
}

async function endGame() {
  clearInterval(state.timerInterval);
  showScreen('screen-end');

  document.getElementById('end-player').textContent = `Người chơi: ${state.name}`;
  document.getElementById('end-score').textContent = state.score;

  const msgs = ['Xuất sắc! 🌟','Rất giỏi! 👏','Khá tốt! 💪','Cố gắng thêm! 📚','Lần sau sẽ tốt hơn! 🍀'];
  document.getElementById('end-message').textContent = state.score>=5?msgs[0]:state.score>=4?msgs[1]:state.score>=3?msgs[2]:state.score>=2?msgs[3]:msgs[4];

  spawnConfetti();

  if (allRecords.length < 999) {
    const r = await window.dataSdk.create({ player_name: state.name, score: state.score, played_at: new Date().toISOString() });
    if (!r.isOk) console.error('Save failed');
  }

  renderLeaderboard();
  lucide.createIcons();
}

function spawnConfetti() {
  const colors = ['#fbbf24','#10b981','#ef4444','#3b82f6','#f472b6','#a78bfa'];
  for (let i = 0; i < 40; i++) {
    const el = document.createElement('div');
    el.className = 'confetti-piece';
    el.style.left = Math.random()*100+'%';
    el.style.background = colors[Math.floor(Math.random()*colors.length)];
    el.style.animationDuration = (2+Math.random()*2)+'s';
    el.style.animationDelay = Math.random()*1.5+'s';
    el.style.borderRadius = Math.random()>0.5?'50%':'0';
    el.style.width = (6+Math.random()*8)+'px';
    el.style.height = (6+Math.random()*8)+'px';
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 5000);
  }
}

function restartGame() {
  state = { name:'', qList:[], qIndex:0, score:0, answered:false, timer:15, timerInterval:null };
  document.getElementById('player-name').value = '';
  showScreen('screen-start');
}

lucide.createIcons();
  </script>
 <script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'9f14f776a2c50952',t:'MTc3NzAzMjIyNi4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
</html>
