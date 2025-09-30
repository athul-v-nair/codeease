# CodeEase – AI-powered Log Analyzer & Code Fixer

CodeEase is an experimental AI-powered tool that watches logs, analyzes errors, and suggests code fixes.  
The project is built as a learning journey into AI coding agents using Hugging Face’s Inference API.

---

## 🚀 Features (Current & Planned)

### ✅ Phase 1: Prototype
- **Basic CLI interface.**
- **Takes logs** (from file or input).
- **Sends them to an AI model.**
- **Suggests possible fixes.**

### 🔄 Phase 2: Watcher & Runner (In-progress)
- **Watcher:** Continuously monitor log files ✅.
- **Runner:** Rerun the program after applying suggested fixes.

### 🔧 Phase 3: Fixer Enhancements
- **Suggest multiple solutions.**
- **Rank solutions** (best-first).
- **Highlight risky changes.**

### 🤖 Phase 4: Agentic AI Extension
- **Build memory:** Remember past errors and fixes.
- **Autonomous loop:** Detect → Suggest → Fix → Test → Repeat.
- **Simple evaluation metrics** (success/failure).

---

## 📂 Project Structure
```
codeease/
├── core/
│ ├── watcher.py # Watches logs & triggers fixer
│ ├── fixer.py # Suggests fixes using AI
│ └── runner.py # Re-runs the target program
├── ai/
│ └── interface.py # Interface for AI model interactions
├── config/
│ └── settings.py # Configuration file
├── main.py # Entry point to combine everything
├── requirements.txt # Dependencies
└── README.md

```

## 💻 Installation & Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/CodeEase.git
    cd CodeEase
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the tool:**

    The basic command to start CodeEase is:

    ```bash
    python main.py --command <command-to run the code> --filepath <path-to-program-file>
    ```

---

## 🧠 How it Works

1. **Log Watcher:**  
   The `watcher.py` module continuously monitors log files, checking for errors and triggering the fixer when necessary.

2. **AI Fixer:**  
   The `fixer.py` module uses AI (via Hugging Face's Inference API) to analyze the logs and suggest code fixes based on the identified errors.

3. **Runner:**  
   The `runner.py` module re-runs the target program after applying the suggested fixes to ensure that the issue is resolved.

---

## 📄 Contributing

We welcome contributions! Feel free to fork the repository, open an issue, or submit a pull request.  
Please ensure that your code follows the style guide and passes all tests.

---

## 📧 Contact

For questions or suggestions, feel free to reach out to [athulvnair2001@gmail.com].
