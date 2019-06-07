from google.cloud import videointelligence
import os
import json
from google.protobuf.json_format import MessageToJson
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Anamika/Downloads/video-api-key.json"
video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.enums.Feature.SPEECH_TRANSCRIPTION]

config = videointelligence.types.SpeechTranscriptionConfig(
    language_code='en-US',
    enable_automatic_punctuation=True)
video_context = videointelligence.types.VideoContext(
    speech_transcription_config=config)

operation = video_client.annotate_video(
    input_uri="gs://anamika_bucket/sample-transcription.mp4",
    features=features,
    video_context=video_context)
result = operation.result(timeout=600)
annotation_results = result.annotation_results[0]
json_data=MessageToJson(annotation_results)
data=json.loads(json_data)
#print(data['speechTranscriptions'][0]['alternatives'][0]['transcript']);
for speech_transcription in annotation_results.speech_transcriptions:
    for alternative in speech_transcription.alternatives:
        print('Alternative level information:')


        print('Transcript: {}'.format(alternative.transcript))
        print('Confidence: {}\n'.format(alternative.confidence))

        print('Word level information:')
        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            print('\t{}s - {}s: {}'.format(start_time.seconds + start_time.nanos * 1e-9,     end_time.seconds + end_time.nanos * 1e-9,   word))
