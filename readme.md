# browser use system using deepseek

## install uv

- macOS

```bash
brew install uv
```

- Windows

```bash
winget install uv
```

## initialize uv project

```bash
uv init
```

## install browser-use

```bash
uv add browser-use
uv sync
```

## add browser-use api key in .env file

- get key from here: `https://cloud.browser-use.com/`
- sign up and get your free api key
- create a `.env` file in the root directory of your project and add the following line:

```plaintext
BROWSER_USE_API_KEY=your-key
```

## run test agent

```bash
uv run test-agent.py
```