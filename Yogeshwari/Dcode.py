from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

# # Load the WAV file
file_path = 'yoKgUeWsEhNwIari.wav'
sample_rate, data = wavfile.read(file_path)

# Checking if the audio data is stereo and converting it to mono if necessary
if len(data.shape) > 1:
    # Assuming the audio is stereo, we'll average the channels to convert it to mono
    data_mono = data.mean(axis=1)
else:
    # If the audio is already mono, we'll use it as is
    data_mono = data

# Retry generating the spectrogram with the mono audio data
plt.figure(figsize=(10, 4))
plt.specgram(data_mono, Fs=sample_rate, NFFT=1024, noverlap=512)
plt.title('Spectrogram of Mono Audio')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.colorbar(label='Intensity (dB)')

# Save the updated spectrogram to an image file
spectrogram_mono_path = 'spectrogram_mono.png'
# plt.savefig(spectrogram_mono_path)
# plt.close()
plt.show()