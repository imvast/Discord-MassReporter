from tls_client import Session
from terminut import printf as print, inputf as input
from os import system; system('cls||clear')

print("\t> Vast Reporter <\n", showTimestamp=False)

client = Session(client_identifier="discord_1_0_9013", random_tls_extension_order=True)

token = input("Token > ")
channelid = input("ChannelID > ")
messageid = input("MsgID > ")

headers = {
    'authority': 'discord.com',
    'accept': '*/*',
    'accept-language': 'en-US',
    'authorization': token,
    'content-type': 'application/json',
    'origin': 'https://discord.com',
    'referer': 'https://discord.com/channels/@me',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9013 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-discord-timezone': 'America/New_York',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDEzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMTMgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMiBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMjIuMy4yIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTk5Njg2LCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMjI2NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
}

payload = {
    "version":"1.0",
    "variant":"3",
    "language":"en",
    "breadcrumbs":[3,31],
    "elements":{},
    "name":"message",
    "channel_id":channelid,
    "message_id":messageid
}
amt=0
for _ in range(5):
    response = client.post('https://discord.com/api/v9/reporting/message', headers=headers, json=payload)
    if "Missing Access" in response.text:
        print("Missing Access.")
        break
    if "report_id" in response.text:
        amt+=1
        print(f"(+) Report Sent. [{amt}]")
    else:
        print(response.text); break
