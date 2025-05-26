
import streamlit as st

# --- 사이드바 (슬라이더) ---
st.sidebar.title("슬라이더")
slider_val1 = st.sidebar.slider("레이아웃 1", 0, 100, 50)
slider_val2 = st.sidebar.slider("레이아웃 3", 0, 1000, 10)

# --- empty ---
placeholder = st.empty()

# --- 탭 구성 ---
tab1, tab2, tab3 = st.tabs(["탭 01", "탭 02", "탭 03"])

with tab1:
    st.write("탭 01 내용")

    # 2x2 레이아웃 구성
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🧱 레이아웃 01")
        st.info(f"슬라이더 값: {slider_val1}")
    with col2:
        st.markdown("### 🧱 레이아웃 02")
        with st.expander("expander"):
          st.write("expander로 숨겨진 내용")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("### 🧱 레이아웃 03")
        st.info(f"슬라이더 값: {slider_val2}")
    with col4:
        st.markdown("### 🧱 레이아웃 04")
        if st.button("누르면 바뀜"):
            placeholder.success("버튼이 눌렸습니다!")
        else:
            placeholder.warning("아직 버튼을 누르지 않았어요.")

with tab2:
    st.write("탭 02 내용")
    # 컨테이너 1 - 요약 영역
    with st.container():
        st.subheader("1️⃣ KPI 요약")
        col1, col2, col3 = st.columns(3)
        col1.metric("매출", "₩120,000")
        col2.metric("주문", "58건")
        col3.metric("고객 수", "34명")

with tab3:
    st.write("탭 03 내용")
    import pandas as pd

    df = pd.DataFrame({
        "과목": ["수학", "영어", "과학"],
        "점수": [90, 85, 95]
    })

    st.dataframe(df)


