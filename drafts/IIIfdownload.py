import urllib.request
import requests
import csv
import json
import pandas as pd

pid = 0
img_urls = {}
img_smalls = {}

def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


# for testing use this function to download a specific collection
collectionURL = "https://cdm16002.contentdm.oclc.org/iiif/info/p16002coll9/manifest.json"

def iiif_download(collectionURL, pid=0):
  resp1 = urllib.request.urlopen(collectionURL)
  data1 = resp1.read().decode("utf-8")
  data2 = json.loads(data1)
  collection = pd.json_normalize(data2['first'])
  for url in collection['@id']:
    resp2 = urllib.request.urlopen(url)
    data3 = resp2.read().decode("utf-8")
    data4 = json.loads(data3)
    item = pd.json_normalize(data4['manifests'])
    for imageurl in item['@id']:
      resp3 = urllib.request.urlopen(imageurl)
      data5 = resp3.read().decode("utf-8")
      image = json.loads(data5)
      for jpg in image['sequences'][0]['canvases']:
          img_urls[pid]=jpg['images'][0]['resource']['service']['@id']
          filename = str(pid) + ".jpg"
          #imagename[pid] = item['label']
          #imagefile = str(imagename[pid]).replace(" ","").lower()
          # print(imagefile)
          #filename = imagefile[0:10] + ".jpg"
          turl = img_urls[pid]+"/full/pct:100/0/default.jpg"
          urllib.request.urlretrieve(turl, filename)
          pid = pid +1
          if pid == 30:
                break


iiif_download(collectionURL)
