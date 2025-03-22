from model import *

def build_model(cfg):

    total_model = {
        'DCGAN': DCGAN,
        'WGAN': WGAN,
        'WGANP': WGANP,
    }
    model = total_model[cfg.MODEL.NAME](cfg)

    if cfg.MODEL.DEVICE == 'cuda':
        model = model.cuda()
    
    return model