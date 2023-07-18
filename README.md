# A random quote a day

This is a program that retrieves a quote from https://github.com/lukePeavey/quotable and then sends it via telegram bot.

## How to install

To send messages via telegram bot, we need to create our bot first. 

1. Search for @BotFather on telegram
2. Type /newbot and pick a name for your bot
3. Save the token you got from the @BotFather
4. Retrieve the chat id from your bot:
    - Write your bot a message 
    - Now you can use this url https://api.telegram.org/bot%7BToken%7D/getUpdates to get your chat id. Replace {TOKEN} with your token from Step 3 and then send a request. 

Here is an example of the response from step 4:

```json
{
  "ok": true,
  "result": [
    {
      "update_id": "<UPDATE_ID>",
      "message": {
        "message_id": "<MESSAGE_ID>",
        "from": {
          "id": "<FROM_ID>",
          "is_bot": false,
          "first_name": "<NAME>",
          "language_code": "<COUNTRY_CODE>"
        },
        "chat": { "id": "<CHAT_ID>", "first_name": "<NAME>", "type": "<TYPE>" },
        "date": "<DATE>",
        "text": "<MESSAGE>"
      }
    }
  ]
}
```

After you gathered your token and chat id, you have to place them in the config.json file.

```json
{
  "token": "Place your token here",
  "chat_id": "Place your chat id here"
}
```

Now you could run the program after installing the python packages listed in the requirements.txt file. 

```
pip install -r requirements.txt
```

Or optionally use systemd to run the program. In the folder systemd are service and timer files for that.



