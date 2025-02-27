from nostr_sdk import Metadata, Client, Keys, Filter, Kind, KindStandard, Contact, PublicKey, EventBuilder
from datetime import timedelta
import asyncio

async def main():
    keys = Keys.parse("nsec_key")
    client = Client()
    await client.add_relay("wss://relay.damus.io")
    await client.connect()
    
    # Get current contact list
    f = Filter().author(keys.public_key()).kind(Kind.from_std(KindStandard.CONTACT_LIST))
    events = await client.fetch_events(f, timedelta(seconds=10))
    event = events.first()

    if event:
        # Get current contact public keys and add a new contact
        public_keys = event.tags().public_keys()
        new_public_key = PublicKey.parse("npub_to_follow")
        public_keys.append(new_public_key)
        
        # Create a new contact list event and send it to relays
        contacts = [Contact(public_key=pk, relay_url=None, alias=None) for pk in public_keys]
        event = EventBuilder.contact_list(contacts).sign_with_keys(keys)
        await client.send_event(event)
        print(f"Added follow to: {new_public_key}")
    else:
        print("No contact list found")

if __name__ == '__main__':
    asyncio.run(main())
