import subprocess
api_dir = "D:\\stableDiffusion\\stable-diffusion-webui\\"
api_bat = "api-webui-user.bat"
cmdstr = ".\\" + api_bat

print(cmdstr)

subprocess.check_call([cmdstr], cwd=api_dir)

# if subprocess.run(cmdstr).returncode == 0:
#     print ("API init Script Ran Successfully")
# else:
#     print ("There was an error running your API init script")

