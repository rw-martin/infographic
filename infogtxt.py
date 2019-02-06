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
        if (index>0):
            detail="{:,}".format(int(detail))
        else:
            filename=detail.split(",")[0]
        draw.multiline_text((xcord, ypos[index]), detail, (R, G, B), font=font)
        index=index+1
    #str(uuid.uuid4())
    img.save('sample-infographic-' + filename + '.png')
    index=0

def readMyFile(filename):
    myData = []

    text_file = open(filename, "r")
    lines = text_file.readlines()

    return lines

myData = readMyFile('mydata.csv')

for line in myData:
    info = line.split(",")
    info[4]=info[4].strip("\n")
    generateInfoGraphic(info,"Arial.ttf",32,55,145,192)

def XgenerateInfoGraphic(message,midpoint,typeface,fontSize,R,G,B):
    img = Image.open("myDesktemplate.png")
    #print(img.size)

    #Title
    hours="RW, here are your numbers for November..."
    offset = round(len(hours)/2)*18
    mycord = 470-offset#-(round(len(hours)))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Microsoft Sans Serif.ttf",32)
    draw.text((mycord, 12),hours,(55,145,192),font=font)

    # total
    hours = "{:,}".format(random.randint(1,12000))
    offset = round(len(hours)/2)*18
    mycord = 12+offset#-(round(len(hours)))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Microsoft Sans Serif.ttf",42)
    draw.text((mycord, 172),hours,(55,145,192),font=font)

    # Hours
    hours = "{:,}".format(random.randint(11900,120000))
    offset = round(len(hours)/2)*18
    mycord = 288-offset#-(round(len(hours)))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Microsoft Sans Serif.ttf",42)
    draw.text((mycord, 172),hours,(55,145,192),font=font)

    # Countries
    hours = "{:,}".format(random.randint(1,99))
    offset = round(len(hours)/2)*18
    mycord = 484-offset#-(round(len(hours)))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Microsoft Sans Serif.ttf",42)
    draw.text((mycord, 172),hours,(55,145,192),font=font)

    # Launches
    hours = "{:,}".format(random.randint(1,99))
    offset = round(len(hours)/2)*18
    mycord = 688-offset#-(round(len(hours)))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Microsoft Sans Serif.ttf",42)
    draw.text((mycord, 172),hours,(55,145,192),font=font)
    img.save('sample-out.png')
    #img.show()