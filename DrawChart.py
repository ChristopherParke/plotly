import plotly.graph_objects as go
from PIL import Image

class DrawChart:
    """
    Draw a bar chart using the Plotly library
    """
    def barChart(regions, dataset):
        southY = dataset[0]
        northY = dataset[1]
        img = Image.open("salesBy.png")

        fig = go.Figure(data=[
            # Draw green bars for "Apples"
            go.Bar(name='Apples', 
                    x=regions, 
                    y=southY, 
                    marker_color='rgb(140, 181, 0)', 
                    text=southY, 
                    textposition='outside', 
                    texttemplate="%{y:$,}"),

            # Draw orange bars for "Oranges"
            go.Bar(name='Oranges', 
                    x=regions, 
                    y=northY, 
                    marker_color='rgb(255, 127, 0)', 
                    text=northY,
                    textposition='outside', 
                    texttemplate="%{y:$,}")
        ])

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

regions = ['South', 'North']
dataset = [[1234.56, 3241.45],[4329.92, 2987.43]]
barChart = DrawChart.barChart(regions, dataset)
barChart