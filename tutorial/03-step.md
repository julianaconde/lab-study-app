# Step 3: Backend and AI Integration

> **Summary:**
> In this step, you'll implement the core functionality of StudyPlan AI by connecting the backend to GitHub's AI models and creating the API endpoint that powers the application.

## StudyPlan App Overview

StudyPlan AI follows a clear processing flow, starting from user input and ending with a personalized study plan:

1. **User Input:** The user fills out a form on the web interface with their profile information (area of interest, current skill level, available study time).

2. **API Layer (`app/api/api.py`):** Receives the request, validates the data, and maps it to the appropriate model objects.

3. **Prompts Service (`app/services/prompts.py`):** Formats the user's information into structured instructions for the AI model, designed to produce optimal results.

4. **GitHub Client (`app/services/github_client.py`):** Sends the formatted instructions to GitHub Models and waits for the AI response.

5. **Response Handling:** The AI-generated response is processed, formatted, and returned to the user through the web interface as a structured, personalized study plan.

## ⌨️ Activity: Implement the GitHub Models Client

The GitHub Models client is essential for communicating with AI services. It handles authentication, request formatting, and response processing, enabling StudyPlan AI to generate personalized content. In this activity, we'll implement the client that communicates with GitHub's AI capabilities.

1. Open `app/services/github_client.py`. You will see the `GitHubModelsClient` class with some pre-defined structure, including initialization and configuration methods.

2. In the `GitHubModelsClient` class, right-click on the class name and select **Explain this** from the GitHub Copilot context menu to understand its structure and intended behavior.

3. Open the **Copilot Chat** panel, switch to **Agent** mode, and ask Copilot to implement the client using the Azure AI Inference library with the following prompt:

    > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
    >
    > ```prompt
    > Implement the GitHub Models client using Azure AI Inference library:
    >
    > - First install the required package: pip install azure-ai-inference
    > - Use ChatCompletionsClient from azure.ai.inference
    > - Use SystemMessage and UserMessage from azure.ai.inference.models
    > - Connect to the endpoint https://models.github.ai/inference
    > - Use the model openai/gpt-4o-mini
    > - Implement a fallback mock response for testing
    > - Handle errors and provide detailed error messages
    > ```

> [!IMPORTANT]
> When you submit this prompt, Copilot Chat may request permission to install the Azure AI Inference package.
> - Click **Continue** in the chat window to authorize the installation
>
> - Click **Keep** when prompted to save the changes to the requirements file
>
> This package is essential for establishing communication with the GitHub Models API and enabling AI-powered study plan generation.

<details>
  <summary>🤔 How it works?</summary><br/>

The **GitHubModelsClient** implementation integrates with GitHub's AI models to generate personalized study plans. It uses the **Azure AI Inference library** to establish secure connections with the GitHub Models API endpoint, handles authentication through **GitHub tokens**, and converts user messages into the appropriate format for AI processing. 

The client includes a **fallback mechanism** that automatically switches to mock responses when the API is unavailable, ensuring the application remains functional during development and testing.

</details>

---

| [← Check your environment](02-step.md) | [Next: Data Models and API Endpoint →](04-step.md) |
|:-----------------------------------|------------------------------------------:|
