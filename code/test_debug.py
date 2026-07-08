import subprocess

result = subprocess.run(
    ['/home/lilybot/llama.cpp/build/bin/llama-cli',
     '-m', '/home/lilybot/llama.cpp/models1/SmolLM2-135M-Instruct-Q3_K_S.gguf',
     '-c', '512', '-n', '100', '-p', 'hello',
     '--single-turn', '--log-disable', '--no-display-prompt'],
    capture_output=True, text=True
)
print('STDOUT WAS:', repr(result.stdout))
print('STDERR WAS:', repr(result.stderr))
