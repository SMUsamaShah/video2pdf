# video2pdf
Convert video slides/presentations to PDF

I had some Udemy videos with presentations in video form only, no PPTs given. Pieced this together to make a presentation slides from those videos.

## Install required packages

```
pip install requests
pip install moviepy
pip install img2pdf
```

## Usage

```
python video2pdf.py -f "d:/data/udemy/lecture1.mp4"
```

# Using Docker

```bash
docker run --rm -it -v d:/data:/d/ video2pdf -f "/d/udemy/Cloud Guru/lecture1.mp4"
```

Bulk example

```python
videodir = "D:/Udemy/Cloud Guru/"
file_filter = lambda p: p.endswith(".mp4") and p.find('Lab') == -1 # mp4 videos which do not contain the word 'Lab'

for f in list(filter(file_filter, os.listdir(videodir))):
    os.system('start docker run --rm -it -v d:/data:/d/ video2pdf -f \"/d/udemy/Cloud Guru/'+f+'"')
```
