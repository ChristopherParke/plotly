import plotly.graph_objects as go
from PIL import Image

class DrawChart:
    """
    Draw a bar chart using the plotly library
    """
    def __init__(self, regions, dataSet):
        self.regions = regions
        self.dataSet = dataSet


    def barChart(self, arg):
        regions = self
        southY = arg[0]
        northY = arg[1]
        im = [Image.open("greenApple.png"), Image.open("orange.png")]

        fig = go.Figure(data=[
            #Draw green bars for Apples
            go.Bar(name='Apples', 
                    x=regions, 
                    y=southY, 
                    marker_color='rgb(140, 181, 0)', 
                    text=southY, 
                    textposition='outside', 
                    texttemplate="%{y:$,}"),

            #Draw orange bars for Oranges
            go.Bar(name='Oranges', 
                    x=regions, 
                    y=northY, 
                    marker_color='rgb(255, 127, 0)', 
                    text=northY,
                    textposition='outside', 
                    texttemplate="%{y:$,}")
        ])

        #add apple image
        fig.add_layout_image(
            dict(
                source=im[0],
                xref="x domain", yref="paper",
                x=0.5, y=1.06,
                sizex=.05, sizey=.05,
                xanchor="right", yanchor="bottom"
            )
        )

        #add orange image
        fig.add_layout_image(
            dict(
                source=im[1],
                xref="paper", yref="paper",
                x=0.6, y=1.06,
                sizex=.05, sizey=.05,
                xanchor="right", yanchor="bottom"
            )
        )

        # Change the bar mode
        fig.update_layout(barmode='group', 
                            yaxis=dict(
                            title='Sales', 
                            tickprefix = '$', 
                            separatethousands=True
                        ), 
                            title="Sales by Region:      Apples vs      Oranges",
                            title_x=0.5,
                            paper_bgcolor="rgb(245,245,219)", 
                            plot_bgcolor="rgb(245,245,219)")
        fig.show()

regions = ['South', 'North']
dataset = [[1234.56, 3241.45],[4329.92, 2987.43]]
barChart = DrawChart.barChart(regions,dataset)
barChart