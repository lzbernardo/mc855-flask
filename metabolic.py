import argparse, json, sys, os.path

import cv2

from video_props import VideoProps
from spatial_layout import find_layout
from frame_state import states_from_video, state_from_frame

from post_process.correct_states import correct_states

def process(f_video, f_fps, f_participant):
    # parser = argparse.ArgumentParser(description='LolOCR python wrapper. Generates raw ocr states from input video.')
    # parser.add_argument('-i', '--video', help='video path', required=True)
    # parser.add_argument('-v', '--version', help='match version', default='6.10')
    # parser.add_argument('-o', '--out', help='output file', required=True)
    # parser.add_argument('-s', '--start', help='start frame', default=0, type=int)
    # parser.add_argument('-e', '--end', help='end frame', default=-1, type=int)
    # parser.add_argument('-f', '--fps', help='frames per second to analyze', default=10, type=int)
    # parser.add_argument('--pretty', help='if true, indents the output', dest='pretty', action='store_true')
    # parser.add_argument('-p','--participant', help='participant id', type=int, required=True)
    # parser.add_argument('--debug', help='debugging flag (opencv prints video)', dest='debug', action='store_true')
    # parser.add_argument('--old', help='uses old layout style', dest='old', action='store_true')
    # args = parser.parse_args()

    # initialization / setup
    cap = cv2.VideoCapture(f_video)
    props = VideoProps(cap)
    layout = find_layout('6.10', props.width(), props.height(), False)
    cap.release()

    if props.frames() <= 0:
        print('end frame must be before start frame')
        return 0

    print(('state tracking %s %s' % (f_video, props.__dict__)))
    states = states_from_video(
        debugging=False,
        video_path=f_video,
        props=props,
        layout=layout,
        first_frame=0,
        last_frame=props.frames(),
        frames_per_sec=f_fps,
        participant=f_participant)

    f = open('demo.json', 'w')
    j = json.dumps(states)
    f.write(j)
    f.close()
    return 1
