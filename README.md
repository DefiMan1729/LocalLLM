
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

## Step 5: Test Your Setup

Run a simple test to ensure everything is working:

```bash
ollama run deepseek-r1:1.5b
```

You can now interact with the DeepSeek model locally on your Raspberry Pi.

## Step 6: VS Code Setup
ssh into VS Code with you Raspberry pi sude user name and password

<sample code attached>

## Additional Resources

- [Ollama Documentation](https://ollama.com/docs)
- [DeepSeek GitHub Repository](https://github.com/deepseek)

---

Feel free to customize this `README.md` to suit your specific setup or requirements! Let me know if you need further assistance.
