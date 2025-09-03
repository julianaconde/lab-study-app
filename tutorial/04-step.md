# Step 4: Data Models and API Endpoint

> **Summary:**
> In this step, you'll create the data models to structure requests and responses, and implement the API endpoint that connects the user interface with the AI integration.

## Data Models and REST API

To complete our StudyPlan AI application, we need to create:

1. **Data Models**: Classes that define the structure of requests and responses, ensuring consistency and facilitating validation.

2. **API Endpoint**: A Flask route that receives user requests, processes the data, interacts with the GitHub Models client, and returns the generated study plan.

This step is crucial for connecting the user interface with the artificial intelligence, completing the application flow.

## ⌨️ Activity: Create Data Models

Before implementing the API endpoint, we need to create the data models that will structure our requests and responses. These models will ensure consistent data formats and facilitate validation.

1. Create a new file `app/models/study_plan.py` to define our data models.

2. Use the following prompt with Copilot to implement the models:

    > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
    >
    > ```prompt
    > Create two data models for our study plan application:
    > 
    > 1. StudyPlanRequest with:
    >    - Fields for area, level, weekly_hours, duration_months, specific_objectives
    >
    > 2. StudyPlanResponse with:
    >    - Fields for structured_plan, success, metadata, error
    > ```

## ⌨️ Activity: Implement the API Endpoint

With our GitHub Models client and data models ready, it's time to create the API endpoint that powers our application. This endpoint serves as the bridge between the frontend and AI, handling requests and returning personalized study plans.

The endpoint receives and validates study plan requests from the frontend, processes user preferences including area, level, and time commitment, communicates with GitHub Models AI service, and returns structured educational content. By implementing this endpoint, we complete the backend infrastructure for our intelligent study plan generator.

1. **Navigate to the API file** by opening `app/api/api.py` in the Explorer panel. This file contains the Flask routes that define all our API endpoints.

2. **Update the imports** to use the models:

```python
from app.models.study_plan import StudyPlanRequest, StudyPlanResponse
```

3. **Open the Copilot Chat panel** and select **Edit** mode to help implement the missing functionality. Use the following prompt:

    > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
    >
    > ```prompt
    > Update the `generate_study_plan` function in Flask API to use the GitHub Models client:
    > 
    > - Add validation to check if github_client.token is configured
    > - Add a try/except structure for detailed error handling
    > - Use `build_study_plan_prompt()` with the correct parameters from StudyPlanRequest
    > - Call `github_client.chat_completion()` asynchronously with the messages
    > - For success case: return StudyPlanResponse with AI-generated plan
    > - For error case: return response with success=False and detailed error message
    > ```

> [!TIP]
> The temperature parameter (set to 0.7 in the example) controls the randomness of the AI's response. Lower values (closer to 0) make responses more deterministic and focused, while higher values (closer to 1) make them more creative and varied. You can experiment with this value to find the right balance for educational content.

---

| [← Backend and AI Integration](03-step.md) | [Next: Crafting Prompts for AI →](05-step.md) |
|:-----------------------------------|------------------------------------------:|

