import os
import time


def signature_image_path(signature, filename):
    ext = os.path.splitext(filename)[-1]
    now = str(time.time()).replace('.', '')
    return os.path.join('signatures', f'{signature}-{now}{ext}')
