from google.cloud import videointelligence
import os
import json
from google.protobuf.json_format import MessageToJson
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Anamika/Downloads/video-api-key.json"
video_client = videointelligence.VideoIntelligenceServiceClient()

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.enums.Feature.OBJECT_TRACKING]
operation = video_client.annotate_video(
input_uri='gs://anamika_bucket/Sample_1mb.mp4', features=features, location_id='us-east1')
print('\nProcessing video for object annotations.')

result = operation.result(timeout=300)
print('\nFinished processing.\n')

# The first result is retrieved because a single video was processed.
object_annotations = result.annotation_results[0].object_annotations
# Get only the first annotation for demo purposes.
print('Entity description: {}'.format(object_annotation.entity.description))
if object_annotation.entity.entity_id:
    print('Entity id: {}'.format(object_annotation.entity.entity_id))

print('Segment: {}s to {}s'.format(
    object_annotation.segment.start_time_offset.seconds +
    object_annotation.segment.start_time_offset.nanos / 1e9,
    object_annotation.segment.end_time_offset.seconds +
    object_annotation.segment.end_time_offset.nanos / 1e9))

print('Confidence: {}'.format(object_annotation.confidence))

# Here we print only the bounding box of the first frame in this segment
frame = object_annotation.frames[0]
box = frame.normalized_bounding_box
print('Time offset of the first frame: {}s'.format(
    frame.time_offset.seconds + frame.time_offset.nanos / 1e9))
print('Bounding box position:')
print('\tleft  : {}'.format(box.left))
print('\ttop   : {}'.format(box.top))
print('\tright : {}'.format(box.right))
print('\tbottom: {}'.format(box.bottom))
print('\n')
