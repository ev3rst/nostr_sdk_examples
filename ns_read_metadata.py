# requires nostr_sdk 0.32.2
# last version 0.39 will crash
# usage example: python ns_read_metadata.py npub1mwce4c8qa2zn9zw9f372syrc9dsnqmyy3jkcmpqkzaze0slj94dqu6nmwy
import asyncio, argparse, json
from nostr_sdk import Metadata, Client, NostrSigner, Keys, Filter, PublicKey, Kind
from datetime import timedelta
 
async def main(npub):
    client = Client()
    await client.add_relay("wss://relay.damus.io")
    await client.connect()
    pk = PublicKey.from_bech32(npub)
    print(f"Getting profile metadata for {npub}:")
    f = Filter().kind(Kind(0)).author(pk).limit(1)
    events = await client.get_events_of([f], timedelta(seconds=15))
    if events:
        event = events[0]
        metadata_dict = json.loads(event.content())
        for key, value in metadata_dict.items():
            print(f"{key}: {value}")
    else:
        print("Could not retrieve metadata for the given public key.")
         
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch all metadata for a given npub')
    parser.add_argument('npub', type=str, help='The npub of the user')
    args = parser.parse_args()
    asyncio.run(main(args.npub))
