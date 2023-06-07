[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8819507&assignment_repo_type=AssignmentRepo)

# COMP0035 Coursework 2022-23: Traffic Monitoring App

To set up the project in your python coding environment (IDE):

1. Clone the repository in your IDE (e.g. PyCharm, Visual Studio Code) from GitHub. Follow the help in your IDE.
2. Add a virtual environment (venv). Use the instructions for your IDE
   or [navigate to your project directory and use python.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the requirements from requirements.txt. Use the instructions for your IDE
   or [use python in your shell.](https://pip.pypa.io/en/latest/user_guide/#requirements-files).
4. Edit .gitignore to add any config files and folders for your IDE. PyCharm, VisualStudio Code, Xcode and NetBeans have
   already been added.
   
   
## Functionality & Context of the Application

The Traffic Monitoring App is designed to provide users with insights into traffic volumes and the factors that impact them in the Minneapolis and St Paul area. The target users of the app include:

* General public users residing near Minneapolis and St Paul
* Environmentalist-policy makers who can utilize the app to guide their policies and research
* Logistics services or delivery couriers who frequently pass through Interstate 94 Westbound and rely on quick and accurate traffic insights

The app enables users to analyze historical traffic data from the MN DoT ATR station, helping them identify patterns and factors influencing traffic volumes. By applying filters that match their specific circumstances, users can make informed decisions about their commuting habits and predict traffic volumes based on specific conditions or days.

## Dataset

The excel datafile [Available here](https://archive.ics.uci.edu/ml/datasets/Metro%20Interstate%20Traffic%20Volume) comprises hourly Interstate 94 Westbound traffic volume for MN DoT ATR station 301, roughly midway between Minneapolis and St Paul, MN. The data ranges from November 2012 to September 2018 and includes attributes such as weather features and holidays to determine impacts on traffic volume.


