import random
from pydub import AudioSegment


def insert_random_cuts_with_silence(
    input_file,
    output_file,
    cut_interval_range=(500, 5000),  # in milliseconds
    silence_duration_range=(1000, 30000),  # in milliseconds
):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(input_file)
    output_audio = AudioSegment.empty()

    current_pos = 0
    duration = len(audio)

    while current_pos < duration:
        print("Current position:", current_pos, "/", duration)

        # Pick a random interval for the next segment
        next_cut = random.randint(*cut_interval_range)
        segment_end = min(current_pos + next_cut, duration)

        # Extract and add the audio segment
        segment = audio[current_pos:segment_end]
        output_audio += segment

        # Create and add silence
        silence_duration = random.randint(*silence_duration_range)
        silence = AudioSegment.silent(duration=silence_duration)
        output_audio += silence

        current_pos = segment_end

    # Export the final audio to MP3
    output_audio.export(output_file, format="mp3")
    print(f"Processed audio saved to: {output_file}")


insert_random_cuts_with_silence("input.mp3", "output.mp3")
