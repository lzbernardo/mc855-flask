import argparse, json, sys, os.path
import cv2

sys.path.append(os.path.join(os.path.dirname(__file__), 'correction'))

class Props(object):
    def __init__(self, fps=0, width=0, height=0, frames=0, codec=''):
        self._fps = fps
        self._width = width
        self._height = height
        self._frames = frames
        self._codec = codec

    def fps(self):
        return self._fps

    def frames(self):
        return self._frames

    def width(self):
        return self._width

    def height(self):
        return self._height

    def codec(self):
        return self._codec

    def seconds(self):
        fps = self.fps()
        frames = self.frames()
        return frames / fps if fps > 0 and frames > 0 else 0

def main():
    parser = argparse.ArgumentParser(description="MBP for reading openCV .mp4 files")
    parser.add_argument('-i', '--video', help='video path', required=True)
    parser.add_argument('-v', '--version', help='match version', default='6.10')
    parser.add_argument('-o', '--out', help='output file', required=True)
    parser.add_argument('-s', '--start', help='start frame', default=0, type=int)
    parser.add_argument('-e', '--end', help='end frame', default=-1, type=int)
    parser.add_argument('-f', '--fps', help='frames per second to analyze', default=10, type=int)
    parser.add_argument('--pretty', help='if true, indents the output', dest='pretty', action='store_true')
    parser.add_argument('-p','--participant', help='participant id', type=int, required=True)
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.video)
    # props = Props(
    #             fps    = cap.get(cv2.CAP_PROP_FPS),
    #             frames = cap.get(cv2.CAP_PROP_FRAME_COUNT),
    #             width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH),
    #             height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT),
    #             codec  = cap.get(cv2.CAP_PROP_FOURCC),
    #         )
    cap.release()

    # if args.end < 0:
    #     args.end = props.frames()
    #
    # if args.end <= args.start:
    #     print('end frame must be before start frame')
    #     sys.exit(1)

    # print('state tracking %s %s' % (args.video, props.__dict__))


if __name__ == '__main__':
    main()
