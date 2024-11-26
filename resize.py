import imageio
from skimage.transform import resize
import numpy as np

# 输入和输出文件路径
for type in ['box','lane']:
    for data in ['5','27','65']:
        target_size = (640,960*2)
        input_file = f'box-lane\\combine_{data}{type}.mp4'
        output_file = f'supply1\\combine_{data}{type}.mp4'
        reader = imageio.get_reader(input_file)

        # 获取原始视频的帧率
        fps = 10

        # 创建输出视频写入器
        writer = imageio.get_writer(output_file, fps=fps)

        # 遍历每一帧
        for frame in reader:
            # 调整帧的大小
            resized_frame = resize(frame, target_size, preserve_range=True).astype(np.uint8)
            # 写入调整后的帧
            writer.append_data(resized_frame)

        # 关闭读取器和写入器
        reader.close()
        writer.close()

        print(f"Video has been resized and saved as {output_file}")