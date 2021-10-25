#!/usr/bin/env python3

import requests
import copy
import wget
import time
import pickle
import os.path
import json

appinfo = {}
applist = []
app_download_count = {}


def get_data_json_top100():
    url = "https://community-store.deepin.com/api/public/stat?order=download&offset=0&limit={limit}&arch=amd64&mode=desktop&platform=community&region=CN&language=zh_CN".format(
        limit=150)
    if not os.path.exists("cache/top100.dump"):
        req = requests.get(url)
        top100 = req.json()
        with open("cache/top100.dump", "wb") as cache:
            pickle.dump(top100, cache, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        with open("cache/top100.dump", "rb") as cache:
            top100 = pickle.load(cache)
    return top100


def get_appid_info(appid=157):
    url = "https://community-store.deepin.com/api/public/app?id={appid}&arch=amd64&mode=desktop&platform=community&region=CN&language=zh_CN".format(
        appid=appid)
    req = requests.get(url)
    req_json = req.json()

    pkg_name = req_json[0]['packages'][0]['name']
    pkg_info = []
    pkg_info.append(req_json[0]['packages'][0]['name'])
    pkg_info.append(req_json[0]['name'])
    pkg_info.append(req_json[0]['packages'][0]['version'])
    pkg_info.append(req_json[0]['info']['category'])
    pkg_info.append(req_json[0]['info']['locales'][0]['description'])

    download_cover = "../assets/" + pkg_info[0] + "_cover_zh_CN.jpeg"
    download_url = "https://community-store.deepin.com/api/public/blob/{uuid}".format(
        uuid=req_json[0]['info']['locales'][0]['cover'])
    # time.sleep(1)
    # todo need open for download
    # wget.download(download_url, download_cover)
    pkg_info.append(pkg_info[0] + "_cover_zh_CN.jpeg")
    appinfo[pkg_name] = pkg_info


def save_appinfo_json():
    info = []
    for appid in appinfo:
        s = {}
        # id , name , isshow, imageURI , description ,category
        s = {"id": appinfo[appid][0],
             "name": appinfo[appid][1],
             "isShow": False,
             "imageURI": "./assets/{0}".format(appinfo[appid][-1]),
             "description": appinfo[appid][-2],
             "category": appinfo[appid][-3],
             }
        info.append(s)
        js = {"info": info}
        with open("cache/appinfo.json", "w") as jw:
            jw.write(json.dumps(js, ensure_ascii=False))

if not os.path.exists("cache/top100.appinfo.dump"):
    applist = get_data_json_top100()
    if (len(applist) > 0):
        for app in applist:
            get_appid_info(app['app_id'])
        with open("cache/top100.appinfo.dump", "wb") as cache:
            pickle.dump(appinfo, cache, protocol=pickle.HIGHEST_PROTOCOL)
else:
    with open("cache/top100.appinfo.dump", "rb") as cache:
        appinfo = pickle.load(cache)
save_appinfo_json()
