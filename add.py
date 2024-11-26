import cv2

# 视频参数
where_list = ['combined_05_3.mp4','combined_05_6.mp4','combined_05_9.mp4','combined_18_3.mp4','combined_18_6.mp4','combined_18_9.mp4','combined_27_3.mp4','combined_27_6.mp4','combined_27_9.mp4','combined_164_3.mp4','combined_164_6.mp4','combined_164_9.mp4']
for where in where_list:
    output_path = f'supply1/{where}'  # 输出视频路径
    video_path = f'supply/{where}'  # 输入视频路径
    h = 640  # 高度
    w = 1920  # 宽度

    # 文字参数
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255)  # 白色
    line_type = 2

    # 文字位置
    left_bottom = (10, h - 20)  # 左下角

    # 分割文本
    text_lines = ['ReconDreamer with', 'Street Gaussians']

    # 计算文本尺寸
    (text_width_1, text_height_1), _ = cv2.getTextSize(text_lines[0], font, font_scale, line_type)
    (text_width_2, text_height_2), _ = cv2.getTextSize(text_lines[1], font, font_scale, line_type)
    
    region_width = 400  # 这个值可以根据需要调整
    # 计算居中位置
    x1 = w - region_width + int((region_width - text_width_1) / 2)
    x2 = w - region_width + int((region_width - text_width_2) / 2)
    y1 = h - 60  # 第一行的位置
    y2 = y1 + text_height_1 + 20  # 第二行的位置，增加一些间距

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 获取视频的帧率
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 创建VideoWriter对象
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 在左下角写入 "street"
        cv2.putText(frame, 'Street Gaussians', left_bottom, font, font_scale, font_color, line_type)
        
        # 在右下角写入 "ReconDreamer with" 和 "Street Gaussians" 居中显示
        cv2.putText(frame, text_lines[0], (x1, y1), font, font_scale, font_color, line_type)
        cv2.putText(frame, text_lines[1], (x2, y2), font, font_scale, font_color, line_type)

        # 写入帧到输出视频
        out.write(frame)

    # 释放资源
    cap.release()
    out.release()

    print(f"视频 {where} 处理完成")