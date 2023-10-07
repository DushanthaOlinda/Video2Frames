import cv2
import os


# Function to extract frames from a video and save as images
def extract_frames(video_path, output_folder):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Check if the video file opened successfully
    if not video_capture.isOpened():
        print("Error: Could not open video file.")
        return

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    frame_count = 0

    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()

        # Break the loop if we have reached the end of the video
        if not ret:
            break

        # Save the frame as an image
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

        # Display the frame number being processed (optional)
        print(f"Processing frame {frame_count}")

    # Release the video capture object
    video_capture.release()

    print(f"Frames extracted and saved to {output_folder}")


if __name__ == "__main__":
    # for i in range(1, 8):
    #     a = str(i)
    #     video_path = "Thith_polanga/Thith_polanga"+a+".MOV"
    #     output_folder = "Thith_polanga_processed/Thith_polanga"+a
    #     extract_frames(video_path, output_folder)
    print("Enter the path of the video file: ")
    readline = input()
    video_path = readline
    # video_path = "video.MOV"  # Replace with the path to your video file
    print("Enter the path of the output folder: ")
    readline = input()
    output_folder = readline
    # output_folder = "frames1"  # Replace with the folder where you want to save the frames

    extract_frames(video_path, output_folder)
