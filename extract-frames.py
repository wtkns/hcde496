import subprocess
ffmpeg = "D:\\bin\\ffmpeg.exe"
source = "\"D:\\hcde496\\Projects\\meshes\\meshes2.mp4\""
output = "\"D:\\hcde496\\Projects\\meshes\\images2\\image%03d.jpg\""


command = ['ffmpeg', '-i', source, '-vf', 'fps=20',  '-y', output]

cmdstr = ' '.join(command)

print(cmdstr)

if subprocess.run(cmdstr).returncode == 0:
    print ("FFmpeg Script Ran Successfully")
else:
    print ("There was an error running your FFmpeg script")

