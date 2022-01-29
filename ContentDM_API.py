from tkinter import image_names
import requests, csv
import json
import pandas as pd
from pandas.io.json import json_normalize
import cv2
import os
import urllib.request
import urllib3
from urllib3 import request


manifestUrl = 'https://cdm16002.contentdm.oclc.org/iiif/info/manifest.json'


resp = urllib.request.urlopen(manifestUrl)
data = resp.read().decode("utf-8")
data = json.loads(data)

df = pd.json_normalize(data['collections'])
del df['@type']
df.rename(columns = {'@id':'ID', 'label':'Label'}, inplace = True)
df.head()

# Create a list of all the collections
collections = df['ID'].tolist()

# convert each manifest.json in list to dataframe
for collection in collections: 
    collectionUrl = 'https://cdm16002.contentdm.oclc.org/iiif/' + collection + '/manifest.json'
    resp = urllib.request.urlopen(collectionUrl)
    data = resp.read().decode("utf-8")
    data = json.loads(data)
    df = pd.json_normalize(data['sequences'])
    del df['@type']
    df.rename(columns = {'@id':'ID', 'label':'Label'}, inplace = True)
    df.head()
    # Create a list of all the sequences
    sequences = df['ID'].tolist()
    # convert each manifest.json in list to dataframe
    for sequence in sequences:
        sequenceUrl = 'https://cdm16002.contentdm.oclc.org/iiif/' + collection + '/' + sequence + '/manifest.json'
        resp = urllib.request.urlopen(sequenceUrl)
        data = resp.read().decode("utf-8")
        data = json.loads(data)
        df = pd.json_normalize(data['canvases'])
        del df['@type']
        df.rename(columns = {'@id':'ID', 'label':'Label'}, inplace = True)
        df.head()
        # Create a list of all the canvases
        canvases = df['ID'].tolist()
        # convert each manifest.json in list to dataframe
        for canvas in canvases:
            canvasUrl = 'https://cdm16002.contentdm.oclc.org/iiif/' + collection + '/' + sequence + '/' + canvas + '/manifest.json'
            resp = urllib.request.urlopen(canvasUrl)
            data = resp.read().decode("utf-8")
            data = json.loads(data)
            df = pd.json_normalize(data['images'])
            del df['@type']
            df.rename(columns = {'@id':'ID', 'label':'Label'}, inplace = True)
            df.head()
            # Create a list of all the images
            images = df['ID'].tolist()
            # convert each manifest.json in list to dataframe
            for image in images:
                imageUrl = 'https://cdm16002.contentdm.oclc.org/iiif/' + collection + '/' + sequence + '/' + canvas + '/' + image + '/manifest.json'
                resp = urllib.request.urlopen(imageUrl)
                data = resp.read().decode("utf-8")
                data = json.loads(data)
                df = pd.json_normalize(data['images'])
                del df['@type']
                df.rename(columns = {'@id':'ID', 'label':'Label'}, inplace = True)
                df.head()
                # Create a list of all the images
                images = df['ID'].tolist()
                # convert each manifest.json in list to dataframe
                for image in images:
                    imageUrl = 'https://cdm16002.contentdm.oclc.org/iiif/' + collection + '/' + sequence + '/' + canvas + '/' + image + '/manifest.json'
                    resp = urllib.request.urlopen(imageUrl)
                    data = resp.read().decode("utf-8")
                    data = json.loads(data)
                    df = pd.json_normalize(data['images'])
                    del df['@type']
                    df.rename(columns = {'@id':'ID', 'label':'Label'}, inplace = True)
                    df.head()
                    # Create a list of all the images
                    images = df['ID'].tolist()
                    # convert each manifest.json in list to dataframe
                    for image in images:
                        imageUrl = 'https://cdm16002.contentdm.oclc.org/iiif/' + collection + '/' + sequence + '/' + canvas + '/' + image + '/manifest.json'
                        resp = urllib.request.urlopen(imageUrl)
                        data = resp.read().decode("utf-8")
                        data = json.loads(data)
                        df = pd.json_normalize(data['images'])
                        del df['@type']
                        df.rename(columns = {'@id':'ID', 'label':'Label'}, inplace = True)
                        df.head()
                        # Create a list of all the images
                        images = df['ID'].tolist()
                        # convert each manifest.json in list to dataframe
                        for image in images:
                            imageUrl = 'https://cdm16002.contentdm.oclc.org/iiif/' + collection + '/' + sequence + '/' + canvas + '/' + image + '/manifest.json'
                            resp = urllib.request.urlopen(imageUrl)
                            data = resp.read().decode("utf-8")
                            data = json.loads(data)
                            df = pd.json_normalize(data['images'])
                            del df['@type']
                            df.rename(columns = {'@id':'ID', 'label':'Label'}, inplace = True)
                            df.head()
                            # Create a list of all the images
                            images = df['ID'].tolist()
                            # convert each manifest.json in list to dataframe
                            for image in images:
                                imageUrl = 'https://cdm16002.contentdm.oclc.org/iiif/' + collection + '/' + sequence + '/' + canvas + '/' + image + '/manifest.json'
                                resp = urllib.request.urlopen(imageUrl)
                                data = resp.read().decode("utf-8")
                                data = json.loads(data)
                                df = pd.json_normalize(data['images'])
                                del df['@type']
                                df.rename(columns = {'@id':'ID', 'label':'Label'}, inplace = True)
                                df.head()
                                # Create a list of all the images
                                images = df['ID'].tolist()
                                # convert each manifest.json in list to dataframe
                                for image in images:
                                    imageUrl = 'https://cdm16002.contentdm.oclc.org/iiif/' + collection + '/' + sequence + '/' + canvas + '/' + image + '/manifest.json'
                                    resp = urllib.request.urlopen(imageUrl)
                                    data = resp.read().decode("utf-8")
                                    data = json.loads(data)
                                    df = pd.json_normalize(data['images'])
                                    del df['@type']
                                    df.rename(columns = {'@id':'ID', 'label':'Label'}, inplace = True)
                                    df.head()
                                    # Create a list of all the images
                                    images = df['ID'].tolist()
                                    # convert each manifest.json in list to dataframe
                                    for image in images:
                                        imageUrl = 'https://cdm16002.contentdm.oclc.org/iiif/' + collection + '/' + sequence + '/' + canvas + '/' + image + '/manifest.json'
                                        resp = urllib.request.urlopen(imageUrl)
                                        data = resp.read().decode("utf-8")
                                        data =
                                        json.loads(data)
                                        df = pd.json_normalize(data['images'])
                                        del df['@type']
                                        df.rename(columns = {'@id':'ID', 'label':'Label'}, inplace = True)
                                        df.head()
                                        # Create a list of all the images
                                        