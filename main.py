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

load_dotenv()


##############################
#     SETTING UP THE BOT     #
##############################


class SupportSoul(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix=commands.when_mentioned_or("-"), intents=intents
        )

    async def on_ready(self):
        print(
            f"{Fore.GREEN}{self.user.name} is Online - Version: {discord.__version__}{Fore.RESET}"
        )


bot = SupportSoul()


##################################
#     MENTAL HEALTH COMMANDS     #
##################################


class ResourceLinks(discord.ui.View):
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
            self.add_item(discord.ui.Button(label=name, url=url))


def official_resources():
    embed = discord.Embed(timestamp=discord.utils.utcnow())
    embed.title = "**Here are some resources that you may need!**"
    embed.add_field(
        name="",
        value=RESOURCES,
    )
    return embed


def adhd_resources():
    embed = discord.Embed(timestamp=discord.utils.utcnow())
    embed.title = "**ADHD**"
    embed.add_field(
        name="**What is ADHD?**",
        value=ADHD_BASE,
        inline=False,
    )
    embed.add_field(
        name="**Resources**",
        value=ADHD_RESOURCES,
        inline=False,
    )
    embed.add_field(
        name="**Coping with ADHD**",
        value=ADHD_COPING,
        inline=False,
    )
    return embed


def depression_resources():
    embed = discord.Embed(timestamp=discord.utils.utcnow())
    embed.title = "**Clinical Depression**"
    embed.add_field(
        name="**What is Clinical Depression?**",
        value=DEPRESSION_BASE,
        inline=False,
    )
    embed.add_field(
        name="**Resources**",
        value=DEPRESSION_RESOURCES,
        inline=False,
    )
    embed.add_field(
        name="**Coping with Depression**",
        value=DEPRESSION_COPING,
        inline=False,
    )
    return embed


def schizophrenia_resources():
    embed = discord.Embed(timestamp=discord.utils.utcnow())
    embed.title = "**Schizophrenia**"
    embed.add_field(
        name="**What is Schizophrenia?**",
        value=SCHIZOPHRENIA_BASE,
        inline=False,
    )
    embed.add_field(
        name="**Resources**",
        value=SCHIZOPHRENIA_RESOURCES,
        inline=False,
    )
    embed.add_field(
        name="**Coping with Schizophrenia**",
        value=SCHIZOPHRENIA_COPING,
        inline=False,
    )
    return embed
    

def bipolar_resources():
    embed = discord.Embed(timestamp=discord.utils.utcnow())
    embed.title = "**Bipolar Disorder**"
    embed.add_field(
        name="**What is Bipolar Disorder?**",
        value=BIPOLAR_BASE,
        inline=False,
    )
    embed.add_field(
        name="**Resources**",
        value=BIPOLAR_RESOURCES,
        inline=False,
    )
    embed.add_field(
        name="**Coping with Bipolar**",
        value=BIPOLAR_COPING,
        inline=False,
    )
    return embed
    
    
def anxiety_resources():
    embed = discord.Embed(timestamp=discord.utils.utcnow())
    embed.title = "**Anxiety Disorder**"
    embed.add_field(
        name="**What is Anxiety Disorder?**",
        value=ANXIETY_BASE,
        inline=False,
    )
    embed.add_field(
        name="**Resources**",
        value=ANXIETY_RESOURCES,
        inline=False,
    )
    embed.add_field(
        name="**Coping with Bipolar**",
        value=ANXIETY_COPING,
        inline=False,
    )
    return embed


def PTSD_resources():
    embed = discord.Embed(timestamp=discord.utils.utcnow())
    embed.title = "**Post-traumatic stress disorder (PTSD)**"
    embed.add_field(
        name="**What is PTSD?**",
        value=PTSD_BASE,
        inline=False,
    )
    embed.add_field(
        name="**Resources**",
        value=PTSD_RESOURCES,
        inline=False,
    )
    embed.add_field(
        name="**Coping with PTSD**",
        value=PTSD_COPING,
        inline=False,
    )
    return embed


def self_harm_resources():
    embed = discord.Embed(timestamp=discord.utils.utcnow())
    embed.title = "**Self Harm**"
    embed.add_field(
        name="**What is Self Harm?**",
        value=SELF_HARM_BASE,
        inline=False,
    )
    embed.add_field(
        name="**Resources**",
        value=SELF_HARM_RESOURCES,
        inline=False,
    )
    return embed


@bot.tree.command(name="resources")
async def resources(interaction: discord.Interaction):
    """
    Sends a list of mental health resources to the user.

    Provides a list of helpline numbers and websites that offer support for mental health, including suicide prevention hotlines, crisis text lines, and LGBTQ+ and veteran-specific resources.
    """
    embed = official_resources()
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed, view=ResourceLinks())


@bot.tree.command(name="adhd")
async def adhd(interaction: discord.Interaction):
    """
    Provides helpful resources for ADHD
    """
    embed = adhd_resources()
    view = ViewResources()

    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed, view=view)


@bot.tree.command(name="depression")
async def depression(interaction: discord.Interaction):
    """
    Provides helpful resources for depression
    """
    embed = depression_resources()
    view = ViewResources()

    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed, view=view)


@bot.tree.command(name="schizophrenia")
async def schizophrenia(interaction: discord.Interaction):
    """
    Provides helpful resources for schizophrenia
    """
    embed = schizophrenia_resources()
    view = ViewResources()

    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed, view=view)
    
    
@bot.tree.command(name="bipolar")
async def bipolar(interaction: discord.Interaction):
    """
    Provides helpful resources for bipolar
    """
    embed = bipolar_resources()
    view = ViewResources()

    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed, view=view)
    
    
@bot.tree.command(name="anxiety")
async def anxiety(interaction: discord.Interaction):
    """
    Provides helpful resources for schizophrenia
    """
    embed = anxiety_resources()
    view = ViewResources()

    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed, view=view)


@bot.tree.command(name="PTSD")
async def PTSD(interaction: discord.Interaction):
    """
    Provides helpful resources for PTSD
    """
    embed = PTSD_resources()
    view = ViewResources()

    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed, view=view)


@bot.tree.command(name="selfharm")
async def selfharm(interaction: discord.Interaction):
    """
    Provides helpful resources for self-harm
    """
    embed = self_harm_resources()
    view = ViewResources()

    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed, view=view)


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
    # if on_or_off.lower() in ["t", "true", "on"]:
    # on_or_off = True
    # else:
    # on_or_off = False
    try:
        set_flagging = set_message_scanning_flag(str(interaction.guild_id), value)

        if set_flagging in [True, False]:
            if value:
                await interaction.response.send_message(
                    f"Successfully turned **on** flagging"
                )
            else:
                await interaction.response.send_message(
                    f"Successfully turned **off** flagging"
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
        name=f"",
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


class ViewResources(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="View Resources", style=discord.ButtonStyle.gray)
    async def confirm(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        embed = official_resources()
        await interaction.response.send_message(embed=embed, view=ResourceLinks())
        self.stop()

class ChatBot(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Open A Chat", style=discord.ButtonStyle.gray)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            view = ViewResources()
            await interaction.user.send("Hey {}, thanks for reaching out. Whats on your mind?".format(interaction.user.name), view=view)
            await interaction.response.send_message("Check your dms!", ephemeral=True)
            self.stop()
            
        except Exception as e:
            await interaction.response.send_message("Try directly messaging me instead, an error occured: {}".format(e), ephemeral=True)

class ChatGPT:
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


chatbot = ChatGPT(os.getenv("OPENAI_KEY"))


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
    await bot.process_commands(message)
    # if message.channel.id == 1133522534223057016:
    #     if message.author.id in [641069257140207616, 838974822288851005]: # for debugging
    if not isinstance(message.channel, discord.DMChannel):
        server_info = get_message_scanning_flag(str(message.guild.id))
        # if isinstance(server_info, dict):

        if message.author.id != 1133522196917145662:
            if server_info["flag_messages"] == True:
                user_id = str(message.author.id)

                result = detector.detect_intent(user_id, message.content)

                try:
                    result["prompt"] = message.content
                except:
                    result["prompt"] = "Blank"
                user = get_user(str(message.author))

                user["suicide_history"].append(result)
                set_user(str(message.author), user)
                # insert_data_to_db(result, connection, "suicide-detection")

                result_categories = result["categories"]
                self_harm = ["self-harm", "self-harm/intent", "self-harm/instructions"]
                embed_content = []

                for item in self_harm:
                    if result_categories[item] == True:
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
                    channel = get_logging_channel(str(message.guild.id))
                    try:
                        channel = bot.get_channel(int(channel))
                        await channel.send(embed=embed)
                    except:
                        pass

                    response = detection_response.get_response(
                        f"{message.author.name}: {message.content}", DETECTION_PROMPT
                    )
                    view = ChatBot()
                    await message.reply(response, view=view)  # sends chatgpt crafted response
                    embed = official_resources()
                    await message.reply(embed=embed, view=ResourceLinks())
    else:
        if message.author != bot.user:
            # Get a response from ChatGPT
            history = ""
            count = 0
            async for history_message in message.channel.history(limit=None):
                if history_message.author != bot.user:
                    history += (
                        history_message.author.name + ": " + history_message.content
                    )
                    count += 1
                else:
                    history += "YOU:" + history_message.content
                if count == 10:
                    break
                history += "\n"

            response = chatbot.get_response(
                f"{message.author.name}: {message.content}", CHATBOT_PROMPT
            )
            view = ViewResources()
            await message.reply(response, view=view)

            # await view.wait()
            # if view.value is None:
            #     pass
            # elif view.value:
            #     embed = official_resources()
            #     await message.reply(embed=embed, view=ResourceLinks())


#########################
#     MISC COMMANDS     #
#########################


@bot.event
async def on_ready():
    print(f'Bot is connected as {bot.user.name}')

@bot.tree.command()
async def error(ctx):
    raise commands.CommandError("Error!")

@bot.event
async def on_command_error(ctx, error):
    # Check if the error is an instance of CommandError
    if isinstance(error, commands.CommandError):
        # Send a message


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
    assurance = random.choice(assurance)
    await ctx.send(assurance)


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
# @commands.is_owner()
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


#######################################

try:
    bot.run(os.getenv("DISCORD_TOKEN"))

finally:
    print(f"{Fore.RED}Support Soul is now Offline{Fore.RESET}")
