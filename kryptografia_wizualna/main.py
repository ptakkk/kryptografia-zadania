from PIL import Image
import random

# img=Image.new('RGB', (100,100),"white")
# img.save('white.png')

img = Image.open("white.png")

img_part1 = Image.new('RGB', (200, 100),"white")
img_part2 = Image.new('RGB', (200, 100),"white") # save later with img_part1.save

width = img.size[0]
height = img.size[1]

# check every pixel, if its white make two pixels (bw+bw or wb+wb) with
# probability 0,5 and add them to a new image (2*x, 2*x+1) if black
# (bw+wb or wb+bw)
# rgb black (0,0,0) rgb white (255,255,255)


for x in range(width):
    for y in range(height):
        color = img.getpixel((x, y))
        options = [1, 2]
        chosen_option = random.choice(options)

        if color == (255, 255, 255, 255):
            if chosen_option == 1:
                img_part1.putpixel((x * 2, y), (0, 0, 0))
                img_part1.putpixel((x * 2 + 1, y), (255, 255, 255))
                img_part2.putpixel((x * 2, y), (0, 0, 0))
                img_part2.putpixel((x * 2 + 1, y), (255, 255, 255))
            else:
                img_part1.putpixel((x * 2, y), (255, 255, 255))
                img_part1.putpixel((x * 2 + 1, y), (0, 0, 0))
                img_part2.putpixel((x * 2, y), (255, 255, 255))
                img_part2.putpixel((x * 2 + 1, y), (0, 0, 0))

        elif color == (0, 0, 0, 255):
            if chosen_option == 1:
                img_part1.putpixel((x * 2, y), (0, 0, 0))
                img_part1.putpixel((x * 2 + 1, y), (255, 255, 255))
                img_part2.putpixel((x * 2, y), (255, 255, 255))
                img_part2.putpixel((x * 2 + 1, y), (0, 0, 0))
            else:
                img_part1.putpixel((x * 2, y), (255, 255, 255))
                img_part1.putpixel((x * 2 + 1, y), (0, 0, 0))
                img_part2.putpixel((x * 2, y), (0, 0, 0))
                img_part2.putpixel((x * 2 + 1, y), (255, 255, 255))

img_part1.save("img_part1.png")
img_part2.save("img_part2.png")

img_part1 = img_part1.convert("L")
img_part1_mask = img_part1.point(lambda p: 255 if p < 1 else 0)
img_part1 = img_part1.convert("RGBA")
img_part1.putalpha(img_part1_mask)

img_part2.paste(img_part1, (0, 0), img_part1)
img_part2.save("img_fused.png")
