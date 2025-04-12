## Requirements

- python : 3.7
- [pytorch](https://pytorch.org/get-started/previous-versions/)

  ```bash
  # CUDA 10.2
  conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=10.2 -c pytorch
  ```

- other dependencies

  ```bash
  pip install -r requirements.txt
  ```

## Dataset

- [anime256](https://github.com/luzhixing12345/anime-face-dataset/releases/download/v0.0.1/anime256.zip)

- [anime](https://github.com/luzhixing12345/Anime-WGAN/releases/download/v0.0.2/faces.zip)

download the dataset zip and unzip it under `dataset` as `dataset/anime256` and `dataset/anime`

## Use

- Download the pretrained inception model by Google from https://download.pytorch.org/models/inception_v3_google-1a9a5a14.pth and set it under `./checkpoints`


### Train

- run DCGAN model as

  ```bash
  python train.py --config-file configs/DCGAN.yaml
  ```

- run WGAN model as

  ```bash
  python train.py --config-file configs/WGAN.yaml
  ```

- run WGANP model as

  ```bash
  python train.py --config-file configs/WGANP.yaml
  ```

### Generate an anime picture

You can download our trained model from [Results](#Results), and unzip `checkpoints.zip ` under `./checkpoints`

- use DCGAN model as

  ```bash
  python generate.py --config-file configs/DCGAN.yaml -g checkpoints/DCGAN/ANIME/DCGAN_G_ANIME.pth
  ```

  ```bash
  python generate.py --config-file configs/DCGAN.yaml -g checkpoints/DCGAN/ANIME256/DCGAN_G_ANIME256.pth
  ```

- use WGAN model as

  ```bash
  python generate.py --config-file configs/WGAN.yaml -g checkpoints/WGAN/ANIME/WGAN_G_ANIME.pth
  ```

  ```bash
  python generate.py --config-file configs/WGAN.yaml -g checkpoints/WGAN/ANIME256/WGAN_G_ANIME256.pth
  ```

- use WGANP model as

  ```bash
  python generate.py --config-file configs/WGANP.yaml -g checkpoints/WGANP/ANIME/WGANP_G_ANIME.pth
  ```

  ```bash
  python generate.py --config-file configs/WGANP.yaml -g checkpoints/WGANP/ANIME256/WGANP_G_ANIME256.pth
  ```

by default it will generate an 8x8 grid fake anime image under `./images`

Arguments:

- `-g`: short for generator, one argument with the path name of the model weights
- `-s`: short for separate, no argument. Use `-s` to separate the grid image into 64 images

### Results

Our model of the training results and generated results are here: https://drive.google.com/drive/folders/1NVpWjMp-ac5W5ZyTzy4WZ_AKvtrLLSVJ?usp=sharing

## About training configuration

All the configuration infomation is in [config/defaults.py](config/defaults.py). I think the name of each parameter is clear enough for you to understand what it infers. You may change as you like, batch size, learning rate and so on.

logging part comes from python module `logging`, I think it's a more elegent way to log something instead of just using `print`.

Except the default configuration information, you **ONLY NEED TO FOUCES ON** detail configurations under folder `configs`, there are two `yaml` file `configs/WGAN.yaml` and `configs/WGANP.yaml`.

[WGAN.yaml](configs/WGAN.yaml) use some configurations different from [defaults.py](config/defaults.py), which needs to declared and it will overwrite the corresponding configurations while the program running.

So if you want to change the dataset from `anime256` to `anime`, you just need to change the yaml file.

FROM

```yaml
PROJECT_NAME: WGAN

DATASET:
  NAME: dataset/anime256
  TRAIN_TEST_RATIO: 1.0
```

TO

```yaml
PROJECT_NAME: WGAN

DATASET:
  NAME: dataset/anime
  TRAIN_TEST_RATIO: 1.0
```

If you don't want to steadily change file, you could also use the same yaml file but follow with the corresponding configuration like

```bash
# change dataset to anime
python train.py --config-file configs/WGAN.yaml DATASET.NAME anime

# change generator iterations to 20000
python train.py --config-file configs/WGANP.yaml MODEL.WGAN.GENERATOR_ITERS 20000
```

- **PAY ATTENTION THAT** if you want to use the same yaml file to train twice or more, **remember to use a unique PROJECT_NAME**, the same PROJECT_NAME would cover the before.

  ```bash
  python train.py --config-file configs/WGAN.yaml PROJECT_NAME MYTRAIN_1
  ```

  or change in yaml file

  ```yaml
  PROJECT_NAME: MYTRAIN_1
  
  DATASET:
    NAME: dataset/anime256
    TRAIN_TEST_RATIO: 1.0
  ```

