
## How to Run the Agent

### Clone the repository

```bash
git clone https://github.com/your-username/llm-agent-demo.git
cd llm-agent-demo
```

---

### Create a virtual environment

```bash
python -m venv venv
```

---

### Activate the virtual environment

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows (PowerShell)**

```bash
venv\Scripts\Activate.ps1
```

**Windows (CMD)**

```bash
venv\Scripts\activate
```

You should now see `(venv)` in your terminal prompt.

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Set your Groq API key

Create a file called `.env` in the project root:

```env
GROQ_API_KEY=your_api_key_here
```
---

### Run the agent

```bash
python agent.py
```

---

### Interact with the agent

You will see:

```text
Ask the agent (or 'exit'):
```

Type a question and press Enter.

To quit:

```text
exit
```

---

## Example Demo Question

```text
How much would it cost to run a 150W server for 30 days if electricity costs 0.35€/kWh?
```

