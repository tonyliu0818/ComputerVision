from thresholds import get_thresholds_beginner, get_thresholds_pro, get_thresholds_normal
from process_picture import ProcessPicbeginner,ProcessPicframe
from utils import get_mediapipe_pose
import av
import os
import sys
import streamlit as st
import cv2
import tempfile

BASE_DIR = os.path.abspath(os.path.join(__file__, '../../'))
sys.path.append(BASE_DIR)


st.title('上傳照片偵測')

mode = st.radio('選擇模式', ['Beginner', 'Normal', 'Advanced'], horizontal=True)

thresholds = None

if mode == 'Beginner':
    thresholds = get_thresholds_beginner()
    upload_process_frame = ProcessPicbeginner(thresholds=thresholds)
    pose = get_mediapipe_pose()

elif mode == 'Normal':
    thresholds = get_thresholds_normal()
    upload_process_frame = ProcessPicframe(thresholds=thresholds)
    pose = get_mediapipe_pose()

elif mode == 'Advanced':
    thresholds = get_thresholds_pro()
    upload_process_frame = ProcessPicframe(thresholds=thresholds)
    pose = get_mediapipe_pose()

download = None

if 'download' not in st.session_state:
    st.session_state['download'] = False
output_picture_file = f'output_recorded.jpg'

if os.path.exists(output_picture_file):
    os.remove(output_picture_file)

with st.form('Upload', clear_on_submit=True):
    up_file = st.file_uploader("Upload a Picture", ['jpg'])
    uploaded = st.form_submit_button("Upload")

stframe = st.empty()

ip_vid_str = '<p style="font-family:Helvetica; font-weight: bold; font-size: 16px;">Input Picture</p>'
warning_str = '<p style="font-family:Helvetica; font-weight: bold; color: Red; font-size: 17px;">Please Upload a Picture first!!!</p>'


warn = st.empty()


download_button = st.empty()

if up_file and uploaded:
    

    download_button.empty()
    #tfile = tempfile.NamedTemporaryFile(delete=False)

    try:
        warn.empty()
        #tfile.write(up_file.read())

        vf = cv2.imread(up_file.name)
        #print(tfile.name)
        # ---------------------  Write the processed video frame. --------------------
        #fps = int(vf.get(cv2.CAP_PROP_FPS))
        #width, height,_ = int(vf.shape)
        #frame_size = (width, height)
        #fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        # picture_output = cv2.imwrite(
        #    output_picture_file)
        # -----------------------------------------------------------------------------

        txt = st.sidebar.markdown(ip_vid_str, unsafe_allow_html=True)
        ip_img = st.sidebar.image(up_file.name, use_column_width=True)

        # while vf.isOpened():
        #    ret, frame = vf.read()
        #    if not ret:
        #        break

        #convert frame from BGR to RGB before processing it.
        frame = cv2.cvtColor(vf, cv2.COLOR_BGR2RGB)
        out_frame, _ = upload_process_frame.process(frame, pose)
        stframe.image(out_frame)
        #picture_output.write(out_frame[..., ::-1])

        # vf.release()
        # picture_output.release()
        # stframe.empty()
        # ip_img.empty()
        # txt.empty()
        # tfile.close()

    except AttributeError:
        warn.markdown(warning_str, unsafe_allow_html=True)


# if os.path.exists(output_video_file):
#    with open(output_video_file, 'rb') as op_vid:
#        download = download_button.download_button(
#            'Download Video', data=op_vid, file_name='output_recorded.mp4')

#    if download:
#        st.session_state['download'] = True


# if os.path.exists(output_video_file) and st.session_state['download']:
#    os.remove(output_video_file)
#    st.session_state['download'] = False
#    download_button.empty()
