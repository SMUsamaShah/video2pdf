# video2pdf
Convert video slides/presentations to PDF

I had some Udemy videos with presentations in video form only, no PPTs given. Pieced this together to make a presentation in form of PDF from those videos. 

Uses moviepy to detect scenes and create images, then img2pdf is used to generate PDF.

## Install required packages

```
pip install requests
pip install moviepy
pip install img2pdf
```

## Usage

```
usage: video2pdf.py [-h] [-t {jpg,png}] [-o OUTPUT] [-d] [-x1 X1] [-y1 Y1]
                    [-x2 X2 | -W W] [-y2 Y2 | -H H]
                    filepath

positional arguments:
  filepath              full path of video file

optional arguments:
  -h, --help            show this help message and exit
  -t {jpg,png}, --type {jpg,png}
                        png or jpg?
  -o OUTPUT, --output OUTPUT
                        output pdf
  -d, --delete          remove images
  -s THRESHOLD, --threshold THRESHOLD
                        scene detection threshold, default=5

crop:
  -x1 X1                top left corner x value
  -y1 Y1                top left corner y value
  -x2 X2                bottom right corner x value
  -W W                  width of the rectangle
  -y2 Y2                bottom right corner y value
  -H H                  height of the rectangle
```
Example
```
python video2pdf.py "d:/data/udemy/lecture1.mp4"
```

## Using Docker

Pull image from docker hub

```
docker pull smusamashah/video2pdf
```

Mount a directory and convert the file

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
