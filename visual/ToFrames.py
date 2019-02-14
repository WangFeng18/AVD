import os
import glob
 
def ToFrames(video_path, frames_path, frames_fps, wxh='112x112', name_format='%04d.jpg'):
    cmd = 'ffmpeg -i \'{}\' -r {} -s {} \'{}\''.format(video_path, frames_fps, wxh, os.path.join(frames_path, name_format))
    os.system(cmd)
    n_imgs = len(glob.glob(pjoin(frames_path, '*.jpg')))
    with open(pjoin(frames_path, 'meta.txt'), 'w') as f:
        f.write(str(n_imgs))
    
