from PIL import Image, ImageFont, ImageDraw

def generateInfoGraphic(info,typeface,fontSize,R,G,B):

    # coords for where to place text
    xpos = [421, 282, 90, 478, 684]
    ypos = [12, 172, 172, 172, 172]

    info[0]=info[0]+", here are your numbers for November..."
    img = Image.open("mytemplate.png")

    index=0
    for detail in info:
        offset = (len(detail)/2)*14
        xcord = xpos[index] - offset
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Microsoft Sans Serif.ttf", fontSize)
        if (index > 0):
            # add commas to numbers
            detail="{:,}".format(int(detail))
        else:
            filename=detail.split(",")[0]
        draw.multiline_text((xcord, ypos[index]), detail, (R, G, B), font=font)
        index=index+1
    #str(uuid.uuid4())
    img.save('sample-infographic-' + filename + '.png')
    index = 0

def readMyFile(filename):
    # Import data from CSV file
    myData = []
    text_file = open(filename, "r")
    lines = text_file.readlines()
    return lines

myData = readMyFile('mydata.csv')

for line in myData:
    info = line.split(",")
    info[4]=info[4].strip("\n")
    generateInfoGraphic(info,"Arial.ttf",32,55,145,192)
