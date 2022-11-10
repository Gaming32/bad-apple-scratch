from moviepy.editor import VideoFileClip


def do_it() -> None:
    with (
        VideoFileClip('Touhou - Bad Apple.mp4', audio=False) as clip,
        open('bad_apple_list.txt', 'w', buffering=1024 * 1024) as fp
    ):
        for frame in clip.iter_frames(logger='bar'):
            run_size = 0
            last_color: bool = False
            for y in range(360):
                for x in range(480):
                    color: bool = frame[y, x, 0] > 127
                    if color != last_color:
                        fp.write(str(int(last_color)) + ' ' + str(run_size) + ' ')
                        last_color = color
                        run_size = 1
                    else:
                        run_size += 1
            fp.write(str(int(last_color)) + ' ' + str(run_size))
            fp.write('\n')


do_it()
