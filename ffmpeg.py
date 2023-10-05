import subprocess

# This script allows users to extract frames from a video file. 
# It prompts the user for the path to the video file, the output file name prefix, and the desired frames per second (FPS). 
# The script then uses the ffmpeg library to extract frames 
# from the video file at the specified FPS and saves them as individual image files. 
# The timestamp of each frame is also added as text on the extracted images. 
# The script handles errors during the frame extraction process and provides appropriate error messages to the user.

creator = "  Script created by w01f"
print(creator)

input_video = input("Enter the path to the video file: ")
output_folder = input("Enter the output file name prefix: ")

custom_fps = input("Enter frames per second (e.g., 30): ")

subprocess.run(["mkdir", "-p", output_folder])

fps_filter = f"fps=1/{custom_fps}"

ffmpeg_command = [
    "ffmpeg",
    "-i", input_video,
    "-vf", f"{fps_filter},drawtext=text='%{{pts\:hms}}{creator}':x=10:y=10:fontsize=24:fontcolor=white:box=1:boxcolor=black@0.5",
    "-q:v", "2",
    "-f", "image2",
    f"{output_folder}/output_%03d.png"
]

try:
    subprocess.run(ffmpeg_command, check=True)
    print(f"Frames extracted successfully to {output_folder}")
except subprocess.CalledProcessError:
    print("Error occurred during frame extraction.")
except KeyboardInterrupt:
    print("Frame extraction canceled by the user.")
