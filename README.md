# JobCruncher


<p align="center">
<img src="https://user-images.githubusercontent.com/52947925/194793741-d5de162e-f915-4187-b463-24300f0ab215.gif">
</p>


[![GitHub](https://img.shields.io/github/license/TejasPrabhu/Job-Analyzer)](https://github.com/TejasPrabhu/Job-Analyzer/blob/main/LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub issues](https://img.shields.io/github/issues-raw/TejasPrabhu/Job-Analyzer)](https://github.com/TejasPrabhu/Job-Analyzer/issues?q=is%3Aopen+is%3Aissue)
[![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/TejasPrabhu/Job-Analyzer)](https://github.com/TejasPrabhu/Job-Analyzer/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub contributors](https://img.shields.io/github/contributors/TejasPrabhu/Job-Analyzer)](https://github.com/TejasPrabhu/Job-Analyzer/graphs/contributors)
![GitHub repo size](https://img.shields.io/github/repo-size/TejasPrabhu/Job-Analyzer)
[![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/TejasPrabhu/Job-Analyzer)](https://github.com/TejasPrabhu/Job-Analyzer/pulls?q=is%3Aopen+is%3Apr)
[![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/TejasPrabhu/Job-Analyzer)](https://github.com/TejasPrabhu/Job-Analyzer/pulls?q=is%3Apr+is%3Aclosed)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/TejasPrabhu/Job-Analyzer/unit-tests)
[![codecov](https://codecov.io/gh/TejasPrabhu/Job-Analyzer/branch/main/graph/badge.svg)](https://codecov.io/gh/TejasPrabhu/Job-Analyzer)
[![DOI](https://zenodo.org/badge/542878273.svg)](https://zenodo.org/badge/latestdoi/542878273)



Juggling multiple assignments, quizzes, projects, presentations, and clutching the deadlines every week? Feel like you have no time to watch your favorite series or sports team play let alone search for job posting on a day-to-day basis? Here comes JobCruncher.

JobCruncher is an online job scraping and analysis tool that provides the user with the ability to filter jobs posted on Linkedin based on the user’s interest. LinkedIn is an employment-oriented online service that is a platform primarily used for professional networking and career development. This allows job seekers to post their CVs and employers to post jobs, hence a perfect site to scrap the job details from.

So, leave the tedious and monotonous task of looking up the job postings to our JobCruncher that not only provides the jobs posted every day but helps to filter out the results based on your liking.

# So why use JobCruncher instead?
Unlike many other job portals, JobCruncher is a simple, lightweight, online tool that helps users get clear information about the jobs posted on LinkedIn and further help the user finetune the results.

Further, it helps to provide the user insights about the job postings and as the scraper is executed every day, the user is always provided with the most recent job postings.


# Installation

## Installing Python 3.10.6

This document gives the instructions to install Python 3.10.6 [document](https://www.python.org/downloads/release/python-3106/).


## All OS (Linux, Mac and Windows)

### 1. Mac OS

[Download Python 3.10.6 for Mac OS](https://www.python.org/ftp/python/3.10.6/python-3.10.6-macos11.pkg).

### 2. Windows

[Download exe for python 3.10.6 for windows](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe).


###### Python 3.10.6 cannot be used on windows 7 or earlier

  

Open the `.exe` Installer.


Answer few questions.


* Press `Enter` to review the license.

* press `Enter`.

* Set an installation path and press `Enter`.

* Congratulations! Python 3.10.6 is installed.

  

### 3. Linux

  

* Open command terminal

  

* Install required dependency

  

	```

	sudo apt install software-properties-common -y

	```

  

* Install python 3.10.6

	```

	sudo apt install python3.10.6

	```

  

# Installing Visual Studio Code

  

## All OS (Linux, Mac and Windows)

  

### 1. Mac OS

  

* [Download Vistual studio](https://go.microsoft.com/fwlink/?LinkID=534106)

  

* Double click on archive

  

* Congrats, your visual studio app is downloaded!

  

### 2. Windows

  

* [Download installer for VSCode](https://go.microsoft.com/fwlink/?LinkID=534107)

  

* Run the installer

  

* If not given any location, VS code will be installed in programs folder of C drive

  

### 3. Linux

  

* Installing using GUI, open Ubuntu software center.


* Click search button and search for vscode.


* Install it, you will be able to see it installed in applications after some time.


### 4. MongoDB

  

* [Download the MongoDB MSI Installer Package](https://www.mongodb.com/try/download/community)

  

*  Install MongoDB with the Installation Wizard and make sure you are logged in as a user with Admin privileges.

  

* If not given any location, VS code will be installed in programs folder of C drive.


# Tech Stack used for the development of this project
 
 <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="python" width="20" height="20"/> Python </br>
 <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original.svg" alt="mongo" width="20" height="20"/> MongoDB </br>
 <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-plain.svg" alt="flask" width="20" height="20"> Flask </br>
 <img src="https://user-images.githubusercontent.com/52947925/194781771-ccf8e200-6b64-41ae-9eac-65f73367f377.svg" alt="selenium" width="20" height="20"> Selenium </br>
 <img src="https://user-images.githubusercontent.com/52947925/194781751-eb3701f1-3770-45d0-824d-721e73711111.svg" alt="pytest" width="20" height="20"> Pytest </br> 


## Phase 2:
  1.	**Deploying on AWS** – The main idea is to make JobCruncher serverless. Removing the need for a local server and pushing to the cloud amplifies usability. Using AWS lambda, S3, Cloudwatch, and SNS services to schedule jobs for every X hours to scrap job listing from each employee-oriented site.

  2.	**User Profile** – Adding the feature of the user profile to JobCruncher provides the functionality of extracting the vital features from user information and accordingly deduces the scraped job based on the extracted feature.

  3.	**Features from Resume** – The user can upload a Resume / CV and cover letter. Using text analysis we can extract the cardinal features such as technical skills, projects, experience, and job position, and cater to the user’s job search needs.
  4.	**Notification System** – In phase 2, as every user has a unique profile associated with them, a notification system can be set up in order to notify the user of any new job updates.

  5.	**Chatbot Integration** – This is a feel-good feature that provides the user with an easy-to-interact chatbot that provides information and ways to access the features provided by JobCruncher.
 
## Contributors
Thanks goes to these wonderful people. 

<table>
  <tr>
    <td align="center"><a href="https://github.com/kartikrawool"><img src="https://avatars.githubusercontent.com/u/55804665?v=4" width="100px;" alt=""/><br/><sub><b>Kartik Rawool</b></sub></a></td>
    <td align="center"><a href="https://github.com/Naveen-Jayanna"><img src="https://avatars.githubusercontent.com/u/52947925?v=4" width="100px;" alt=""/><br/><sub><b>Naveen Jayanna</b></sub></a></td>
    <td align="center"><a href="https://github.com/samarth-p"><img src="https://avatars.githubusercontent.com/u/42717178?v=4" width="100px;" alt=""/><br/><sub><b>Samarth Purushothaman</b></sub></a></td>
    <td align="center"><a href="https://github.com/TejasPrabhu"><img src="https://avatars.githubusercontent.com/u/100992314?v=4" width="100px;" alt=""/><br/><sub><b>Tejas Prabhu</b></sub></a></td>
    <td align="center"><a href="https://github.com/crmgogo"><img src="https://avatars.githubusercontent.com/u/55990000?v=4" width="100px;" alt=""/><br/><sub><b>Shubham Loya</b></sub></a></td>
  </tr>
</table>
