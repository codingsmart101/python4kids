# Week 8 Homework Task - A Basic Activity Tracker Algorithm

We learned how to use the accelerometer on Micro:bit and stream its measurement data to a receiving Micro:bit via radio connection. This platform enables us to collect a lot of sensor data from Micro:bit and this homework task will utilise accelerometer to track body activity, for example: running. Follow the below steps to accomplish a basic algorithm to measure your running activity.

1. Prepare your Micro:bit pair, one is battery powered and used for acceleration measurement. Another one connected to your Mu Edictor’s Plotter function and receives the radio data from the other Micro:bit. 
1. Perform a running activity and check the logged data by Mu Editor. 
1. Upload your “.csv” file which contains the accelerometer measurement ( you can find it in “data capture” folder from “mu_code” ( perform a Windows Search to find the directory of the “mu_code”). Make sure the capture time indicated by “.csv” file name matches your measurement time. 
1. Upload the “.csv” file to your Google Drive, As we covered in class, open the file with Google Sheet and add headers (time, x, y, z)  to the data table, visualise your data by creating a line chart for each axis. Identify your activity duration and data features from the chart.
1. Use Python code to perform data analysis, open the “Week9” Google Colab Notebook, and mount your Google Drive with the Colab Notebook. 
1. Once the Google Drive is mounted, it’s connect can be list by command: 
   
   `!ls /gdrive/MyDrive/`

	If you place your .csv file on a folder called “week9” at the upper most level of your Google Drive, then do the following command to find your files: 
   
   `!ls /gdrive/MyDrive/week9` 

	It is recommended not using space in your folder name or file name, to avoid any unknown issues. 

1. Follow the example code in the “week9” notebook to make a line chart and visualise your data. 
1. A hit for counting the running steps in Included in the example code. Think about your own way for counting the steps and implement it in the notebook. 

This homework shows a process of conducting experiments with data analysis. In the next class we will learn more practical skills for data analysis, stay tuned. 

