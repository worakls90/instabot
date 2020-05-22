import random

APP_VERSION = "142.0.0.34.110"
VERSION_CODE = "215464403"
DEVICES = {
    "one_plus_7": {
        "app_version": APP_VERSION,
        "android_version": "29",
        "android_release": "10.0",
        "dpi": "420dpi",
        "resolution": "1080x2340",
        "manufacturer": "OnePlus",
        "device": "GM1903",
        "model": "OnePlus7",
        "cpu": "qcom",
        "version_code": VERSION_CODE,
    },
    "one_plus_3": {
        "app_version": APP_VERSION,
        "android_version": "28",
        "android_release": "9.0",
        "dpi": "420dpi",
        "resolution": "1080x1920",
        "manufacturer": "OnePlus",
        "device": "ONEPLUS A3003",
        "model": "OnePlus3",
        "cpu": "qcom",
        "version_code": VERSION_CODE,
    },
    # Released on March 2016
    "samsung_galaxy_s7": {
        "app_version": APP_VERSION,
        "android_version": "26",
        "android_release": "8.0",
        "dpi": "640dpi",
        "resolution": "1440x2560",
        "manufacturer": "samsung",
        "device": "SM-G930F",
        "model": "herolte",
        "cpu": "samsungexynos8890",
        "version_code": VERSION_CODE,
    },
    # Released on January 2017
    "huawei_mate_9_pro": {
        "app_version": APP_VERSION,
        "android_version": "24",
        "android_release": "7.0",
        "dpi": "640dpi",
        "resolution": "1440x2560",
        "manufacturer": "HUAWEI",
        "device": "LON-L29",
        "model": "HWLON",
        "cpu": "hi3660",
        "version_code": VERSION_CODE,
    },
    # Released on February 2018
    "samsung_galaxy_s9_plus": {
        "app_version": APP_VERSION,
        "android_version": "28",
        "android_release": "9.0",
        "dpi": "640dpi",
        "resolution": "1440x2560",
        "manufacturer": "samsung",
        "device": "SM-G965F",
        "model": "star2qltecs",
        "cpu": "samsungexynos9810",
        "version_code": VERSION_CODE,
    },
    # Released on November 2016
    "one_plus_3t": {
        "app_version": APP_VERSION,
        "android_version": "26",
        "android_release": "8.0",
        "dpi": "380dpi",
        "resolution": "1080x1920",
        "manufacturer": "OnePlus",
        "device": "ONEPLUS A3010",
        "model": "OnePlus3T",
        "cpu": "qcom",
        "version_code": VERSION_CODE,
    },
    # Released on April 2016
    "lg_g5": {
        "app_version": APP_VERSION,
        "android_version": "23",
        "android_release": "6.0.1",
        "dpi": "640dpi",
        "resolution": "1440x2392",
        "manufacturer": "LGE/lge",
        "device": "RS988",
        "model": "h1",
        "cpu": "h1",
        "version_code": VERSION_CODE,
    },
    # Released on June 2016
    "zte_axon_7": {
        "app_version": APP_VERSION,
        "android_version": "23",
        "android_release": "6.0.1",
        "dpi": "640dpi",
        "resolution": "1440x2560",
        "manufacturer": "ZTE",
        "device": "ZTE A2017U",
        "model": "ailsa_ii",
        "cpu": "qcom",
        "version_code": VERSION_CODE,
    },
    # Released on March 2016
    "samsung_galaxy_s7_edge": {
        "app_version": APP_VERSION,
        "android_version": "23",
        "android_release": "6.0.1",
        "dpi": "640dpi",
        "resolution": "1440x2560",
        "manufacturer": "samsung",
        "device": "SM-G935",
        "model": "hero2lte",
        "cpu": "samsungexynos8890",
        "version_code": VERSION_CODE,
    },
}
DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
