from pyrogram import Client
import config
from help import register_help_handlers
from aiohttp import web
import asyncio
import os

app = Client(
    "RoseProBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="modules") # Auto-load all separate modules
)

# Help module handlers registration
register_help_handlers(app)

# Render ke liye dummy web server (Port bind karne ke liye)
async def handle(request):
    return web.Response(text="Rose Pro Bot is active!")

async def web_server():
    web_app = web.Application()
    web_app.router.add_get("/", handle)
    runner = web.AppRunner(web_app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

if __name__ == "__main__":
    print("Rose Pro Bot Ready & Starting...")
    
    # Loop utha kar web server aur bot dono ko ek sath chalane ke liye
    loop = asyncio.get_event_loop()
    loop.create_task(web_server())
    
    app.run()
