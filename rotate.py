
from PIL import Image 
import sys

file = sys.argv[1]
im = Image.open(file)

def flipleft(im):
    out = im.transpose(Image.FLIP_LEFT_RIGHT)
    out.show()

def flipbottom(im):
    out = im.transpose(Image.FLIP_TOP_BOTTOM)
    out.show()

def rotate(im):
    out = im.transpose(Image.ROTATE_90)
    out.show()

func = {"flip left": flipleft, "flip bottom": flipbottom, "rotate 90": rotate}

print("Here are your options:")

for o in func.keys():
    print(o)

trans = input("What transformation would you like: ").lower()
try: 
    func[trans](im)

except:
    print("Please enter a valid transformation ")
    exit
    
a = "vinaya hazel krish"
print(a.split())


