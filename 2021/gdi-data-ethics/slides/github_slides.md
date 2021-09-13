---
title: "<h2>Building Ethical Data Models</h2> <br> <img src='https://images.squarespace-cdn.com/content/v1/5c1c2963e17ba34123cd873f/1545349619440-91VG3UWSI57TENTLIN9U/GDI+logo.PNG?format=1500w' height='80' >"
author: "Vivek Katial"
date: "08/09/2021"
output: revealjs::revealjs_presentation
---
<style type="text/css">
  .reveal ul {
    display: block;
  }
  .reveal ol {
    display: block;
  }
  .reveal code {
    font-family: monospace;
    color: #48e255;
  }
</style>

- Check out the slides at https://tinyurl.com/vk-gdi-ethics

# Introduction

## About Me

>- Disclaimer: **I am not an expert in ethics and philosophy**
>- Vivek Katial (vkatial@student.unimelb.edu.au)
>  - PhD Candidate (Optimisation on Quantum Computers)
>  - Data Scientist (5 years - Quantiful, Multitudes)
>- I love traveling and trying new types of food and meeting interesting people

>- <img src="https://instagram.fakl8-1.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/192174776_835204797412194_5166168999853458133_n.jpg?_nc_ht=instagram.fakl8-1.fna.fbcdn.net&_nc_cat=106&_nc_ohc=aIiikwK_zmoAX9zgol2&edm=AP_V10EBAAAA&ccb=7-4&oh=129a3e1eddc5fc89c928a3300df05803&oe=613EC2DF&_nc_sid=4f375e" alt="Vivek at Uluru" height="30%" width="30%">

## What are / is ethics?

>- The word “Ethics” is derived from the Greek word Ethos, meaning habit or custom. 
>- Ethics help us distinguish between right and wrong.
>- Many schools of thoughts that philosophers have argued over for centuries.
>- We are going to assume that whatever there is social consensus on today, is our view on ethics.

## Robert McDaniel 

<img src='https://cdn.vox-cdn.com/thumbor/MGScoEVQmSsnRKGhzr4HelqymvQ=/140x219:1911x1149/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/22535737/4542_Social_3.jpg' height='400' >

## Predictive Policing

<img src='https://rss.onlinelibrary.wiley.com/cms/asset/f30ca57c-f0ec-49a5-a444-9f15ca790b9f/sign960-fig-0001-m.jpg' height='400' >

## Why do we need to consider ethics in Data Science?
>- Fastest growing industry, expected to continue
>- Often undesirable consequence can occur. Especially in relation to, privacy, fairness, etc.
>- Considering *ethics* provides us a framework to decide what is "OK" to do.

## Agenda
>- Data Governance
>- Bias
>- Data Collection
>- Model Building

# Data Governance

>- Privacy
>- Anonymity

## Privacy

>- Handling data needs to respect confidentiality and anonymity
>- How do we avoid harm that can occur due to data about us being collected, linked and analysed?
>- Internet archives hold information forever

## Privacy - Collection vs Use
>- Your ID is taken at a club (Name, address, age)
>    - How is this data being used?
>    - Is this data stored or sold elsewhere?

## Anonymity

<img src='https://i.kym-cdn.com/photos/images/facebook/000/427/561/7ad.jpg' height='400' >

## Anonymity

>- Some anonymous services **do** exist:
>   - Using `tor` the onion browser
>   - One can pay using Bitcoin, or other crypto currencies
>- Most services require some sense of ID

<!-- Provide an example of ego surfing 
- Search for yourself on the internet
- Most people ego-surf periodically
- Most people don't repeatedly look for the same person
- Web search company, without any information, can look at your search history adn identify you
-->

# Algorithimic Bias

## Algorithimic Bias

What does bias actually mean?

## Algorithimic Bias
<img src='https://images.immediate.co.uk/production/volatile/sites/30/2020/02/pears-28f8900.jpg?quality=90&resize=385%2C350' height='400' >

>- Pear, sliced apple

## Algorithimic Bias
<img src='http://specialtyproduce.com/sppics/16898.png' height='400' >

>- Red Pear, Read Sliced Pair

## Bias

>- Humans label and categorise the world to reduce complex sensory inputs into **simple** groups that we can understand
>- For everything, our minds create 'typical' representations of a concept or objects
>- We thus notice "atypical things"
>- **Biases** and **stereotypes** arise when particular labels and features confound our decisions

## Facial Recognition

<img src='https://scontent.fakl8-1.fna.fbcdn.net/v/t1.15752-9/240876020_556003005825787_2104600819249760598_n.png?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_ohc=Hx6dpzVk6g4AX_qT_oK&_nc_ht=scontent.fakl8-1.fna&oh=f016f201796953fe48f6dc6ae6921b92&oe=615EE343' height='400' >

## Facial Recognition

<img src='https://scontent.fakl8-1.fna.fbcdn.net/v/t1.15752-9/240758535_375784523987104_3014957741791250259_n.png?_nc_cat=100&ccb=1-5&_nc_sid=ae9488&_nc_ohc=OHJH4vRj0HQAX9IcINq&tn=MlIYbC6yL9GaFzeg&_nc_ht=scontent.fakl8-1.fna&oh=dac9e8fe785d92d68a4f4116be078a0a&oe=615D91B2' height='400' >

## Understanding why?

<img src='https://scontent.fakl8-1.fna.fbcdn.net/v/t1.15752-9/241359038_1719589021544885_6273264584288949063_n.png?_nc_cat=101&ccb=1-5&_nc_sid=ae9488&_nc_ohc=mYLzVH49PLkAX8_UIHy&tn=MlIYbC6yL9GaFzeg&_nc_ht=scontent.fakl8-1.fna&oh=db887637a26e15522b0ca1e053679af6&oe=615E2991' height='400' >

## The Machine Learning Lifecycle
>- Data collection and preparation
>- Feature engineering and selection
>- Model formulation and training
>- Model deployment and evaluation
>- Interpretation and decisions

## Data Collection
>- Data selection does not reflect real-world distribution
>- Frequency in training data distributed differently
>- Model performance skews to perform better on classes present in the data

## Data Collection
<img src='https://scontent.fakl8-1.fna.fbcdn.net/v/t1.15752-9/241533851_4239218889532966_8608497518533609337_n.png?_nc_cat=100&ccb=1-5&_nc_sid=ae9488&_nc_ohc=g4J1CRdyogAAX_lmrTo&_nc_ht=scontent.fakl8-1.fna&oh=b153c0e3e88d76f9d0af0040991b1b8f&oe=615EF820' height='400'>

## Data Collection

<img src='https://scontent.fakl8-1.fna.fbcdn.net/v/t1.15752-9/241177341_1201555303668533_5007028722220760051_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=I_aw7Hr76JoAX_KS0UH&tn=MlIYbC6yL9GaFzeg&_nc_ht=scontent.fakl8-1.fna&oh=6c2c07e0521f43d31efb7bd06947cfdb&oe=615FC6C1' height='400'>

## Is this bad?
>- Very common issue in many classification problems
>- Dangerous in healthcare applications
>- Consider a MRI tumour prediction algorithm (99% are )

## Mitigation
>- Batch Selection
>   - Feed samples to the training in balanced manner
>- Adjust cost function
>- Oversample datapoints from the lower dataset

## Modelling and Feature Engineering
>- Bias Mitigation
>   - Bias data, model
>   - Remove aspects/features that are causing bias (LIME) 
>- Inclusion
>   - Biased Model, dataset
>   - Add signal to features that improve fairness

## Evaluation
>- Use balanced datasets for evaluation
>- Compare accuracy to de-bias models
  >- Performance metric should be the error (between different subclasses)
  >- Measure distribution shifts


## Conclusions

>- Follow AI Best practices
  >- Dataset Docs (Gebru 2018)
  >- Model Reporting and Curation
  >- Transparency and reproducibility
>- R&D in algorithm research

## Extra Links / Resources
- [Robert McDaniel](https://www.theverge.com/22444020/chicago-pd-predictive-policing-heat-list)
- [Making a racist AI](https://www.theverge.com/22444020/chicago-pd-predictive-policing-heat-list)
- [Coursera MOOC on Data Ethics](https://www.theverge.com/22444020/chicago-pd-predictive-policing-heat-list)
- [Automating Inequality](https://www.theverge.com/22444020/chicago-pd-predictive-policing-heat-list)
- [Weapons of Maths Destruction](https://www.theverge.com/22444020/chicago-pd-predictive-policing-heat-list)

# Thank You!
vivek@gooddatainstitute.com


