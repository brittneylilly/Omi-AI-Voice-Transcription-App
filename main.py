from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


#Instance of the app
app = FastAPI()
# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

#old webhook
@app.post("/webhook")
def webhook(uid: str, transcript: dict):
    print(transcript)

    # Hint: The transcript contains segments with text data
    # Hint: Access the latest segment with transcript["segments"][-1]["text"]
    # Hint: Return a dictionary with a "message" key and the value being the notification message

    # Task: Implement keyword detection and response logic of your choice
    # example: if the word "tired" is mentioned, return a message notifying the user to take a break

    # TODO: Write your code below this line

#new webhook
@app.post('/livetranscript')
def webhook(memory: dict, uid: str):
    print(memory)
    print(uid)
    return {"message": "we got it"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
