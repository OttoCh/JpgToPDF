import os
import sys
from PIL import Image

inputDir = './input'
outputDir = './output'

for filename in os.listdir(inputDir):
    if (filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.jpeg')):
        targetImage = Image.open(inputDir + '/' + filename)
        resultPdf = targetImage.convert('RGB')
        pdfFilename = filename.replace('.jpg', '.pdf').replace('.png', '.pdf').replace('.jpeg', '.pdf');
        resultPdf.save(outputDir + '/' + pdfFilename)