import asyncio
import websockets

# Define the WebSocket server handler
async def server_handler(websocket, path):
    print("A client connected.")
    try:
        async for message in websocket:
            print(f"Received from client: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.ConnectionClosed:
        print("Client disconnected.")

# Start the server
async def start_server():
    server = await websockets.serve(server_handler, "0.0.0.0", 8080)  # Listen on all network interfaces
    print("WebSocket server started on ws://<server-ip>:8080")
    await server.wait_closed()

# Run the server
asyncio.run(start_server())
