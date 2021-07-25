import visbeat as vb
import os


source_video_url = 'https://www.youtube.com/watch?v=tgfDbTactbE'
target_music_url = 'https://www.youtube.com/watch?v=prPjpwsGiws'

output_path = './MyFunnyVideo.mp4'

vb.SetAssetsDir('.'+os.sep+'VisBeatAssets'+os.sep)
source = vb.PullVideo(source_location=source_video_url)
target = vb.PullVideo(source_location=target_music_url)

synch_video_beat = 0
synch_audio_beat = 0
nbeats = 16


warped = vb.Dancefer(source_video=source, target=target, synch_video_beat=synch_video_beat,
                    synch_audio_beat=synch_audio_beat, force_recompute=True, warp_type = 'quad',
                    nbeats=nbeats, output_path = output_path)


print("Your result was saved to: {}".format(warped.getPath()))
