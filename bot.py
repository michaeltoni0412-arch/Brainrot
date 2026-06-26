import discord
import aiohttp
import random
import os

TOKEN = os.environ["MTUxMzI2NjAyMjE4NTE3MzIzMw.GIyAJm.Y4aNsIlIQQRV06E2N96hz8TVrMmPUPA6b45YP0"]
PLACE_ID = 109983668079237

bot = discord.Bot(intents=discord.Intents.default())

@bot.slash_command(name="view", description="Watch a random live server in Steal a Brainrot")
async def view(ctx):
    await ctx.defer()
    url = f"https://games.roblox.com/v1/games/{PLACE_ID}/servers/Public?limit=100"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            servers = data.get("data", [])
    if not servers:
        await ctx.followup.send("❌ No active servers!")
        return
    server = random.choice(servers)
    embed = discord.Embed(
        title="🎥 Steal a Brainrot — Live Server",
        description=f"**Players:** `{server['playing']}/{server['maxPlayers']}`",
        color=0x00ff00
    )
    join_url = f"https://www.roblox.com/games/start?placeId={PLACE_ID}&gameInstanceId={server['id']}"
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="🎮 Join", url=join_url, style=discord.ButtonStyle.green))
    await ctx.followup.send(embed=embed, view=view)

bot.run(TOKEN)
