import base64
import os
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
    </style>
""",
    unsafe_allow_html=True,
)

if "page" not in st.session_state:
    st.session_state.page = "main"


def change_page(page_name):
    st.session_state.page = page_name


def get_model_src(file_path_or_url):
    if os.path.exists(file_path_or_url):
        with open(file_path_or_url, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
        return f"data:model/gltf-binary;base64,{encoded}"
    return file_path_or_url


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

    # 로컬 ak47.glb 파일이 없을 경우 실제 AK-47 3D 모델 URL을 자동으로 로드
    local_glb_path = "ak47.glb"
    ak_online_url = "https://raw.githubusercontent.com/yomotsu/camera-controls/main/examples/resources/models/ak47.glb"

    model_src = get_model_src(
        local_glb_path if os.path.exists(local_glb_path) else ak_online_url
    )

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
            }}
            .Hotspot {{
                background: rgba(30, 30, 30, 0.85);
                border-radius: 4px;
                padding: 6px;
                border: 1px solid #666;
                color: #eee;
                font-family: sans-serif;
                font-size: 12px;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <model-viewer 
            src="{model_src}" 
            alt="AK-47 3D Model" 
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

# ==========================================
# 2. 상세 설명 화면
# ==========================================
elif st.session_state.page == "info":
    st.title("AK-47, AKM, AK-74의 역사와 차이점")
    st.button("⬅ 3D 뷰어로 돌아가기", on_click=change_page, args=("main",))

    st.markdown("---")
    st.subheader("제조사 및 기원")
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
        * **특징:** 철판을 찍어내는 **프레스 가공(Stamped)** 도입으로 경량화 및 대량생산 성공. 총구의 경사형 소염기가 외형적 특징이며, 강한 타격감과 반동을 가짐.
        """)

    with col3:
        st.subheader("AK-74")
        st.write("""
        * **채택:** 1974년
        * **탄약:** 5.45x39mm (소구경 고속탄)
        * **특징:** 미군 M16(5.56mm)에 대응하여 개발. 탄약 소형화로 반동이 대폭 감소하여 연발 사격 명중률이 향상됨. 대형 원통형 소염기 탑재.
        """)
