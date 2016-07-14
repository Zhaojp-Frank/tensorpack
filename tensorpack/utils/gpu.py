#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: gpu.py
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>


from .utils import change_env

__all__ = ['change_gpu', 'get_nr_gpu', 'get_gpus']

def change_gpu(val):
    return change_env('CUDA_VISIBLE_DEVICES', str(val))

def get_nr_gpu():
    env = os.environ.get('CUDA_VISIBLE_DEVICES', None)
    assert env is not None  # TODO
    return len(env.split(','))

def get_gpus():
    """ return a list of GPU physical id"""
    env = os.environ.get('CUDA_VISIBLE_DEVICES', None)
    assert env is not None  # TODO
    return map(int, env.strip().split(','))

