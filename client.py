import asyncio
import websockets

# Define the WebSocket client
async def client_handler():
    uri = "ws://<server-ip>:8080"  # Replace with the server's IP
    async with websockets.connect(uri) as websocket:
        print("Connected to server.")
        
        # Send a message to the server
        await websocket.send("Hello from the client!")
        
        # Receive and print a response from the server
        response = await websocket.recv()
        print(f"Received from server: {response}")

# Run the client
asyncio.run(client_handler())
