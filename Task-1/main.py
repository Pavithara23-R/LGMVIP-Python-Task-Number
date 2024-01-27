from moviepy.editor import ImageSequenceClip

image_files = ['flower1.png', 'flower2.png', 'flower3.png']
frame_duration = 5.0
clips = ImageSequenceClip(image_files, fps=frame_duration)
output_gif_path = 'output.gif'
clips.write_gif(output_gif_path, fps=frame_duration)
print(f"GIF created successfully: {output_gif_path}")
