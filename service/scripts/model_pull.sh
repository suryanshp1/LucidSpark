#!/bin/bash

# Function to check if Ollama server is running
check_ollama_server() {
    if ollama list &>/dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to start Ollama server
start_ollama_server() {
    echo "Starting Ollama server..."
    /bin/ollama serve &
    pid=$!

    # Wait for Ollama server to become active
    while ! check_ollama_server; do
        sleep 1
    done
    echo "Ollama server started successfully."
}

# Function to pull Ollama model
pull_ollama_model() {
    local model=$1
    echo "🔴 Retrieving $model model..."
    if ollama pull "$model"; then
        echo "🟢 $model model pulled successfully!"
    else
        echo "❌ Failed to pull $model model."
        exit 1
    fi
}

# Main script
main() {
    # Check if Ollama server is already running
    if ! check_ollama_server; then
        start_ollama_server
    else
        echo "Ollama server is already running."
    fi

    # Pull the Ollama model
    pull_ollama_model "$LLM_MODEL_NAME"

    # If we started the server, wait for it
    if [[ -n $pid ]]; then
        wait $pid
    fi
}

# Run the main function
main