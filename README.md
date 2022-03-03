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


#### 1. generate pattern of Malicious URL by using 'DGA' algorithm

<br />
<img width="764" alt="2022-02-19 (7)" src="https://user-images.githubusercontent.com/57047863/154812551-bb277bd5-6e4f-45d8-b3e2-52e95eff52ed.png">
<br />
<br />

#### 2. scraping URL data from the internet

<br />
<img width="868" alt="2022-02-19 (5)" src="https://user-images.githubusercontent.com/57047863/154812256-a5e451a8-1c8d-427e-8aaf-2f34da69a774.png">
<br />
<br />

#### 3. language generation with 'Transformers' (generate new urls using Transformers)

<br />
<img width="712" alt="2022-02-19 (2)" src="https://user-images.githubusercontent.com/57047863/154808352-27642fa1-a0c5-4521-822e-6a1ae6e9dbfe.png">
<br />
<img width="474" alt="2022-02-19 (1)" src="https://user-images.githubusercontent.com/57047863/154808366-cb17080b-cec6-4a42-bec0-38e1a8da78b0.png">
<br />

<img width="468" alt="2022-03-02 (5)" src="https://user-images.githubusercontent.com/57047863/156618074-04e1b96c-d6dc-47fb-a045-411a6853915b.png">
<br />
<img width="383" alt="2022-03-02 (6)" src="https://user-images.githubusercontent.com/57047863/156618228-d942f0d5-4f29-4ae7-9234-bbc6ed7149c4.png">
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

1. run the 'prediction.py' file <br /> 
2. insert URL for prediction <br />

<br />
<br />

<img width="876" alt="2022-03-02" src="https://user-images.githubusercontent.com/57047863/156618977-e52d00cf-cc4f-485a-a4fe-98b91a9e064d.png">

<br />
<br />

<img width="875" alt="2022-03-02 (1)" src="https://user-images.githubusercontent.com/57047863/156619122-2bf03f4d-16bf-4d37-b7ca-e1550bde0013.png">

<br />
<br />

<img width="887" alt="2022-03-02 (2)" src="https://user-images.githubusercontent.com/57047863/156619334-a7d1f6d5-8698-4ff6-8742-5e81a9cd6fb9.png">

<br />
<br />

<img width="862" alt="2022-03-02 (3)" src="https://user-images.githubusercontent.com/57047863/156619458-e58c7f44-a5ff-4eee-a836-c43136fb3ff9.png">
