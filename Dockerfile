FROM python:3

RUN pip install requests
RUN pip install moviepy
# this downloads ffmpeg required by moviepy
RUN python -c 'from moviepy.editor import VideoFileClip' 
RUN pip install img2pdf

WORKDIR /data
COPY video2pdf.py ./

ENTRYPOINT [ "python", "./video2pdf.py"]
