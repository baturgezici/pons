from PIL import Image
from numpy import asarray

img = Image.open(r"C:\Users\Batur\Desktop\emergencynet\covidus2\COVID-US\data\image\clean\1_butterfly_covid_prc_convex_clean_frame0.jpg")

numpydata = asarray(img)

print(numpydata.shape)