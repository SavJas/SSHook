import os
import sys
import requests
import threading
import time
from colorama import Fore, init
from dhooks import Webhook, Embed

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
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Transitioning...\n")
    time.sleep(1)

def print_logo():
    print(f"""{Fore.BLUE}
▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·  ▄ .▄            ▄ •▄     ▄▄▄▄▄            ▄▄▌  
██· █▌▐█▀▄.▀·▐█ ▀█▪██▪▐█▪     ▪     █▌▄▌▪    •██  ▪     ▪     ██•  
██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄██▀▐█ ▄█▀▄  ▄█▀▄ ▐▀▀▄·     ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  
▐█▌██▐█▌▐█▄▄▌██▄▪▐███▌▐▀▐█▌.▐▌▐█▌.▐▌▐█.█▌     ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌
 ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀ ▀▀▀ · ▀█▄▀▪ ▀█▄▀▪·▀  ▀     ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  
{Fore.RESET}""")

def main():
    try:
        while True:
            clear()
            setTitle("Webhook Menu")
            print_logo()
            print(f"""{Fore.YELLOW}[{Fore.BLUE}+{Fore.YELLOW}]{Fore.WHITE} WebHooks Tools:
    \n          {Fore.YELLOW}[{Fore.WHITE}1{Fore.YELLOW}]{Fore.WHITE} Spammer
    \n          {Fore.YELLOW}[{Fore.WHITE}2{Fore.YELLOW}]{Fore.WHITE} Remover
    \n          {Fore.YELLOW}[{Fore.WHITE}3{Fore.YELLOW}]{Fore.WHITE} Check Validity
    \n          {Fore.YELLOW}[{Fore.WHITE}4{Fore.YELLOW}]{Fore.WHITE} WebHook Details
    \n          {Fore.YELLOW}[{Fore.WHITE}5{Fore.YELLOW}]{Fore.WHITE} Avatar Changer
    \n          {Fore.YELLOW}[{Fore.WHITE}6{Fore.YELLOW}]{Fore.WHITE} Embed Maker
    \n          {Fore.YELLOW}[{Fore.WHITE}7{Fore.YELLOW}]{Fore.WHITE} Name Changer
    \n          {Fore.YELLOW}[{Fore.WHITE}8{Fore.YELLOW}]{Fore.WHITE} Bulk Sender
    \n""")
            choice = input(f"""{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Choice: """)

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
                bulk_message_sender()
            else:
                clear()
                print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Invalid choice. Please choose from 1 to 7.")
                time.sleep(2)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Exiting program.")
        sys.exit(0)

def name_changer():
    clear()
    setTitle("WebHook Name Changer")
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to change its name ")
    webhook_url = input(f"""{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} WebHook URL: """)
    
    try:
        webhook = Webhook(webhook_url)
        print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter new name for the WebHook ")
        new_name = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} New Name: ")

        webhook.modify(name=new_name)

        print(f"\n{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} WebHook name changed successfully")
        input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")
    except Exception as e:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error changing WebHook name: {e}")
        input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")


def bulk_message_sender():
    setTitle("Bulk Message Sender")
    clear()
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to send a .txt file as some messages ")
    webhook_url = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} WebHook Link: ")

    try:
        webhook = Webhook(webhook_url)
    except Exception as e:
        print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Invalid WebHook URL: {e}")
        time.sleep(2)
        return

    print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the path to the text file with messages ")
    file_path = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} File Path: ")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            messages = file.readlines()
    except FileNotFoundError:
        print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} File not found. Please check the path.")
        input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")
        return

    print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Number of messages found: {len(messages)}\n")




def webhook_spam():
    setTitle("WebHook Spammer")
    clear()
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook you want to spam ")
    webhook_url = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} WebHook Link: ")

    try:
        webhook = Webhook(webhook_url)
    except Exception as e:
        print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Invalid WebHook URL: {e}")
        time.sleep(2)
        return

    print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the message to spam ")
    message = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Message: ")
    print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Amount of messages to send ")
    amount = int(input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Amount: "))

    def spam():
        nonlocal webhook_url
        for _ in range(amount):
            webhook.send(message)
            update_message_count(webhook_url)
            time.sleep(1)  # Default delay of 1 second between each message
            print(f"{Fore.YELLOW}[{Fore.WHITE}Sent.{Fore.YELLOW}]")

    spam_thread = threading.Thread(target=spam)
    spam_thread.start()

    clear()
    print(f"{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Webhook spamming has started")
    input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")

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
        webhook = input(f"""{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} WebHook Link: """)
        response = requests.delete(webhook.rstrip())
        if response.status_code == 204:
            print(f"\n{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Webhook has been deleted")
        else:
            print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Webhook could not be deleted")
        input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")
    except Exception as e:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Webhook could not be deleted. Error: {e}")
        input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")

def check_webhook_validity():
    clear()
    setTitle("WebHook Validity Checker")
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to check its validity ")
    webhook = input(f"""{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} WebHook URL: """)
    
    try:
        response = requests.get(webhook.rstrip())
        if response.status_code == 200:
            print(f"\n{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Webhook is valid")
        else:
            print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Webhook is invalid")
            
        input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")
    except Exception as e:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error checking webhook validity: {e}")
        input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")

    main()

def webhook_details_extended():
    clear()
    setTitle("Extended WebHook Details")
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to fetch extended details ")
    webhook = input(f"""{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} WebHook URL: """)

    try:
        response = requests.get(webhook.rstrip())
        if response.status_code == 200:
            webhook_data = response.json()
            print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook ID       : {webhook_data.get('id')}")
            print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook Guild ID : {webhook_data.get('guild_id')}")
            print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook Channel ID: {webhook_data.get('channel_id')}")
            print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook Token    : {webhook_data.get('token')}")
            print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook Name     : {webhook_data.get('name')}")

            # Display the avatar image if available
            if 'avatar' in webhook_data:
                avatar_url = f"https://cdn.discordapp.com/avatars/{webhook_data['id']}/{webhook_data['avatar']}"
                print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook Avatar   : {avatar_url}")
            else:
                print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook Avatar   : Not set")

            # Fetch and display user details if available
            if 'user' in webhook_data and webhook_data['user']:
                user = webhook_data['user']
                print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} WebHook User     : {user.get('username', 'N/A')}#{user.get('discriminator', 'N/A')}")

        else:
            print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Failed to fetch extended details. Status code: {response.status_code}")

        input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")
    except Exception as e:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error fetching extended webhook details: {e}")

    main()


def avatar_changer():
    clear()
    setTitle("WebHook Avatar Changer")
    print_logo()
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to change its avatar ")
    webhook_url = input(f"""{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} WebHook URL: """)

    try:
        webhook = Webhook(webhook_url)
        print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter new avatar image file path or URL ")
        avatar_path = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Avatar Path/URL: ")

        if avatar_path.startswith('http'):
            # If it's a URL, download the image
            response = requests.get(avatar_path)
            avatar_data = response.content
        else:
            # Otherwise, treat it as a local file path
            with open(avatar_path, 'rb') as avatar_file:
                avatar_data = avatar_file.read()

        # Set the new avatar
        webhook.modify(avatar=avatar_data)

        print(f"\n{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Avatar changed successfully")
        input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")
    except Exception as e:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error changing avatar: {e}")
        input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")


def create_embed():
    clear()
    setTitle("Embed Maker")
    print_logo()

    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Let's create a custom embed message:\n")

    # Prompt user for embed details
    title = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Enter the title of the embed: ")
    description = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Enter the description of the embed: ")
    color = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Enter the color of the embed in hex format (e.g., 0xFF0000 for red): ")
    url = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} (Optional) URL that will be linked when the embed's title is clicked: ")
    thumbnail = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} (Optional) Enter the URL for the thumbnail: ")
    footer_text = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} (Optional) Enter the footer text: ")
    footer_icon = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} (Optional) Enter the URL for the footer icon: ")
    image_url = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} (Optional) Enter the URL for the large image (banner): ")
    author_name = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} (Optional) Enter the author name: ")
    author_icon = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} (Optional) Enter the URL for the author icon: ")

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
        webhook_url = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Enter the WebHook URL to send the embed message: ")
        webhook = Webhook(webhook_url)
        webhook.send(embed=embed)

        print(f"\n{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Embed message sent successfully")
    except Exception as e:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error sending embed message: {e}")

    input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")



if __name__ == "__main__":
    main()

