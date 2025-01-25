# MultipurposeWebTool

## 1- Introduction

As the name suggests, MultipurposeWebTool is a versatile web application that enables you to take down notes, maintain a journal, manage your budget, track your savings, and observe the weather in a particular location. It has been created with Python Django and provides easy to use interface.

## 2- Features
MultipurposeWebTool aims to provide features that can assists to people in their daily tasks and plans. It can be seen as a web application that aims to be open in your side tab while you spend time in front of the computer while planning your budget, the work you will do, and jotting down your thoughts.

### 2.1 - Notes
Notes page allows user to create a note up to 1600 characters. User can display the created notes with their title, category(tag), date of last edition. Notes can be updated or deleted if desired. 

### 2.2 - To Do List
Users can be able to create a To Do List with this page. Tasks are displayed with their deadlines, titles and descriptions. If user choose the completion status as done, the task is seen with strikethrough. The tasks can be updated or deleted if desired also.  

### 2.3 - Budget
Budget page focuses on planning and monitoring users' budget with savings and expenses. Users can input their incomes, outcomes or investments with their amounts, categories, descriptions and dates. Page stores and displays the total income, outcome and investments in the current month. After all, user can download its budget breakdown as Excel format. 

### 2.4 - Assets
Users can keep an account of their savings with assets page. User can record their possessions with their currency types, amounts and dates. User can view their savings with time-based line graphs and can also view the distribution of their assets with pie chart. This page uses evds api to get currency exchange rates.

### 2.5 - Weather
Weather page lets users create locations with their latitudes and longitudes and view the weather forecast for that location. Weather page uses OpenWeatherMap api to get the weather conditions.

## 3- Installation
I recommend using anaconda environments when installing MultipurposeWebTool because of its ease of management and isolation of dependencies.

### 3.1 - Clone the Repository
```
git clone https://github.com/emretasar/MultipurposeWebTool.git
cd MultipurposeWebTool
```
### 3.2 - Create Conda Environment
```
conda create --name MultipurposeWebTool --file spec-file.txt
conda activate MultipurposeWebTool
```
### 3.3 - Make Migrations
```
python manage.py makemigrations
python manage.py migrate
```
### 3.4 - Run
```
python manage.py runserver
```

Also keep in mind that the MultipurposeWebTool uses following APIs to gather necessary data.
- [EVDS API](https://evds2.tcmb.gov.tr/index.php?)
- [OPENWEATHER API](https://openweathermap.org/)

To be able to run MultipurposeWebTool, you should create local_settings.py files inside assets and wheather projects and store your API credentials inside them.

## 4- Usage

You can watch the sneak peek video that shows how to use the MultipurposeWebTool in the below link. 
[![MultipurposeWebTool](https://img.youtube.com/vi/M3XKuE3eeSg/0.jpg)](https://www.youtube.com/watch?v=M3XKuE3eeSg)

## 5- Feature Enhancements
## 6- License







  



