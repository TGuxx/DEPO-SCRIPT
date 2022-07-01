from discordwebhook import Discord
import pyautogui

#DC WEBHOOK
WEBHOOK = "<INSERT YOUR WEBHOOKHERE>"

#COLORS
IAM_READY_COLOR = (0,199,77) #BRIGHT GREEN COLOR

#POSITIONS
CLICK_POS = (1050,750)

#DISCORD NOTIFICATION
def SEND_NOTIFICATION():
    discord = Discord(url=WEBHOOK)
    discord.post(
        embeds=[
            {
                "title": "READY TO DELIVER",
            }
        ],
    )

#MAIN LOOP
def main():
    while True:
       #SCREENSHOT OF A SCREEN
       sc = pyautogui.screenshot();

       #CHECKING PHASE
       pixel_check = sc.getpixel(CLICK_POS)
       if pixel_check == (IAM_READY_COLOR):
           pyautogui.click(CLICK_POS)
           SEND_NOTIFICATION()
main()
