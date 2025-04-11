import whisper
from langchain.chat_models import ChatOpenAI

class VoiceAgent:
    def __init__(self):
        """
        Initializes the VoiceAgent with a Whisper model for transcription
        and a ChatOpenAI model for generating responses.
        """
        self.model = whisper.load_model("base")
        self.llm = ChatOpenAI()

    def transcribe_and_respond(self, audio_file_path):
        """
        Transcribes an audio file and generates a response.

        Args:
            audio_file_path (str): The path to the audio file to transcribe.

        Returns:
            str: The generated response based on the transcribed text.
        """
        # Transcribe the audio file
        result = self.model.transcribe(audio_file_path)
        # Generate a response using the transcribed text
        response = self.llm.predict(f"Respond to: {result['text']}")
        return response

if __name__ == "__main__":
    # Example usage
    agent = VoiceAgent()
    response = agent.transcribe_and_respond("sample_audio.wav")
    print(f"Generated Response: {response}")