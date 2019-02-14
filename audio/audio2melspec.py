import dcase_util
import dcase_util.features.features as extractor
import os
import time
import numpy as np
import librosa

def melspec2(audio_path):
    y, sr = librosa.load(audio_path, sr=44100)
    assert sr == 44100

    D = librosa.stft(y=y, n_fft=2048, hop_length=441, win_length=882, window='hann', center=True, pad_mode='reflect')
    D = np.abs(D)**2
    S = librosa.feature.melspectrogram(S=D, sr=sr)
    S = librosa.power_to_db(S, ref=np.max)
    return S

def melspec2npy(audio_path, output_path, meta_path):
    S = melspec2(audio_path)
    np.save(output_path, S)
    if meta_path is not None:
        with open(meta_path, 'w') as f:
            f.write(str(S.shape))
    
    
def kinetics_audio2mel():
    root = '/data/kinetics_aud/'
    target_root = '/data/kinetics_melspec/'
    for label in os.listdir(root): 
        label_path = os.path.join(root, label)
        target_label_path = os.path.join(target_root, label)
        for audio_name in os.listdir(label_path):
            audio_path = os.path.join(label_path, audio_name)
            target_mel_path = os.path.join(target_label_path, audio_name.split('.')[0])
            if not os.path.exists(target_mel_path): os.makedirs(target_mel_path)
            if not os.path.exists(os.path.join(target_mel_path, 'mel.npy')): 
                melspec2npy(audio_path, os.path.join(target_mel_path, 'mel.npy'))

def melspec(audio_path, fps=24):
    try:
        print(audio_path)
        audio_container = dcase_util.containers.AudioContainer().load(filename=audio_path, fs=48000, mono=True)
        a = extractor.MelExtractor(fs=48000, n_fft=2048, fmin=0., fmax=24000., htk=True,logarithmic=True, \
                win_length_seconds=1/float(fps), hop_length_seconds=1/float(fps))
        feat = a.extract(audio_container).T
    except:
        return None
    return feat

def melspecnpy(audio_path, melspecnpy_path, fps=24):
    base_name = os.path.basename(audio_path)
    vid = base_name.split('.')[0][len('audio_'):]
    feat = melspec(audio_path, fps=fps)
    if feat is None:return None
    if not os.path.exists(os.path.join(melspecnpy_path, vid)):
        os.makedirs(os.path.join(melspecnpy_path, vid))
    np.save(os.path.join(melspecnpy_path, vid, 'melspec.npy'), feat)
    return feat

if __name__ == '__main__':
    kinetics_audio2mel()
