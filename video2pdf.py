import os
import img2pdf
import tempfile
import argparse
import sys
import random
import shutil
import moviepy.editor as mpe
import moviepy.video.tools.cuts as mpc

def video2images(filepath, imagesdir, imageformat):
    ''' Return a list of images from a given video '''

    video = mpe.VideoFileClip(filepath)
    video_small = video
    # video_small = video.resize(width=150)
    scenes = mpc.detect_scenes(video_small)

    i = 0
    for t1, t2 in scenes[0]:
        if t1 < 3 or t2 - t1 < 0.5: # skip first 3 seconds and ignore small changes
            continue
        
        img = os.path.join(imagesdir, "{}.{}".format(i, imageformat)) 
        print(img)

        video.save_frame(img, t1)  # save frame as JPEG
        i += 1

    return i



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="full path of video file")
    parser.add_argument("-t", "--type", help="png or jpg?", default="jpg", choices=['jpg', 'png'])
    parser.add_argument("-o", "--output", help="output pdf")
    parser.add_argument("-d", "--delete", help="remove images", action='store_true')
    
    args = parser.parse_args()
    args.filepath = args.filepath.replace('\\', os.sep)

    base_name = os.path.splittext(os.path.basename(args.filepath))[0]

    pdf_path = base_name + ".pdf" if args.output is None else args.output

    img_dir = tempfile.mkdtemp()
    print("Images will be saved in " + img_dir)
    img_count = video2images(args.filepath ,img_dir, args.type)

    print("Saving PDF as " + pdf_path)

    with open(pdf_path, "wb") as f:            
        f.write(img2pdf.convert([os.path.join(img_dir, '{}.{}'.format(i, args.type)) for i in range(0,img_count)]))

    print("PDF saved at " + pdf_path)

    if args.delete:
        shutil.rmtree(img_dir)
