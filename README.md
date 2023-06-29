[![Open in Jupyter Notebook](https://img.shields.io/badge/Open%20in-Jupyter%20Notebook-orange?logo=jupyter)](https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/HEAD?urlpath=lab)
![Python](https://img.shields.io/badge/Python-3.10-blue)


# OCR Post-Correction for Machine Translation Enhancement


The accuracy of Optical Character Recognition (OCR) outputs can significantly impact the performance of Machine Translation (MT) systems. This one-month internship aims to explore and develop strategies to improve the quality and usability of OCR'd texts for MT purposes. The intern will conduct experiments utilizing a range of post-correction techniques (such as rule-based strategies or leveraging large language models), and evaluate the performance of state-of-the-art MT systems when translating OCR'd texts.   


## Data Sources

    - French: Cremma Wikipedia containing both handwritten and printed text images of Wikipedia text from 2022-2023 and ground truth.    
      https://github.com/HTR-United/cremma-wikipedia. 
    - English: OCR Ground Truth for Historical Commentariescontaining both handwritten and printed text images and ground truth.
      https://github.com/AjaxMultiCommentary/GT-commentaries-OCR/tree/master


## Instructions

For the best experience and accurate results, it's essential to execute the code cells in the provided Jupyter notebook in the order they appear. As you work through this project, you may encounter the need to install additional Python libraries, such as NLTK and symspellpy, which are not included in the standard Python distribution.

To install some of these libraries, you can use the pip package manager, which is typically included with your Python installation. For instance, to install NLTK, you would use the following command in your command line interface: *pip install NLTK*

To install sympspellpy follow the instruction here: https://symspellpy.readthedocs.io/en/latest/users/installing.html

Please ensure these libraries are correctly installed before attempting to run the code cells that depend on them. This will ensure the smooth running of the program and the accuracy of the results.

```
Project
├─ Code                             <- The code used for the analysis 
│  ├─ baseline-2.ipynb              <- segments sentences
│  ├─ extraction.py                 <- function to extract ground truth from an XML file
│  ├─ segmentation.py               <- function to segment sentences
│  ├─ symspellpy.ipynb              <- Post-processing OCR'd text with symspellpy 
│  └─ transcript.ipynb              <- processing an XML file to extract the ground truth
│    
│   
├─ Data                             <- all the datasets used for this project
├─ README.md
└─ Requirements.txt                 <- contains all the required libraries
```
<!-- ©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator) -->

-------------------------------------------------------------------------------
Thank you for using this code. We hope you find it both useful and enjoyable to use. \
Please don't hesitate to reach out if you require any further assistance.

-------------------------------------------------------------------------------

### Credits: 
-[Dinara Akmurzina](https://github.com/dakmurzina), \
-[Shaifali Khulbe](https://github.com/ShaifaliKhulbe).
