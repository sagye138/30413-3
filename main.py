import streamlit as st
import streamlit.components.v1 as components

# 1. 전체 페이지 설정 (다크모드 친화적 레이아웃)
st.set_page_config(page_title="AK 시리즈 3D 뷰어", layout="wide")

# 2. CSS를 활용한 전체 다크모드 강제 적용
st.markdown("""
    <style>
        /* 전체 배경 및 텍스트 색상 */
        .stApp {
            background-color: #121212;
            color: #e0e0e0;
        }
        /* 버튼 스타일링 (다크 테마) */
        div.stButton > button {
            background-color: #2b2b2b;
            color: #ffffff;
            border: 1px solid #4a4a4a;
            transition: all 0.2s ease-in-out;
        }
        div.stButton > button:hover {
            background-color: #3b3b3b;
            border: 1px solid #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# 3. 세션 상태(Session State) 초기화 - 화면 전환용
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def change_page(page_name):
    st.session_state.page = page_name

# ==========================================
# 메인 화면: 3D 모델 뷰어
# ==========================================
if st.session_state.page == 'main':
    st.title("AK 소총 3D 모델 뷰어")
    
    # 정보 화면으로 넘어가는 버튼
    st.button("AK 시리즈 상세 설명 및 차이점 보기 ➔", on_click=change_page, args=('info',))
    
    # 3D 모델 URL (실제 프로젝트 시 로컬에 ak.glb 파일을 넣고 해당 경로로 변경 필요)
    # 예시 URL로 대체되어 있습니다.
    model_url = "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb" 
    
    # HTML 및 Google model-viewer 코드
    html_code = f"""
    <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.1.1/model-viewer.min.js"></script>
    <model-viewer 
        src="{model_url}" 
        alt="AK 3D Model" 
        auto-rotate 
        camera-controls 
        environment-image="neutral"
        exposure="1"
        style="width: 100%; height: 600px; background-color: #1a1a1a; border-radius: 8px; border: 1px solid #333;">
        
        <button class="Hotspot" slot="hotspot-1" data-position="0 0.2 0.3" data-normal="0 0 1">
            <div class="annotation">노리쇠 뭉치</div>
        </
