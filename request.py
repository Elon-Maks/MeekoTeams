import requests
import json

#make request to Ampereanalysis to get raw data
reply = requests.get('http://www.ampereanalysis.com/insights',  verify=False)

#extract JS objest with necessary data as string
text = (reply.text.split('let report_obj = [')[1].split('];')[0])

#create array to write data to
results = []

#split JS object string into posts data to work with one post at a time
for post in text.split('{')[1:]:
    #add data from each post to results (information is extracted by splitting string using names of fields)
    results.append({"date": post.split('publish_on: "')[1].split('"')[0],
                    "author": post.split('authors: "')[1].split('"')[0],
                    "title": post.split('title: "')[1].split('"')[0]})
print(results)

#open json file to save results
f = open("results.json", "w")
json.dump(results, f)
