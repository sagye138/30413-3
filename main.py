import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AK 시리즈 2.5D 뷰어", layout="wide")

# 다크모드 강제 적용 CSS
st.markdown(
    """
    <style>
        .stApp { background-color: #121212; color: #e0e0e0; }
        div.stButton > button {
            background-color: #2b2b2b; color: #ffffff; border: 1px solid #4a4a4a;
        }
        div.stButton > button:hover { background-color: #3b3b3b; border: 1px solid #ffffff; }
    </style>
""",
    unsafe_allow_html=True,
)

if "page" not in st.session_state:
    st.session_state.page = "main"

def change_page(page_name):
    st.session_state.page = page_name

# ==========================================
# 1. 메인 화면 (2D 인터랙티브 뷰어)
# ==========================================
if st.session_state.page == "main":
    st.title("AK 소총 부품 인터랙티브 뷰어")

    st.button(
        "AK 시리즈 상세 설명 및 차이점 보기 ➔",
        on_click=change_page,
        args=("info",),
    )

    st.markdown("---")

    # 2D 이미지 위에 마커를 띄우는 HTML/CSS
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; background-color: #121212; display: flex; justify-content: center; }
            .image-container {
                position: relative;
                width: 100%;
                max-width: 900px; /* 이미지 최대 크기 */
                background-color: #1a1a1a;
                border-radius: 8px;
                border: 1px solid #333;
                padding: 20px;
                box-sizing: border-box;
            }
            .image-container img {
                width: 100%;
                height: auto;
                display: block;
            }
            /* 마커 (맥박 뛰는 효과) */
            .hotspot {
                position: absolute;
                width: 20px;
                height: 20px;
                background-color: rgba(255, 50, 50, 0.8);
                border-radius: 50%;
                transform: translate(-50%, -50%);
                cursor: pointer;
                box-shadow: 0 0 0 0 rgba(255, 50, 50, 0.7);
                animation: pulse 1.5s infinite;
            }
            @keyframes pulse {
                0% { transform: translate(-50%, -50%) scale(0.95); box-shadow: 0 0 0 0 rgba(255, 50, 50, 0.7); }
                70% { transform: translate(-50%, -50%) scale(1); box-shadow: 0 0 0 10px rgba(255, 50, 50, 0); }
                100% { transform: translate(-50%, -50%) scale(0.95); box-shadow: 0 0 0 0 rgba(255, 50, 50, 0); }
            }
            /* 마우스를 올렸을 때 나타나는 툴팁 */
            .tooltip {
                visibility: hidden;
                width: 200px;
                background-color: rgba(30, 30, 30, 0.95);
                color: #fff;
                text-align: left;
                border-radius: 6px;
                padding: 10px;
                position: absolute;
                z-index: 1;
                bottom: 150%; 
                left: 50%;
                transform: translateX(-50%);
                border: 1px solid #555;
                opacity: 0;
                transition: opacity 0.3s;
                font-family: sans-serif;
                font-size: 13px;
                line-height: 1.4;
            }
            .tooltip::after {
                content: "";
                position: absolute;
                top: 100%;
                left: 50%;
                margin-left: -5px;
                border-width: 5px;
                border-style: solid;
                border-color: #555 transparent transparent transparent;
            }
            .hotspot:hover .tooltip {
                visibility: visible;
                opacity: 1;
            }
            .title { color: #ff6666; font-weight: bold; margin-bottom: 5px; display: block; font-size: 15px; }
        </style>
    </head>
    <body>
        <div class="image-container">
            <!-- 투명 배경의 2D AK-47 이미지 -->
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/65/AK-47_type_II_noBG.png" alt="AK-47">
            
            <!-- 부품 마커 1: 노리쇠 뭉치 -->
            <div class="hotspot" style="top: 36%; left: 45%;">
                <span class="tooltip">
                    <span class="title">노리쇠 뭉치 (Bolt Carrier)</span>
                    가스 압력을 받아 후퇴하며 탄피를 배출하고 다음 탄을 장전하는 핵심 구동부입니다.
                </span>
            </div>

            <!-- 부품 마커 2: 탄창 -->
            <div class="hotspot" style="top: 75%; left: 42%;">
                <span class="tooltip">
                    <span class="title">탄창 (Magazine)</span>
                    7.62x39mm 탄약 30발이 들어가는 바나나형 탄창입니다. 특유의 곡선이 특징입니다.
                </span>
            </div>

            <!-- 부품 마커 3: 가스관 -->
            <div class="hotspot" style="top: 32%; left: 63%;">
                <span class="tooltip">
                    <span class="title">가스관 (Gas Tube)</span>
                    발사 시 발생하는 가스의 일부를 뒤로 보내 노리쇠 뭉치를 밀어내는 역할을 합니다.
                </span>
            </div>

            <!-- 부품 마커 4: 방아쇠 -->
            <div class="hotspot" style="top: 55%; left: 33%;">
                <span class="tooltip">
                    <span class="title">방아쇠 (Trigger)</span>
                    격발을 위한 장치입니다.
                </span>
            </div>
        </div>
    </body>
    </html>
    """
    
    # HTML 컴포넌트 렌더링
    components.html(html_code, height=700)

# ==========================================
# 2. 상세 설명 화면
# ==========================================
elif st.session_state.page == "info":
    st.title("AK-47, AKM, AK-74의 역사와 차이점")
    st.button("⬅ 인터랙티브 뷰어로 돌아가기", on_click=change_page, args=("main",))

    st.markdown("---")
    st.subheader("🛠️ 제조사 및 기원")
    st.write("""
    * **제조사:** 칼라시니코프 콘체른 (Kalashnikov Concern)
    * **설계자:** 미하일 칼라시니코프 (Mikhail Kalashnikov)
    * **특징:** 극한의 오염 환경에서도 정합성이 유지되는 독보적인 신뢰성.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("AK-47")
        st.write("""
        * **채택:** 1949년
        * **탄약:** 7.62x39mm
        * **특징:** 쇳덩어리를 깎아 만든 **절삭가공(Milled)** 방식. 매우 튼튼하지만 무겁고 생산 단가가 높음.
        """)

    with col2:
        st.subheader("AKM")
        st.write("""
        * **채택:** 1959년
        * **탄약:** 7.62x39mm
        * **특징:** 철판을 찍어내는 **프레스 가공(Stamped)** 도입으로 경량화 성공. 강한 타격감과 반동이 특징.
        """)

    with col3:
        st.subheader("AK-74")
        st.write("""
        * **채택:** 1974년
        * **탄약:** 5.45x39mm (소구경 고속탄)
        * **특징:** 탄약 소형화로 반동이 감소하여 명중률 향상. 대형 원통형 소염기 탑재.
        """)
