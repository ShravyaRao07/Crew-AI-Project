from crewai import Crew, Process
from agents import researcher, writer, proof_reader
from tasks import research_task, write_task, proof_read_task

def run_crew(topic: str):
    crew = Crew(
        agents=[researcher, writer, proof_reader],
        tasks=[research_task, write_task, proof_read_task],
        process=Process.sequential
    )

    result = crew.kickoff(inputs={"topic": topic})
    return result