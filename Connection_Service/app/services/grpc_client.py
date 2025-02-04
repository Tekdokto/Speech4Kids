import grpc
from common_pb2 import AudioRequest
from common_pb2_grpc import ASRServiceStub

class GRPCClient:
    def __init__(self, host, port):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = ASRServiceStub(self.channel)

    def send_audio(self, audio_data):
        request = AudioRequest(audio_data=audio_data)
        response = self.stub.Transcribe(request)
        print(f"Received transcription: {response.transcription}")
        return response.transcription