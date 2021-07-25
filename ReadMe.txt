Work on python 3.5.1  
Jupiter Notebook compatibility has not been tested.   


First, you need to install the associated libraries. You can do this with pip. 

>>>pip istall audioread==2.1.0 beautifulsoup4==4.9.3 bs4==0.0.1 certifi==2019.9.11 cffi==1.13.2 cycler==0.10.0 ffmpeg==1.4 ffmpeg-python==0.2.0 imageio==2.4.1 imageio-ffmpeg==0.4.0 librosa==0.6.0 llvmlite==0.30.0  matplotlib==3.0.3 moviepy==0.2.3.1 numba==0.46.0 numpy==1.16.5 opencv-python==3.4.2.16 Pillow==6.2.1 pip==19.3.1 scipy==1.2.2 setuptools==41.6.0 some-package==0.1 SoundFile==0.10.2 soupsieve==1.9.5 urllib3==1.25.7 youtube-dl==2021.6.6

All files and folders must be located in the project folder.


You will see error that "bytes/bytes_obj cannot be interpreted as an str", you can fix that like hear:
>>>    if type(path) == bytes:							#Chek what we have
>>>        return (str(path.decode('utf-8'))).replace(os.sep + os.sep, os.sep)	#Return what we need

How i understand movieplay at same moment convert str to bytes and support libs don`t gone for that. 

After fixing support libs visbeat ready for be use.