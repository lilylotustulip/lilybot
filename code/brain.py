import subprocess
import time
import requests

MODEL_PATH = "/home/lilybot/llama.cpp/models1/SmolLM2-135M-Instruct-Q3_K_S.gguf"
SERVER_BIN = "/home/lilybot/llama.cpp/build/bin/llama-server"

def wait_for_server(max_wait=30):
    start = time.time()
    while time.time() - start < max_wait:
        try:
            r = requests.get("http://127.0.0.1:8080/health", timeout=1)
            if r.status_code == 200:
                return True
        except requests.exceptions.RequestException:
            pass
        time.sleep(0.5)
    return False

def ask(prompt, max_tokens=100):
    server_process = subprocess.Popen(
        [SERVER_BIN, "-m", MODEL_PATH, "-c", "512", "--port", "8080"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    try:
        if not wait_for_server():
            return "[ERROR: server never became ready]"

        response = requests.post(
            "http://127.0.0.1:8080/v1/chat/completions",
            json={
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens
            },
            timeout=30
        )
        data = response.json()

        if "choices" in data:
            result = data["choices"][0]["message"]["content"].strip()
        else:
            result = f"[SERVER ERROR: {data}]"

    finally:
        server_process.terminate()
        try:
            server_process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            server_process.kill()
            server_process.wait()

    return result
