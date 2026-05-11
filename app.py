import streamlit as st

st.set_page_config(page_title="バッテリー持続計算", layout="centered")

st.markdown("""
<style>
.stNumberInput label { font-size: 18px !important; font-weight: 800 !important; color: #CC7722 !important; }
.result-box { background-color: #fffaf0; padding: 20px; border-radius: 10px; border-left: 5px solid #CC7722; margin-top: 20px; }
.credit { text-align: right; font-size: 14px; color: #666; margin-bottom: -20px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title('🔋 バッテリー持続計算')

col1, col2 = st.columns(2)
cap_ah = col1.number_input("バッテリー容量 (Ah)", value=7.2, format="%.1f")
load_a = col2.number_input("負荷電流 (A)", value=0.500, format="%.3f")

# 余裕率のデフォルトを0.8に設定
safety_factor = st.slider("余裕率（保守率）", 0.1, 1.0, 0.8)

if load_a != 0:
    hours = (cap_ah * safety_factor) / load_a
else:
    hours = 0.0

st.markdown('<div class="result-box">', unsafe_allow_html=True)
st.subheader("📊 計算結果")
st.metric("推定持続時間", f"{hours:.1f} 時間")
st.write(f"計算式: ({cap_ah}Ah × {safety_factor}) ÷ {load_a}A")
st.markdown('</div>', unsafe_allow_html=True)
st.caption("※バッテリーの劣化や周囲温度によって時間は短縮される場合があります。")


# --- 画面下部中央に「戻る」ボタンを配置 ---
st.markdown("---")  # 区切り線
col1, col2, col3 = st.columns([1, 1, 1])

with col2:  # 中央の列を使用
    # 水色のアイコン（🏠）と「戻る」を表示するボタン
    if st.link_button("🏠\n\n戻る", "https://7fjndw39dicdzckugyepb2.streamlit.app/", use_container_width=True):
        pass

# ボタンの色（水色）を調整するカスタム設定
st.markdown("""
    <style>
    div.stLinkButton > a {
        background-color: #00BFFF !important; /* 水色（DeepSkyBlue） */
        color: white !important;
        border-radius: 10px;
        text-align: center;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

