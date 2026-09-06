import base64
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AK 시리즈 3D 뷰어", layout="wide")

# 다크모드 적용 CSS
st.markdown(
    """
    <style>
        .stApp { background-color: #121212; color: #e0e0e0; }
        div.stButton > button {
            background-color: #2b2b2b; color: #ffffff; border: 1px solid #4a4a4a;
        }
        div.stButton > button:hover { background-color: #3b3b3b; border: 1px solid #ffffff; }
        .st-emotion-cache-1wivap2 { color: #e0e0e0; } /* 업로더 텍스트 색상 */
    </style>
""",
    unsafe_allow_html=True,
)

if "page" not in st.session_state:
    st.session_state.page = "main"

def change_page(page_name):
    st.session_state.page = page_name

# ==========================================
# 1. 메인 화면 (3D 모델 뷰어)
# ==========================================
if st.session_state.page == "main":
    st.title("AK 소총 3D 모델 뷰어")

    st.button(
        "AK 시리즈 상세 설명 및 차이점 보기 ➔",
        on_click=change_page,
        args=("info",),
    )

    st.markdown("---")
    
    # 로컬 파일 업로더 생성 (외부 링크 차단 문제 원천 해결)
    uploaded_file = st.file_uploader("📥 다운로드 받은 AK 소총 3D 모델(.glb) 파일을 여기에 드래그 앤 드롭하세요", type=['glb'])

    if uploaded_file is not None:
        # 업로드된 파일을 Base64로 인코딩하여 HTML에 직접 주입
        encoded = base64.b64encode(uploaded_file.getvalue()).decode("utf-8")
        model_src = f"data:model/gltf-binary;base64,{encoded}"

        html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.3.0/model-viewer.min.js"></script>
            <style>
                body {{ margin: 0; background-color: #121212; }}
                model-viewer {{
                    width: 100vw;
                    height: 600px;
                    background-color: #1a1a1a;
                    border-radius: 8px;
                    border: 1px solid #333;
                }}
                .Hotspot {{
                    background: rgba(30, 30, 30, 0.85);
                    border-radius: 4px;
                    padding: 6px;
                    border: 1px solid #666;
                    color: #eee;
                    font-family: sans-serif;
                    font-size: 13px;
                    font-weight: bold;
                    cursor: pointer;
                }}
            </style>
        </head>
        <body>
            <model-viewer 
                src="{model_src}" 
                alt="AK 3D Model" 
                auto-rotate 
                camera-controls 
                shadow-intensity="1">
                
                <button class="Hotspot" slot="hotspot-1" data-position="0 0.05 0.15" data-normal="0 0 1">
                    노리쇠 뭉치
                </button>
            </model-viewer>
        </body>
        </html>
        """
        components.html(html_code, height=620)
    else:
        st.info("💡 외부 링크는 브라우저 보안에 의해 자주 차단됩니다. 3D 모델 뷰어를 보려면 위 공간에 .glb 파일을 업로드해 주세요.")

# ==========================================
# 2. 상세 설명 화면
# ==========================================
elif st.session_state.page == "info":
    st.title("AK-47, AKM, AK-74의 역사와 차이점")
    st.button("⬅ 3D 뷰어로 돌아가기", on_click=change_page, args=("main",))

    st.markdown("---")
    st.subheader("🛠️ 제조사 및 기원")
    st.write("""
    * **제조사:** 칼라시니코프 콘체른 (Kalashnikov Concern, 구 이젭스크 기계공장)
    * **설계자:** 미하일 칼라시니코프 (Mikhail Kalashnikov)
    * **특징:** 극한의 오염 환경(모래, 진흙, 수중)에서도 정합성이 유지되는 독보적인 신뢰성.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("AK-47")
        st.write("""
        * **채택:** 1949년
        * **탄약:** 7.62x39mm
        * **특징:** 쇳덩어리를 깎아 만든 **절삭가공(Milled)** 방식. 매우 튼튼하지만 무게가 무겁고 대량 생산 단가가 높음.
        """)

    with col2:
        st.subheader("AKM")
        st.write("""
        * **채택:** 1959년
        * **탄약:** 7.62x39mm
        * **특징:** 철판을 찍어내는 **프레스 가공(Stamped)** 도입으로 경량화 및 대량생산 성공. 총구의 경사형 소염기가 외형적 특징.
        """)

    with col3:
        st.subheader("AK-74")
        st.write("""
        * **채택:** 1974년
        * **탄약:** 5.45x39mm (소구경 고속탄)
        * **특징:** 미군 M16(5.56mm)에 대응하여 개발. 탄약 소형화로 반동이 대폭 감소하여 연발 사격 명중률 향상. 대형 원통형 소염기 탑재.
        """)
