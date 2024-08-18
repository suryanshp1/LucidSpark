# dream_analysis_client.py
import asyncio
import grpc
from protos import service_pb2
from protos import service_pb2_grpc

async def run():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.DreamAnalysisServiceStub(channel)
        dream_description = "I see myself naked."
        response = await stub.AnalyzeDream(service_pb2.DreamRequest(dream_description=dream_description))
        print("Dream Analysis:")
        print(response.analysis)

if __name__ == '__main__':
    asyncio.run(run())