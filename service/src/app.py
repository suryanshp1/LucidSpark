# service_server.py
import asyncio
import grpc
from concurrent import futures
from protos import service_pb2
from protos import service_pb2_grpc
from crewai import Agent, Task, Crew
from exception import CustomException
from logger import logging
from langchain_community.llms import Ollama
from enums import ServiceEnum
import os
import sys

os.environ["OPENAI_API_KEY"] = "NA"

class DreamAnalysisServicer(service_pb2_grpc.DreamAnalysisServiceServicer):
    async def AnalyzeDream(self, request, context):

        logging.info("Received dream description: %s", request.dream_description)

        llm = Ollama(
            model=ServiceEnum.model.value,
            base_url=ServiceEnum.base_url.value
        )

        # Create an agent
        dream_analyst_agent = Agent(
            role="Dream Analyst",
            goal="Interpret dreams shared by individuals, providing psychological insights and possible meanings behind the dream symbols and narratives. Also finally provide some solutions.",
            backstory="You are an experienced dream analyst with a deep understanding of psychology, psychoanalysis, and modern neuroscientific approaches to dreaming. You have helped countless individuals uncover hidden meanings in their dreams, leading to personal growth and self-understanding.",
            allow_delegation=False,
            verbose=True,
            llm=llm
        )

        task = Task(
            description=request.dream_description,
            agent=dream_analyst_agent,
            expected_output="A dream analysis report with brief analysis and possible solutions and recommendations. Some tasks to improve personal growth are also suggested."
        )

        crew = Crew(
            agents=[dream_analyst_agent],
            tasks=[task],
            verbose=2
        )

        result = await asyncio.to_thread(crew.kickoff)

        logging.info("Dream analysis done")
        return service_pb2.DreamAnalysisResponse(analysis=result)

async def serve():
    try:
        server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
        service_pb2_grpc.add_DreamAnalysisServiceServicer_to_server(DreamAnalysisServicer(), server)
        listen_addr = '[::]:50051'
        server.add_insecure_port(listen_addr)
        print(f"Starting server on {listen_addr}")
        await server.start()
        await server.wait_for_termination()

    except Exception as e:
        logging.error("Exception occured at serve() | Error: ", e)
        raise CustomException(e, sys)

if __name__ == '__main__':
    asyncio.run(serve())