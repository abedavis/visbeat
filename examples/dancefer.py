
# coding: utf-8

# # TL;DR - Just show me dancing stuff
#
# Ok -- just specify a source video and a target video and press go. Look at the other notebooks if you want to fine-tune your results.

# In[8]:

import sys
import matplotlib
matplotlib.use('PS')
import visbeat

source_url = 'https://www.youtube.com/watch?v={}'.format(sys.argv[0]);
target_url = 'https://www.youtube.com/watch?v={}'.format(sys.argv[1]);

output_path = sys.argv[2];

result = visbeat.AutoDancefer(source=source_url, target = target_url,
                              output_path = output_path,
                              synch_video_beat = 0,
                              synch_audio_beat = 0,
                              beat_offset = 64,
                              nbeats = 128);
result.play();