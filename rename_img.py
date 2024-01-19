import os


folder = "lights/red/"
imgspath = os.listdir(folder)
os.chdir(folder)

counter = 0
for img in imgspath:
    os.rename(img, "red_" + str(counter) + ".png")
    counter += 1
    