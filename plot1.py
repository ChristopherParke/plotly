import plotly.graph_objects as go
from PIL import Image

class DrawChart:
    """
    Draw a bar chart using the plotly library
    """
    def barChart(regions, dataset):
        southY = args[0]
        northY = args[1]
        img = Image.open("salesBy.png")

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

        #add orange image
        fig.add_layout_image(
            dict(
                source=img,
                xref="paper", yref="paper",
                x=0.85, y=1,
                sizex=0.5, sizey=0.5,
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
                            paper_bgcolor="rgb(245,245,219)", 
                            plot_bgcolor="rgb(245,245,219)")
        fig.show()

regions = ['South', 'North']
dataset = [[1234.56, 3241.45],[4329.92, 2987.43]]
barChart = DrawChart.barChart(regions, dataset)
barChart