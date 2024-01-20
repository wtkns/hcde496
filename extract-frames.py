import subprocess
ffmpeg = "D:\\bin\\ffmpeg.exe"
source = "\"D:\\hcde496\\ffmpeg\\videos\\tightrope.mov\""
output = "\"D:\\hcde496\\ffmpeg\\images\\image%03d.jpg\""


command = ['ffmpeg', '-i', source, '-vf', 'fps=2',  '-y', output]

cmdstr = ' '.join(command)

print(cmdstr)

if subprocess.run(cmdstr).returncode == 0:
    print ("FFmpeg Script Ran Successfully")
else:
    print ("There was an error running your FFmpeg script")

