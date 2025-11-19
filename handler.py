import runpod
import time

def handler(job):
    job_input = job["input"]
    prompt = job_input.get("prompt")
    seconds = job_input.get("seconds", 0)

    time.sleep(seconds)
    return {"output": prompt}

runpod.serverless.start({"handler": handler})
