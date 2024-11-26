from moviepy.editor import VideoFileClip, clips_array

def combine_videos_horizontally(input_video1_path, input_video2_path, output_video_path):
    # 加载视频
    clip1 = VideoFileClip(input_video1_path)
    clip2 = VideoFileClip(input_video2_path)
    
    # 确保两个视频的帧率和尺寸相同
    if clip1.fps != clip2.fps:
        clip2 = clip2.set_fps(clip1.fps)
    
    if clip1.size != clip2.size:
        clip2 = clip2.resize((640,960))
        clip1 = clip1.resize((640,960))
    
    # 左右拼接视频
    final_clip = clips_array([[clip1, clip2]])
    
    # 导出视频
    final_clip.write_videofile(output_video_path, codec='libx264', fps=clip1.fps)

# 调用函数
for type in ['box','lane']:
    for data in ['5','27','65']:
        input_video1_path = f'box-lane\\baseline{data}{type}6.mp4'
        input_video2_path = f'box-lane\\{data}{type}6.mp4'
        output_video_path = f'box-lane\\combine_{data}{type}.mp4'

        combine_videos_horizontally(input_video1_path, input_video2_path, output_video_path)