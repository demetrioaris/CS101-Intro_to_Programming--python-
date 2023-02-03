from PIL import Image

image_green = Image.open('spaceshuttle.jpg')
image_sunset = Image.open('sunset.jpg')

combined_imagen = Image.new('RGB' , image_sunset.size)

pixels_sunset = image_sunset.load()
pixels_green = image_green.load()
pixels_combined = combined_imagen.load()

(width, height)= image_sunset.size

color = pixels_green[1, 1] 

for x in range(0, width):
  for y in range(0, height):
    (r, g, b) = pixels_green[x, y]
    if r <= 150 and g >= 210 and b <= 60:
      pixels_green[x, y] = pixels_sunset[x, y]
    elif r <= 145 and g >= 210 and b <= 145:
      pixels_green[x, y] = pixels_sunset[x, y]
    elif r <= 230 and g >= 254 and b <= 155:
      pixels_green[x, y] = pixels_sunset[x, y]
    elif r <= 164 and g >= 164 and b <= 230:
      pixels_green[x, y] = pixels_sunset[x, y]
    elif r <= 66 and g >= 120 and b <= 84:
      pixels_green[x, y] = pixels_sunset[x, y]
    elif r <= 130 and g >= 200 and b <= 130:
      pixels_green[x, y] = pixels_sunset[x, y]
    #elif r <= 121 and g >= 178 and b <= 134:
      #pixels_green[x, y] = pixels_sunset[x, y] too much??

    pixels_combined[x, y] = pixels_green[x, y]
    
combined_imagen.save('space.jpg')
combined_imagen.show()

#image_green.show()
#image_desert.show()





