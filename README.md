# hcde496

## week 2
09-jan through 15-jan

**Technical**: I set up an api connection from Colab to OpenAI so I can get ChatGPT responses to prompts via Python. I configured Stable Diffusion 1.7 using [Automatic1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui), [Controlnet 1.1](https://github.com/Mikubill/sd-webui-controlnet) a few models from [civitai](https://civitai.com/) (CW: some models contain nudity/violence) [realistic](https://civitai.com/models/15003/cyberrealistic)/[fantasy](https://civitai.com/models/129681/sdxl-faetastic?modelVersionId=291443) along with some [Low-Rank Adaptors](https://medium.com/@AIBites/lora-low-rank-adaptation-of-llms-paper-explained-5ae866871c8a) (LoRA) and [Variational Autoencoders](https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73) (VAE). These are new to me, but Bard produced a handy table explaining the differences between them. I used [Controlnet](https://stable-diffusion-art.com/controlnet/) and [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) to identify and assign character poses and composition. I used inpainting with mask to replace parts of an image. I created [https://github.com/wtkns/hcde496](https://github.com/wtkns/hcde496) to store code, and used python to generate some images and ffmpeg to extract frames from a .mov file.

<img src="https://lh7-us.googleusercontent.com/LOx5yowHkkMjC5v3Jj8y3TEw7-soVhVi80AQS9twnos9lWdceYe2BLabvvu3hwz0x4ue-ET9UnbaUBQi45o5gjK6g-7XYU_dnPlphFJdCSlrySUCKusfGHYlXFrn1z500dQ3DhkxRYXv0BugPqbQfg" width="200" /> <img src="https://lh7-us.googleusercontent.com/RB00paYkE63H5j7PWh4rCs81SIbBqksimoTj84pbOetG3dg0-A7g6oSsFMZtACtSXTXwkI6Lq2AruoMOltcplZYRW1Zchlcl6FxCbcJ-x4DGQQW-IyOkHzb9EHEOAuxXm-Ob6kqOCHqLnvumQfAzow" width="200" />

<img src="https://lh7-us.googleusercontent.com/vAAwZJhttlPteWYUqtnfvZBVq3NGA4MqQT8ERNW50U07kZYWR0NWssiH5jjKdaAQT4pGByDuUxq5PIOqPhuzJGMJB9vLKI4Xw_zV1bNvL1Fh9BXWPSalyzocXF8UckyPlF_TPmGYH6tDvf0cR-vXsQ" width="100" /> <img src="https://lh7-us.googleusercontent.com/ijGEJ0AK1VS9FEyr2_wo6BwYMi8pBkt5kiTdEdSr18MLs9jHDNJuiFRSit_4qlkn1xKsTy9vUoQ7Ip4F5FlkOV0JnPNM19PBndticHs_LTC1k19sc7u-y1z6T-_8SJxiTNoyRVTSSGk7wHFRPrTKJA" width="100" /> <img src="https://lh7-us.googleusercontent.com/y-77QFXfKg0kT740XLXMGy8xk4t05crLaSl2tSU9Uka4GtjtGxSN02ZLVQZ1H9wlQRtL_Q07kSFc6BNS3Bz-10jXd0nS32VlaBVluyiFuvrFTRn5_8QOIlVZ5dtEeH06K7TAneI6smzf9yVIZfH2aA" width="100" />

**Social**: I spent some more time reading and considering the social construction/discursive formation of “AI”, (which is not a discrete technology but a rhetorical construction). I can see four primary categories of perceived threat: as an economic threat, as a repressive state apparatus, as an ideological state apparatus, and as an existential risk. Economic threat parallels the “immigrant threat” to labor value, and the construction of AI has significant echoes of the construction of race. RSA includes a variety of systems of surveillance and control. ISA includes bias/monoculture in the corpus, algorithmic bias/filter bubble, and gatekeeping in hiring and evaluating workers. Existential threats include those scenarios where humanity is replaced, colonized, or simply destroyed.

**Readings**: I really like the use of hauntology in analyzing AI generated performance art, in a sense the core technique of image generation systems function parallel “pareidolia” in extracting images from noise. This reminds me of [EVP](https://en.wikipedia.org/wiki/Electronic_voice_phenomenon). I also appreciate the profound lack of empathy in the generated score. “Until they cannot continue.” that’s pretty cold-blooded and highlights the possibility of “haunted, immoral, and even soulless aesthetics”. I wonder if there are ways that Mulvey’s own attempts at [ascopophilic cinema](https://docs.google.com/document/d/1qwnHkRCjv_C5XI7hyYtN8Jz_vjQzfsi-O0QHYmERg3E/edit?usp=sharing) can inform interventions that enrich the possibilities beyond reproducing “epistemic, discursive, visual” violence.**


## week 1 
02-jan through 08-jan

Over the past week I spent some time exploring the [Espresso Dad](https://www.instagram.com/reel/C0ttPyvubFz/?igsh=MTVxYXl3aHc5a2dneg%3D%3D)/[Hard Mix](https://www.instagram.com/p/C0SH4hsSeqZ/?img_index=1) method, the [Oatmeal](https://emshort.blog/2016/09/21/bowls-of-oatmeal-and-text-generation/) problem, and contemplated parallels between the “[The Menace of Mechanical Music](https://ocw.mit.edu/courses/21m-380-music-and-technology-contemporary-history-and-aesthetics-fall-2009/18ab3aba9fe7aa1502a55cd049333659_MIT21M_380F09_read02_sousa.pdf)” (1906) and today’s anxieties about AI art and [commercial](https://slate.com/technology/2014/05/white-smith-music-case-a-terrible-1908-supreme-court-decision-on-player-pianos.html) music [copyright](https://en.wikipedia.org/wiki/White-Smith_Music_Publishing_Co._v._Apollo_Co.). I used CGPT4 to compile a list of artists (below) relevant to the course and started reviewing their work.

I got some direct experience with the cis/white/het/male [algorithmic bias](https://arxiv.org/ftp/arxiv/papers/2312/2312.14769.pdf) in ChatGPT 4 with it becoming extremely apparent when generating characters and illustrations of characters. One of my scripts included a “diverse” panel discussion on AI When I asked it to be specific, it suggested stereotypical diversity: an Asian male AI programmer, a White woman AI ethicist, a Hispanic male community organizer. When I challenged this as “superficial diversity” it agreed, apologized, and then generated a wise, old, South Asian man and a young Black woman with “strong feelings” about AI, instead. Finally, when it generated an image of this panel, it hallucinated a white male moderator. 

I generated a few short narrative and essay film script ideas, none were compelling, and I started looking at [ML Agents in Unity](https://unity.com/products/machine-learning-agents) and connecting it to ChatGPTI via api, to generate real time improvised AI cinema. Towards this end I generated a couple of GPT Chatbots for characters and had them interact by copying and pasting their responses to each other in the web client. 1. [Rocque](https://chat.openai.com/g/g-sFehsJgva-rocque), “a punk expert, privacy advocate, and progressive activist”; and 2. [Pat Parley](https://chat.openai.com/g/g-RBpOagWOS-pat-parley), “a conservative, vegan, pizza parlor manager, juggling work and family while facing personal challenges.” I put these two into conflict by suggesting Rocque was late to work at the pizza parlor; but their conflict was unhelpfully healthy. I get it, I am conflict averse, too, so I may just end up generating non-narrative cinema.



![random image](output.png?raw=true "image")


## setup SD
## setup ffmpeg


## start SD
cd D:\stableDiffusion\stable-diffusion-webui
.\api-webui-user.bat

## Setup
py -m venv .venv
.venv\Scripts\activate
py -m pip install --upgrade pip
py -m pip install requests pillow



