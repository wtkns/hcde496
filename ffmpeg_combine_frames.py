#  ffmpeg -framerate 20 -i D:\hcde496\Projects\name\images\output\image-%03d.png -c:v libx264 -pix_fmt yuv420p out-hd.mp4

import subprocess

session="20240131_174653"

ffmpeg = "D:\\bin\\ffmpeg.exe"
images_input = "\"D:\\hcde496\\Projects\\meshes\\images\\output\\ \\image%03d.jpg\""
video_output = "\"D:\\hcde496\\Projects\\meshes\\meshes2.mp4\""

command = ['ffmpeg', '-i', source, '-vf', 'fps=20',  '-y', output]

cmdstr = ' '.join(command)

print(cmdstr)

if subprocess.run(cmdstr).returncode == 0:
    print ("FFmpeg Script Ran Successfully")
else:
    print ("There was an error running your FFmpeg script")


f'{project_name}.mkv'