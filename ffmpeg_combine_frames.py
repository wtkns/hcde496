#  ffmpeg -framerate 20 -i D:\hcde496\Projects\name\images\output\image-%03d.png -c:v libx264 -pix_fmt yuv420p out-hd.mp4

import subprocess

session="20240204_113139"

ffmpeg = "D:\\bin\\ffmpeg.exe"
images_input = "\"D:\\hcde496\\Projects\\tophat\\images\\output\\20240204_113139\\image-\%03d.jpg\""
video_output = "\"D:\\hcde496\\Projects\\tophat\\20240204_113139.mp4\""

command = ['ffmpeg', '-i', images_input, '-vf', 'fps=20',  '-y', video_output]

cmdstr = ' '.join(command)

print(cmdstr)

if subprocess.run(cmdstr).returncode == 0:
    print ("FFmpeg Script Ran Successfully")
else:
    print ("There was an error running your FFmpeg script")


# f'{project_name}.mkv'