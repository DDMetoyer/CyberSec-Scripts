'''
EXIF Data Acquistion Example
'''

'''
Using this script provide as a baseline.
Expand the script as follows:

1) Allow the user to enter a path to a directory containing jpeg files.
2) Using that path, process all the .jpg files contained in that folder (use the testimages.zip set of images)
3) Extract the GPS coordinates for each jpg (if they exist)
4) Use the extracted GPS coordinates and put them on a map (manually or programmatically using a CSV file)

NOTE: There are several ways to do this, however, the easiest method would be to use something like the MapMaker App, at https://mapmakerapp.com/
      you can either manually enter the lat/lon values your script generates or you can place your results in a CSV file and upload
      the data to the map.
      
Submit:

1) Your Python script

2) A screenshot of the successful execution and output

3) A screenshot of a map with the extracted GPS coordinates marked on it

'''
# Usage Example:
# python Assignment6.py
#
# Requirement: Python 3.x
#
# Requirement: 3rd Party Library that is utilized is: PILLOW
#                   pip install PILLOW  from the command line
#                   this is already installed in the Virtual Desktop


''' LIBRARY IMPORT SECTION '''

import os
import csv
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from prettytable import PrettyTable

def extract_gps_dictionary(file_name):
    """ Extracts GPS data and basic EXIF information from an image file. """
    try:
        pil_image = Image.open(file_name)
        exif_data = pil_image._getexif()
    except Exception:
        return None, None

    image_time_stamp = "NA"
    camera_model = "NA"
    camera_make = "NA"
    gps_dictionary = {}

    if exif_data:
        for tag, value in exif_data.items():
            tag_value = TAGS.get(tag, tag)

            if tag_value == 'DateTimeOriginal':
                image_time_stamp = exif_data.get(tag).strip()

            if tag_value == "Make":
                camera_make = exif_data.get(tag).strip()

            if tag_value == 'Model':
                camera_model = exif_data.get(tag).strip()

            if tag_value == "GPSInfo":
                for cur_tag in value:
                    gps_tag = GPSTAGS.get(cur_tag, cur_tag)
                    gps_dictionary[gps_tag] = value[cur_tag]

        return gps_dictionary, [image_time_stamp, camera_make, camera_model]
    
    return None, None


def extract_lat_lon(gps):
    """ Converts GPS EXIF data to latitude and longitude decimal degrees. """
    try:
        latitude = gps["GPSLatitude"]
        latitude_ref = gps["GPSLatitudeRef"]
        longitude = gps["GPSLongitude"]
        longitude_ref = gps["GPSLongitudeRef"]
        return convert_to_degrees(latitude, latitude_ref, longitude, longitude_ref)
    except KeyError:
        return None


def convert_to_degrees(lat, lat_ref, lon, lon_ref):
    """ Converts EXIF GPS format to decimal degrees. """
    def dms_to_decimal(dms):
        degrees, minutes, seconds = dms
        return degrees + (minutes / 60.0) + (seconds / 3600.0)

    lat_decimal = dms_to_decimal(lat)
    lon_decimal = dms_to_decimal(lon)

    if lat_ref == 'S':
        lat_decimal *= -1
    if lon_ref == 'W':
        lon_decimal *= -1

    return lat_decimal, lon_decimal


def process_images(directory):
    """ Processes all JPEG files in the directory, extracts GPS, and outputs results. """
    if not os.path.isdir(directory):
        print("Invalid directory. Please provide a valid directory path.")
        return

    result_table = PrettyTable(['File Name', 'Latitude', 'Longitude', 'Timestamp', 'Make', 'Model'])
    csv_data = []

    for file_name in os.listdir(directory):
        if file_name.lower().endswith(".jpg"):
            file_path = os.path.join(directory, file_name)
            gps_dictionary, exif_data = extract_gps_dictionary(file_path)

            if exif_data:
                timestamp, make, model = exif_data
            else:
                timestamp, make, model = "NA", "NA", "NA"

            if gps_dictionary:
                lat_lon = extract_lat_lon(gps_dictionary)
                if lat_lon:
                    lat, lon = lat_lon
                    result_table.add_row([file_name, f"{lat:.6f}", f"{lon:.6f}", timestamp, make, model])
                    csv_data.append([file_name, lat, lon, timestamp, make, model])
                else:
                    result_table.add_row([file_name, "No GPS", "No GPS", timestamp, make, model])
            else:
                result_table.add_row([file_name, "No GPS", "No GPS", timestamp, make, model])

    print(result_table)

    # Save results to a CSV file for MapMaker or other GIS tools
    csv_file = os.path.join(directory, "image_gps_data.csv")
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["File Name", "Latitude", "Longitude", "Timestamp", "Make", "Model"])
        writer.writerows(csv_data)
    
    print(f"\nCSV file saved: {csv_file}")


if __name__ == "__main__":
    print("\nExtracting EXIF GPS Data from JPEG Files")
    print("Script Started:", str(datetime.now()), "\n")

    # Prompt user for directory path
    directory_path = input("Enter the directory containing JPEG files: ").strip()

    # Process all images in the given directory
    process_images(directory_path)
