from footprint.api import EditorApi
from astropy.io import fits 

e = EditorApi()
e.delete_footprint()


#read fits
filename = "C:/Users/tomshark/Downloads/example.fits"

image = fits.open(filename)

#store image data
data = image[0].data
#store header
header = image[0].header

#read different parameters from header
n = header["NAXIS1"]
m = header["NAXIS2"]

centerx = header["CRPIX1"]
centery = header["CRPIX2"]

center_ra = header["CRVAL1"]
center_dec = header["CRVAL2"]

pix_to_degree = header["CDELT2"]

