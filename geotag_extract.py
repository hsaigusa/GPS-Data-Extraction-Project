import os
import PIL
from PIL import Image, ExifTags

# Workspace
img_folder = r"D:\QField\shp\DCIM"
img_contents = os.listdir(img_folder)

# GPS Info Dictioanry
gps_all = {}
coord_list = []

def convert_to_degrees(value):

    # d0 = value[0][0]
    # d1 = value[0][1]
    # d = float(d0) / float(d1)
    d = value[0]

    # m0 = value[1][0]
    # m1 = value[1][1]
    # m = float(m0) / float(m1)
    m = value[1]

    # s0 = value[2][0]
    # s1 = value[2][1]
    # s = float(s0) / float(s1)
    s = value[2]

    return d + (m/60.0) + (s/3600.0)


for img in img_contents:
    img = Image.open(os.path.join(img_folder,img))
    exif = {PIL.ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
    for key in exif['GPSInfo'].keys():
        print(f"This is the code value {key}")
        decodedValue = ExifTags.GPSTAGS.get(key)
        print(f"This is its associated label {decodedValue}")
        print(exif['GPSInfo'][key])
        gps_all[decodedValue] = exif['GPSInfo'][key]
    long_ref = gps_all.get('GPSLongitudeRef')
    lat_ref = gps_all.get('GPSLatitudeRef')
    long = gps_all.get('GPSLongitude')
    lat = gps_all.get('GPSLatitude')
    if long_ref == "W":
        long_in_degrees =  -abs(convert_to_degrees(long))
    else:
        long_in_degrees =  convert_to_degrees(long)
    if lat_ref == "S":
        lat_in_degrees =  -abs(convert_to_degrees(lat))
    else:
        lat_in_degrees = convert_to_degrees(lat)

    coord_list.append([long_in_degrees, lat_in_degrees])
    print(coord_list)
