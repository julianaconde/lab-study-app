# Step 8: Commit and Code Review with GitHub Copilot

> **Summary:**
> In this step, you'll learn how to use GitHub Copilot to automatically generate meaningful commit messages based on your code changes and to perform code reviews before committing. These features help improve your Git workflow and maintain high code quality.

## ⌨️ Activity: Generating a Commit Message

Let's use GitHub Copilot to generate a commit message for the accessibility improvements you've made:

1. **Open the Source Control view** in VS Code by clicking the Git icon or pressing `Ctrl+Shift+G` (`Cmd+Shift+G` on macOS).

2. Stage your changes by clicking the `+` icon next to the modified files or using the "Stage All Changes" option.

   <details>
      <summary>📸 Show screenshot</summary>
       <img src="images/7-stage-changes.png" alt="Screenshot of stagging all changes" />
   </details>
   
3. **Click the GitHub Copilot icon** in the commit message input area (looks like a sparkle or AI icon).

   <details>
      <summary>📸 Show screenshot</summary>
       <img src="images/7-generate-commit-message.png" alt="Screenshot of commit interface with Copilot button" />
   </details>

4. **Wait for Copilot to analyze your changes** and generate a commit message automatically. The message will appear in the commit input field.

5. **Review and edit** the generated message if needed. Even with AI assistance, it's good practice to verify the message accurately reflects your changes.

6. **Complete the commit** by clicking the checkmark icon or pressing `Ctrl+Enter` (`Cmd+Enter` on macOS).

<details>
  <summary>Example of a generated commit message</summary>

```
Improve accessibility in StudyPlan AI dashboard

- Add semantic HTML5 landmarks (header, nav, main, footer)
- Make all interactive elements keyboard accessible
- Add proper ARIA attributes to icons and UI components
- Improve form field labeling and associations
- Add status message announcements for screen readers

These changes ensure WCAG 2.1 AA compliance and improve the experience for users with disabilities.
```

</details>

## ⌨️ Activity: Performing Code Reviews with Copilot

Before finalizing your commit, use GitHub Copilot to review your code changes:

1. **Open the Command Palette** with `Ctrl+Shift+P` (`Cmd+Shift+P` on macOS).

2. **Search for "GitHub Copilot: Review Changes"** and select it.

3. **Wait for Copilot to analyze your changes** and provide feedback on potential issues or improvements.

   <details>
      <summary>📸 Show screenshot</summary>
       <img src="images/7-code-review.png" alt="Screenshot of code review feature" />
   </details>

4. Review the suggestions provided by Copilot, which may include potential bugs or logic errors, accessibility issues, performance optimizations, security vulnerabilities, and code style improvements.

5. Address any relevant suggestions before proceeding with your commit.

6. Generate a new commit message that reflects any additional improvements you've made.


## 💡 Best Practices for Using These Features

1. **Always review the generated commit messages** before committing to ensure accuracy.

2. **Add context when needed** - AI may not understand the "why" behind certain changes.

3. **Consider Copilot's code review as a complementary tool** - it doesn't replace human code review.

4. **Combine with accessibility checks** from the previous step for comprehensive quality assurance.

5. **Use these features consistently** to build good development habits.

---

| [← Creating Custom Chat Modes for Accessibility Testing](07-step.md) | [Next: Review and next steps →](09-step.md) |
|:-----------------------------------|------------------------------------------:|
