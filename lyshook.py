# MIT License

# Copyright (c) 2024 sjlazaridis

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys
import requests
import threading
import time
from colorama import Fore, init
from dhooks import Webhook, Embed
import discord
import json

# Initialize colorama
init(autoreset=True)

# Global variable to store message counts for each webhook URL
message_count = {}

# Helper functions

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def setTitle(title):
    os.system(f'title {title}' if os.name == 'nt' else f'echo -n -e "\033]0;{title}\007"')

def transition():
    clear()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Loading...\n")
    time.sleep(1)

def print_logo():
    print(f"""{Fore.RED}

 ▄█       ▄██   ▄      ▄████████    ▄█    █▄     ▄██████▄   ▄██████▄     ▄█   ▄█▄ 
███       ███   ██▄   ███    ███   ███    ███   ███    ███ ███    ███   ███ ▄███▀ 
███       ███▄▄▄███   ███    █▀    ███    ███   ███    ███ ███    ███   ███▐██▀   
███       ▀▀▀▀▀▀███   ███         ▄███▄▄▄▄███▄▄ ███    ███ ███    ███  ▄█████▀    
███       ▄██   ███ ▀███████████ ▀▀███▀▀▀▀███▀  ███    ███ ███    ███ ▀▀█████▄    
███       ███   ███          ███   ███    ███   ███    ███ ███    ███   ███▐██▄   
███▌    ▄ ███   ███    ▄█    ███   ███    ███   ███    ███ ███    ███   ███ ▀███▄ 
█████▄▄██  ▀█████▀   ▄████████▀    ███    █▀     ▀██████▀   ▀██████▀    ███   ▀█▀ 
▀                                                                       ▀         

{Fore.RESET}""")

def main():
    try:
        while True:
            clear()
            setTitle("Webhook Menu")
            print_logo()
            print(f"""{Fore.YELLOW}[{Fore.RED}+{Fore.YELLOW}]{Fore.WHITE} WebHooks Tools:      
          
          {Fore.YELLOW}[{Fore.WHITE}1{Fore.YELLOW}]{Fore.WHITE} Spammer                   {Fore.YELLOW}[{Fore.WHITE}7{Fore.YELLOW}]{Fore.WHITE} Name Changer 
          
          {Fore.YELLOW}[{Fore.WHITE}2{Fore.YELLOW}]{Fore.WHITE} Remover                   {Fore.YELLOW}[{Fore.WHITE}8{Fore.YELLOW}]{Fore.WHITE} Poll Creator
          
          {Fore.YELLOW}[{Fore.WHITE}3{Fore.YELLOW}]{Fore.WHITE} Check Validity            {Fore.YELLOW}[{Fore.WHITE}9{Fore.YELLOW}]{Fore.WHITE} Delete all Messages (Patched)
          
          {Fore.YELLOW}[{Fore.WHITE}4{Fore.YELLOW}]{Fore.WHITE} WebHook Details           {Fore.YELLOW}[{Fore.WHITE}10{Fore.YELLOW}]{Fore.WHITE} Exit
          
          {Fore.YELLOW}[{Fore.WHITE}5{Fore.YELLOW}]{Fore.WHITE} Avatar Changer
          
          {Fore.YELLOW}[{Fore.WHITE}6{Fore.YELLOW}]{Fore.WHITE} Embed Maker
    """)  # add a space after the triple quotes for better spacing

            choice = input(f"""{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Choice: """)

            if choice == '1':
                transition()
                webhook_spam()
            elif choice == '2':
                transition()
                webhook_remover()
            elif choice == '3':
                transition()
                check_webhook_validity()
            elif choice == '4':
                transition()
                webhook_details_extended()
            elif choice == '5':
                transition()
                avatar_changer()
            elif choice == '6':
                transition()
                create_embed()
            elif choice == '7':
                transition()
                name_changer()
            elif choice == '8':
                transition()
                create_poll_menu()
            elif choice == '9':
                transition()
                delete_all_messages_menu()
            elif choice == '10':
                print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Exiting program.")
                sys.exit(0)
            else:
                print_invalid_choice_message()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Exiting program.")
        sys.exit(0)



def delete_messages(webhook_url, delete_all=False):
    try:
        if delete_all:
            # Delete all messages on the channel
            response = requests.delete(f"{webhook_url}/messages")
            if response.status_code == 204:
                print(f"{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}✓{Fore.YELLOW}]{Fore.WHITE} All messages deleted successfully.")
            else:
                print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}✗{Fore.YELLOW}]{Fore.WHITE} Failed to delete all messages. Status code: {response.status_code}")
        else:
            print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}✗{Fore.YELLOW}]{Fore.WHITE} Invalid operation. Please choose to delete all messages.")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}✗{Fore.YELLOW}]{Fore.WHITE} Failed to delete messages. Error: {e}")

def delete_all_messages_menu():
    clear()
    setTitle("Delete All Messages")
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to delete all messages ")
    webhook_url = input(f"""{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} WebHook URL: """)

    confirm = input(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Are you sure you want to delete all messages on the channel? (y/n): ")

    if confirm.lower() == 'y':
        delete_messages(webhook_url, delete_all=True)
    else:
        print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Operation canceled.")

    input(f"\n{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")

def create_poll_menu():
    clear()
    setTitle("Poll Creator")
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to send the poll message ")
    webhook_url = input(f"""{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} WebHook URL: """)
    
    print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the question for the poll ")
    question = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Question: ")

    options = []
    while True:
        option = input(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter an option for the poll (or 'done' to finish): ")
        if option.lower() == 'done':
            break
        options.append(option)

    create_poll(webhook_url, question, options)  # Call create_poll with user inputs
    input(f"\n{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")

def create_poll(webhook_url, question, options):
    # Prepare the poll message
    poll_message = f"**{question}**\n\n"

    # Prepare the options with reactions (up to 10 options)
    reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']

    for i, option in enumerate(options):
        poll_message += f"{reactions[i]} {option}\n"

    # Prepare JSON payload for the webhook message
    payload = {
        "content": poll_message
    }

    # Send POST request to the webhook URL
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

        if response.status_code == 204:
            print(f"{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Poll created successfully.")
        else:
            print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Failed to create poll. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Failed to create poll. Error: {e}")

# Webhook spammer function
def webhook_spam():
    clear()
    setTitle("WebHook Spammer")
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to spam ")
    webhook_url = input(f"""{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} WebHook URL: """)
    
    try:
        webhook = Webhook(webhook_url)
    except Exception as e:
        print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Invalid WebHook URL: {e}")
        time.sleep(2)
        return

    print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the message to spam ")
    message = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Message: ")
    print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Amount of messages to send ")
    amount = int(input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Amount: "))

    def spam():
        for _ in range(amount):
            try:
                webhook.send(message)
                update_message_count(webhook_url)
                print(f"{Fore.YELLOW}[{Fore.WHITE}Sent.{Fore.YELLOW}]")
            except requests.exceptions.HTTPError as ex:
                print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Failed to send message: {ex}")
            time.sleep(1)  # Default delay of 1 second between each message

    spam_thread = threading.Thread(target=spam)
    spam_thread.start()

    clear()
    print(f"{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Webhook spamming has started")
    input(f"\n{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")

def update_message_count(webhook_url):
    if webhook_url in message_count:
        message_count[webhook_url] += 1
    else:
        message_count[webhook_url] = 1

def webhook_remover():
    try:
        setTitle("WebHook Remover")
        clear()
        print_logo()
        print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook you want to delete ")
        webhook = input(f"""{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} WebHook Link: """)
        response = requests.delete(webhook.rstrip())
        if response.status_code == 204:
            print(f"\n{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Webhook has been deleted")
        else:
            print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Webhook could not be deleted")
        input(f"\n{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")
    except Exception as e:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Webhook could not be deleted. Error: {e}")
        input(f"\n{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")

def check_webhook_validity():
    clear()
    setTitle("WebHook Validity Checker")
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to check its validity ")
    webhook = input(f"""{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} WebHook URL: """)
    
    try:
        response = requests.get(webhook)
        if response.status_code == 200:
            print(f"\n{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Webhook is valid")
        else:
            print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Webhook is invalid")
    except Exception as e:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error checking Webhook validity: {e}")
    input(f"\n{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")

def webhook_details_extended():
    clear()
    setTitle("WebHook Details")
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to view its details ")
    webhook = input(f"""{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} WebHook URL: """)

    try:
        response = requests.get(webhook)
        if response.status_code == 200:
            details = response.json()
            avatar_url = f"https://cdn.discordapp.com/avatars/{details['id']}/{details['avatar']}.png" if details['avatar'] else "No Avatar"

            print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook Name: {details['name']}")
            print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook Channel ID: {details['channel_id']}")
            print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook Guild ID: {details['guild_id']}")
            print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook ID: {details['id']}")
            print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook Avatar: {avatar_url}")
            print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook Token: {details['token']}")
            print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook Application ID: {details['application_id']}")
            print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook URL: {details['url']}")
        else:
            print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Invalid WebHook URL")
    except Exception as e:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error fetching WebHook details: {e}")
    input(f"\n{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")

def avatar_changer():
    clear()
    setTitle("WebHook Avatar Changer")
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to change its avatar ")
    webhook_url = input(f"""{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} WebHook URL: """)

    try:
        webhook = Webhook(webhook_url)
        print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the path to the new avatar image ")
        image_path = input(f"""{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Image Path: """)

        with open(image_path, 'rb') as f:
            webhook.modify(avatar=f.read())

        print(f"\n{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} WebHook avatar changed successfully")
        input(f"\n{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")
    except Exception as e:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error changing WebHook avatar: {e}")
        input(f"\n{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")

def create_embed():
    clear()
    setTitle("Embed Maker")
    print_logo()

    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Let's create a custom embed message:\n")

    # Prompt user for embed details
    title = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Enter the title of the embed: ")
    description = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Enter the description of the embed: ")
    color = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Enter the color of the embed in hex format (e.g., ff0000 for red): ")
    url = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} (Optional) URL that will be linked when the embed's title is clicked: ")
    thumbnail = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} (Optional) Enter the URL for the thumbnail: ")
    footer_text = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} (Optional) Enter the footer text: ")
    footer_icon = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} (Optional) Enter the URL for the footer icon: ")
    image_url = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} (Optional) Enter the URL for the large image (banner): ")
    author_name = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} (Optional) Enter the author name: ")
    author_icon = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} (Optional) Enter the URL for the author icon: ")

    embed = Embed()
    embed.title = title
    embed.description = description

    # Convert color input to integer
    try:
        color = int(color.replace('#', '0x'), 16)  # Convert hex string to integer
    except ValueError:
        print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Invalid color format. Using default color.")
        color = 0x00FF00  # Default to green if input is invalid

    embed.color = color

    if url:
        embed.url = url

    if thumbnail:
        embed.set_thumbnail(thumbnail)

    if footer_text or footer_icon:
        embed.set_footer(text=footer_text, icon_url=footer_icon)

    if image_url:
        embed.set_image(image_url)

    if author_name or author_icon:
        embed.set_author(name=author_name, icon_url=author_icon)

    try:
        # Send the embed message
        webhook_url = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to send the embed message: ")
        webhook = Webhook(webhook_url)
        webhook.send(embed=embed)

        print(f"\n{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Embed message sent successfully")
    except Exception as e:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error sending embed message: {e}")

    input(f"\n{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")


def name_changer():
    clear()
    setTitle("WebHook Name Changer")
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to change its name ")
    webhook_url = input(f"""{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} WebHook URL: """)
    
    try:
        webhook = Webhook(webhook_url)
        print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter new name for the WebHook ")
        new_name = input(f"{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} New Name: ")

        webhook.modify(name=new_name)

        print(f"\n{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} WebHook name changed successfully")
        input(f"\n{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")
    except Exception as e:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error changing WebHook name: {e}")
        input(f"\n{Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")

# Main entry point
if __name__ == "__main__":
    main()
