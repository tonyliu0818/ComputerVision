import streamlit as st
import time

st.title('深蹲姿勢檢測')

# 封面影片
recorded_file = 'final_demo.mp4'
sample_vid = st.empty()
sample_vid.video(recorded_file)
