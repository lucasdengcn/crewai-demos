#!/usr/bin/env python
import sys
from demo_001.crew import Demo001Crew

# patch to disable OTL
from crewai.telemetry import Telemetry

def noop(*args, **kwargs):
    print("Telemetry method called and noop'd\n")
    pass


for attr in dir(Telemetry):
    if callable(getattr(Telemetry, attr)) and not attr.startswith("__"):
        setattr(Telemetry, attr, noop)


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    Demo001Crew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        Demo001Crew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
