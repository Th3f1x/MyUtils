from rembg import remove
from PIL import Image 

input_path = input("write the path of image:")
output_path = input_path + 'clean.png'


input1 = Image.open(input_path)
output = remove(input1)

output.save(output_path)
