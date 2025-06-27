#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ml_collections as mlc
import numpy as np
import os
import os.path as osp


def train_cfg():
    """returns training configuration."""

    cfg = mlc.ConfigDict()
    cfg.resume = False
    cfg.display = True
    cfg.print_rate = 5
    cfg.batch_size = 8
    cfg.epoch = 40

    # network setting
    cfg.use_rgb = False  # use 'RGB' or 'XYZRGB' as input dimensions
    if cfg.use_rgb:
        cfg.in_dim = 6
    else:
        cfg.in_dim = 3
    cfg.out_dim = 64
    cfg.sub_sampling_ratio = [
        4,
        4,
        4,
        4,
    ]  # down sample rate of the input point clouds of each layer
    cfg.down_rate = np.prod(cfg.sub_sampling_ratio)
    cfg.num_layers = len(cfg.sub_sampling_ratio)
    cfg.k_neighbors = 16  # The k value in LFA module

    # dataset setting
    cfg.n_samples = 8192  # the point number of the input point clouds
    cfg.remove_plane = True  # if remove the ground plane of PCs
    cfg.plane_threshold = 0.50
    cfg.norm_data = True

    # path
    cfg.path = mlc.ConfigDict()
    cfg.path.data_root = "/workspaces/3DCDNet/3DCDNet/data"
    # cfg.path.data_root = 'F:\\WZXData\\SHREC2021-3DCD\\dataset7'
    cfg.path.test_dataset = (
        os.path.join(cfg.path.data_root, "test_seg")
        + "_split_plane_"
        + str(cfg.n_samples)
        + "_thr_"
        + str(cfg.plane_threshold)
    )
    cfg.path.train_dataset = (
        os.path.join(cfg.path.data_root, "train_seg")
        + "_split_plane_"
        + str(cfg.n_samples)
        + "_thr_"
        + str(cfg.plane_threshold)
    )
    cfg.path.val_dataset = cfg.path.train_dataset
    cfg.if_prepare_data = (
        True  # saving processed PCs to .npy to accelerate training phase.
    )
    cfg.path.prepare_data = (
        cfg.path.data_root
        + "/prapared_data_"
        + str(cfg.n_samples)
        + "_thr_"
        + str(cfg.plane_threshold)
        + "_"
        + str(cfg.k_neighbors)
    )
    # cfg.path.save_txt = "./data"
    # cfg.path.train_txt = "./data/train.txt"
    # cfg.path.val_txt = "./data/val.txt"
    # cfg.path.test_txt = "./data/test.txt"
    # cfg.path.outputs = "./outputs"
    # cfg.path.weights_save_dir = "./outputs/weights"
    # cfg.path.best_weights_save_dir = "./outputs/best_weights"
    # cfg.path.val_prediction = "./outputs/val_prediction"
    # cfg.path.test_prediction = "./outputs/test_prediction"
    # cfg.path.test_prediction_PCs = "./outputs/test_prediction_PCs"
    # cfg.path.feature = "./outputs/feature"

    # some problem with the mounts. This way it works, but it's important to be in 3DCDNet in the terminal (due to cwd)

    # added /data in front
    # cfg.path.save_txt = "/data/data"
    # cfg.path.train_txt = "/data/data/train.txt"
    # cfg.path.val_txt = "/data/data/val.txt"
    # cfg.path.test_txt = "/data/data/test.txt"
    cfg.path.save_txt = osp.join(os.getcwd(), "data")
    cfg.path.train_txt = osp.join(os.getcwd(), "data/train.txt")
    cfg.path.val_txt = osp.join(os.getcwd(), "data/val.txt")
    cfg.path.test_txt = osp.join(os.getcwd(), "data/test.txt")
    # cfg.path.outputs = "/data/outputs"
    # cfg.path.weights_save_dir = "/data/outputs/weights"
    # cfg.path.best_weights_save_dir = "/data/outputs/best_weights"
    # cfg.path.val_prediction = "/data/outputs/val_prediction"
    # cfg.path.test_prediction = "/data/outputs/test_prediction"
    # cfg.path.test_prediction_PCs = "/data/outputs/test_prediction_PCs"
    # cfg.path.feature = "/data/outputs/feature"
    cfg.path.outputs = osp.join(os.getcwd(), "outputs")
    cfg.path.weights_save_dir = osp.join(os.getcwd(), "outputs/weights")
    cfg.path.best_weights_save_dir = osp.join(os.getcwd(), "outputs/best_weights")
    cfg.path.val_prediction = osp.join(os.getcwd(), "outputs/val_prediction")
    cfg.path.test_prediction = osp.join(os.getcwd(), "outputs/test_prediction")
    cfg.path.test_prediction_PCs = osp.join(os.getcwd(), "outputs/test_prediction_PCs")
    cfg.path.feature = osp.join(os.getcwd(), "outputs/feature")

    # optimizer setting
    cfg.optimizer = mlc.ConfigDict()
    cfg.optimizer.lr = 0.001
    cfg.optimizer.momentum = 0.9
    cfg.optimizer.weight_decay = 0.0005
    cfg.optimizer.lr_step_size = 1
    cfg.optimizer.gamma = 0.95

    # validation and testing setting
    cfg.save_prediction = True  # if save the prediction results.
    cfg.criterion = "miou"  # criterion for selecting models: 'miou' or 'oa'

    return cfg


CONFIGS = {
    "Train": train_cfg(),
}
