import discord
import os
import atexit
from discord import app_commands
from dotenv import load_dotenv
import random

def main():
    # defines intents
    intents = discord.Intents.default()

    # allows message content to be accessed and manipulated
    intents.message_content = True

    # global check variables
    global val
    val = False
    global check
    check = False

    # allows token to be stored in ENV file securely
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    # defines client intents and commands
    client = discord.Client(intents=intents, command_prefix='!')

    # makes tree for commands
    tree = app_commands.CommandTree(client, fallback_to_global=True)

    def begin():
        """sets val true, starting frog reactions"""
        global val
        val = True
        print('Start')

    def fin():
        """sets val false, starting frog reactions"""
        global val
        val = False
        print('Stop')

    def exit_handler():
        """saves archive when program exits"""
        print('Exiting . . .')
        if check:
            print('Saving file')
            global outfile
            outfile.close()

    def adaptor(verse):
        books = {'Genesis': 'Ge', 'Exodus':'Exo', 'Leviticus':'Lev', 'Numbers': 'Num', 'Deuteronomy': 'Deu', 'Joshua': 'Josh',
                'Judges': 'Jdgs', 'Ruth': 'Ruth', '1 Samuel': '1Sm', '2 Samuel': '2Sm', '1 Kings': '1Ki', '2 Kings': '2Ki', 
                '1 Chronicles': '1Chr', '2 Chronicles': '2Chr', 'Ezra': 'Ezra', 'Nehemiah': 'Neh', 'Esther': 'Est', 'Job': 'Job', 
                'Psalms': 'Psa', 'Proverbs': 'Prv', 'Ecclesiastes': 'Eccl', 'Song of Solomon': 'SSo', 'Isaiah': 'Isa', 'Jeremiah': 'Jer', 
                'Lamentations':'Lam', 'Ezekial': 'Eze', 'Daniel': 'Dan', 'Hosea': 'Hos', 'Joel': 'Joel', 'Amos': 'Amos', 'Obadiah': 'Obad', 
                'Jonah':'Jonah', 'Micah': 'Mic', 'Nahum': 'Nahum', 'Habakkuk': 'Hab', 'Zephaniah': 'Zep', 'Haggai': 'Hag', 'Zechariah': 'Zec',
                'Malachi': 'Mal', 'Matthew': 'Mat', 'Mark': 'Mar', 'Luke': 'Luke', 'John': 'John', 'Acts': 'Acts', 'Romans': 'Rom', 
                '1 Corinthians': '1Cor', '2 Corinthians': '2Cor', 'Galatians': 'Gal', 'Ephesians': 'Eph', 'Philippians': 'Phi', 'Colossians': 'Col', 
                '1 Thessalonians': '1Th', '2 Thessalonians': '2Th', '1 Timothy': '1Tim', '2 Timothy': '2Tim', 'Titus': 'Titus', 'Philemon': 'Phmn', 
                'Hebrews': 'Heb', 'James': 'Jas', '1 Peter': '1Pet', '2 Peter': '2Pet', '1 John': '1Jn', '2 John': '2Jn', '3 John': '3Jn', 'Jude': 'Jude', 
                'Revelation': 'Rev'}
        
        verse_split = verse.split()
        
        if len(verse_split) > 1:
            if verse_split[0].isdigit():
                book = f'{verse_split[0]} {verse_split[1]}'
                ch_vr = verse_split[2]
            else:
                book = verse_split[0]
                ch_vr = verse_split[1]
            
            for key in books:
                if key == book:
                    verse = books[key]
                    verse += ch_vr
                else:
                    pass
        else:
            pass

        return verse

    @client.event
    async def on_ready():
        """prints message when login and connection is successful (bot is up and running)"""
        await tree.sync(guild=None)
        print("Reddy")
        print("-------------")

    @tree.command(name="henlo", guild=None)
    async def henlo(interaction):
        """Responds with fren to command /henlo"""
        await interaction.response.send_message("fren")

    @tree.command(name="fren", guild=None)
    async def fren(interaction):
        """Responds with henlo to command /fren"""
        await interaction.response.send_message("henlo")

    @tree.command(name="repost", guild=None)
    async def repost(interaction: discord.Interaction, mess: str):
        """Reposts posted message after /repost"""
        await interaction.response.send_message(mess)

    @tree.command(name="frog", guild=None)
    async def frog(interaction):
        """Responds with :frog: to command /frog"""
        await interaction.response.send_message("🐸")

    @tree.command(name="startfrog", guild=None)
    async def start(interaction):
        """Begins reacting to every message with :frog:"""
        await interaction.response.send_message("Going froggie mode 🐸")
        begin()

    @tree.command(name="stopfrog", guild=None)
    async def stop(interaction):
        """Stops reacting to every message with :frog:"""
        await interaction.response.send_message("Going sleepy mode 😴")
        fin()

    @tree.command(name="archivefrog", guild=None)
    async def readwrite(interaction):
        """Reads and write every message in channel to archive.txt"""
        await interaction.response.send_message("Archiving 🐸")
        global check
        check = True

        global outfile
        outfile = open('archive.txt', 'a', encoding='utf-8')

    @tree.command(name="noarchivefrog", guild=None)
    async def end(interaction):
        """Stops archiving messages"""
        await interaction.response.send_message("Not archiving 😔")
        global check
        check = False

        global outfile
        outfile.close()

    @tree.command(name="allarchivefrog", guild=None)
    async def arc(interaction):
        """Archives all messages"""
        global outfile
        outfile = open('archive.txt', 'a', encoding='utf-8')

        await archive_all(interaction, outfile)

    @tree.command(name="showarchive", guild=None)
    async def show_arc(interaction):
        """Sends message with archive file"""
        await interaction.response.send_message(file=discord.File('archive.txt'))

    @tree.command(name="erasearchive", guild=None)
    async def erase_archive(interaction):
        """Erases contents of archive"""
        archive = open('archive.txt', 'w')
        archive.write('')
        archive.close()
        await interaction.response.send_message('Archive erased')

    @tree.command(name="help", guild=None)
    async def list_commands(interaction):
        """Displays list of commands"""
        await interaction.response.send_message("/henlo - responds 'fren'\n/fren - responds 'henlo'\n"
                                                "/frog - sends :frog:\n/startfrog - bots reacts to each messages with"
                                                " :frog:\n/stopfrog - bot stops reacting to each message\n"
                                                "/repost - sends the message you input\n/archivefrog - archives"
                                                " every message sent after this command\n/noarchivefrog - stops"
                                                " archiving every message sent\n/allarchivefrog - archives all"
                                                " messages in the channel\n/showarchive - sends archive text file\n"
                                                "/erasearchive - erases archive contents\n"
                                                "/verse - responds with inputted Bible verse or verses\n/randomverse - "
                                                "responds with a random Bible verse")

    @tree.command(name="verse", guild=None)
    async def verse(interaction: discord.Interaction, verse: str):
        """Responds with entered verse"""
        
        try:
            bible = open('holybible.txt', 'r')
            found = False
            verse = adaptor(verse)
            verse = verse.replace(" ", "")
            verse = verse.lower()
            verses_split = verse.split('-')
            output = f''

            await interaction.response.send_message('Searching. . .')

            if '-' in verse:
                for line in bible:
                    line_list = line.split()
                    location = line_list[0]
                    location_split = location.split(':')
                    verse = int(verses_split[1])
                    current_verse = int(location_split[1])
                    search_verse = verses_split[0].split(':')

                    if search_verse[0].lower() == location_split[0].lower() and int(search_verse[1]) <= current_verse \
                            <= verse:
                        if output == '':
                            output += line
                        else:
                            output += location_split[1] + line.lstrip(location)
                        found = True

                if found and len(output) < 2000:
                    await interaction.edit_original_response(content=output)

                elif len(output) > 2000:
                    await interaction.followup.send('Cannot send message, too long')
                else:
                    await interaction.followup.send('Verse not found (maybe you typed it wrong)')


            else:
                for line in bible:
                    line_list = line.split()
                    location = line_list[0].lower()

                    if location == verse:
                        await interaction.edit_original_response(content=line)
                        found = True

                if not found:
                    await interaction.followup.send('Verse not found (maybe you typed it wrong)')

            bible.close()

        except TypeError as err:
            await interaction.followup.send('Error: Maybe you typed something wrong.')
            print(err)

        except IndexError as err:
            await interaction.followup.send('Error: Maybe you typed something wrong.')
            print(err)

        except:
            await interaction.followup.send('Error: Maybe you typed something wrong.')

    @tree.command(name="randomverse", guild=None)
    async def random_verse(interaction):
        """Responds with a random verse"""
        bible = open('holybible.txt', 'r')
        ran_verse = random.randint(0, 31103)
        bible_list = bible.readlines()

        await interaction.response.send_message(bible_list[ran_verse])

        bible.close()

    async def archive_all(para, file):
        """archives each message in a channel"""
        await para.response.send_message("Archiving all messages in channel . . .")

        async for message in para.channel.history(limit=None, oldest_first=True):
            try:

                print(f'{str(message.attachments)}:{str(message.created_at)}:{str(message.channel)}:'
                      f'{str(message.author)}:{str(message.content)}')

                file.write(f'|{str(message.attachments)}:{str(message.created_at)}:{str(message.channel)}:'
                           f'{str(message.author)}:{str(message.content)}|\n')

            except UnicodeEncodeError:
                print('Unicode encoding error')
            except ValueError:
                print('Error converting message to string')
            except:
                print('Error')

        await para.edit_original_response(content='Done!')

        file.close()
        print('All messages archived and saved')

    @client.event
    async def on_message(message):
        """for each message, if val add reaction frog if check, archive message"""
        if val:
            await message.add_reaction('🐸')

        if check:
            try:
                print('archiving...')

                print(f'{str(message.attachments)}:{str(message.created_at)}:{str(message.channel)}:'
                      f'{str(message.author)}:{str(message.content)}')

                outfile.write(f'|{str(message.attachments)}:{str(message.created_at)}:{str(message.channel)}:'
                              f'{str(message.author)}:{str(message.content)}|\n')

                await message.add_reaction('📚')

            except UnicodeEncodeError as err:
                print(err)
                print('Error writing emoji')
            except ValueError:
                print('Error converting message to string')
            except:
                print('Error')

    # run at program exit
    atexit.register(exit_handler)

    client.run(TOKEN)


if __name__ == '__main__':
    main()
