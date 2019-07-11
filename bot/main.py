import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ban_bot_panel.settings")
import django
django.setup()
import discord
import config
from app.models import Ban

bot = discord.Client()


@bot.event
async def on_guild_join(guild):
    bans = await guild.bans()
    for ban in bans:
        ban_obj = Ban.objects.filter(reason=ban.reason, user_id=ban.user.id, server_id=guild.id)
        if not ban_obj.exists():
            if not ban.reason:
                ban.reason = ""
            ban_obj = Ban(reason=ban.reason, user_name=ban.user.name, user_id=ban.user.id, server_name=guild.name,
                          server_id=guild.id)
            ban_obj.save()


@bot.event
async def on_member_ban(guild, user):
    bans = await guild.bans()
    for ban in bans:
        ban_obj = Ban.objects.filter(reason=ban.reason, user_id=ban.user.id, server_id=guild.id)
        if not ban_obj.exists():
            if not ban.reason:
                ban.reason = ""
            ban_obj = Ban(reason=ban.reason, user_name=ban.user.name, user_id=ban.user.id, server_name=guild.name,
                          server_id=guild.id)
            ban_obj.save()


@bot.event
async def on_member_join(member):
    guild = member.guild
    bans = Ban.objects.order_by("-id").all()
    bans_string = ""
    ban_index = 1
    for ban in bans:
        if str(ban.user_id) == str(member.id):
            bans_string += f"{ban_index}. {ban.reason}\n"
            ban_index += 1
    embed = discord.Embed(title=f"Bans voor {member.name}", description=bans_string)
    await guild.owner.send(embed=embed)

bot.run(config.TOKEN)