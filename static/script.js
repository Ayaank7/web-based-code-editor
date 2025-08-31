document.addEventListener("DOMContentLoaded", () => {
  const codeInput = document.getElementById("code-input");
  const languageSelect = document.getElementById("language-select");
  const runButton = document.getElementById("run-button");
  const outputArea = document.getElementById("output-area");

  const flaskBaseUrl = "http://127.0.0.1:5000";

  codeInput.value = `print("Hello, World!")`;

  runButton.addEventListener("click", async () => {
    const code = codeInput.value;
    const language = languageSelect.value;

    runButton.disabled = true;
    runButton.textContent = "Running...";
    outputArea.textContent = "Executing code...";

    try {
      const response = await fetch(`${flaskBaseUrl}/run_code`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ code, language }),
      });

      const result = await response.json();

      outputArea.textContent = result.output;
    } catch (error) {
      outputArea.textContent = `Failed to connect to the server: ${error.message}. Check that the Flask server is running at ${flaskBaseUrl}.`;
    } finally {
      runButton.disabled = false;
      runButton.textContent = "Run Code";
    }
  });

  languageSelect.addEventListener("change", () => {
    const language = languageSelect.value;
    let placeholderText = "";
    switch (language) {
      case "python":
        placeholderText = 'print("Hello, World!")';
        break;
      case "cpp":
        placeholderText =
          '#include <iostream>\n\nint main() {\n    std::cout << "Hello, World!" << std::endl;\n    return 0;\n}';
        break;
      case "java":
        placeholderText =
          'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}';
        break;
    }
    codeInput.value = placeholderText;
  });
});
