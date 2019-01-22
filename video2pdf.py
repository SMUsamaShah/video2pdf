import os
import img2pdf
import tempfile
import argparse
import sys
import random
import shutil
import moviepy.editor as mpe
import moviepy.video.tools.cuts as mpc

def video2images(fullname, imageformat="png"):
    ''' Return a list of images from a given video '''
    filename_noext = os.path.basename(fullname).rsplit(".", 1)[0]
    imagesdir = os.path.join(tempfile.gettempdir(), filename_noext + str(random.randint(0, 9999)))

    if os.path.exists(imagesdir) == False:
        os.mkdir(imagesdir)
    print("Images will be save to ", imagesdir)

    video = mpe.VideoFileClip(fullname)
    video_small = video.resize(width=150)
    scenes = mpc.detect_scenes(video_small)

    i = 0
    for t1, t2 in scenes[0]:
        if t1 < 3 or t2 - t1 < 0.5: # skip first 3 seconds and ignore small changes
            continue
        
        img = os.path.join(imagesdir, "{:0>3d}.jpg".format(i)) 
        print(img)

        video.save_frame(img, t1)  # save frame as JPEG
        i += 1

    # list of full path of each image
    return [os.path.join(imagesdir, i) for i in sorted(os.listdir(imagesdir)) if i.endswith("."+imageformat)]


def images2pdf(images, pdfpath):
    ''' Make PDf file from list of given images '''

    assert len(images) > 0
    
    print(images)

    try:
        with open(pdfpath, "wb") as f:            
            f.write(img2pdf.convert(images))
            return pdfpath

    except Exception as e:
        print("File Error: ", e)
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepath", help="full path of video file", type=str, required=True)
    parser.add_argument("-t", "--type", help="png or jpg?", type=str, const="jpg", default="jpg", nargs='?')
    parser.add_argument("-o", "--output", help="output pdf", type=str)
    parser.parse_args()

    args = parser.parse_args()
    args.filepath = args.filepath.replace('\\', os.sep)

    # by default, pdf will be created on the same path as input with the same name
    if args.output == None:
        args.output = os.path.abspath(args.filepath)+".pdf"

    images = video2images(args.filepath, args.type)
    print("Saving PDF as " + args.output)
    pdf = images2pdf(images, args.output)
    print("PDF saved at " + pdf)

    # cleanup
    # for i in images:
    #     os.remove(i)

    # except Exception as e:
    #     exc_type, exc_obj, exc_tb = sys.exc_info()
    #     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #     print(e, exc_type, fname, exc_tb.tb_lineno)