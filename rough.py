""" 
 The above code is written in Python and it is importing several libraries such as pandas,
 webbrowser, and tkinter.
"""
import pandas as pd
import webbrowser
import tkinter as tk
from tkinter import filedialog ,messagebox
import os

"""
 The above code is creating two empty pandas DataFrames named df1 and df2.
"""
df1 = pd.DataFrame
df2 = pd.DataFrame

def Main_page_content():
    """
     The function Main_page_content() is used to define the content of the main page.
    """
    """ 
     The above code is defining the content of a main page in HTML. It includes CSS styling for the
     page, a title, a heading, and two buttons. The buttons have onclick events that call JavaScript
     functions to open a file dialog and redirect to a different page based on the selected file. The
     code also includes a hidden file input element and a JavaScript function to handle the file
     selection and redirection.
    """
    main_page_content = """
    <html>
    <head>
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-image: linear-gradient(to right, #DECBA4, #3E5151);
        }
        h1 {
            text-align: center;
            color: #3E5151;
            font-size: 100px;
            margin-top: 80px;
            text-shadow: 5px 2px #222324, 2px 4px #222324, 3px 5px #222324;
        }
        .button-container {
            display: inline-grid;
            text-align: center;
            margin-top: 120px;
            grid-template-columns: 1fr 1fr;
            grid-gap: 200px;
        }
        .button {
            background-color: #D0D0D0;
            color: #3E5151;
            padding: 10px 20px;
            border: 5px solid #3E5151;
            border-radius: 5px;
            font-size: 20px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #F0F0F0;
            color: #3E5151;
        }
        </style>
        <script>
            function open_excel1() {
                window.location.href = 'Dashboard.html';
            }
            function open_excel2() {
                window.location.href = 'Dashboard2.html';
            }
        </script>
        </head>
        <body>
        <div class="w3-container w3-cursive w3-center w3-animate-top">
            <title>Main</title>
            <h1>Welcome To Dashboard!</h1>
            <div class="button-container">
                <button class="button" onclick="openFileDialog('porsc.html')">project - X01976_PORSC_992_FAD_Produktaufwertung_FAD</button>
                <button class="button" onclick="openFileDialog('Dashboard.html')">Project - T1XX_GLOBAL B</button>
            </div>
            <input type="file" id="file-input" style="display: none;">
        </div>
        <script>
            function openFileDialog(nextPage) {
                const fileInput = document.getElementById('file-input');
                fileInput.click();
                fileInput.addEventListener('change', function(event) {
                    const selectedFile = event.target.files[0];    
                    console.log('Selected file:', selectedFile);
                    if (selectedFile) {
                        window.location.href = nextPage;  
                    }   
                });
            }
        </script>
        </body>
    </html>
    """

    """ 
     The above code is opening a file named 'Main.html' in write mode and writing the content of the
     variable 'main_page_content' to the file. After writing the content, the file is closed.
    """
    with open('Main.html', 'w') as f:
        f.write(main_page_content)
    f.close()
    
"""
The above code is calling a function named Main_page_content().
"""
Main_page_content()

def open_file_dialog(file_num):
    """
    The function open_file_dialog opens a file dialog box.
    
    :param file_num: The file number is a parameter that represents the number of files that can be
    selected in the file dialog
    """
    """
    The above code is declaring two global variables, `df1` and `df2`.
    """
    global df1, df2
    
    """ 
     The above code is using the tkinter and filedialog modules to open a file dialog box and allow
     the user to select an Excel file. If a file is selected, it uses the pandas module to read the
     Excel file into a DataFrame. If the file_num variable is 1, it assigns the DataFrame to df1 and
     prints its shape. If the file_num variable is not 1, it assigns the DataFrame to df2 and prints
     its shape. If no file is selected, it prints "No file selected".
    """
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    
    if file_path:
        if file_num == 1:
            df1 = pd.read_excel(file_path)
            print("DataFrame 1 shape:", df1.shape)
        else:
            df2 = pd.read_excel(file_path)
            print("DataFrame 2 shape:", df2.shape)
    else:
        print("No file selected.")



def dashboard_page_content():
    """
    The function returns the content of a dashboard page.
    """
       
    
    """ 
     The above code is checking if the column 'State' exists in DataFrame 1 (df1). If it does, it
     creates a new DataFrame (df_state) containing only the 'State' column from df1. It then
     calculates the count of each unique value in the 'State' column using the value_counts() method
     and assigns it to the variable state_counts. The index of state_counts (i.e., the unique values
     in the 'State' column) is converted to a list and assigned to the variable state_labels. The
     count values in state_counts are also converted to a list and assigned.
    """
    if 'State' in df1.columns:
        df_state = df1['State']
        state_counts = df_state.value_counts()
        state_labels = state_counts.index.tolist()
        state_values = state_counts.tolist()
    else:
        print("'State' column does not exist in DataFrame 1.")
            
    """ 
     The above code is generating a state chart using the Chart.js library. It creates a pie chart
     with data labels showing the percentage of each state value. The chart is rendered on a canvas
     element with the id "stateChart". The chart's data and options are defined using JavaScript
     variables. The data for the chart is provided through the "state_labels" and "state_values"
     variables. The chart is then created using the Chart.js library and the specified options.
    """
    state_chart_script = f"""
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels"></script>
        <canvas id="stateChart"></canvas>
        <script>
            var ctx_state = document.getElementById('stateChart').getContext('2d');
            var stateData = {{
                labels: {state_labels},
                datasets: [{{
                    data: {state_values},
                    backgroundColor: [
                        '#007bff',
                        '#28a745',
                        '#dc3545',
                        '#ffc107',
                        '#17a2b8',
                        '#6c757d'
                    ]
                }}]
            }};
            var stateOptions = {{
                responsive: true,
                plugins: {{
                    datalabels: {{
                        formatter: (value, ctx) => {{
                            let sum = 0;
                            let dataArr = ctx.chart.data.datasets[0].data;
                            dataArr.map(data => {{
                                sum += data;
                            }});
                            let percentage = (value * 100 / sum).toFixed(2) + "%";
                            return percentage;
                        }},
                        color: '#fff',
                        font: {{
                            weight: 'bold'
                        }}
                    }}
                }}
            }};
            new Chart(ctx_state, {{
                type: 'pie',
                data: stateData,
                options: stateOptions
            }});
        </script>
    """

    """ 
    The above code is defining a Python string variable `porsc_page_content` that contains an HTML
    template. The HTML template includes CSS styles and JavaScript code. It creates a webpage with a
    title, a header, a frame, and a button. The webpage also includes a canvas element with an id of
    "stateChart" and a script tag that references a JavaScript function called `openUserPage()`.
    """
    porsc_page_content = f"""
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            
            <title>Porsc</title>
            <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
            
            <style>
            body {{    
                font-family: Arial, sans-serif;
                padding: 20px;
                background-image: linear-gradient(to right, #DECBA4, #3E5151);
            }}
            #frame-container {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            #frame {{
                width: 700px;
                height: 700px;    
                background-color: #D0D0D0;                
                border: 5px solid #3E5151;
                border-radius: 20px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                padding: 20px;
                box-sizing: border-box;
                text-align: center;
                margin-top: 5px;
            }}
            header.container {{
                color: #333;
                margin-bottom: 10px;
                text-align: center;
            }}
            h1 {{
                text-align: center;
                color: #3E5151;
                font-size: 60px;
                margin-top: 50px;
                text-shadow: 5px 2px #222324, 2px 4px #222324, 3px 5px #222324;
            }}
            title {{
                font-size: 100px;
                height: 50px;
            }}
            #stateChart {{
                display: block;
                margin: 0 auto;
                max-width: 100%;
                max-height: 100%;
            }}
            .button-container {{
                text-align: center;
                margin-top: 100px;
            }}
            .button {{
                background-color: #000000;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
            }}
            .button:hover {{
                background-color: #555555;
                color: #fff;
            }}
            </style>
            <script>
                function openUserPage() {{
                    window.location.href = 'user1.html';
                }}
            </script>
        </head>
        <body>
            <div class="w3-container w3-cursive w3-center w3-animate-top">
                <h1>Project - X01976_PORSC_992_FAD_Produktaufwertung_FAD</h1>
            </div>
            <div id="frame-container">
                <div id="frame">
                    <h2 style="font-size: 30px">SW Release: PAG_PA_D0_010_000_000_20221123_1114_102</h2>
                    <canvas id="stateChart"></canvas>
                    <div class="button-container">
                        <button class="button" onclick="openUserPage()">user</button>
                    </div>
                </div>
            </div>
            {state_chart_script}
        </body>
    </html>
    """

    """
     The above code is writing the content of a web page to a file named "porsc.html". It first opens
     the file in write mode using the `open()` function and assigns it to the variable `f`. Then, it
     writes the content of the web page, which is stored in the variable `porsc_page_content`, to the
     file using the `write()` method. Finally, it closes the file using the `close()` method.
    """
    with open('porsc.html', 'w') as f:
        f.write(porsc_page_content)
    f.close ()
    
    
    """
     The above code is converting a pandas DataFrame object `df1` into an HTML table format and
     storing it in the variable `html_table`.
    """
    html_table = df1.to_html()

    """
     The above code is defining a string variable `table_page_content` that contains an HTML template
     for a web page. The template includes CSS styles for the page layout and a table element. The
     table element will be populated with data from a variable `html_table` (which is not shown in
     the code snippet). The resulting web page will display the table data along with a heading and a
     canvas element for a chart.
    """

    table_page_content = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    padding: 20px;
                    background-image: linear-gradient(to right, #DECBA4, #3E5151);
                }}
                h1 {{
                    color: #3E5151;
                    margin-top: 1px;
                    font-size: 50px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin-top: 20px;
                }}
                th, td {{
                    border: 1px solid #000;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #3E5151;
                    color: #fff;
                }}
            </style>
        </head>
        <body>
            <div class="heading-container">
                <title>Dashboard</title>
                <h1>Table Data</h1>
                <canvas id="chart"></canvas>
            </div>
            <div>
                <table>
                {html_table}
                </table>
            </div>
        </body>
    </html>
    """

    """ 
     The above code is writing the content of a variable called `table_page_content` to a file named
     "user1.html". It opens the file in write mode using the `open()` function and the `'w'`
     parameter. Then, it writes the content to the file using the `write()` method of the file
     object. Finally, it closes the file using the `close()` method.
    """
    with open('user1.html', 'w') as f:
        f.write(table_page_content)
    f.close()

 
def dashboard_page_content_2():
    """
    The function `dashboard_page_content_2` is defined to generate the content for a dashboard page.
    """
    
    # def open_excel2():
    #     root = tk.Tk()
    #     root.withdraw()
    #     file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    #     if file_path:
    #         try:
    #             global df2
    #             df2 = pd.read_excel(file_path)
    #             webbrowser.open('Dashboard.html')
    #         except Exception as e:
    #             print(e)
    #             messagebox.showerror("Error", "Please select a valid Excel file.")
    #     else:
    #         messagebox.showerror("Error", "Please select an Excel file.")
    

    """
     The above code is checking if the column 'State' exists in the DataFrame df2. If it does, it
     creates a new DataFrame df_state containing only the 'State' column from df2. It then calculates
     the count of each unique value in df_state using the value_counts() method and stores the result
     in state_counts. It also creates two lists, state_labels and state_values, which contain the
     unique values and their corresponding counts, respectively. If the 'State' column does not exist
     in df2, it prints a message indicating that.
    """
    
    if 'State' in df2.columns:
        df_state = df2['State']
        state_counts = df_state.value_counts()
        state_labels = state_counts.index.tolist()
        state_values = state_counts.tolist()
    else:
        print("'State' column does not exist in the DataFrame 2.")
    
    """
     The above code is extracting the 'State' column from a DataFrame called 'df2'. It then counts
     the occurrences of each unique state value and stores the counts in the 'state_counts' variable.
     The 'state_labels' variable contains a list of the unique state values, and the 'state_values'
     variable contains a list of the corresponding counts.
    """
    df_state = df2['State']
    state_counts = df_state.value_counts()
    state_labels = state_counts.index.tolist()
    state_values = state_counts.tolist()
        
            
    """
     The above code is generating a pie chart using the Chart.js library. It creates a canvas element
     with the id "stateChart" where the chart will be rendered. The code then defines the data for
     the chart, including the labels and values for each slice of the pie. It also specifies the
     colors for each slice. The code then sets options for the chart, including making it responsive
     and adding data labels with percentage values. Finally, it creates a new Chart object with the
     specified data and options, and renders it on the canvas element.
    """
    state_chart_script = f"""
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels"></script>
        <canvas id="stateChart"></canvas>
        <script>
            var ctx_state = document.getElementById('stateChart').getContext('2d');
            var stateData = {{
            labels: {state_labels},
                datasets: [{{
                    data: {state_values},
                    backgroundColor: [
                        '#007bff',
                        '#28a745',
                        '#dc3545',
                        '#ffc107',
                        '#17a2b8',
                        '#6c757d'
                        ]
                }}]
            }};
            var stateOptions = {{
                responsive: true,
                plugins: {{
                    datalabels: {{
                        formatter: (value, ctx) => {{
                            let sum = 0;
                            let dataArr = ctx.chart.data.datasets[0].data;
                            dataArr.map(data => {{
                                sum += data;
                            }});
                            let percentage = (value * 100 / sum).toFixed(2) + "%";
                            return percentage;
                        }},
                        color: '#fff',
                        font: {{
                            weight: 'bold'
                        }}
                    }}
                }}
            }};
            new Chart(ctx_state, {{
                type: 'pie',
                data: stateData,
                options: stateOptions
            }});
        </script>
    """
        
    """
    The above code is defining a string variable `first_page_content` that contains an HTML template
    for a web page. The template includes CSS styles and JavaScript code. The HTML structure
    includes a header with a title, a main content area with a frame, a canvas element for a chart,
    and a button to navigate to a user page. The template also includes a placeholder
    `{state_chart_script}` which can be replaced with JavaScript code to generate a chart.
    """
    first_page_content = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
            
        <title>Dashboard2</title>
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
            
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
                background-image: linear-gradient(to right, #DECBA4, #3E5151);
            }}
            #frame-container {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            #frame {{
                width: 600px;
                height: 600px;
                background-color: #D0D0D0;
                border: 5px solid #3E5151;
                border-radius: 20px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                padding: 20px;
                box-sizing: border-box;
                text-align: center;
                margin-top: 5px;
            }}
            header.container {{
                color: #333;
                margin-bottom: 10px;
                text-align: center;
            }}
            h1 {{
                text-align: center;
                color: #3E5151;
                font-size: 80px;
                margin-top: 50px;
                text-shadow: 5px 2px #222324, 2px 4px #222324, 3px 5px #222324;
            }}
            title {{
                font-size: 100px;
                height: 50px;
            }}
            #stateChart {{
                display: block;
                margin: 0 auto;
                max-width: 100%;
                max-height: 100%;
            }}
            .button-container {{
                text-align: center;
                margin-top: 70px;
            }}
            .button {{
                background-color: #000000;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
            }}
            .button:hover {{
                background-color: #555555;
                color: #fff;
            }}
            </style>
        <script>
            function openUserPage() {{
                window.location.href = 'user.html';
            }}    
        </script>
    </head>
    <body>
        <div class="w3-container w3-cursive w3-center w3-animate-top">
            <h1>Project - T1XX_GLOBAL B</h1>
        </div>
        <div id="frame-container">
        <div id="frame">
                <h2>SW Release : SW38.0.2</h2>
                <canvas id="stateChart"></canvas>
                <div class="button-container">
                    <button class="button" onclick="openUserPage()">user</button>
                </div>
            </div>
        </div>
        {state_chart_script}
    </body>
    </html>
    """
    
    """
    The above code is writing the content of a variable called `first_page_content` to a file called
    "Dashboard.html". It opens the file in write mode using the `open()` function and the `'w'`
    parameter. Then, it writes the content to the file using the `write()` method of the file
    object. Finally, it closes the file using the `close()` method.
    """
    with open('Dashboard.html', 'w') as f:
        f.write(first_page_content)
    f.close()
        
        
    """
     The above code is selecting specific columns from a DataFrame called `df2` and creating a new
     DataFrame called `df_second` with those selected columns. The selected columns are 'ID', 'Type',
     'Subject', 'State', 'Assigned User', 'Total number of tests executed?', 'Number of tests
     Passed', 'Number of tests Failed', 'Test Report Checkpoint Label', and 'Test Data Checkpoint
     Label'.
    """
    df_second = df2[['ID', 'Type', 'Subject', 'State', 'Assigned User', 'Total number of tests executed?',
                    'Number of tests Passed', 'Number of tests Failed', 'Test Report Checkpoint Label',
                    'Test Data Checkpoint Label']]
    user_data = df_second.to_html(index=False)
        
    """
     The above code is calculating the total number of tests passed and failed from a DataFrame
     called `df_second`. It then creates a list of labels ['Passed', 'Failed'] and a corresponding
     list of values [passed_count, failed_count].
    """
    passed_count = df_second['Number of tests Passed'].sum()
    failed_count = df_second['Number of tests Failed'].sum()
    labels = ['Passed', 'Failed']
    values = [passed_count, failed_count]

    """
     The above code is generating a JavaScript script that creates a pie chart using the Chart.js
     library.
    """
    second_chart_script = f"""
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        var ctx = document.getElementById('chart').getContext('2d');
        var data = {{
            labels: {labels},
            datasets: [{{
                data: {values},
                backgroundColor: [
                    'green',
                    'red'
                ]
            }}]
        }};
        var options = {{
            responsive: true,
            plugins: {{
                legend: {{
                    display: true
                }},
                datalabels: {{
                    formatter: (value, ctx) => {{
                        let sum = data.datasets[0].data.reduce((a, b) => a + b, 0);
                        let percentage = (value * 100 / sum).toFixed(2) + "%";
                        return percentage;
                    }},
                    color: '#fff',
                    font: {{
                        weight: 'bold'
                    }}
                }}
            }},
        }};
        new Chart(ctx, {{
            type: 'pie',
            data: data,
            options: options
        }});
    </script>
    """
        


    """
     The above code is generating the content for the second page of a web application. It is
     creating an HTML page with a title, heading, chart, and a table. The content is styled using
     CSS. The `user_data` variable is used to populate the table with data. The `second_chart_script`
     variable is used to include any JavaScript code necessary for rendering the chart.
    """
    second_page_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
                background-image: linear-gradient(to right, #DECBA4, #3E5151);
            }}
            h1 {{
                color: #3E5151;
                margin-top: 1px;
                font-size: 50px;
            }}
            #chart {{
                display: block;
                margin: 0 auto;
                width: 300px;
                height: 200px;          
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin-top: 20px;
            }}
            th, td {{
                border: 1px solid #000;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #3E5151;
            }}
        </style>
    </head>
    <body>
        <div class="heading-container">
            <title>Dashboard</title>
            <h1>Test Count</h1>
            <canvas id="chart"></canvas>
        </div>
        <div>
            <table>
                {user_data}
            </table>
        </div>
        {second_chart_script}
    </body>
    </html>
    """
        
    with open('user.html', 'w') as f:
        f.write(second_page_content)
    f.close()



"""
 The above code is printing the shape of two DataFrames, `df1` and `df2`. The shape of a DataFrame
 represents the number of rows and columns in the DataFrame.
"""
print("DataFrame shape:", df1.shape ,df2.shape)


"""
 The above code is using the `webbrowser` module in Python to open the file `Main.html` in a web
 browser.
"""
webbrowser.open('Main.html')



