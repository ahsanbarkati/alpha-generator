from PIL import Image
import sys
import matplotlib.pyplot as plt

args=sys.argv[1:]

image_path= args[0]
out_name=args[1]
image = Image.open(image_path).convert('RGBA')
alpha = image.split()[-1]
plt.imsave(out_name, alpha)
