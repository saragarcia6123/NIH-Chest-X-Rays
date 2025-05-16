```sh
git clone https://github.com/saragarcia6123/NIH-Chest-X-Rays.git
cd NIH-Chest-X-Rays

conda create --name nih
conda install --yes --file requirements.txt

ipython kernel install --user --name=nih
jupyter lab
```

Popular ML libraries & architectures for medical image analysis:

- U-Net: A CNN architecture commonly used for image segmentation tasks.
- ResNet: A CNN architecture that can be used for image classification tasks.
- DenseNet: A CNN architecture that can be used for image classification tasks.
- PyTorch: A popular deep learning library that provides tools for building and training neural networks.
- TensorFlow: A popular deep learning library that provides tools for building and training neural networks.
- OpenCV: A computer vision library that provides tools for image processing and analysis.
- ITK-SNAP: A software framework for medical image analysis that provides tools for image segmentation and registration.