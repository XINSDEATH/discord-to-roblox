import urllib.request
import json
@client.command()
async def userinfo(ctx, userid):
    await ctx.send(f"fetching info on {userid}")
    #data's
    url = f"https://users.roblox.com//v1/users/{userid}"
    data = urllib.request.urlopen(url).read().decode()
    data1 = json.loads(data)
    # user infos
    username = data1['name']
    disp = data1['displayName']
    id = data1['id']
    des = data1['description']
    created = data1['created']
    isbanned = data1['isBanned']
    # embed
    embed=discord.Embed(title="user info")
    embed.add_field(name="username:", value=username, inline=False)
    embed.add_field(name="display name:", value=disp, inline=False)
    embed.add_field(name="id:", value=id, inline=False)
    embed.add_field(name="description:", value=des, inline=False)
    embed.add_field(name="created:", value=created, inline=False)
    embed.add_field(name="is banned?:", value=isbanned, inline=False)
    await ctx.send(embed=embed)

@client.command()
async def getuserid(ctx, member: discord.Member):
    #data's
    url = f"https://api.blox.link/v1/user/{member.id}"
    data = urllib.request.urlopen(url).read().decode()
    data1 = json.loads(data)
    # user info's
    status = data1['status']
    if status == "ok":
        await ctx.send(f"fetching user id for {member.mention}")
        userid = data1['primaryAccount']
        await ctx.send(f"found userid for {member.mention}")
        await ctx.send(userid)
    else:
        await ctx.send(f"{member.mention} not linked with bloxlink")
