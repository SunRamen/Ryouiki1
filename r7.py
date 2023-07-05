{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyOf7SGC69Nl/2efbGZX5YXN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SunRamen/Ryouiki1/blob/main/Untitled0.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j-cRYfSBsJO_",
        "outputId": "cf167dca-c9d5-45e2-afdf-d4fbc0880a55"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n",
            "/content/drive/MyDrive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')\n",
        "%cd ./drive/MyDrive"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/ultralytics/ultralytics\n",
        "%cd ultralytics\n",
        "!pip install -r requirements.txt\n",
        "from ultralytics import YOLO\n",
        "model = YOLO(\"yolov8x.pt\")\n",
        "results = model(\"https://ultralytics.com/images/bus.jpg\", save=True,\n",
        "save_txt=True, save_conf=True)\n",
        "boxes = results[0].boxes\n",
        "for box in boxes:\n",
        " print(box.data)\n",
        "print(results[0].names)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0HDBVhhDstty",
        "outputId": "e9609870-3e20-4d7c-94ba-f5afedf95089"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'ultralytics'...\n",
            "remote: Enumerating objects: 11629, done.\u001b[K\n",
            "remote: Counting objects: 100% (873/873), done.\u001b[K\n",
            "remote: Compressing objects: 100% (449/449), done.\u001b[K\n",
            "remote: Total 11629 (delta 553), reused 655 (delta 417), pack-reused 10756\u001b[K\n",
            "Receiving objects: 100% (11629/11629), 7.44 MiB | 13.58 MiB/s, done.\n",
            "Resolving deltas: 100% (7734/7734), done.\n",
            "Updating files: 100% (412/412), done.\n",
            "/content/drive/MyDrive/ultralytics/ultralytics/ultralytics\n",
            "Requirement already satisfied: matplotlib>=3.2.2 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 5)) (3.7.1)\n",
            "Requirement already satisfied: opencv-python>=4.6.0 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 6)) (4.7.0.72)\n",
            "Requirement already satisfied: Pillow>=7.1.2 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 7)) (8.4.0)\n",
            "Requirement already satisfied: PyYAML>=5.3.1 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 8)) (6.0)\n",
            "Requirement already satisfied: requests>=2.23.0 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 9)) (2.27.1)\n",
            "Requirement already satisfied: scipy>=1.4.1 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 10)) (1.10.1)\n",
            "Requirement already satisfied: torch>=1.7.0 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 11)) (2.0.1+cu118)\n",
            "Requirement already satisfied: torchvision>=0.8.1 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 12)) (0.15.2+cu118)\n",
            "Requirement already satisfied: tqdm>=4.64.0 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 13)) (4.65.0)\n",
            "Requirement already satisfied: pandas>=1.1.4 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 22)) (1.5.3)\n",
            "Requirement already satisfied: seaborn>=0.11.0 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 23)) (0.12.2)\n",
            "Requirement already satisfied: psutil in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 38)) (5.9.5)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.2.2->-r requirements.txt (line 5)) (1.1.0)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.2.2->-r requirements.txt (line 5)) (0.11.0)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.2.2->-r requirements.txt (line 5)) (4.40.0)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.2.2->-r requirements.txt (line 5)) (1.4.4)\n",
            "Requirement already satisfied: numpy>=1.20 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.2.2->-r requirements.txt (line 5)) (1.22.4)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.2.2->-r requirements.txt (line 5)) (23.1)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.2.2->-r requirements.txt (line 5)) (3.1.0)\n",
            "Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.2.2->-r requirements.txt (line 5)) (2.8.2)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.23.0->-r requirements.txt (line 9)) (1.26.16)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.23.0->-r requirements.txt (line 9)) (2023.5.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests>=2.23.0->-r requirements.txt (line 9)) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.23.0->-r requirements.txt (line 9)) (3.4)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from torch>=1.7.0->-r requirements.txt (line 11)) (3.12.2)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.10/dist-packages (from torch>=1.7.0->-r requirements.txt (line 11)) (4.6.3)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from torch>=1.7.0->-r requirements.txt (line 11)) (1.11.1)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.10/dist-packages (from torch>=1.7.0->-r requirements.txt (line 11)) (3.1)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from torch>=1.7.0->-r requirements.txt (line 11)) (3.1.2)\n",
            "Requirement already satisfied: triton==2.0.0 in /usr/local/lib/python3.10/dist-packages (from torch>=1.7.0->-r requirements.txt (line 11)) (2.0.0)\n",
            "Requirement already satisfied: cmake in /usr/local/lib/python3.10/dist-packages (from triton==2.0.0->torch>=1.7.0->-r requirements.txt (line 11)) (3.25.2)\n",
            "Requirement already satisfied: lit in /usr/local/lib/python3.10/dist-packages (from triton==2.0.0->torch>=1.7.0->-r requirements.txt (line 11)) (16.0.6)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.1.4->-r requirements.txt (line 22)) (2022.7.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.7->matplotlib>=3.2.2->-r requirements.txt (line 5)) (1.16.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->torch>=1.7.0->-r requirements.txt (line 11)) (2.1.3)\n",
            "Requirement already satisfied: mpmath>=0.19 in /usr/local/lib/python3.10/dist-packages (from sympy->torch>=1.7.0->-r requirements.txt (line 11)) (1.3.0)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Downloading https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt to yolov8x.pt...\n",
            "100%|██████████| 131M/131M [00:00<00:00, 163MB/s]\n",
            "\n",
            "Downloading https://ultralytics.com/images/bus.jpg to bus.jpg...\n",
            "100%|██████████| 476k/476k [00:00<00:00, 11.6MB/s]\n",
            "image 1/1 /content/drive/MyDrive/ultralytics/ultralytics/ultralytics/bus.jpg: 640x480 5 persons, 1 bicycle, 1 bus, 62.1ms\n",
            "Speed: 2.3ms preprocess, 62.1ms inference, 1.4ms postprocess per image at shape (1, 3, 640, 480)\n",
            "Results saved to \u001b[1m/content/drive/MyDrive/ultralytics/runs/detect/predict3\u001b[0m\n",
            "1 label saved to /content/drive/MyDrive/ultralytics/runs/detect/predict3/labels\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "tensor([[  1.1242, 230.5177, 804.2791, 741.8676,   0.9680,   5.0000]], device='cuda:0')\n",
            "tensor([[668.5291, 392.1565, 809.5764, 879.8139,   0.9311,   0.0000]], device='cuda:0')\n",
            "tensor([[ 50.5359, 398.1865, 247.5806, 900.8975,   0.9183,   0.0000]], device='cuda:0')\n",
            "tensor([[221.9554, 406.1465, 343.9901, 860.0883,   0.9019,   0.0000]], device='cuda:0')\n",
            "tensor([[2.1835e-01, 5.5076e+02, 7.8427e+01, 8.7218e+02, 6.9789e-01, 0.0000e+00]], device='cuda:0')\n",
            "tensor([[2.3819e-01, 5.5013e+02, 7.9402e+01, 1.0642e+03, 5.3844e-01, 0.0000e+00]], device='cuda:0')\n",
            "tensor([[6.6625e+02, 1.5416e+01, 7.4806e+02, 9.0126e+01, 4.3446e-01, 1.0000e+00]], device='cuda:0')\n",
            "{0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}\n"
          ]
        }
      ]
    }
  ]
}