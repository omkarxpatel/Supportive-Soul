import os
import random
import openai
import discord
from constants import *
from colorama import Fore
from discord import app_commands
from discord.ext import commands
from typing import Literal, Optional
from utility.firebase import *
from dotenv import load_dotenv
from constants import *
from colorama import Fore
from discord.ext import commands
from discord import Intents, ButtonStyle
from discord.ui import View, Button
from typing import Literal, Optional
from utility.firebase import *
from dotenv import load_dotenv

load_dotenv()

##############################
#     SETTING UP THE BOT     #
##############################

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("-"), intents=intents)

@bot.event
async def on_ready():
    print(
        f"{Fore.GREEN}{bot.user.name} is Online - Version: {discord.__version__}{Fore.RESET}"
    )

##############################
#     MENTAL HEALTH COMMANDS     #
##############################

class ResourceLinks(View):
    def __init__(self):
        super().__init__()
        resources = {
            "NAMI": "https://www.nami.org/",
            "MHA": "https://www.mhanational.org/",
            "ADAA": "https://adaa.org/",
            "NIMH": "https://www.nimh.nih.gov/index.shtml",
            "AFSP": "https://afsp.org/",
        }

        for name, url in resources.items():
            self.add_item(Button(label=name, url=url, style=ButtonStyle.link))

def create_embed(title, base_value, resources_value, coping_value):
    embed = discord.Embed(timestamp=discord.utils.utcnow())
    embed.title = title
    embed.add_field(name=base_value, value=resources_value, inline=False)
    embed.add_field(name="**Coping**", value=coping_value, inline=False)
    return embed

def create_resource_command(name, title, base, resources, coping):
    @bot.tree.command(name=name)
    async def command(interaction: discord.Interaction):
        embed = create_embed(title, base, resources, coping)
        view = ResourceLinks()

        embed.set_footer(text=f"Requested by {interaction.user.name}")
        await interaction.response.send_message(embed=embed, view=view)

create_resource_command("resources", "**Here are some resources that you may need!**", "", RESOURCES, "")
create_resource_command("adhd", "**ADHD**", "**What is ADHD?**", ADHD_BASE, ADHD_RESOURCES, ADHD_COPING)
create_resource_command("depression", "**Clinical Depression**", "**What is Clinical Depression?**", DEPRESSION_BASE, DEPRESSION_RESOURCES, DEPRESSION_COPING)
create_resource_command("schizophrenia", "**Schizophrenia**", "**What is Schizophrenia?**", SCHIZOPHRENIA_BASE, SCHIZOPHRENIA_RESOURCES, SCHIZOPHRENIA_COPING)
create_resource_command("bipolar", "**Bipolar Disorder**", "**What is Bipolar Disorder?**", BIPOLAR_BASE, BIPOLAR_RESOURCES, BIPOLAR_COPING)
create_resource_command("anxiety", "**Anxiety Disorder**", "**What is Anxiety Disorder?**", ANXIETY_BASE, ANXIETY_RESOURCES, ANXIETY_COPING)
create_resource_command("PTSD", "**Post-traumatic stress disorder (PTSD)**", "**What is PTSD?**", PTSD_BASE, PTSD_RESOURCES, PTSD_COPING)
create_resource_command("selfharm", "**Self Harm**", "**What is Self Harm?**", SELF_HARM_BASE, SELF_HARM_RESOURCES, "")

#################################
#     SETUP SERVER COMMANDS     #
#################################

@bot.tree.command(name="set_flag_channel")
@app_commands.describe(channel="The channel to set as the flag channel")
async def set_flag_channel(
    interaction: discord.Interaction, channel: discord.TextChannel
):
    """
    Sets a channel as the flag channel in the server.
    """
    try:
        set_logging = set_logging_channel(str(interaction.guild_id), str(channel.id))

        if set_logging:
            await interaction.response.send_message(
                f"Successfully set the self harm flagging channel to: {channel.mention}"
            )

            channel = bot.get_channel(channel.id)
            await channel.send("This is now the self harm flagging channel")
        else:
            await interaction.response.send_message(set_logging)

    except Exception as e:
        await interaction.response.send_message(e)

@bot.tree.command(name="set_flagging")
@app_commands.describe(value="Whether to turn on or off flagging")
async def set_flagging(interaction: discord.Interaction, value: bool):
    """
    Sets whether to turn on or off flagging in the server.
    """
    try:
        set_flagging = set_message_scanning_flag(str(interaction.guild_id), value)

        if set_flagging in [True, False]:
            status = "on" if value else "off"
            await interaction.response.send_message(
                f"Successfully turned **{status}** flagging"
            )
        else:
            await interaction.response.send_message(set_flagging)

    except Exception as e:
        await interaction.response.send_message(e)

@bot.tree.command(name="server_settings")
async def server_settings(interaction: discord.Interaction):
    """
    Returns the current server settings.
    """
    message_scanning = get_message_scanning_flag(str(interaction.guild_id))[
        "flag_messages"
    ]
    logging_channel = get_logging_channel(str(interaction.guild_id))

    embed = discord.Embed(
        timestamp=discord.utils.utcnow(),
        title="**Here are your server settings**",
        color=discord.Color.red(),
    )
    embed.add_field(
        name="",
        value=f"Message Scanning: **{message_scanning}**\nLogging Channel: <#{logging_channel}>",
    )
    await interaction.response.send_message(embed=embed)

##################################
#     MENTAL HEALTH LISTENER     #
##################################

openai.api_key = os.getenv("OPENAI_KEY")

class SuicidalIntentDetector:
    def __init__(self):
        self.user_messages = {}

    def detect_intent(self, user_id, message):
        response = openai.Moderation.create(input=message)
        output = response["results"][0]
        self.user_messages.setdefault(user_id, []).append(
            {"message": message, "intent": output}
        )
        return output

    def get_user_messages(self, user_id):
        return self.user_messages.get(user_id, [])

detector = SuicidalIntentDetector()

class ChatBot:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    def get_response(self, prompt, type_of_prompt, max_tokens=100):
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": type_of_prompt},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"Error: {str(e)}"

chatbot = ChatBot(os.getenv("OPENAI_KEY"))

class Davinci:
    def __init__(self, api_key, model="text-davinci-003"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    def get_response(self, prompt, type_of_prompt, max_tokens=100):
        try:
            prompt = type_of_prompt + prompt
            response = openai.Completion.create(
                engine=self.model, prompt=prompt, max_tokens=max_tokens
            )
            return response.choices[0].text.strip()

        except Exception as e:
            return f"Error: {str(e)}"

detection_response = Davinci(os.getenv("OPENAI_KEY"))

@bot.tree.command(name="chat")
async def chat(interaction: discord.Interaction):
    """
    Opens a chat with the invoking user in 
    """
    view = ChatBot()

    await interaction.response.send_message("Click below to open a chat with me!", view=view)

@bot.event
async def on_guild_join(guild):
    set_message_scanning_flag(str(guild.id), True)

    # TODO setup on guild join config message using: guild.system_channel

@bot.event
async def on_message(message):
    """
    Scans every single message sent that is accessible to the bot for suicidal tendencies. If a message is flagged, more action will be taken upon that message & the author.
    """
    if isinstance(message.channel, discord.DMChannel):
        return
    
    if not isinstance(message.author, discord.User) or message.author.bot:
        return

    if message.author.id == bot.user.id:
        return
    
    server_info = get_message_scanning_flag(str(message.guild.id))
    if server_info["flag_messages"]:
        user_id = str(message.author.id)
        result = detector.detect_intent(user_id, message.content)
        try:
            result["prompt"] = message.content
        except:
            result["prompt"] = "Blank"
        user = get_user(str(message.author))
        user["suicide_history"].append(result)
        set_user(str(message.author), user)

        result_categories = result["categories"]
        self_harm = ["self-harm", "self-harm/intent", "self-harm/instructions"]
        embed_content = []

        for item in self_harm:
            if result_categories[item]:
                embed_content.append(item)

        if len(embed_content) > 0:
            embed = discord.Embed(
                timestamp=discord.utils.utcnow(),
                title="**A message has been flagged**",
                color=discord.Color.red(),
            )
            embed.add_field(
                name=f"Reason: `{', '.join(embed_content)}`",
                value=f"Message content: {message.content}\nMessage sender: {message.author.mention}\n\nMessage link: https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}",
            )
            channel_id = get_logging_channel(str(message.guild.id))
            try:
                channel = bot.get_channel(int(channel_id))
                await channel.send(embed=embed)
            except:
                pass

            response = detection_response.get_response(
                f"{message.author.name}: {message.content}", DETECTION_PROMPT
            )
            view = ChatBot()
            await message.reply(response, view=view)  # sends chatgpt crafted response
            embed = create_embed(
                "**Here are some resources that you may need!**", "", RESOURCES, ""
            )
            await message.reply(embed=embed, view=ResourceLinks())
            
    await bot.process_commands(message)

#########################
#     MISC COMMANDS     #
#########################

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.send(error)

@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    """
    Returns the current ping of the bot.
    """
    embed = discord.Embed(timestamp=discord.utils.utcnow())
    embed.add_field(
        name="**Current ping of bot**",
        value=f"> :ping_pong: {round(bot.latency * 1000)}ms",
    )
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed)

# List of flowers
flowers = [
    "Rose",
    "Lily",
    "Sunflower",
    "Tulip",
    "Daisy",
    "Orchid",
    "Carnation",
    "Daffodil",
    "Peony",
    "Hyacinth"
]

# List of affirmative messages
assurance = [
    "You're doing great!",
    "Keep up the good work!",
    "You're amazing!",
    "You've got this!",
    "You're making progress!",
    "You're an inspiration!",
    "Believe in yourself!",
    "You're capable of great things!",
    "You're strong and resilient!",
    "You're loved and appreciated!"
]

@bot.tree.command(name="flower")
async def send_flower(ctx):
    # Get a random flower from the list
    flower = random.choice(flowers)
    await ctx.send(f"Here's a {flower} for you!")

@bot.tree.command(name="assurance")
async def send_assurance(ctx):
    # Get a random assurance from the list
    assurance_msg = random.choice(assurance)
    await ctx.send(assurance_msg)

@bot.tree.command(name="hug")
async def hug(interaction: discord.Interaction):
    """
    Sends a virtual hug.
    """
    embed = discord.Embed(title="Here's a hug!", timestamp=discord.utils.utcnow())
    embed.set_image(
        url=f"https://cdn.nekos.life/hug/hug_{str(random.randint(1, 89)).zfill(3)}.gif"
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="affirmation")
async def affirmation(interaction: discord.Interaction):
    await interaction.response.send_message(
        chatbot.get_response(
            "Please write this user an affirmation.",
            "Please write this user an affirmation.",
        )
    )

@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
    """
    Displays the help message!
    """
    embed = discord.Embed(
        title="Supportive Soul Help",
        description="Here to provide positivity and mental health support!",
        color=0xFF69B4,
        timestamp=discord.utils.utcnow(),
    )

    embed.set_author(name="Supportive Soul", icon_url="https://i.imgur.com/lm8s41J.png")
    embed.set_thumbnail(url="https://i.imgur.com/xfhXrXw.png")
    embed.add_field(
        name="🫂 **Need someone to talk to?** ",
        value="**/chat** Have a conversation with me in dms",
        inline=False,
    )
    embed.add_field(
        name="😊 **Want some positivity?** ",
        value="**/affirmation** Get an uplifting message\n**/hug** Receive a virtual hug",
        inline=False,
    )
    embed.add_field(
        name="🌈 **Helpful Resources** ",
        value="**/resources** Mental health & crisis resources\n**/adhd** ADHD info & resources\n**/depression** Depression info & resources\n**/selfharm** Self-harm info & resources",
        inline=False,
    )
    embed.add_field(
        name="⚙️ **Server Configuration**",
        value="**/set_flag_channel** Set self-harm flag channel\n**/set_flagging** Turn flagging on/off\n**/server_settings** View current settings",
        inline=False,
    )
    embed.set_footer(text="Use -help <command> for more info!")
    embed.set_image(url="https://i.imgur.com/xfhXrXw.png")

    await interaction.response.send_message(embed=embed)

@bot.command()
@commands.guild_only()
async def sync(
    ctx: commands.Context,
    guilds: commands.Greedy[discord.Object],
    spec: Optional[Literal["~", "*", "^"]] = None,
) -> None:
    """
    Used for syncing slash commands
    """
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

try:
    bot.run(os.getenv("DISCORD_TOKEN"))
finally:
    print(f"{Fore.RED}Support Soul is now Offline{Fore.RESET}")
