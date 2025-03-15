
# Installing Ollama and DeepSeek on Raspberry Pi 5

This guide will walk you through the steps to install **Ollama** and **DeepSeek** on a Raspberry Pi 5. (without GPU or AI HAT)

## Prerequisites

- Raspberry Pi 5 (I used 16GB RAM + SD card. You can use SSD with M HAT)
- A 64-bit version of Raspberry Pi OS (Bookworm)
- Internet connection (for downloading the model unless you have it offline and use ESP32 access point. Covered later)


## Step 1: Update Your System

Start by updating your Raspberry Pi to ensure all packages are up-to-date.

ssh into your Raspberry Pi from your computer and use the terminal

```bash
sudo apt update
sudo apt upgrade -y
```

## Step 2: Install Required Tools

Install `curl`, which is needed to download the installation scripts.

```bash
sudo apt install curl -y
```

## Step 3: Install Ollama

Run the following command to install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

After installation, verify that Ollama is installed:

```bash
ollama --version
```

## Step 4: Install DeepSeek

DeepSeek can be run using the Ollama platform. Follow these steps:

1. **Download the DeepSeek-R1 Model**:
   - Use Ollama to download the model:
     ```bash
     ollama pull deepseek-r1:1.5b
     ```

2. **Verify the Model**:
   - Check if the model is available:
     ```bash
     ollama list
     ```
<img width="565" alt="Screenshot 2025-03-15 at 4 39 20 PM" src="https://github.com/user-attachments/assets/ae3290a4-8631-4afd-a4e2-8ef3cb480db2" />

## Step 5: Test Your Setup

Run a simple test to ensure everything is working:

```bash
ollama run deepseek-r1:1.5b
```
<img width="549" alt="Screenshot 2025-03-15 at 4 41 33 PM" src="https://github.com/user-attachments/assets/305e8a4b-d37f-420f-8ca8-031f5e6cd8cb" />

You can now interact with the DeepSeek model locally on your Raspberry Pi.

## Step 6: VS Code Setup
- ssh into VS Code with you Raspberry pi sude user name and password
- activate virtual environment
- run your code locally on your PI

<img width="965" alt="Screenshot 2025-03-15 at 4 46 01 PM" src="https://github.com/user-attachments/assets/696f5bcc-7e06-479e-9aa8-117d4bcb7361" />


## Additional Resources

- [Ollama Documentation](https://ollama.com/docs)
- [DeepSeek GitHub Repository](https://github.com/deepseek)

---

Feel free to customize this `README.md` to suit your specific setup or requirements! Let me know if you need further assistance.
