#%%
import os
import shutil

#%%

dir = r"data/AIDER/"

res = []

for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        res.append([path, path.split("_")[2]])

# %%
os.mkdir("other")
os.mkdir("pneumonia")
os.mkdir("normal")
os.mkdir("covid")


# %%
for i in res:
    shutil.move(dir+i[0], i[1])

# %%
