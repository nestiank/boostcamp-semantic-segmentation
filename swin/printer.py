#
# boostcamp AI Tech
# Trash Semantic Segmentation Competition
#


from mmcv import Config

from options import CONFIG_PATH


if __name__ == '__main__':
    cfg = Config.fromfile(CONFIG_PATH)
    print(cfg.pretty_text)
