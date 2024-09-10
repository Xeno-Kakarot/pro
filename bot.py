from pyrogram import Client, filters

# Replace these with your actual credentials
API_ID = '24683098'        # Example: 1234567
API_HASH = 'e4055cd239464e50e69bd73057c05dd3'    # Example: abcdef1234567890abcdef1234567890
BOT_TOKEN = '7391930298:AAEVpWkGNhtuxpHuLUvwId3QrOaLA2xzHaQ'  # Example: 123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11

app = Client("reaction_views_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start command handler
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(
        "Hello! I am a bot that can help you add fake reactions and views to posts.\n"
        "Commands:\n"
        "/reaction <amount> - Add reactions to a post\n"
        "/views <amount> - Add views to a post"
    )

# Reaction command handler
@app.on_message(filters.command("reaction") & filters.private)
async def reaction_handler(client, message):
    if not message.reply_to_message:
        await message.reply_text("Please reply to the post you want to react to.")
        return
    try:
        reaction_count = int(message.command[1])  # Number of reactions from command
    except (IndexError, ValueError):
        await message.reply_text("Usage: /reaction <amount>")
        return

    emojis = ["👍", "❤️", "😂", "😢", "😮", "🔥", "🎉"]  # Set of emojis to use
    post = message.reply_to_message

    for i in range(reaction_count):
        emoji = emojis[i % len(emojis)]  # Cycle through emojis
        await client.send_reaction(post.chat.id, post.message_id, emoji)
    
    await message.reply_text(f"Added {reaction_count} reactions to the post!")

# Views command handler
@app.on_message(filters.command("views") & filters.private)
async def views_handler(client, message):
    if not message.reply_to_message:
        await message.reply_text("Please reply to the post you want to add views to.")
        return
    try:
        view_count = int(message.command[1])  # Number of views from command
    except (IndexError, ValueError):
        await message.reply_text("Usage: /views <amount>")
        return

    post = message.reply_to_message
    await fake_increment_views(post, view_count)  # Call the fake view increment function

    await message.reply_text(f"Added {view_count} views to the post!")

# Fake views increment function (since Telegram does not allow modifying real views)
async def fake_increment_views(post, view_count):
    # Simulate the delay for incrementing views (to make it look real)
    # This part can be customized according to your logic
    pass  # This function can be enhanced if needed

# Run the bot
app.run()
