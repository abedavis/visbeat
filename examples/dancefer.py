import sys
import argparse
import matplotlib
matplotlib.use('PS')
import visbeat
import os

def main(args):
    if(os.path.exists(args.source)):
        source_url = args.source;
    else:
        source_url = 'https://www.youtube.com/watch?v={}'.format(args.source);

    if(os.path.exists(args.target)):
        target_url = args.target;
    else:
        target_url = 'https://www.youtube.com/watch?v={}'.format(args.target);

    print("Source: {}\nTarget: {}".format(source_url, target_url));

    output_path = args.output_path;
    if(output_path is None):
        output_path = './result.mp4';

    result = visbeat.AutoDancefer(source=source_url, target = target_url,
                                  output_path = output_path,
                                  synch_video_beat = 0,
                                  synch_audio_beat = 0);
    print("Result saved to {}".format(result.getPath()));


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("source",
                        help="Source video you want to warp. Can be a youtube vide id (get it from youtube urls 'https://www.youtube.com/watch?v=[VIDEO_ID]') or a path to a video file.");
    parser.add_argument("target",
                        help="Target song. For now now use a video (will update later). Can be a youtube vide id or a path to a video file.)");
    parser.add_argument("-o", "--output_path", help="path for the output file");
    args = parser.parse_args();
    main(args);