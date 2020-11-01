import plotly.graph_objects as go
from PIL import Image

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
    
    def __setBarData(self):
        """
        Draw the bars for the Chart
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

    def draw(self):
        """
        Draw a bar chart from the data
        """
        img = Image.open("salesBy.png")        

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
                            title='Sales', 
                            tickprefix = '$', 
                            separatethousands=True
                        ), 
                            paper_bgcolor="rgb(245,245,219)", 
                            plot_bgcolor="rgb(245,245,219)")
        # Label X axis
        fig.update_xaxes(title_text="Region")
        
        # Draw Chart
        fig.show()

# EXAMPLE 1
# regions = ['South', 'North']
# dataset = [[1234.56, 3241.45],[4329.92, 2987.43]]

# EXAMPLE 2
regions = ['South', 'North', 'East']
dataset = [[1234.56, 3241.45, 3435.46],[4329.92, 443.50, 2987.43],[4329.92, 2987.43, 1234.55]]

barChart = DrawBarChart(regions, dataset)

barChart.barColors = ['rgb(140,181,0)','rgb(255, 127, 0)', 'rgb(123, 255, 100)']
barChart.draw()