from moviepy.editor import VideoFileClip, clips_array

def combine_videos_horizontally(input_video1_path, input_video2_path, output_video_path):
    # 加载视频
    clip1 = VideoFileClip(input_video1_path)
    clip2 = VideoFileClip(input_video2_path)
    
    # 确保两个视频的帧率和尺寸相同
    if clip1.fps != clip2.fps:
        clip2 = clip2.set_fps(clip1.fps)
    

    clip2 = clip2.resize((960,640))
    clip1 = clip1.resize((960,640))
    
    # 左右拼接视频
    final_clip = clips_array([[clip1, clip2]])
    
    # 导出视频
    final_clip.write_videofile(output_video_path, codec='libx264', fps=clip1.fps)

# 调用函数
for type in ['box','lane']:
    for data in ['5','27','65']:
        input_video1_path = f'supply1/1.5_org_part2.mp4'
        input_video2_path = f'supply1/1.5_20_r.mp4'
        output_video_path = f'restore/81combine.mp4'

        combine_videos_horizontally(input_video1_path, input_video2_path, output_video_path)
        break
    break