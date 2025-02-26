# test with 0.39
# working
import asyncio
from nostr_sdk import Client, NostrSigner, Keys, PublicKey, init_logger, LogLevel

async def send_direct_message(nsec, recipient_npub, message):
    init_logger(LogLevel.INFO)
    sender_keys = Keys.parse(nsec)
    sender_client = NostrSigner.keys(sender_keys)
    client = Client(sender_client)
    public_key = sender_keys.public_key()
    print(f"From Public key (npub): {public_key.to_bech32()}")       
    await client.add_relay("wss://relay.damus.io")
    await client.connect()

    print(f"to Public key (npub): {recipient_npub}")  
    await client.send_private_msg(PublicKey.parse(recipient_npub), message, [])
    await asyncio.sleep(10)
    print(f"Message sent")

if __name__ == '__main__':
    nsec = "nsec1 ... replace with your nsec"
    recipient_npub = "npub ... replace with npub to send dm"
    message = "Hello there, this is the message!"
    asyncio.run(send_direct_message(nsec, recipient_npub, message))

