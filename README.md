# Machine-Learning-In-Cyber-Security
<br />
<br />

## Main Project: Malicious URL Detection 
<br />
<br />

### Description

Lack of data is the most common yet fixable machine learning issue. <br />
In this project the purpose was not only to develop Machine Learning system for detecting malicious urls <br />
but also to deal with a standard unbalanced URL dataset and try to improve the model results by creating additional data: <br />

<br />


1. generate pattern of Malicious URL by using 'DGA' algorithm

<br />
<img width="764" alt="2022-02-19 (7)" src="https://user-images.githubusercontent.com/57047863/154812551-bb277bd5-6e4f-45d8-b3e2-52e95eff52ed.png">
<br />

2. scraping URL data from the internet

<br />
<img width="868" alt="2022-02-19 (5)" src="https://user-images.githubusercontent.com/57047863/154812256-a5e451a8-1c8d-427e-8aaf-2f34da69a774.png">
<br />

3. language generation with 'Transformers' (generate new urls by using deep learning methods)

<br />
<img width="712" alt="2022-02-19 (2)" src="https://user-images.githubusercontent.com/57047863/154808352-27642fa1-a0c5-4521-822e-6a1ae6e9dbfe.png">
<br />
<img width="474" alt="2022-02-19 (1)" src="https://user-images.githubusercontent.com/57047863/154808366-cb17080b-cec6-4a42-bec0-38e1a8da78b0.png">
<br />


<br />
<br />

### Requiremets

1. Python 3 <br />
2. pandas <br />
3. faker <br />
4. urllib <br />
5. numpy <br />
6. seaborn (Graphing/Plotting) <br />
7. sklearn <br />
8. pickle <br />
9. tensorflow <br />
10. transformers (pip install -q git+https://github.com/huggingface/transformers.git) <br />
11. selenium (and the preferred web driver)


<br />
<br />

#### machine learning architecture

<br />

<img width="481" alt="1" src="https://user-images.githubusercontent.com/57047863/156202137-d345ffb1-82d7-492d-b9ea-f18c8d3e63aa.png">

<br />
<br />

### How to use
go to 'Malicious URL Detection' folder  <br /> <br />

### Train A Model (Basic Model/Mixed Data Model)
<br />

#### Basic Model (based on the 'url_data.scv' dataset) and 'url_classification.ipynb' notebook
1. run the 'url_classification.ipynb' file <br /> 


<br /> 

#### Mixed Data Model (based on the 'mixed_data.scv' dataset) and 'url_classification-artificial-data.ipynb' notebook
1. create the artificial sub datasets (using 'url_data_generator.py', 'scraping_automation.py' and transformers.ipynb) <br /> 
2. run the 'url_classification-artificial-data.ipynb' file <br /> 

<br />
<br />
 
### Use The Model

1. run the 'prediction.py' file <br /> <br />

<br />
<br />

<img width="590" alt="2022-02-10" src="https://user-images.githubusercontent.com/57047863/153758121-b667c4e9-46c3-4041-a11c-a4bb89441128.png">

<br />
<br />

<img width="608" alt="2022-02-10 (1)" src="https://user-images.githubusercontent.com/57047863/153758139-7ab41c1c-931f-41da-b384-675b4ec0695c.png">
