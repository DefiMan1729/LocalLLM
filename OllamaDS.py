import ollama
import time
import psutil  # For CPU and memory stats

# Define the model and question
desiredModel = 'deepseek-r1:1.5b'
questionToAsk = 'What are the roots of x^2+5*x+6=0'

# Measure response time
start_time = time.time()  # Record the start time

response = ollama.chat(model=desiredModel, messages=[
    {
        'role': 'user',
        'content': questionToAsk,
    },
])

end_time = time.time()  # Record the end time
response_time = end_time - start_time  # Calculate response time

# Extract response content
OllamaResponse = response['message']['content']

# Get system metrics
cpu_usage = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()

# Print the response content
print("Ollama Response:")
print(OllamaResponse)

# Print the metrics
print("\nMetrics:")
print(f"Response Time: {response_time:.2f} seconds")
print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_info.percent}%")

# Save the response content to a file
with open("OutputOllama.txt", "w", encoding="utf-8") as text_file:
    text_file.write(OllamaResponse)