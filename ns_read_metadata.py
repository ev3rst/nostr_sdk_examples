# requires nostr_sdk 0.32.2
# last version 0.39 will crash
# usage example: python ns_read_metadata.py npub1mwce4c8qa2zn9zw9f372syrc9dsnqmyy3jkcmpqkzaze0slj94dqu6nmwy
# ns_read_metadata.py
# version 3
import asyncio, argparse, json
from nostr_sdk import Metadata, Client, NostrSigner, Keys, Filter, PublicKey, Kind
from datetime import timedelta
 
async def main(npub):
    client = Client()
    await client.add_relay("wss://relay.damus.io")
    await client.connect()
    pk = PublicKey.parse(npub)
    print(f"\nGetting profile metadata for {npub}:")
    metadata = await client.fetch_metadata(pk, timedelta(seconds=15))
    print(metadata)
         
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch all metadata for a given npub')
    parser.add_argument('npub', type=str, help='The npub of the user')
    args = parser.parse_args()
    asyncio.run(main(args.npub))

