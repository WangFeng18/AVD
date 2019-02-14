import skvideo.io
import skvideo.datasets
import json
import time
def meta(path):
    metadata = skvideo.io.ffprobe(path)
    return metadata

def fps(path):
    metadata = skvideo.io.ffprobe(path)
    _fps = metadata['video']['@avg_frame_rate']
    return eval(_fps)

if __name__ == '__main__':
    test_path = '/matrix/AVL/data/origin/Video/video_4fmu365Ioak.mp4'
    meta(test_path)
