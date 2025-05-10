# Code written following the examples provided here: 
# https://www.agisoft.com/pdf/metashape_python_api_1_6_0.pdf

import Metashape
from os import listdir
from os.path import isfile, join

# The basic workflow for processing an EXISTING project and saving the results
doc = Metashape.app.document
doc.open("project.psz")
chunk = doc.chunk
chunk.matchPhotos(downscale=1, generic_preselection=True, reference_preselection=False)
chunk.alignCameras()
chunk.buildDepthMaps(downscale=4, filter=Metashape.AggressiveFiltering)
chunk.buildDenseCloud()
chunk.buildModel(surface_type=Metashape.Arbitrary, interpolation=Metashape.EnabledInterpolation)
chunk.buildUV(mapping=Metashape.GenericMapping)
chunk.buildTexture(blending=Metashape.MosaicBlending, size=4096)
doc.save()




imageFolderPath = ''
imgFiles = [f for f in listdir(imageFolderPath) if isfile(join(imageFolderPath, f))]

chunk = Metashape.app.document.addChunk()
chunk.addPhotos(imgFiles)
camera = chunk.cameras[0]
camera.photo.meta["Exif/FocalLength"]



# Code for setting up a multispectral camera
doc = Metashape.app.document
chunk = doc.chunk
rgb = ["RGB_0001.JPG", "RGB_0002.JPG", "RGB_0003.JPG"]
nir = ["NIR_0001.JPG", "NIR_0002.JPG", "NIR_0003.JPG"]
images = [[rgb[0], nir[0]], [rgb[1], nir[1]], [rgb[2], nir[2]]]
chunk.addPhotos(images, Metashape.MultiplaneLayout)


#image matching and alignment for the active chunk
chunk = Metashape.app.document.chunk
for frame in chunk.frames:
    frame.matchPhotos(downscale=1)
chunk.alignCameras()