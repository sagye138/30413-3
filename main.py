import streamlit as st
import streamlit.components.v1 as components

st.title("3D 총기 부품 인터랙티브 뷰어")

# 1. 3D 모델 파일 경로 (로컬 파일 또는 웹 URL)
# 실제 적용 시 로컬의 "ak47_model.glb" 파일을 웹 서버로 서빙하거나 base64로 변환하여 넣습니다.
model_url = "https://modelviewer.dev/shared-assets/models/Astronaut.glb" # 예시용 3D 모델

# 2. HTML/JS를 이용한 구글 model-viewer 및 핫스팟 임베딩
html_code = f"""
<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.1.1/model-viewer.min.js"></script>

<model-viewer 
    src="{model_url}" 
    alt="3D 무기 모델" 
    auto-rotate 
    camera-controls 
    style="width: 100%; height: 600px; background-color: #2c2c2c;">
    
    <!-- 부품 1: 핫스팟 마커 배치 (data-position에 3D 좌표 입력) -->
    <button class="Hotspot" slot="hotspot-1" data-position="0.1 0.5 0.2" data-normal="0 0 1">
        <div class="annotation">노리쇠 뭉치<br><span style="font-size:10px; font-weight:normal;">가스 압력으로 후퇴하는 구동부</span></div>
    </button>
    
    <!-- 부품 2: 핫스팟 마커 배치 -->
    <button class="Hotspot" slot="hotspot-2" data-position="-0.2 0.1 0" data-normal="0 0 1">
        <div class="annotation">방아쇠<br><span style="font-size:10px; font-weight:normal;">격발 장치</span></div>
    </button>
</model-viewer>

<style>
  .Hotspot {{
    background: rgba(255, 255, 255, 0.9);
    border-radius: 4px;
    padding: 6px;
    border: 1px solid #333;
    cursor: pointer;
    box-shadow: 0 2px 4px rgba(0,0,0,0.25);
  }}
  .annotation {{
    font-size: 13px;
    font-family: sans-serif;
    font-weight: bold;
    color: #111;
  }}
</style>
"""

# 3. 스트림릿에 HTML 컴포넌트 렌더링
components.html(html_code, height=650)
