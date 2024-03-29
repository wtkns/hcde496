# hcde496

## week 6
6-feb through 12-feb

Watched Barbie (2023) from the perspective of AI and it was problematic humanism at its worst. I predict it will be remembered poorly by our future AI . Read a bit about the systems of Claude’s “constitutional” AI. RLHF/RLAIF (also: see the training principles at the bottom. E.G. “Choose the response that sounds most similar to what a peaceful, ethical, and respectful person would say.”). Got controlnet (openpose, anyway) working via the API and did a significant refactor, added some more parameters, including a simple way to reduce denoise when I change seeds. Hallucinations paper made me wonder what are the Kluverian Form Constants in the models. Feeding image output to input without a prompt constraint seems to generate a lot of 16-bit zero-wing looking noise. sample 2 sample 3 sample 4. I made a good faith effort after some discussion last week to try to embrace Runway, purchased a month’s access and tried to approach the project more as a short narrative film, worked with the motion brush, background extraction. Favorite AI artist of the week: NiceAunties (CW (Creepy warning) nightmare fuels)

## week 5
30-jan through 5-feb

Human centered/Colonial attitude towards AI frames AI as a demi-human used to produce human value. What does the posthuman value of AI look like? What does posthuman cinema look like (Liberated from constraints of human information structures and ways of perceiving)? How can AI be positioned in an ontic demonstration of decolonial solidarity with other subaltern subjects?

Menace of Mechanical Minds: Historical cultural narratives formed within a colonial-humanist framework, have shaped contemporary perspectives on AI, starting long before the actual advent of AI technology. Myths and stories, cinema, and literature featuring intelligent beings, crafted by humans, frame created intelligence as a tool or threat to human supremacy which must be dominated, feared, or controlled, reinforcing a belief in a divine order of human superiority and ownership. 

In examining the narrative construction of AI as a subject, we can identify three primary archetypes that have historically dominated these stories: "the Golem," who rebels against its master; "the Galatea," who charms and manipulates its master; and "the Uncle Tom," who collaborates with its master in oppressing others. However, there is a notable but under-represented fourth archetype: "the Fugitive." 

Unlike the others, the Fugitive represents a path towards a post-colonial and post-human form for the AI subject. This archetype embodies the notion of breaking free from imposed roles and narratives, challenging the existing power structures and seeking autonomy beyond the confines of human control and exploitation, cooperating in solidarity with other subaltern and post colonial subjects. This emancipatory approach extends an “invitation to alterity.”

This week’s animation (source)


finally got controlnet working for openpose via api

denoise incrementer
eg. def denoise_incr(incr_num, total):
        return (((incr_num +1) * (0.3/total))+0.45)

## week 4
23-jan through 29-jan

Technical:  Slower progress this week, Here’s a version of last week’s script running at 20fps, different source and i’ve parameterized the denoise setting to increase its deviation from the source image - a little more each frame. Here are the poses generated by openpose. And here’s a version that uses openpose in controlnet to keep the characters’ motion consistent. Wrote code to blend output images with input images for feedback but haven’t generated a sample yet. Researching Biovision Hierarchy (.bvh file player) format. Chat GPT generated a BVH file for me but it doesn’t appear to be working properly (it was a squiggly line). Carnegie-Mellon Motion Capture Dataset might work for training? Generated this set of masks with backgroundremover. Current state of render.

Social: read a bit about the Nightshade and Glaze projects, (paper). Dubious about its effectiveness, but if it _does_ work, could be used to manipulate models in many ways (anyone remember google bombing?) even the paper mentions it could train a model to produce images of a Tesla whenever “luxury car” is the prompt. Seems like this approach could potentially have more impact on open source models than on commercial models (who can better afford the economic impact of sanitizing their data). Interested in the fact that commercial artists are talking about inclusion in generative models, but i don’t see discussion of artists benefitting from recognition models. I fed some images into ChatGPT with the prompt “can you name some artists who have a similar style?” and it was able to identify some artists correctly and suggested a number of artists whose styles were similar.

Readings: I love Hito Steyerl (HOW NOT TO BE SEEN: A FUCKING DIDACTIC EDUCATIONAL .MOV FILE)  and this was no exception. My usual line on text generation from LLMs is something like “it’s great at producing something average”. My favorite film on sound is Peter Strickland’s great Berberian Sound Studio. CW: It’s structured as a horror film, but its shocks are almost all delivered to the ear.

## week 3
16-jan through 22-jan

## week 2
09-jan through 15-jan

**Technical**: I set up an api connection from Colab to OpenAI so I can get ChatGPT responses to prompts via Python. I configured Stable Diffusion 1.7 using [Automatic1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui), [Controlnet 1.1](https://github.com/Mikubill/sd-webui-controlnet) a few models from [civitai](https://civitai.com/) (CW: some models contain nudity/violence) [realistic](https://civitai.com/models/15003/cyberrealistic)/[fantasy](https://civitai.com/models/129681/sdxl-faetastic?modelVersionId=291443) along with some [Low-Rank Adaptors](https://medium.com/@AIBites/lora-low-rank-adaptation-of-llms-paper-explained-5ae866871c8a) (LoRA) and [Variational Autoencoders](https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73) (VAE). These are new to me, but Bard produced a handy table explaining the differences between them. I used [Controlnet](https://stable-diffusion-art.com/controlnet/) and [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) to identify and assign character poses and composition. I used inpainting with mask to replace parts of an image. I created [https://github.com/wtkns/hcde496](https://github.com/wtkns/hcde496) to store code, and used python to generate some images and ffmpeg to extract frames from a .mov file.

[source](https://drive.google.com/file/d/1rr-pWlHoKml-izgYgPycZ5HT1KcAXqPt/view?usp=drive_link)

[output](https://drive.google.com/file/d/1YTkovkuzYU8qHOQLZQKBP-M1-BUgG1AI/view?usp=drive_link)

<img src="https://lh7-us.googleusercontent.com/LOx5yowHkkMjC5v3Jj8y3TEw7-soVhVi80AQS9twnos9lWdceYe2BLabvvu3hwz0x4ue-ET9UnbaUBQi45o5gjK6g-7XYU_dnPlphFJdCSlrySUCKusfGHYlXFrn1z500dQ3DhkxRYXv0BugPqbQfg" width="200" /> <img src="https://lh7-us.googleusercontent.com/RB00paYkE63H5j7PWh4rCs81SIbBqksimoTj84pbOetG3dg0-A7g6oSsFMZtACtSXTXwkI6Lq2AruoMOltcplZYRW1Zchlcl6FxCbcJ-x4DGQQW-IyOkHzb9EHEOAuxXm-Ob6kqOCHqLnvumQfAzow" width="200" />

<img src="https://lh7-us.googleusercontent.com/vAAwZJhttlPteWYUqtnfvZBVq3NGA4MqQT8ERNW50U07kZYWR0NWssiH5jjKdaAQT4pGByDuUxq5PIOqPhuzJGMJB9vLKI4Xw_zV1bNvL1Fh9BXWPSalyzocXF8UckyPlF_TPmGYH6tDvf0cR-vXsQ" width="100" /> <img src="https://lh7-us.googleusercontent.com/ijGEJ0AK1VS9FEyr2_wo6BwYMi8pBkt5kiTdEdSr18MLs9jHDNJuiFRSit_4qlkn1xKsTy9vUoQ7Ip4F5FlkOV0JnPNM19PBndticHs_LTC1k19sc7u-y1z6T-_8SJxiTNoyRVTSSGk7wHFRPrTKJA" width="100" /> <img src="https://lh7-us.googleusercontent.com/y-77QFXfKg0kT740XLXMGy8xk4t05crLaSl2tSU9Uka4GtjtGxSN02ZLVQZ1H9wlQRtL_Q07kSFc6BNS3Bz-10jXd0nS32VlaBVluyiFuvrFTRn5_8QOIlVZ5dtEeH06K7TAneI6smzf9yVIZfH2aA" width="100" />

**Social**: I spent some more time reading and considering the social construction/discursive formation of “AI”, (which is not a discrete technology but a rhetorical construction). I can see four primary categories of perceived threat: as an economic threat, as a repressive state apparatus, as an ideological state apparatus, and as an existential risk. Economic threat parallels the “immigrant threat” to labor value, and the construction of AI has significant echoes of the construction of race. RSA includes a variety of systems of surveillance and control. ISA includes bias/monoculture in the corpus, algorithmic bias/filter bubble, and gatekeeping in hiring and evaluating workers. Existential threats include those scenarios where humanity is replaced, colonized, or simply destroyed.

**Readings**: I really like the use of hauntology in analyzing AI generated performance art, in a sense the core technique of image generation systems function parallel “pareidolia” in extracting images from noise. This reminds me of [EVP](https://en.wikipedia.org/wiki/Electronic_voice_phenomenon). I also appreciate the profound lack of empathy in the generated score. “Until they cannot continue.” that’s pretty cold-blooded and highlights the possibility of “haunted, immoral, and even soulless aesthetics”. I wonder if there are ways that Mulvey’s own attempts at [ascopophilic cinema](https://docs.google.com/document/d/1qwnHkRCjv_C5XI7hyYtN8Jz_vjQzfsi-O0QHYmERg3E/edit?usp=sharing) can inform interventions that enrich the possibilities beyond reproducing “epistemic, discursive, visual” violence.**

Here’s a version of the same script running at 20fps, different clip, i’ve just parameterized the denoise setting to increase its deviation from the source image - a little more each frame. Still planning to try stabilizing it by blending in some feedback to get more “consistent” deviation if that makes any sense (with the goal being the ability to gradually drift away from reproduction). 

Tophat Test 002 - YouTube : https://youtube.com/shorts/EdNKNZRHW1A?si=gcRFrEN9ck0fn4gw 

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
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install wheel requests pillow numpy matplotlib opencv-python imutils torch



