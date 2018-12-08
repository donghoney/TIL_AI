# SimpleITK/Tutorials/MICCAI2015

< [SimpleITK](https://itk.org/Wiki/SimpleITK)

본문 링크 : https://itk.org/Wiki/SimpleITK/Tutorials/MICCAI2015



[![MiccaiBanner.jpg](https://itk.org/Wiki/images/thumb/1/14/MiccaiBanner.jpg/1000px-MiccaiBanner.jpg)](http://www.miccai2015.org/)



Monday October 5'th 2015

## After The Tutorial

All of the tutorial material, including slide's from Dr. Tustison's talk on registration, is available on the github repository:

```
  https://github.com/InsightSoftwareConsortium/SimpleITKTutorialMICCAI2015.git
```

To continue exploring SimpleITK in general and registration in particular, additional notebooks are available from SimpleITK's main notebook repository:

```
 https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks
```

## Before The Tutorial

- Before the tutorial you will have to either install a Python environment as described [below](https://itk.org/Wiki/SimpleITK/Tutorials/MICCAI2015#Three_paths_forward) or Docker (lightweight virtual machine).
- You will then need to download the IPython notebooks and data:



```
 git clone https://github.com/InsightSoftwareConsortium/SimpleITKTutorialMICCAI2015.git
```



```
 python downloaddata.py ./Data ./Data/manifest.json
```

## Who Should Attend

- Do you want your students to gain practical experience with registration while minimizing their programming load?
- Do you want to easily experiment with various ITK registration configurations, or optimize the settings of a specific registration configuration?

If you answered yes to either of these questions, then this tutorial is for you.



The goal of this half-day tutorial is to introduce students and researchers to SimpleITK’s interface for the ITK version 4 registration framework. SimpleITK is, as the name suggests, a simpler interface to ITK. It provides a procedural interface and bindings to several interpreted languages, facilitating fast experimentation with ITK algorithms. In this tutorial we will use the Python programming language and the IPython Notebook interactive environment to explore the various features of the ITKv4 registration framework. Key features presented include: uniform treatment of linear, deformable and composite transformations, embedded multi-resolution registration and self calibrating optimizers. Using a hands on approach, participants will experiment with various registration tasks, learning how to use SimpleITK in order to gain insight into the effects of registration component selection and parameter settings on accuracy and running time of ITK based registration algorithms.

## Organizers

| [![Nlm.jpg](https://itk.org/Wiki/images/thumb/b/b9/Nlm.jpg/60px-Nlm.jpg)](https://itk.org/Wiki/File:Nlm.jpg) | [![Kitware.jpg](https://itk.org/Wiki/images/thumb/0/07/Kitware.jpg/150px-Kitware.jpg)](https://itk.org/Wiki/File:Kitware.jpg) | [![Upenn.jpg](https://itk.org/Wiki/images/thumb/1/1e/Upenn.jpg/120px-Upenn.jpg)](https://itk.org/Wiki/File:Upenn.jpg) | [![Uofiowa.jpg](https://itk.org/Wiki/images/4/43/Uofiowa.jpg)](https://itk.org/Wiki/File:Uofiowa.jpg) | [![Uva.jpg](https://itk.org/Wiki/images/9/91/Uva.jpg)](https://itk.org/Wiki/File:Uva.jpg) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |                                                              |                                                              |                                                              |

- Brian Avants, University of Pennsylvania.
- Hans Johnson, University of Iowa.
- Bradley Lowekamp, Medical Science & Computing and National Institutes of Health.
- Matthew McCormick, Kitware Inc.
- Nick Tustison, University of Virginia.
- Ziv Yaniv, TAJ Technologies Inc. and National Institutes of Health.

## Prerequisites

We **do not** require knowledge of C++ templates, CMake or how to compile code.

We **do require** basic knowledge of the Python programming language. If you are not familiar with Python but are well versed in MATLAB, Java, C++... then don't worry. You will be up to speed with a minimal investment of time. Please read or skim through the [official Python language tutorial](https://docs.python.org/3/tutorial/index.html) or any of the tutorials listed [here](https://wiki.python.org/moin/BeginnersGuide/Programmers).

You will need to bring your laptop (don't forget the adapter plug for your power cord if you are coming from outside of Europe).

The minimal installation of Python will have to include the following packages: (1) ipython; (2) numpy; (3) matplotlib; (4) SimpleITK

### Three paths forward

If you selected to go with your own Python installation, options 1 and 2, then you will have to download the IPython notebooks and data as described [above](https://itk.org/Wiki/SimpleITK/Tutorials/MICCAI2015#Before_The_Tutorial).

#### 1. Manual

This path installs the minimal set of required components. It is only recommended if you are familiar with Python and Python package management (**we assume your system has a working compiler**):

1. Get Python ( version 3.4 recommended, 2.7 compatible ) [Download](https://www.python.org/downloads/) and install Python version 2.7.9.

From the command line:

1. if pip is not installed see [pip](https://pip.pypa.io/en/latest/installing/)'s installation instructions.
2. (sudo) pip install virtualenv
3. virtualenv sitkpy --no-site-packages
4. unix/mac: source sitkpy/bin/activate 
   win: sitkpy\Scripts\activate
5. pip install -U pip
6. pip install 'ipython[all]' numpy matplotlib ipywidgets
7. pip install --trusted-host www.simpleitk.org -f http://www.simpleitk.org/SimpleITK/resources/software.html --timeout 30 SimpleITK (for other options see [here](http://www.itk.org/Wiki/SimpleITK/GettingStarted))

Note that you may need to install some matplotlib dependencies if they are not already on your system (sudo apt-get install libpng-dev, sudo apt-get install libfreetype6-dev). You only need to do this if you receive corresponding error messages when running pip install.

#### 2. Disk Space is Cheap

This path installs a full fledged scientific computing environment. Install (free) Python distributions for scientific and numeric computing from commercial vendors, either [Continuum’s](http://continuum.io/) Anaconda or [Enthought’s](https://store.enthought.com/) Canopy. If you want the full list of packages that come with each of these distributions simply follow these links:[Anaconda](http://docs.continuum.io/anaconda/pkg-docs.html), [Canopy](https://www.enthought.com/products/canopy/package-index/).

| Anaconda[Download](http://continuum.io/downloads) and install.From the command line:conda update conda anacondaconda create -n sitkpy -c https://conda.binstar.org/simpleitk python=3.4 anaconda SimpleITK ipywidgetsunix/mac: source activate sitkpy  win: activate sitkpy | Canopy ( Known to work on Windows )[Download](https://store.enthought.com/downloads/#default) and install.Update the installation using the Package Manager.From the command line (cd to the directory where canopy is installed):User/bin/canopy_cli venv -s sitkpyunix/mac: source sitkpy/bin/activate  win: sitkpy\Scripts\activatedownload the wheel from SourceForge as described [here](https://itk.org/Wiki/SimpleITK/GettingStarted)pip install wheel_file_name |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

#### 3. Reproducible Environment

This path uses a [reproducible computational environment](http://nbviewer.ipython.org/format/slides/github/thewtex/scipy-2015-docker-presentation/blob/master/Docker_for_Improved_Reproducibility_of_Scientific_Python_Analyses.ipynb#/) that will work the same way across platforms and over time. For efficient use of disk, memory, and cpu, rapid execution, and easy distribution, we will use [Docker](https://www.docker.com/) instead of a virtual machine.

1. [Install Docker](http://docs.docker.com/installation/)

- *Windows 10*: uninstall VirtualBox, if installed, and use [this installer](http://midas3.kitware.com/midas/download/item/318751/DockerToolbox-1.8.1a-windows-10-test.exe).

1. Obtain the SimpleITK Notebooks Docker image.
   1. If you have a network connection, run
   2. If you have the USB drive from the conference:
2. Even if you encountered errors in the previous step, execute **./run.sh** in the SimpleITKTutorialMICCAI2015 repository.

### Additional Programs

In some SimpleITK notebooks we use an external viewer to look at our images. The default viewer is [ImageJ](http://imagej.nih.gov/ij/). If you do not have any viewer installed, please install ImageJ.

If you already have another viewer such as ITK-SNAP or Slicer and do not want to install ImageJ, you only need to set an environment variable SITK_SHOW_COMMAND to point to your program of choice. This can also be done inside the ipython notebook:

%env SITK_SHOW_COMMAND /Applications/ITK-SNAP.app/Contents/MacOS/ITK-SNAP

## Program

- 8:30am: Setup and introduction [Matthew McCormick and Hans Johnson].
- 9:00am: SimpleITK basics: loading data, image access, image transformations, image resampling, basic filters [Matthew McCormick].
- 10:00am: The ITKv4 registration framework [Nick Tustison and Brian Avants].
- 10:30am: Coffee break.
- 10:45am: Registration 1: composite transform, transformation initialization, embedded multi-resolution, scale parameter estimation, optimization termination criteria [Ziv Yaniv].
- 11:30am: Registration 2: nonrigid registration - Nonrigid registration, Bspline and displacement field transformations [Ziv Yaniv].
- 12:30pm: Lunch.

## A Taste of What's to Come: SimpleITK Registration, It's Really Simple

The following script illustrates the use of SimpleITK to perform rigid registration between a CT and MR (registration specific code is highlighted). By the end of the tutorial you will be familiar with the various components that are available as part of the SimpleITK registration framework, easily modifying this example to suite your specific needs.

```
import SimpleITK as sitk

#read the images
fixed_image =  sitk.ReadImage('training_001_ct.mha', sitk.sitkFloat32)
moving_image = sitk.ReadImage('training_001_mr_T1.mha', sitk.sitkFloat32) 

#initial alignment of the two volumes
transform = sitk.CenteredTransformInitializer(fixed_image, 
                                              moving_image, 
                                              sitk.Euler3DTransform(), 
                                              sitk.CenteredTransformInitializerFilter.GEOMETRY)

#multi-resolution rigid registration using Mutual Information
registration_method = sitk.ImageRegistrationMethod()
registration_method.SetMetricAsMattesMutualInformation(numberOfHistogramBins=50)
registration_method.SetMetricSamplingStrategy(registration_method.RANDOM)
registration_method.SetMetricSamplingPercentage(0.01)
registration_method.SetInterpolator(sitk.sitkLinear)
registration_method.SetOptimizerAsGradientDescent(learningRate=1.0, 
                                                  numberOfIterations=100, 
                                                  convergenceMinimumValue=1e-6, 
                                                  convergenceWindowSize=10)
registration_method.SetOptimizerScalesFromPhysicalShift()
registration_method.SetShrinkFactorsPerLevel(shrinkFactors = [4,2,1])
registration_method.SetSmoothingSigmasPerLevel(smoothingSigmas=[2,1,0])
registration_method.SmoothingSigmasAreSpecifiedInPhysicalUnitsOn()
registration_method.SetInitialTransform(transform)
registration_method.Execute(fixed_image, moving_image)

sitk.WriteTransform(transform, 'ct2mrT1.tfm')
```


To run this example you will need to download the [CT](http://midas3.kitware.com/midas/download/?items=317034,1) and [MR](http://midas3.kitware.com/midas/download/?items=317035,1) data. These are part of the training data provided by the [Retrospective Image Registration Evaluation Project](http://www.insight-journal.org/rire/).

A bit of additional [code](https://itk.org/Wiki/images/4/41/RegistrationExample.txt) also allows us to visually follow the registration process:

[![RegistrationAnimation.gif](https://itk.org/Wiki/images/f/fc/RegistrationAnimation.gif)](https://itk.org/Wiki/File:RegistrationAnimation.gif)