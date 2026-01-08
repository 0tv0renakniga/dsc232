# Milestone 1
## Abstract, Data, and Group Selection
### Description (**Points: 10**)
- Abstract submission is worth 10 points out of 100. If you do can not create your own group, you will be randomly assigned one. A signup sheet for those of you that would like to be randomly assigned has been made available. See above.

- Please submit your abstract along with a short description of your data, and a link to your data, as well as a list of your partners and their UCSD emails. Any deviation from this will result in a loss of points. Make sure you chose a dataset that does not have what you would like to do already published. If we see that there is overlap in what you would like to do with the project, it will be rejected.

- All late submissions and rejected abstracts will not be awarded credit, but we will allow you to resubmit late for review only and not for credit. A different late credit assignment for the 1st milestone will be released after the due date for review purposes only. You must have your abstract approved before submitting subsequent milestones.

- The abstract should be one paragraph. Please do not write more than one paragraph. You can find more information on how to create an abstract [here](https://www.grammarly.com/blog/academic-writing/write-an-abstract/). You are also welcome to look at abstract examples on Google Scholar or Web of Science.

- Submit to [Gradescope](https://www.gradescope.com/login)

- You will need to submit your abstract and data description to this assignment on Gradescope using the text box provided in Gradescope. Your instructional team will then review your abstract, provide feedback and contact you if revisions are needed to move forward in the project at which point you will be invited to resubmit. If revisions are needed, points will be deducted, but once you resubmit, address the comments and the abstract is approved, you can recover your points for full credit.

# Milestone 2
## Data Exploration and Initial PreProcessing
### Description (**Points: 15**)
- **Your submission will be a link to your GitHub Repository.**

- In this assignment you will need to:

    - Create a GitHub ID.
    - Create a GitHub Repository (Public or Private, it is up to you. In the end it will have to be Public.) and add your group members as collaborators.
    - Perform the data exploration step (i.e. evaluate your data, # of observations, details about your data distributions, scales, missing data, column descriptions) Note: For image data you can still describe your data by the number of classes, # of images, plot example classes of the image, size of images, are sizes uniform? Do they need to be cropped? normalized? etc.
    - Plot your data. For tabular data, you will need to run scatters, for image data, you will need to plot your example classes.
    - How will you preprocess your data? You should explain this in your README.md file and link your Jupyter notebook to it. All code and Jupyter notebooks have be uploaded to your repo.
You must also include in your Jupyter Notebook, a link for data download and environment setup requirements: 
        - !wget !unzip like functions as well as !pip install functions for non standard libraries not available in colab are required to be in the top section of your jupyter lab notebook. Or having the data on GitHub (you will need the academic license for GitHub to do this, larger datasets will require a link to external storage).

- Note: You will still be able to of course edit your GitHub repo for the data exploration part for your final submission, but we will grade this part of your submission as if it were finalized for milestone2 given the deadline! Only commits before the deadline will be used to evaluate your submission. You are expected to finalize the data exploration by Sunday of next week.

- Important: Prior to submitting, create a branch of your main Repo named Milestone2

- Any git commits past the deadline will not be considered!

- Submit your GitHub URL for your Milestone2 branch.

# Milestone 3
## Data PreProcessing
### Description (**Points: 30**)
- In this milestone, you will continue working on your main branch, and focus on finishing any preprocessing and build your first model. You will also need to evaluate your this model and see where it fits in the underfitting/overfitting graph.

1. Finish major preprocessing. This includes scaling and/or transforming your data, imputing your data, encoding your data, and feature expansion (example is taking features and generating new features by transforming via polynomial, log multiplication of features).

2. Train your first model.

3. Evaluate your model compare training vs. test error.

4. Where does your model fit in the fitting graph?

5. What are the next models you are thinking of and why?

6. Update your README.md to include your new work and updates you have all added. Make sure to upload all code and notebooks. Provide links in your README.md.

7. Conclusion section: What is the conclusion of your 1st model? What can be done to possibly improve it?

- Please make sure preprocessing is complete and your first model has been trained. If you are doing supervised learning, include example ground truth and predictions for train, validation, and test. 

- Important: Prior to submitting, create a branch of your main Repo named Milestone3

- Any git commits past the deadline will not be considered!

- Submit your GitHub URL for your Milestone3 branch.

# Milestone 4
## Second Model and Final Submission
### Description (**Points: 40**)
- This is the graded part of the final submission of your Group Project. The listed due date is below and @ 11:59 p.m.

- Your next model must undergo the same requirements as the previous model for evaluation. Please see the previous milestone for clarification. You will update your README.md in your main branch.

- You will require the following in your README.md:

    - A complete Introduction
    - A complete submission of all prior submissions
    - All code uploaded in the form of Jupyter notebooks that can be easily followed along to your GitHub repo
    - A completed write that includes the following
        - **Introduction** of your project: Why chosen? Why is it cool? General/Broader impact of having a good predictive mode. i.e., Why is this important?
        - **Figures** (of your choosing to help with the narration of your story) with legends (similar to a scientific paper): For reference you search machine learning and your model in google scholar for reference examples.
        - **Methods** section: This section will include the exploration results, preprocessing steps, models chosen in the order they were executed. Parameters chosen. Please make sub-sections for every step (i.e., Data Exploration, Preprocessing, Model 1, Model 2, additional models are optional). Note: Models can be the same (i.e., DNN but different versions of it if they are distinct enough. Changes can not be incremental.) You can put links here to notebooks and/or code blocks using three ` in markup for displaying code. so it would look like this: 
        ```python 
        MY CODE BLOCK
        ```
            - Note: A methods section does not include any why. The reason why will be in the discussion section. This is just a summary of your methods.
        - **Results** section: This will include the results from the methods listed above (C). You will have figures here about your results as well.
            - No exploration of results is done here. This is mainly just a summary of your results. The sub-sections will be the same as the sections in your methods section.
        - **Discussion** section: This is where you will discuss the why, and your interpretation and your thought process from beginning to end. This will mimic the sections you have created in your methods section as well as new sections you feel you need to create. You can also discuss how believable your results are at each step. You can discuss any short comings. It's okay to criticize as this shows your intellectual merit, as to how you are thinking about things scientifically and how you are able to correctly scrutinize things and find short comings. In science, we never really find the perfect solution, especially since we know something will probably come up in the future (i.e., donkeys) and mess everything up. If you do, it's probably a unicorn or the data and model you chose are just perfect for each other!
        - **Conclusion** section: This is where you do a mind dump on your opinions and possible future directions. Basically, what you wish you could have done differently. Here you close with final thoughts.
        - **Collaboration** section: This is a statement of contribution by each member. This will be taken into consideration when making the final grade for each member in the group. Did you work as a team? Was there a team leader? Project manager? Coding? Writer? etc. Please be truthful about this as this will determine individual grades in participation. There is no job that is better than the other. If you did no code but did the entire write up and gave feedback during the steps and collaborated, then you would still get full credit. If you only coded but gave feedback on the write up and other things, then you still get full credit. If you managed everyone and the deadlines and setup meetings and communicated with teaching staff only, then you get full credit. Every role is important as long as you collaborated and were integral to the completion of the project. If the person did nothing. they risk getting a big fat 0. Just like in any job, if you did nothing, you have the risk of getting fired. Teamwork is one of the most important qualities in industry and academia!!!
        - Start with Name: Title: Contribution. If the person contributed nothing then just put in writing: Did not participate in the project.
    - Your final model and final results summary will go in the last paragraph in of Part D.
    - Your GitHub repo must be made public by the morning of the next day of the submission deadline.
- Note: The 5 left over points will be awarded for participating in the voting event. Voting will be released and you will have 2 days to decide on your top 3 favorite projects. You can vote for yourself, but you cannot vote for any one group more than once. You must submit 3 votes to get credit.

# Milestone 5
## Voting
### Description (**Points: 5**)
- You must vote for your top 3 groups. You cannot get credit if you do not vote for 3 groups, voting for your own group is allowed.

- Note: You are allowed to vote for any single group only once. If you cast more than 1 vote for a single group you will get 0 credit and your votes will be nullified.

- Also, group numbers will be randomly assigned.
