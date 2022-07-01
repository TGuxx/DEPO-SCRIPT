from discordwebhook import Discord
import pyautogui

#DC WEBHOOK (Use your own webhook)
WEBHOOK = "https://discord.com/api/webhooks/992425649740455937/Qa5IIsnaOHlG56IdfsB23JeoDF65-CKMIJ-18d_q87KI1J_MOwIQ3QAH0tmDqYesIWIF"

#COLORS
IAM_READY_COLOR = (0,199,77) #BRIGHT GREEN COLOR

#POSITIONS
CLICK_POS = (1050,750)

#DISCORD NOTIFICATION
def SEND_NOTIFICATION():
    discord = Discord(url=WEBHOOK)
    discord.post(content="YOUR ITEM IS READY TO BE DELIVERED")

#MAIN LOOP
def main():
    while True:
       #SCREENSHOT OF A SCREEN
       sc = pyautogui.screenshot();

       #CHEKING PHASE
       pixel_check = sc.getpixel(CLICK_POS)
       if pixel_check == (IAM_READY_COLOR):
           pyautogui.click(CLICK_POS)
           SEND_NOTIFICATION()
main()
