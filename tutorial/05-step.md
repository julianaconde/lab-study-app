# Step 5: Crafting Prompts for AI

> **Summary:**
> In this step, you’ll learn how to craft prompts for AI content generation via API requests. You’ll implement a structured prompt system for StudyPlan AI, test it in different scenarios, and refine it iteratively to produce high-quality study plans.

The quality of AI-generated study plans depends heavily on how prompts are written. Clear, well-structured prompts help the AI understand the context, include all the required components, and return responses in the right format. A robust prompt system usually includes two parts:

* **System Prompt** – Defines the AI’s role, tone, and behavioral guidelines. For example, you might instruct the AI to act as an educational mentor or to always provide concise, structured responses.
* **User Prompt** – Contains the specific request and input data, usually formatted with a template to guide the AI’s output.

## ⌨️ Activity: Implement the Build Study Plan Prompt Function

The `build_study_plan_prompt` function creates personalized prompts that guide the AI in generating relevant study plans. Let’s implement it with GitHub Copilot.

1. **Open the prompts file** at `app/services/prompts.py`. You’ll find sample prompts and a placeholder for the function.

2. Let's complete the `build_study_plan_prompt` function using Agent mode. Open the **Copilot Chat** panel, switch to **Agent** mode and provide the following instructions:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
   >
   > ```prompt
   > Complete the `build_study_plan_prompt` function so that it returns a list of messages:
   >
   > **System prompt should include:**
   > - You're an education specialist with 10+ years of experience
   > - Always respond in the user's preferred language
   > - Create practical, structured, and realistic plans
   > - Include hands-on projects and specific resources
   >
   > **User prompt should include:**
   > - Template with variables: area, level, time, duration, goals
   > - Request for detailed weekly schedule
   > - Request for specific resources (courses, books, tools)
   > - Request for progressive practical projects
   > - Request for monthly evaluation milestones
   > ```

3. Save the changes and test with sample inputs. For example:

   | Area          | Level        | Weekly Time | Duration | Specific Goal                                 |
   | ------------- | ------------ | ----------- | -------- | --------------------------------------------- |
   | backend       | beginner     | 10          | 3        | "I want to build REST APIs with Node.js"      |
   | frontend      | intermediate | 15          | 4        | "I need to master React and learn Next.js"    |
   | data\_science | advanced     | 20          | 6        | "I want to implement ML models in production" |
   | fullstack     | beginner     | 12          | 6        | "I want to create a complete web application" |
   | ai\_ml        | intermediate | 18          | 5        | "I need to understand deep learning for NLP"  |

These examples test different areas, skill levels, and goals, giving you a clear picture of how your prompt system adapts to various scenarios.

---

| [← Data Models and API Endpoint](04-step.md) | [Next: Adding Form Validation →](06-step.md) |
|:-----------------------------------|------------------------------------------:|
