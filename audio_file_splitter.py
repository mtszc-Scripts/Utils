import sys
from pydub import AudioSegment


def parse_timestamp(timestamp: str) -> int:
    """
    Convert timestamp in MM:SS format to seconds
    :param timestamp: str
    :return: int
    """
    minutes, seconds = map(int, timestamp.split(':'))
    return minutes * 60 + seconds


def cut_audio(input_file, timestamps):
    audio = AudioSegment.from_file(input_file)
    total_duration = len(audio) / 1000  # Total duration in seconds

    for i, timestamp in enumerate(timestamps):
        start_time = parse_timestamp(timestamp)
        end_time = parse_timestamp(timestamps[i + 1]) if i + 1 < len(timestamps) else total_duration

        # Convert timestamps to milliseconds
        start_ms = int(start_time * 1000)
        end_ms = int(end_time * 1000)

        # Cut the audio and export
        segment = audio[start_ms:end_ms]
        output_file = f"{i + 1:02d}.mp3"
        segment.export(output_file, format="mp3")
        print(f"Segment {i + 1} exported to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python cut_audio.py <input_file> <timestamp1> <timestamp2> ...")
        sys.exit(1)

    input_file = sys.argv[1]
    timestamps = sys.argv[2:]

    cut_audio(input_file, timestamps)
