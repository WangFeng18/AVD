import os

def video2visual(video_path, visual_path):
    cmd = 'ffmpeg -i \'{}\' -vcodec copy –an \'{}\''.format(video_path, visual_path)
    os.system(cmd)

def video2audio(video_path, audio_path):
    cmd = 'ffmpeg -i \'{}\' -vn -y -acodec copy \'{}\''.format(video_path, audio_path)
    os.system(cmd)

def compose(visual_path, audio_path, video_path):
    cmd = 'ffmpeg -i \'{}\' -i \'{}\' -vcodec copy -acodec copy \'{}\''.format(visual_path, audio_path, video_path)

if __name__ == '__main__':
    kinetics_video2audio()
