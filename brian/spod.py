'''
Save FedEx Proof of Delivery PDF for a given tracking number
'''

import requests
import json

# find the line containing "getSpodImage" in main to see where the POST request is made.
# find "WTRK_ENDPOINTS" to see capabilities of the api.

# note that www is required for application/x-www-form-urlencoded request!
# without www only responds to the request as query parameters
# trkcUrl = 'https://fedex.com/trackingCal/track'
trkcUrl = 'https://www.fedex.com/trackingCal/track'

# test how requests sends the payload with netcat
# nc -kl 8265
# trkcUrl = 'http://localhost:8265'

trackingNumber = "282309656732"

TrackPackagesRequest = {
         "TrackPackagesRequest": {
            "appDeviceType":"DESKTOP",
            "appType":"WTRK",
            "processingParameters":{},
            "uniqueKey":"",
            "supportCurrentLocation":True,
            "supportHTML":True,
            "trackingInfoList":[{
                "trackNumberInfo":{
                    "trackingNumber": trackingNumber,
                    "trackingQualifier":None,
                    "trackingCarrier":None
                }
            }]
        }
    }

payload = {
    "action": "trackpackages",
    "data": json.dumps(TrackPackagesRequest),
    "format": "json",
    "locale": "en_US",
    "version": "1"
}

# headers not necessary but can change if you want
# headers = {
#     "user-agent": "my-app/0.0.1"
# }

r = requests.post(trkcUrl, data=payload)

TrackPackagesResponse = json.loads(r.text)

# TrackPackagesResponse contains full tracking history
# print(json.dumps(TrackPackagesResponse, indent=2))

if TrackPackagesResponse["TrackPackagesResponse"]["successful"]:
    trackingNbr = TrackPackagesResponse["TrackPackagesResponse"]["packageList"][0]["trackingNbr"]
    trackingQualifier = TrackPackagesResponse["TrackPackagesResponse"]["packageList"][0]["trackingQualifier"]
    trackingCarrierCd = TrackPackagesResponse["TrackPackagesResponse"]["packageList"][0]["trackingCarrierCd"]

    retrievePDFUrl = "https://www.fedex.com/trackingCal/retrievePDF.jsp"

    payload = {
        "accountNbr":None,
        "anon":True,
        "appType":None,
        "destCountry":None,
        "locale":"en_US",
        "shipDate":None,
        "trackingCarrier":trackingCarrierCd,
        "trackingNumber":trackingNbr,
        "trackingQualifier":trackingQualifier,
        "type":"SPOD"
    }

    r = requests.get(retrievePDFUrl, params=payload)

    filename = "SPOD_" + trackingNbr + ".pdf"

    open(filename, 'wb').write(r.content)
