import os
import sys
from PIL import Image

inputDir = './input'
outputDir = './output'
filesizeTreshold = 1000000
thumbnailScale = (600,800)


for filename in os.listdir(inputDir):
    if (filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.jpeg')):
        targetImage = Image.open(inputDir + '/' + filename)
        # reduce size to < 300 kb
        filesize = os.path.getsize(inputDir + '/' + filename)
        if(filesize > filesizeTreshold):
            print("reduce image size: " + str(filesize))
            targetImage.thumbnail(thumbnailScale, Image.ANTIALIAS)
        resultPdf = targetImage.convert('RGB')
        pdfFilename = filename.replace('.jpg', '.pdf').replace('.png', '.pdf').replace('.jpeg', '.pdf');
        resultPdf.save(outputDir + '/' + pdfFilename)