import plotly.graph_objects as go
from PIL import Image
import random

class DrawBarChart:
    """
    Draw Bar Charts using the Plotly library
    """
    def __init__(self, dataTitles, dataset):
        self.dataTitles = dataTitles
        self.dataset = dataset
        self.barColors = ['rgb(140,181,0)','rgb(255, 127, 0)']
        self.barNames = ['Apples', 'Oranges']
        self.textposition = 'outside'
        self.texttemplate= "%{y:$,}"
        self.canvasTitle = 'Sales'
        self.paper_bgcolor = "rgb(245,245,219)"
        self.plot_bgcolor = "rgb(245,245,219)"
        self.title_text = "Region"

    
    def __setBarData(self):
        """
        Set the bar data to be drawn
        """
        myData = []
        for i in range(0, len(self.dataset)):
            myData.append(
                go.Bar(name=self.dataTitles[i],
                        x=self.dataTitles,
                        y=self.dataset[i],
                        marker_color=self.barColors[i],
                        text=self.dataset[i],
                        textposition=self.textposition,
                        texttemplate=self.texttemplate)
            )

        return myData

    def __assignColors(self):
        """
        If data sets are increased beyond 2,
        create a random color for each new set (bar)
        """
        myRange = len(dataset) - len(self.barColors)

        if myRange > 0:
            for i in range(0, myRange):
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
                myBarColor = 'rgb('+ str(r) + ',' + str(g) + ',' + str(b) + ')'
                self.barColors.append(myBarColor)



    def draw(self):
        """
        Draw a bar chart from the data
        """
        img = Image.open("salesBy.png")        

        # Assign new bar colors if none are assigned
        self.__assignColors()

        # Set bar data
        myData = self.__setBarData()

        fig = go.Figure(data=myData)

        # Add Title Image
        fig.add_layout_image(
            dict(
                source=img,
                xref="paper", yref="paper",
                x=0.85, y=1,
                sizex=0.5, sizey=0.5,
                xanchor="right", yanchor="bottom"
            )
        )

        # Setup Canvas Layout
        fig.update_layout(barmode='group', 
                            yaxis=dict(
                            title=self.canvasTitle, 
                            tickprefix = '$', 
                            separatethousands=True
                        ), 
                            paper_bgcolor=self.paper_bgcolor, 
                            plot_bgcolor=self.plot_bgcolor)
        # Label X axis
        fig.update_xaxes(title_text=self.title_text)
        
        # Draw Chart
        fig.show()

# EXAMPLE 1
regions = ['South', 'North']
dataset = [[1234.56, 3241.45],[4329.92, 2987.43]]

# EXAMPLE 2
# regions = ['South', 'North', 'East']
# dataset = [[1234.56, 3241.45, 3435.46],[4329.92, 443.50, 2987.43],[4329.92, 2987.43, 1234.55]]

barChart = DrawBarChart(regions, dataset)

# barChart.barColors = ['rgb(140,181,0)','rgb(255, 127, 0)', 'rgb(123, 255, 100)']
barChart.draw()