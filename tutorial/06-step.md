# Step 6: Adding Form Validation

> **Summary:**
> In this step, you'll use GitHub Copilot's Agent mode to implement validation for the Plan Parameters form, ensuring users complete all necessary fields before submission.

Form validation is essential for web apps that collect user data. It ensures users provide required information in the correct format, gives immediate feedback on errors, and prevents the backend from receiving invalid or incomplete data. 

Currently, our study plan form allows users to submit without completing all fields, which can cause errors or incomplete plans.

## ⌨️ Activity: Implement Form Validation with Copilot Agent

Let's use GitHub Copilot's Agent mode to add validation to our form:

1. Open the **Copilot Chat** panel and switch to **Agent** mode.

2. Provide the following instructions to the agent:

    > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
    >
    > ```prompt
    > Modify the JavaScript code in the index.html file to add validation to the Plan Parameters form.
    > 
    > Implement JavaScript validation for the Plan Parameters form in index.html with these requirements:
    > - Mark required fields visually to guide the user
    > - Prevent form submission if any required field (area, level, weekly time, duration and specific objectives) is empty
    > - Show specific error messages for missing fields
    > - Highlight invalid fields with a red border
    > - Remove the highlight when a field is corrected
    > ```

### 🧪 Test the Form Validation

After implementing the validation, test it to ensure it works as expected:

1. Run the application if it's not already running
2. Try clicking the "Generate Study Plan" button without filling any fields
3. Verify that error messages appear for all required fields
4. Fill in some fields and try again to verify that error messages persist only on empty fields
5. Fill in all required fields and verify that the form submits correctly

### 📝 Implementation Considerations

When using GitHub Copilot Agent for this task, observe how it:

1. Analyzes the existing HTML and JavaScript structure
2. Maintains consistency with the existing code
3. Implements a solution that integrates seamlessly with the existing flow
4. Adds visual feedback to enhance the user experience

Form validation is an excellent opportunity to use GitHub Copilot's Agent mode as it involves understanding existing code structure, adding validation logic, and enhancing user experience—tasks that the Copilot Agent can efficiently accomplish with a single clear instruction.

---

| [← Crafting Prompts for AI](05-step.md) | [Next: Creating Custom Chat Modes for Accessibility Testing →](07-step.md) |
|:-----------------------------------|------------------------------------------:|
