#dependancies
from apng import APNG
from PIL import Image
import os

#extract frames from the result APNG
animated = APNG.open("result.apng")
pngs = []
for i, (png, control) in enumerate(animated.frames):
    currentp = f"Frame_{i}.png"
    png.save(currentp)
    pngs.append(currentp)

#iterate through all the PNG frames
original = Image.open("ostrich.jpg")
flag = ""
for png in pngs:
    #open the image
    img = Image.open(png)

    #iterate through all pixels and compare to the original
    #if the current pixel differs, it was what was used for steganography calculation
    found = None
    for x in range(original.width):
        #break if found (to save execution time)
        if found:
            break

        for y in range(original.height):
            if original.getpixel((x,y)) != img.getpixel((x,y)):
                found = (x,y)
                break

    #if nothing was found, alert
    if not found:
        print(f"No pixels for {png}")
        continue

    #get the current pixel
    print(f"Pixel located at {found}")
    original_pixel = original.getpixel(found)
    current_pixel = img.getpixel(found)

    #generate the byte string for the current flag char
    result = [current_pixel[0]]
    if current_pixel[1] != original_pixel[1]:
        result.append(current_pixel[1])

    #turn the result into an integer
    #divide the result by the last pixel and append the result to the flag
    result = int.from_bytes(bytearray(result), "big")
    result //= original_pixel[2]
    flag += chr(result)

    #delete the png file after we're done
    os.remove(png)

#print flag
print(flag)
