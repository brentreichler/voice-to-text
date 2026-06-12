from faster_whisper import WhisperModel
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

audio_file = project_root / "audio" / "sample.m4a"

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

segments, info = model.transcribe(audio_file)

transcript = []

for segment in segments:
    transcript.append(segment.text)

full_text = "\n".join(transcript)

output_file = project_root / "output" / "sample.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(full_text)

print("Transcription saved.")
