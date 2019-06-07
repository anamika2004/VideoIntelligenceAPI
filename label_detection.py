import argparse
from google.cloud import videointelligence
import os
import json
from google.protobuf.json_format import MessageToJson
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Anamika/Downloads/video-api-key.json"
client = videointelligence.VideoIntelligenceServiceClient()
job = client.annotate_video(
    input_uri='gs://anamika_bucket/Sample_1mb.mp4',
    features=['LABEL_DETECTION'],)
result = job.result();
print(result)
json_data=MessageToJson(result)
data=json.loads(json_data)




