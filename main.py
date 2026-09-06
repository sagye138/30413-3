import pandas as pd
import streamlit as st

st.set_page_config(page_title="AK 도면 부품 분석기", layout="wide")

# 다크모드 스타일
st.markdown(
    """
    <style>
        .stApp { background-color: #121212; color: #e0e0e0; }
        div.stButton > button { background-color: #2b2b2b; color: #ffffff; border: 1px solid #4a4a4a; }
        div.stButton > button:hover { background-color: #3b3b3b; border: 1px solid #ffffff; }
        .blueprint-box { border: 1px solid #333; padding: 15px; border-radius: 8px; background-color: #1a1a1a; }
    </style>
""",
    unsafe_allow_html=True,
)

if "page" not in st.session_state:
    st.session_state.page = "main"


def change_page(page_name):
    st.session_state.page = page_name


# 도면 부품 데이터 (처음 올린 도면의 주요 번호 매칭)
parts_df = pd.DataFrame(
    {
        "번호": [1, 13, 16, 17, 19, 25, 36, 49, 53, 63],
        "러시아어/명칭": [
            "1. пружина крышки (덮개 스프링)",
            "13. курок (공이치기/쿠록)",
            "16. затворная рама (노리쇠 뭉치)",
            "17. затвор (노리쇠)",
            "19. стержень возвратной пружины (복좌울 스프링 축)",
            "25. возвратная пружина (복좌울 스프링)",
            "36. мушка (가늠쇠)",
            "49. цевье (총열 덮개/목재 부품)",
            "53. корпус магазина (탄창 몸체)",
            "63. спусковой крючок (방아쇠)",
        ],
        "기능 설명": [
            "개머리판 또는 총몸 덮개의 고정을 보조하는 스프링입니다.",
            "방아쇠와 연동되어 격발을 위해 공이를 때려주는 핵심 해머 부품입니다.",
            "가스 압력을 받아 후퇴하며 탄피를 배출하고 다음 탄을 밀어넣는 구동부입니다.",
            "약실을 폐쇄하고 탄환을 고정하는 노리쇠 본체입니다.",
            "발사 후 노리쇠를 원위치로 전진시키는 스프링을 지지하는 축입니다.",
            "후퇴한 노리쇠를 다시 전진시키는 장력 제공 스프링입니다.",
            "원거리 사격 시 표적을 맞추기 위해 조준하는 앞쪽 가늠쇠입니다.",
            "사수가 손으로 잡는 부위로, 총열 하단을 감싸고 보호합니다.",
            "7.62x39mm 탄약을 수납하는 바나나 형태의 탄창 케이스입니다.",
            "사수가 당겨서 격발을 일으키는 방아쇠울 내부의 기구입니다.",
        ],
    }
)

# ==========================================
# 1. 메인 화면: 도면 + 부품 선택 뷰어
# ==========================================
if st.session_state.page == "main":
    st.title("AK-47 도면 인터랙티브 분석기")
    st.button(
        "AK 시리즈 역사 및 차이점 보기 ➔",
        on_click=change_page,
        args=("info",),
    )

    st.markdown("---")

    col_img, col_ctrl = st.columns([2, 1])

    with col_img:
        st.subheader("blueprint")
        # 사용자가 올린 도면 이미지 파일명을 로컬에 'ak_blueprint.jpg'로 저장해두거나 아래 경로에 맞추면 됨
        # 이미지가 없으면 대체 텍스트 출력
        try:
            st.image(
                "ak_blueprint.jpg",
                caption="7.62-mm автомат Калашникова (AK) 단면도",
                use_column_width=True,
            )
        except:
            st.warning(
                "💡 프로젝트 폴더에 도면 이미지 파일을 `ak_blueprint.jpg` 이름으로 넣어두면 여기에 출력됩니다."
            )
            st.info(
                "우측 패널에서 부품 번호를 골라 상세 기능을 확인할 수 있습니다."
            )

    with col_ctrl:
        st.subheader("부품 인덱스 탐색")
        selected_num = st.selectbox(
            "도면 번호 선택:", parts_df["러시아어/명칭"].tolist()
        )

        matched_row = parts_df[parts_df["러시아어/명칭"] == selected_num].iloc[
            0
        ]

        st.markdown(
            f"""
        <div class="blueprint-box">
            <h4>선택한 부품 정보</h4>
            <p><b>부품 번호:</b> {matched_row['번호']}</p>
            <p><b>명칭:</b> {matched_row['러시아어/명칭']}</p>
            <p><b>설명:</b><br>{matched_row['기능 설명']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ==========================================
# 2. 서브 화면: AK 모델별 차이점 설명
# ==========================================
elif st.session_state.page == "info":
    st.title("AK-47, AKM, AK-74의 역사와 차이점")
    st.button("⬅ 도면 뷰어로 돌아가기", on_click=change_page, args=("main",))

    st.markdown("---")
    st.subheader("🛠️ 제조사 및 기원")
    st.write("""
    * **제조사:** 소련 이젭스크 기계공장 (현 칼라시니코프 콘체른)
    * **설계자:** 미하일 칼라시니코프
    * 어떤 환경에서도 작동하는 극단적인 신뢰성이 핵심 특징입니다.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("AK-47")
        st.write("""
        * **채택:** 1949년
        * **탄약:** 7.62x39mm
        * **특징:** 통짜 쇳덩이를 깎아 만든 **절삭가공(Milled)** 리시버. 튼튼하지만 무겁고 생산성이 낮음.
        """)

    with col2:
        st.subheader("AKM")
        st.write("""
        * **채택:** 1959년
        * **탄약:** 7.62x39mm
        * **특징:** 철판 프레스 공법을 도입해 대량 생산과 경량화 달성. 우리가 흔히 아는 AK의 대명사. 묵직한 7.62mm 반동 유지.
        """)

    with col3:
        st.subheader("AK-74")
        st.write("""
        * **채택:** 1974년
        * **탄약:** 5.45x39mm (소구경 고속탄)
        * **특징:** 미군 M16에 대응하기 위해 탄을 소형화. 반동이 획기적으로 줄어들어 연사 시 집탄율이 대폭 상승.
        """)
