# CodeGeniusBot

CodeGeniusBot is a Discord bot that generates code using the OpenAI API for a specific use case provided by the user.

## Installation

1. Clone the repository:

```
git clone https://github.com/juniorvish/CodeGeniusBot.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory with the following variables:

```
DISCORD_TOKEN=<your_discord_bot_token>
OPENAI_API_KEY=<your_openai_api_key>
```

Replace `<your_discord_bot_token>` with your Discord bot token and `<your_openai_api_key>` with your OpenAI API key.

## Usage

1. Run the bot:

```
python main.py
```

2. In Discord, use the `!bot` command followed by your desired use case to generate code:

```
!bot <your_use_case_here>
```

The bot will generate code based on the provided use case and send it as a message in the Discord channel.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)