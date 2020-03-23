#!/usr/bin/env python3
#
# Copyright 2020 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Script assists with collecting information that can be used to optimize costs.

import google.auth
from googleapiclient.discovery import build
from googleapiclient.http import HttpError
import json
import time
import sys
import datetime

credential, project_id = google.auth.default()
cloudbilling = build('cloudbilling', 'v1')
page_size = 5000
delay = 1

# You need to authenticate using the "gcloud auth application-default login" command first.
# Not running the above command can result in an authentication error with the script.

# You may need to set the quota project using the "gcloud auth application-default set-quota-project" command first.
# Not running the above command can result in the script taking a very long time (days?) due to small quotas.

service_results = dict()
while True:

    # get servces results
    # since there are quotas, introduced exponential delays on on quota/limit failures.
    while True:
        try:
            services_results = cloudbilling.services().list(pageSize=page_size, pageToken=service_results.get('nextPageToken')).execute()
            delay = 1
            break
        except HttpError as e:
            isodate = datetime.datetime.utcnow().isoformat()
            print("{}Z - We have hit a quota. Caught exception: {}".format(isodate,e),file=sys.stderr)
            print("{}Z - Sleeping for {} seconds".format(isodate,delay),file=sys.stderr)
            time.sleep(delay)
            delay = delay * 2

    # for each service.
    for service in services_results.get('services'): 

        skus_results = dict()
        while True:
            
            # get sku results.
            # since there are quotas, introduced exponential delays on on quota/limit failures.
            while True:
                try:
                    skus_results = cloudbilling.services().skus().list(parent='services/'+service.get('serviceId'), pageSize=page_size, pageToken=skus_results.get('nextPageToken')).execute()
                    delay = 1
                    break
                except HttpError as e:
                    isodate = datetime.datetime.utcnow().isoformat()
                    print("{}Z - We have hit a quota. Caught exception: {}".format(isodate,e),file=sys.stderr)
                    print("{}Z - Sleeping for {} seconds".format(isodate,delay),file=sys.stderr)
                    time.sleep(delay)
                    delay = delay * 2

            # for each sku
            for sku in skus_results.get('skus'):

                # dump the json in a single like (JSONL format)
                print(json.dumps(sku))

            # break if there is no next page of skus.
            if skus_results.get('nextPageToken') == None:
                break
            
    # break if there is no next page of services
    if services_results.get('nextPageToken') == None:
        break